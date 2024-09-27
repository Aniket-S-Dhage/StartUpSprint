# Generated by Django 5.1.1 on 2024-09-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disbursement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installment',
            name='status',
            field=models.CharField(blank=True, choices=[('ok', 'ok'), ('late', 'late'), ('pending', 'pending'), ('', '')], default='pending', max_length=100),
        ),
    ]
