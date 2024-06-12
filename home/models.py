from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from .validators import *

validatorDescription = RegexValidator(r"^[a-zA-ZÀ-ÿ0-9\s]{1,40}$","La descripcion de tu producto no puede contener caracteres especiales")


# Create your models here.



class Producto(models.Model):
    idProducto = models.BigAutoField(db_column='idProduco',primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(db_column='nombre',max_length=100)
    user = models.ForeignKey(User,db_column='Usuario', on_delete=models.CASCADE,related_name='Mis_productos',null=True)
    disponible = models.BooleanField(db_column='Disponible',default=True)
    timestamp = models.DateTimeField(db_column='Fecha de subida',auto_now_add=True)
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoria',default=None)  
    precio= models.DecimalField(db_column='Precio', max_digits=6, decimal_places=3,verbose_name='Precio',default=None)  
    descripcion = models.TextField(db_column='Descripcion', max_length=150,null=True,default=None,blank=True) 
    foto= models.ImageField(db_column='Foto', null=True,upload_to='products')
    estado = models.BooleanField(db_column='estado',default=True, blank=True)


    class Meta:
        ordering=['-timestamp']
        verbose_name_plural='Productos'
    
    def __str__(self):
        return f'{self.nombre} - de {self.user.username}'
    

class Categoria(models.Model):
    idProducto = models.BigAutoField(db_column='idCategoria',primary_key=True, serialize=False, verbose_name='ID')
    nombre = models.CharField(db_column='Nombre', max_length=45)  

    class Meta:
        verbose_name_plural='Categoria' 

    def __str__(self):
        return self.nombre


class Comprador(models.Model):
    idcomprador= models.AutoField(db_column='idPersona', primary_key=True)  
    nombres = models.CharField(db_column='Nombres', max_length=50)  
    apellidos = models.CharField(db_column='Apellidos', max_length=50)  
    numidentificacion = models.BigIntegerField(db_column='NumIdentificacion')  
    numcelular = models.BigIntegerField(db_column='NumCelular')  
    correoelectronico = models.CharField(db_column='CorreoElectronico', max_length=45)  
    direccion = models.CharField(db_column='direccion',max_length=50)

    class Meta:
        verbose_name_plural='Compradores' 

    def __str__(self):
        cadenaName = self.nombres + ' ' + self.apellidos
        return cadenaName

class carrito_compras(models.Model):
    idcar= models.AutoField(db_column='idCar', primary_key=True)  
    productos = models.ForeignKey('Producto', models.DO_NOTHING, db_column='productos',default=None)



class Perfilusuario(models.Model):
    idroles = models.AutoField(db_column='idRoles', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    descripcionrol = models.TextField(db_column='descripcionRol', blank=True, null=True)  
    user = models.ForeignKey(User,db_column='Usuario', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural='Perfil Usuario' 



#----------------------------
# class Pedido(models.Model)
# class Empleado(models.Model)
# class Proveedor(models.Model)