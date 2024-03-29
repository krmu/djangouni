# Generated by Django 4.2.dev20220718043020 on 2022-07-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Lietotājvārds')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktīvs')),
                ('staff', models.BooleanField(default=False, verbose_name='Ir darbinieks')),
                ('admin', models.BooleanField(default=False, verbose_name='Ir administrators')),
                ('vards', models.CharField(default='-', max_length=255, verbose_name='Vārds')),
                ('uzvards', models.CharField(default='-', max_length=255, verbose_name='Uzvārds')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
