# Generated by Django 4.2.6 on 2023-10-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_poost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poost',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
