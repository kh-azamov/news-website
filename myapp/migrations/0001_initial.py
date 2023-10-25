# Generated by Django 4.2.5 on 2023-10-16 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='article')),
                ('url', models.URLField()),
                ('category', models.CharField(choices=[('P', 'Politics'), ('S', 'Sports'), ('E', 'Economics'), ('T', 'Technologies'), ('M', 'Medicine'), ('B', 'Business'), ('o', 'Other')], max_length=1)),
                ('important', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.author')),
            ],
        ),
    ]
