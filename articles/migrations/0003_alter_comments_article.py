# Generated by Django 4.0.10 on 2025-07-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.articles'),
        ),
    ]
