# Generated by Django 2.0.6 on 2018-07-01 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Campaign'),
        ),
    ]
