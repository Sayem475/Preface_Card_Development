# Generated by Django 3.1.4 on 2023-03-13 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0018_alter_professionalitems_work_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professionalitems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='skillsintems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sociallinksintems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
