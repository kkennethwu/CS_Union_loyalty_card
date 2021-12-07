# Generated by Django 3.2.9 on 2021-12-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0006_auto_20211207_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='id',
        ),
        migrations.AlterField(
            model_name='sheet',
            name='student_id',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='uid',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
