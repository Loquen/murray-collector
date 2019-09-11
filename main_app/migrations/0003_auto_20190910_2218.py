# Generated by Django 2.2.3 on 2019-09-10 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='bill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Bill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotes',
            name='text',
            field=models.CharField(default='urrrgggghh (Zombie Sounds)', max_length=250),
        ),
    ]
