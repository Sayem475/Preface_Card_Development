# Generated by Django 4.1.7 on 2023-03-07 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0007_remove_carduser_card_linked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carduser',
            old_name='bio',
            new_name='designation',
        ),
    ]
