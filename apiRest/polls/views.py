from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UsuarioSerializer


# Vista para mostrar los usuarios en el índice
def index(request):
    getUsers = User.objects.all()
    return render(request, 'index.html', {'users': getUsers})

# Registro de usuario
@csrf_exempt
@api_view(['POST'])
def registrar_usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guarda el usuario directamente
            user.set_password(serializer.validated_data['password'])  # Hashea la contraseña
            user.save()  # Guarda el usuario de nuevo para actualizar la contraseña hasheada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login de usuario
@api_view(['POST'])
def login_usuario(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({"error": "Email y contraseña son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
        
        # Check the password
        if user.check_password(password):  
            serializer = UsuarioSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
    
    except User.DoesNotExist:
        return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)