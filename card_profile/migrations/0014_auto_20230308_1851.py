# Generated by Django 3.1.4 on 2023-03-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0013_alter_carduser_id_alter_carduser_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sociallinksintems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
