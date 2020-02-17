from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('list', views.ProductListView, basename='list')
router.register('create', views.ProductCreateView, basename='product')


urlpatterns = [

    path('', include(router.urls), name='api'),


]