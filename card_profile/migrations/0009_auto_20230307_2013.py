# Generated by Django 3.1.4 on 2023-03-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0008_rename_bio_carduser_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
