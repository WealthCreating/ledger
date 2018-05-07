# Generated by Django 2.0.5 on 2018-05-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_add_account_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ('bank__short_name', 'name')},
        ),
        migrations.AlterModelOptions(
            name='balance',
            options={'ordering': ('-sheet__date', 'account__order')},
        ),
        migrations.AlterModelOptions(
            name='balancesheet',
            options={'get_latest_by': 'date', 'ordering': ('-date',)},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('short_name',), 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'get_latest_by': 'date', 'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='transaction',
            name='complete',
            field=models.BooleanField(default=False, help_text='If the transaction is included in the beginning balance'),
        ),
    ]
