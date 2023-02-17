# Generated by Django 4.1.6 on 2023-02-14 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answere',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='op4',
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op4', models.CharField(max_length=100)),
                ('answere', models.CharField(max_length=100)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.question')),
                ('question_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.subject')),
            ],
            options={
                'verbose_name_plural': 'Option',
            },
        ),
    ]
