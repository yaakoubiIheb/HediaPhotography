# Generated by Django 4.0.4 on 2022-05-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_information_description_information_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='linkedIn',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]