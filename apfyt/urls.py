#apfyt URL Configuration

#The `urlpatterns` list routes URLs to views. For more information please see:
#    https://docs.djangoproject.com/en/1.10/topics/http/urls/
#Examples:
#Function views
#    1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^', include('main.urls')),
	url(r'^surveys/', include('surveys.urls')),
	url(r'^company/', include('companies.urls')),

	url(r'^api/', include('api.urls'))
	#url(r'^rest-auth/', include('rest_auth.urls')),
	#url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
