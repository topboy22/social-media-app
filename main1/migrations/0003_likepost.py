# Generated by Django 4.0.4 on 2022-06-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0002_post_alter_profile_location_alter_profile_profileimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
