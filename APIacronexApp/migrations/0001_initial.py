# Generated by Django 4.0.5 on 2022-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='maquinas',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('clase', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
            ],
        ),
    ]
