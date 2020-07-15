# Generated by Django 3.0.6 on 2020-07-14 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0004_auto_20200713_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicchainblock',
            name='previous_block',
        ),
        migrations.AddField(
            model_name='publicchainblock',
            name='side_block',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blockchain.SideChainBlock'),
            preserve_default=False,
        ),
    ]