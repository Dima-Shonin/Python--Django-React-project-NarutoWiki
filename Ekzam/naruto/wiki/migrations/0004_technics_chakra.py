# Generated by Django 3.2.4 on 2021-07-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_remove_technics_chakra'),
    ]

    operations = [
        migrations.AddField(
            model_name='technics',
            name='chakra',
            field=models.CharField(blank=True, choices=[('Фууто́н', 'Ветер'), ('Райто́н', 'Молнии'), ('Като́н', 'Огонь'), ('Суйто́н', 'Вода'), ('Дото́н', 'Земля')], default='Ве', max_length=15),
        ),
    ]
