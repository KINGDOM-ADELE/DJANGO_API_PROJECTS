from .views import *
from django.urls import path, include    
from . import views

urlpatterns = [
    # Create users and request tokens endpoints
    path('users', views.user),
    path('users/user/me', views.userProfile),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # User group management endpoints
    path('groups/manager/users', views.managerSet),
    path('groups/manager/users/<int:id>', views.managerDelete),
    path('groups/delivery-crew/users', views.deliveryCrewSet),  
    path('groups/delivery-crew/users/<int:id>', views.deliveryCrewDelete),

    # Menu-items endpoints
    path('menu-items', views.menu),
    path('menu-items/<int:id>', views.menuItem),
    
    # Cart management endpoints
    path('cart/menu-items', views.cart),
    
    # Order Management endpoints
    path('orders', views.order),
    path('orders/<int:id>', views.orderItem),    
]