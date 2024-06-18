from rest_framework import viewsets
from .serializer import UsuarioSerializer, FichaSerializer, AprendizSerializer
from .models import Usuario, Ficha, Aprendiz

# Create your views here.
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()  

class FichaView(viewsets.ModelViewSet):
    serializer_class = FichaSerializer
    queryset = Ficha.objects.all()
    
    
class AprendizView(viewsets.ModelViewSet):
    serializer_class = AprendizSerializer
    queryset = Aprendiz.objects.all()
    
