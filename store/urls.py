from django.contrib import admin
from django.urls import path,include
from .views.home import search,TestView,Index
from .views.login import Login,logout,Post
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware
from rest_framework.authtoken.views import  obtain_auth_token


urlpatterns = [

    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('post', Post, name='post'),
    path('search', search, name='search'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),





    path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('test_view', TestView.as_view(), name='test'),
    path('order_view',OrderView.as_view(), name='order'),
    path('sign_up',Signup.as_view(), name='sign-up'),
    path('Index',Index.as_view(), name='Index'),
    path('Login',Login.as_view(), name='login'),
    path('logout',logout, name='logout'),
    # path('CheckOut',CheckOut.as_view, name='CheckOut'),

    # path('Product',Product.as_view(),name=Product),
    # path('search',search, name='search'),

]
