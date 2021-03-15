# Generated by Django 3.0.7 on 2020-12-01 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.StudentGroup')),
            ],
            options={
                'verbose_name_plural': 'quizzes',
                'ordering': ['date', 'name'],
            },
        ),
    ]
