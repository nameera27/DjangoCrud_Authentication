# Generated by Django 4.2 on 2023-06-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_is_authenticate_alter_teacher_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
