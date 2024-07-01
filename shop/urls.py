from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CartViewSet

app_name = 'shop'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/cart/add/', CartViewSet.as_view({'post': 'add_item'}), name='add_item'),
    path('api/cart/update/', CartViewSet.as_view({'post': 'update_item'}), name='update_item'),
    path('api/cart/remove/', CartViewSet.as_view({'post': 'remove_item'}), name='remove_item'),
    path('api/cart/clear/', CartViewSet.as_view({'post': 'clear_cart'}), name='clear_cart'),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]
