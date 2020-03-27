# Generated by Django 2.2.3 on 2020-03-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0008_auto_20200327_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoring',
            name='result',
            field=models.CharField(choices=[('SR', 'Sem resposta'), ('PO', 'Positivo'), ('NE', 'Negativo')], default='Sem resposta', max_length=12, verbose_name='Resultado do exame'),
        ),
    ]