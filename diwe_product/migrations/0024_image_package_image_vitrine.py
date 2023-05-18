# Generated by Django 4.1.7 on 2023-05-14 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0023_accueil'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.package'),
        ),
        migrations.AddField(
            model_name='image',
            name='vitrine',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]