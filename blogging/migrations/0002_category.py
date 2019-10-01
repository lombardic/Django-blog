# Generated by Django 2.1.1 on 2019-10-01 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='modeified_date',
            new_name='modified_date',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post'),
        ),
    ]
