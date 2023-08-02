from django.db import models


# Create your models here.

class Advertisements(models.Model):
    title = models.CharField('заголовок', max_length=100)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Возможен торг или нет')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'advertisements(id = {self.id}, title = {self.title}, price = {self.price})'

    class Meta:
        db_table = 'advertisements'
