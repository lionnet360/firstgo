# Generated by Django 4.2.6 on 2023-10-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_poost_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poost',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
