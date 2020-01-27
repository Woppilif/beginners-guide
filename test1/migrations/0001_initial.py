# Generated by Django 2.2.7 on 2020-01-27 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now=True, null=True)),
                ('chat', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='test1.Users')),
            ],
        ),
    ]