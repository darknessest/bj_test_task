# Generated by Django 3.2.4 on 2021-06-13 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('task_text', models.TextField()),
                ('edited_by_admin', models.BooleanField(default=False)),
                ('task_status', models.IntegerField(choices=[(0, 'not done'), (1, 'not done edited'), (10, 'done'), (11, 'done edited')], default=0)),
            ],
        ),
    ]