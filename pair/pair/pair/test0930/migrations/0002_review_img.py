# Generated by Django 3.2.13 on 2022-09-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test0930', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
