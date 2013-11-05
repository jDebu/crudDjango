from django.db import models

class Hospital(models.Model):
    nombre      =models.CharField(max_length=200)
    direccion   =models.CharField(max_length=200)
    status      =models.BooleanField(default=True)
    pedidos     =models.PositiveIntegerField(default=0)
    ''' es el mismo que numero de Pedido '''
    def __unicode__(self):
        return self.nombre
''''''
class Producto(models.Model):
    def url(self,filename):
        ruta="MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
        return ruta
    nombre     =models.CharField(max_length=100)
    grupo      =models.CharField(max_length=100)
    descripcion =models.TextField(max_length=300,null=True,blank=True)
    status      =models.BooleanField(default=True)
    imagen      =models.ImageField(upload_to=url,null=True,blank=True)
    ''' stock'''
    cantidad     =models.IntegerField()

    def __unicode__(self):
        return "%s %s"%(self.nombre,self.grupo)

class Pedido(models.Model):

    numero      =models.PositiveIntegerField(default=0)
    fecha       =models.DateTimeField(auto_now_add=True)
    '''grupo      =models.CharField(max_length=100)'''
    descripcion =models.TextField(max_length=300,null=True,blank=True)
    status      =models.CharField(max_length=100)
    '''acuerdo'''
    '''precio      =models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)'''
    cantidad    =models.IntegerField()
    hospital    =models.ForeignKey(Hospital,null=False,blank=False)
    producto    =models.ManyToManyField(Producto)

    def __unicode__(self):
        return "%s %s"%(self.numero, self.hospital)



