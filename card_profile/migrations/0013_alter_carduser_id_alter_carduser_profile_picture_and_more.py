# Generated by Django 4.1.7 on 2023-03-08 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_profile', '0012_auto_20230308_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carduser',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures'),
        ),
        migrations.CreateModel(
            name='SocialLInksIntems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(blank=True, max_length=400, null=True)),
                ('social_link', models.CharField(blank=True, max_length=600, null=True)),
                ('card_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_profile.carduser')),
            ],
        ),
    ]