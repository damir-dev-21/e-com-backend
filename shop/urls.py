from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUserView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path('products/',views.ProductListView.as_view()),
    path('products/create/',views.ProductCreateView.as_view()),
    path('products/<id>/',views.ProductDetailView.as_view()),
    path('products/<id>/update/',views.ProductUpdateView.as_view()),
    path('products/<id>/delete/',views.ProductDeleteView.as_view()),
    path('orders/',views.OrderListView.as_view()),
    path('orders/create/',views.OrderCreateView.as_view()),
    path('orders/<id>/update/',views.OrderUpdateView.as_view()),
    path('orders/<id>/delete/',views.OrderDeleteView.as_view()),
    path('status/',views.StatusItems.as_view()),
]