from django.urls import path
from .views import home,LoginView,RegisterView,ProtectedView

urlpatterns = [
    path('',home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
