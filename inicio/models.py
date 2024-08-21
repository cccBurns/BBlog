from django.db import models

# Create your models here.
class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.titulo