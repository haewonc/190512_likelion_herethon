# Generated by Django 2.1.7 on 2019-05-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
