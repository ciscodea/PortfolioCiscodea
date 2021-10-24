# Generated by Django 3.2.8 on 2021-10-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='skill name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='skill description')),
                ('icon', models.ImageField(blank=True, height_field=80, null=True, upload_to='images/skills/icons/', verbose_name='skill icon', width_field=80)),
                ('since_date', models.DateField(help_text='since what date did you acquire this skill', verbose_name='skill from date')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
    ]