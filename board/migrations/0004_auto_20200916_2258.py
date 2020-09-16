# Generated by Django 3.1.1 on 2020-09-16 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.board'),
        ),
    ]
