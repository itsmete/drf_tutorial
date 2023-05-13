# Generated by Django 4.2.1 on 2023-05-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(max_length=100, verbose_name='Content')),
                ('active', models.BooleanField(default=True, verbose_name='Active Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Forums',
                'ordering': ['-created', '-updated'],
            },
        ),
    ]
