from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('product_details/', views.product_details, name='product_details'),
    path('brands/', views.all_brands, name='brands'),
    path('<slug:slug>/', views.full_brands, name='full_brands'),
    path('skin_type', views.skin_type, name='skin_type'),
    path('skin_concern', views.skin_concern, name='skin_concern'),
]
