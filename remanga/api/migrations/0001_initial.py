# Generated by Django 4.1.3 on 2022-11-08 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(default='', max_length=100)),
                ('alternative_names', models.CharField(default='', max_length=300)),
                ('description', models.TextField(default='')),
                ('tags', models.ManyToManyField(blank=True, related_name='titles_with_tag+', to='api.tag')),
            ],
            options={
                'ordering': ['russian_name'],
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('cost', models.IntegerField()),
                ('position', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='api.title')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('cost', models.IntegerField()),
                ('position', models.IntegerField()),
                ('watch_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='api.volume')),
            ],
            options={
                'ordering': ['volume', 'position'],
            },
        ),
    ]
