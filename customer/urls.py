from django.urls import path

from customer.views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordComplete

urlpatterns = [
    path('activate/', ActivationView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('forgot_password_complete/', ForgotPasswordComplete.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view()),
]
