# Generated by Django 4.2.6 on 2023-10-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(max_length=500)),
                ('period', models.CharField(max_length=100)),
                ('technologiesSkills', models.ManyToManyField(to='experiences.technologyskill')),
            ],
        ),
    ]
