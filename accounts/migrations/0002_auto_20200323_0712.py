# Generated by Django 3.0.4 on 2020-03-23 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='people',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
                ('country', models.CharField(choices=[('CHN', 'China'), ('BRA', 'Brasil'), ('ESP', 'Espanha'), ('USA', 'Estados Unidos'), ('ITA', 'Itália')], max_length=3)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(choices=[('TR', 'Cansaço'), ('DI', 'Diarreia'), ('SB', 'Dificuldade respiratória'), ('ST', 'Dor de garganta'), ('AP', 'Dores no corpo'), ('FV', 'Febre'), ('DC', 'Tosse'), ('RN', 'Nariz escorrendo'), ('DI', 'Náusea')], max_length=2)),
                ('intensity', models.CharField(choices=[('L', 'Baixa'), ('M', 'Média'), ('H', 'Alta')], max_length=1)),
                ('onset', models.DateField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comorbidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('H', 'Doença arterial coronariana'), ('A', 'Fibrilação atrial'), ('S', 'AVC'), ('T', 'Hipertensão'), ('D', 'Diabetes'), ('E', 'Demência'), ('C', 'Bronquite crônica'), ('N', 'Câncer'), ('L', 'Doença crônica no fígado'), ('R', 'Doença renal crônica')], max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]