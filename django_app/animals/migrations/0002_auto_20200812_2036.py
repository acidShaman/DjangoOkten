# Generated by Django 3.1 on 2020-08-12 17:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalmodel',
            options={'verbose_name': 'animal', 'verbose_name_plural': 'animals'},
        ),
        migrations.AlterField(
            model_name='animalmodel',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^([a-zA-Z]{1,30})$', 'Only a-z A-Z max 30 symbols')]),
        ),
        migrations.AlterField(
            model_name='animalmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AnimalMonikerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moniker', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^([a-zA-Z]{1,30})$', 'Only a-z A-Z max 30 symbols')])),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monikers', to='animals.animalmodel')),
            ],
            options={
                'db_table': 'monikers_of_animals',
            },
        ),
    ]
