from culinary_explorer_api.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email_address': user.email_address,
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

    # Now save the user info in the culinary_explorer_api table
    user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email_address=request.data['email_address'],
        profile_image_url=request.data['profile_image_url'],
        uid=request.data['uid']
    )

    # Return the user info to the client
    data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email_address': user.email_address,
            'profile_image_url': user.profile_image_url,
            'uid': user.uid,
    }
    return Response(data)
