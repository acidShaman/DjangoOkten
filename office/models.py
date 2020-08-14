from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class CityModel(models.Model):
    class Meta:
        db_table = 'city'

    city = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.city)


class OfficeModel(models.Model):
    class Meta:
        db_table = 'office'

    name = models.CharField(max_length=30)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10, blank=True, validators=[RegexValidator('^([0])(\d{9})$', 'Not a valid number')])
    price = models.IntegerField()
    users = models.ManyToManyField(User, related_name='offices')    #many-to-many

    def __str__(self):
        return f'{self.name} - {self.city}'
