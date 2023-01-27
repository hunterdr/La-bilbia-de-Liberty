from django.db import models

# Create your models here.
class Documentos(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    fecha_subida = models.DateField(auto_now=True)
    descripcion = models.TextField(null=False, blank=False)
    documento = models.ImageField(upload_to='foto/', max_length=255, null=False, blank=False)


    def __str__(self):
        return self.nombre

