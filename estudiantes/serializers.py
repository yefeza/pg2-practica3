from estudiantes.models import *
from rest_framework import serializers


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = [
            "id",
            "nombre",
            "apellido",
            "fecha_hora_matricula",
            "apodo",
            "intereses",
            "ciudad",
            "pais",
            "edad",
            "correo",
        ]


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"
