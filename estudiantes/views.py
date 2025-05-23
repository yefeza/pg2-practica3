# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from estudiantes.serializers import *
from estudiantes.models import *


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.filter(
        fecha_hora_matricula__lte=tz.localtime() - timedelta(minutes=1)
    )
    serializer_class = EstudianteSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
