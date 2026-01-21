from rest_framework.decorators import api_view
from rest_framework.response import Response
from culinary_explorer_api.models import User

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    if 'uid' not in request.data:
        return Response({'error': 'uid is required'}, status=400)

    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'valid': True,
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email_address': user.email,
            'profile_image_url': user.profile_image_url,
            'uid': user.uid,
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    required_fields = ['first_name', 'last_name', 'email_address', 'uid']
    for field in required_fields:
        if field not in request.data:
            return Response({'error': f'{field} is required'}, status=400)

    # Check if user already exists
    if User.objects.filter(uid=request.data['uid']).exists():
        return Response({'error': 'User with this uid already exists'}, status=400)

    # Now save the user info in the auth_user table (via our custom User model)
    user = User.objects.create(
        uid=request.data['uid'],  # This becomes the username field
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email_address'],
        profile_image_url=request.data.get('profile_image_url', ''),
        password=''  # No password for external auth
    )

    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email_address': user.email,
        'profile_image_url': user.profile_image_url,
        'uid': user.uid,
    }
    return Response(data)