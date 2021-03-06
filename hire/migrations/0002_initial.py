# Generated by Django 3.2.5 on 2021-09-09 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireprofessional',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hire_by', to='users.client'),
        ),
        migrations.AddField(
            model_name='hireprofessional',
            name='professional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hire_to', to='users.professionals'),
        ),
    ]
