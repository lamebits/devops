How to Create a basic API using Django Rest Framework ?

1. pip install django
2. pip install djangorestframework
3. Create Django Project
	django-admin startproject create_api_using_django
4. Create app
	python manage.py startapp apis
5. Add 'rest_framwork' & 'apis' in settings.py file.
	
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apis',
]

6.Add below code in urls.py file

from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apis.urls"))
]

7. Add below code in apis/models.py

from django.db import models


class ApiModel(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title

8. Create new .py file i.e. serializer.py in apis folder and paste below code

from rest_framework import serializers
from .models import ApiModel

class APISerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = ApiModel
		fields = ('title', 'description')

9. Add below code in apis/views.py file

from rest_framework import viewsets
from .serializers import APISerializer
from .models import ApiModel

# create a viewset


class ApiViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = ApiModel.objects.all()

	# specify serializer to be used
	serializer_class = APISerializer

10. Add below code in urls.py file

from django.urls import include, path
from rest_framework import routers
from apis.views import *

router = routers.DefaultRouter()

router.register(r'apis', ApiViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]

11. Run server to check API

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

