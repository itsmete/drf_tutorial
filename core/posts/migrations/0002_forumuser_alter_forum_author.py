# Generated by Django 4.2.1 on 2023-05-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True, max_length=512)),
            ],
        ),
        migrations.AlterField(
            model_name='forum',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='posts.forumuser'),
        ),
    ]
