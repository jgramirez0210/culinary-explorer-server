INSTALLED_APPS = [
    # ... your other apps
    'corsheaders',  # Add this line
]

MIDDLEWARE = [
    # ... your other middleware
    'corsheaders.middleware.CorsMiddleware',  # Add this line (usually after other middleware)
    'django.middleware.common.CommonMiddleware',
]

# Add CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:3002",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

# Optional: Allow credentials if needed
CORS_ALLOW_CREDENTIALS = True

# Optional: Allow all headers
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
