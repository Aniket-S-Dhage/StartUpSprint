# Generated by Django 5.1.1 on 2024-09-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=50)),
                ('ratings', models.FloatField(default=0.0)),
                ('feedback_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=250)),
                ('query', models.TextField()),
                ('answer', models.TextField(blank=True, null=True)),
                ('question_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
