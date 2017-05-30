
# Django settings for apfyt project.

# Generated by 'django-admin startproject' using Django 1.10.5.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.10/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.10/ref/settings/


import os
from django.contrib.messages import constants as messages
from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = (
	("Josh", "snare117@gmail.com"),
	("Ryan", "whettenrmw@gmail.com"),
	("Dillon", "dfranke@stanford.edu")
	)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+x-p0koll&q9v!#=_(%*o3c&$&#1+#9&_fgl1#77)2f5a2cn3v'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*']
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook',
	'companies',
	'crispy_forms',
	'easy_thumbnails',
	'image_cropping',
	'rest_framework',
	'rest_framework.authtoken',
	'rest_auth',

	'main',
	'surveys',
	'users',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
	# Needed to login by username in Apfyt admin, regardless of `allauth`
	'django.contrib.auth.backends.ModelBackend',

	# `allauth` specific authentication methods, such as login by e-mail
	'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'apfyt.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, "templates")],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'apfyt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# [START dbconfig]
DATABASES = {
	'default': {
		# If you are using Cloud SQL for MySQL rather than PostgreSQL, set
		# 'ENGINE': 'django.db.backends.mysql' instead of the following.
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'polls',
		'USER': 'snare117',
		'PASSWORD': '3p1cJ05h!',
	}
}
# In the flexible environment, you connect to CloudSQL using a unix socket.
# Locally, you can use the CloudSQL proxy to proxy a localhost connection
# to the instance
DATABASES['default']['HOST'] = '/cloudsql/apfyt-fullstack-webapp:us-central1:sqlinstance-apfyt'
if os.getenv('GAE_INSTANCE'):
	pass
else:
	DATABASES['default']['HOST'] = '127.0.0.1'
# [END dbconfig]


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = 'https://storage.googleapis.com/apfyt-fullstack-webapp/static/'

STATIC_ROOT = 'https://storage.googleapis.com/apfyt-fullstack-webapp/static/' 
	
STATICFILES_DIRS = (
	'https://storage.googleapis.com/apfyt-fullstack-webapp/static/'
	#os.path.join(BASE_DIR, "static_in_env"),
	#'/var/www/static/',
)

MEDIA_URL = "https://storage.googleapis.com/apfyt-fullstack-webapp/static/media_root/"
MEDIA_ROOT = "https://storage.googleapis.com/apfyt-fullstack-webapp/static/media_root/"

EMAIL_HOST = 'smtp.sendgrid.com'
EMAIL_HOST_USER = 'snare117'
EMAIL_MAIN = 'snare117@gmail.com'
EMAIL_HOST_PASSWORD = '3p1cj05h'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# DJANGO-ALLAUTH SETTINGS
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SESSION_REMEMBER = None
ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'
ACCOUNT_LOGOUT_REDIRECT_URL ="/accounts/login"

SOCIALACCOUNT_PROVIDERS = \
	{'facebook':
	   {'METHOD': 'oauth2',
		'SCOPE': ['email', 'public_profile', 'user_friends'],
		'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
		'FIELDS': [
			'id',
			'email',
			'name',
			'first_name',
			'last_name',
			'verified',
			'locale',
			'timezone',
			'link',
			'gender',
			'updated_time'],
		'EXCHANGE_TOKEN': True,
		'LOCALE_FUNC': lambda request: 'en_US',
		'VERIFIED_EMAIL': True,
		'VERSION': 'v2.4'}
	}

MESSAGE_TAGS = {messages.DEBUG: 'debug',
messages.INFO: 'info',
messages.SUCCESS: 'success',
messages.WARNING: 'warning',
messages.ERROR: 'danger',}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

THUMBNAIL_PROCESSORS = (
	'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

REST_SESSION_LOGIN = True
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication',
	),
}
REST_SESSION_LOGIN = True
REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': (
	'rest_framework.permissions.IsAuthenticated',
),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication',
	),
}
