# Generated by Django 3.2.11 on 2022-02-27 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'ordering': ['-pk']},
        ),
    ]
