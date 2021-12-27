from django.urls import path

from customer.views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordComplete
from order.views import CreateOrderView, UsersOrdersList, UpdateOrderStatusView, CartItemView, UsersCartItemsList, UpdateCartItemStatusView

urlpatterns = [
    path('orders/', CreateOrderView.as_view()),
    path('orders/own/', UsersOrdersList.as_view()),
    path('orders/<int:pk>/', UpdateOrderStatusView.as_view()),

    path('cartitem/', CartItemView.as_view()),
    path('cartitem/own/', UsersCartItemsList.as_view()),
    path('cartitem/<int:pk>/', UpdateCartItemStatusView.as_view()),
]