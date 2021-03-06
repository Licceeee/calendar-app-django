# Generated by Django 3.2.13 on 2022-04-29 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_routine'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRoutine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(max_length=400)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarapp.routine')),
            ],
            options={
                'unique_together': {('day', 'routine')},
            },
        ),
    ]
