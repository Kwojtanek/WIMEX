from django.db import models
# Create your models here.


class Product(models.Model):
    
    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'
    
    name = models.CharField('Nazwa Produktu', max_length=128)

    def __str__(self):
        return self.name

    date = models.DateTimeField('Data dodania', auto_now_add=True, editable=False)
    serial = models.CharField('Numer Seryjny', max_length=128, null=True, blank=True)
    model = models.CharField('Model', max_length=128, null=True, blank=True)
    description = models.TextField('Opis', null=True, blank=True, max_length=1024)
    power = models.CharField('Moc', max_length=128, null=True, blank=True)
    cena = models.FloatField('Cena')


class AdditionalInfo(models.Model):

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = verbose_name_plural = 'Dodatkowe informacje'
    product = models.ForeignKey(to=Product, related_name='infos', on_delete=None)
    description = models.CharField('Opis', null=True, blank=True, max_length=1024)


class Image(models.Model):

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Zdjęcie'
        verbose_name_plural = 'Zdjęcia'

    photo = models.ImageField(verbose_name='Zdjęcie')
    product = models.ForeignKey(to=Product, related_name='images', on_delete=None)


class Promotion(models.Model):
    active = models.BooleanField(default=False)
