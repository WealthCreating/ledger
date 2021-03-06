# Generated by Django 2.0.5 on 2018-05-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('GBP', 'GBP'), ('EUR', 'EUR'), ('CNY', 'CNY'), ('JPY', 'JPY'), ('MXN', 'MXN')], default='USD', help_text='Specify the currency associated with the account', max_length=3),
        ),
    ]
