"""
Django settings for LibraryProject project.
Secure configuration for production with XSS, CSRF, and SQL injection protections.
Generated using Django 5.2.7
"""

from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# SECURITY SETTINGS
# ----------------------------

# Keep secret key secret in production!
SECRET_KEY = 'django-insecure-(_9417r@5#2_6c-*ug%e5lu1*w2aydm24pe+0nac5p2tr+!nbe'

DEBUG = False  # Disable debug mode in production

# Replace with your server host/domain in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# ----------------------------
# APPLICATIONS
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'bookshelf',
    'relationship_app',

    # Security app for Content Security Policy
    'csp',
]

# ----------------------------
# MIDDLEWARE
# ----------------------------
MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',  # Content Security Policy
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevent clickjacking
     'LibraryProject.middleware.ContentSecurityPolicyMiddleware',
]

# ----------------------------
# URLS & WSGI
# ----------------------------
ROOT_URLCONF = 'LibraryProject.urls'
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# ----------------------------
# TEMPLATES
# ----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add custom template dirs if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ----------------------------
# DATABASE
# ----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------
# PASSWORD VALIDATION
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------------------
# INTERNATIONALIZATION
# ----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------
# STATIC FILES
# ----------------------------
STATIC_URL = 'static/'

# ----------------------------
# DEFAULT PRIMARY KEY FIELD
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------------------
# CUSTOM USER MODEL
# ----------------------------
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# ----------------------------
# AUTHENTICATION REDIRECTS
# ----------------------------
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'list_books'
LOGOUT_REDIRECT_URL = 'login'

# ----------------------------
# SECURITY ENHANCEMENTS
# ----------------------------
X_FRAME_OPTIONS = 'DENY'                 # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True       # Prevent content sniffing
SECURE_BROWSER_XSS_FILTER = True         # Browser XSS protection

# Ensure cookies are sent only over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ----------------------------
# CONTENT SECURITY POLICY (CSP)
# ----------------------------
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'img-src': ("'self'", 'data:'),  # allows inline images/data URIs
        'script-src': ("'self'",),
        'style-src': ("'self'", 'https://fonts.googleapis.com'),
        'font-src': ("'self'", 'https://fonts.gstatic.com'),
    }
}


