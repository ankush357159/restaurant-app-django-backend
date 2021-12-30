from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from menu import views
from menu.routers import router


# router = DefaultRouter()

# router.register('menu', views.MenuViewset, basename='menu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
