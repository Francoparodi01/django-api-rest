from django.shortcuts import render
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UsuarioSerializer

# Create your views here.

def index (request):
    getUsers = User.objects.all()
    print(getUsers)
    return render(request, 'index.html', {
        'users': getUsers,
    })

@api_view(['POST'])
def registrar_usuario(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({'mensaje': 'Usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()  # Guardar el nuevo usuario
            return Response({'mensaje': 'Registro exitoso'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_usuario(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            usuario = User.objects.get(email=email, password=password)
            return Response({'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'mensaje': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
