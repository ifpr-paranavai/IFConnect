# Generated by Django 4.1.7 on 2023-08-22 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_remove_midia_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midia',
            name='arquivo',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='midia',
            name='dataInicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='midia',
            name='dataTermino',
            field=models.DateField(),
        ),
    ]
