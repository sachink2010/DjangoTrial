# Generated by Django 3.2.7 on 2021-10-31 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_alter_story_user_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='user_input',
            field=models.CharField(max_length=600),
        ),
    ]
