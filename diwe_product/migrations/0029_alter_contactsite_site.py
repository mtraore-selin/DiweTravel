# Generated by Django 4.1.7 on 2023-05-15 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0028_alter_commande_code_postal_alter_commande_numero_rue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsite',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.site'),
        ),
    ]