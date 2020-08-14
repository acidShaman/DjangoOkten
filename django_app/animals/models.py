from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()


class AnimalModel(models.Model):
    class Meta:
        db_table = 'animals'
        verbose_name = 'animal'
        verbose_name_plural = 'animals'

    name = models.CharField(max_length=30, validators=[RegexValidator('^([a-zA-Z]{1,30})$', 'Only a-z A-Z max 30 symbols')])
    animal_types = [
        (1, 'cat'),
        (2, 'dog'),
        (3, 'wolf')
    ]
    animal_type = models.IntegerField(choices=animal_types)
    user = models.ForeignKey(User, related_name='animals', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AnimalMonikerModel(models.Model):
    class Meta:
        db_table = 'monikers_of_animals'

    moniker = models.CharField(max_length=30, validators=[RegexValidator('^([a-zA-Z]{1,30})$', 'Only a-z A-Z max 30 symbols')])
    animal = models.ForeignKey(AnimalModel, related_name='monikers', on_delete=models.CASCADE)
