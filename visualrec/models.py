from django.db import models

# Create your models here.
class venta_articulo(models.Model):
    titulo = models.CharField(max_length=25)
    analisis= models.CharField(max_length=20, default='', blank=True) #Como ya hay elementos en la base
    analiticas= models.TextField(default='', blank=True) #es necesario colocar un default
    precio = models.IntegerField(default=0)
    CARROS_MARCAS = (
        ('Bmw', 'CarroBmw'),
        ('Volkswagen', 'CarroVolkswagen'),
        ('Chevrolet', 'CarroChevrolet'),
        ('Ford', 'CarroFord'),
        ('Nissan', 'CarroNissan'),
    )
    marca_carros= models.CharField(max_length=10, choices=CARROS_MARCAS)
    descripcion=models.TextField()
    foto=models.ImageField(blank=True)

    def __str__(self):
        return self.titulo+' '+str(self.id)
