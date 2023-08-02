# Generated by Django 3.2.20 on 2023-08-02 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.IntegerField(choices=[(0, 'low'), (1, 'medium'), (2, 'high')])),
                ('crated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expired_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
