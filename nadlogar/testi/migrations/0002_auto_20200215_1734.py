# Generated by Django 3.0.3 on 2020-02-15 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['datum', 'naslov'], 'verbose_name_plural': 'testi'},
        ),
    ]