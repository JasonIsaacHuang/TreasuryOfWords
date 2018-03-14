from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from thesaurus import views

router = routers.DefaultRouter()
router.register(r'word', views.WordViewSet)
router.register(r'synonym', views.SynonymViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
