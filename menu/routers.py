from rest_framework import routers
from django.urls import path, include
from menu.views import MenuViewset

router = routers.SimpleRouter()
router.register(r'menu', MenuViewset, basename='menu')


urlpatterns = [
    path('menu/', include((router.urls, 'menu')))
]

urlpatterns += router.urls
