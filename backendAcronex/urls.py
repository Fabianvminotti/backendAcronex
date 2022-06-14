
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from APIacronexApp import views

router = routers.DefaultRouter()
router.register(r'maqs', views.maquinasView, 'maquinasView')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
