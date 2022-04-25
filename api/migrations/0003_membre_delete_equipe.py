# Generated by Django 4.0.4 on 2022-04-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_equipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('photo', models.ImageField(upload_to='membrePhoto/')),
            ],
        ),
        migrations.DeleteModel(
            name='equipe',
        ),
    ]
