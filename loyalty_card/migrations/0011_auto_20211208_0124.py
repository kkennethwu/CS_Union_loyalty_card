# Generated by Django 3.2.9 on 2021-12-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty_card', '0010_auto_20211208_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='grade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='student_id',
            field=models.CharField(max_length=20),
        ),
    ]
