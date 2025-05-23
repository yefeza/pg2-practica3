from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    fecha_hora_matricula = models.DateTimeField(auto_now_add=True)
    apodo = models.TextField()
    intereses = models.TextField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    anio = models.IntegerField()
    estudiantes = models.ManyToManyField(Estudiante, related_name="materias")


class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField()
    nota = models.FloatField()


class ComidaFavorita(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name="comidas_favoritas"
    )


class Hobby(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name="hobbies"
    )
