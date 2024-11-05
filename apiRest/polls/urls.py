from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),

    # Rutas para autenticación con tokens
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
