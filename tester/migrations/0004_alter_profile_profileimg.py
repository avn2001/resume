# Generated by Django 3.2.15 on 2022-09-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0003_auto_20220923_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
