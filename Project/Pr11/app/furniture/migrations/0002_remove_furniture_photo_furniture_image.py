# Generated by Django 5.1.1 on 2024-09-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='photo',
        ),
        migrations.AddField(
            model_name='furniture',
            name='image',
            field=models.ImageField(default=0, upload_to='furniture/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
