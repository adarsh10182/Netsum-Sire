# Generated by Django 4.0.5 on 2022-06-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sireproj', '0003_delete_questn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chapter', models.CharField(max_length=3)),
                ('Stext', models.CharField(max_length=100)),
                ('FText', models.CharField(max_length=400)),
                ('Qno', models.CharField(max_length=10)),
                ('HQtn', models.CharField(max_length=30)),
                ('PQtn', models.CharField(max_length=30)),
                ('HuQtn', models.CharField(max_length=30)),
                ('Qtype', models.CharField(max_length=10)),
                ('Chemical', models.BooleanField()),
                ('LNG', models.BooleanField()),
                ('LPG', models.BooleanField()),
                ('Oil', models.BooleanField()),
                ('Conditional', models.BooleanField()),
                ('Roviq', models.CharField(max_length=300)),
            ],
        ),
    ]
