# Generated by Django 4.2.dev20220718043020 on 2022-07-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_no', models.CharField(max_length=10)),
                ('module_code', models.CharField(max_length=8)),
                ('mark', models.IntegerField(choices=[(0, 'NP'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Atzīme')),
            ],
            options={
                'db_table': 'marks',
            },
        ),
    ]
