# Generated by Django 3.2 on 2022-02-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_spotless_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='picture_url',
            field=models.TextField(),
        ),
    ]
