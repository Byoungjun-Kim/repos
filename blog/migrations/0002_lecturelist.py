# Generated by Django 2.1.5 on 2020-11-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureList',
            fields=[
                ('no', models.AutoField(db_column='NO', primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, db_column='CODE', max_length=200, null=True)),
                ('lecture', models.CharField(blank=True, db_column='LECTURE', max_length=200, null=True)),
                ('prof', models.CharField(blank=True, db_column='PROF', max_length=200, null=True)),
                ('location', models.CharField(blank=True, db_column='LOCATION', max_length=200, null=True)),
                ('start', models.IntegerField(blank=True, db_column='START', null=True)),
                ('end', models.IntegerField(blank=True, db_column='END', null=True)),
                ('day', models.CharField(blank=True, db_column='DAY', max_length=200, null=True)),
            ],
            options={
                'db_table': 'lecture_list',
                'managed': False,
            },
        ),
    ]
