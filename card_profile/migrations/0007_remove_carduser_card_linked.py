# Generated by Django 4.1.7 on 2023-03-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0006_alter_carduser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carduser',
            name='card_linked',
        ),
    ]