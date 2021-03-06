# Generated by Django 3.2.7 on 2021-11-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0009_alter_story_user_input'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_input', models.CharField(max_length=600)),
                ('api_response', models.CharField(blank=True, max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
