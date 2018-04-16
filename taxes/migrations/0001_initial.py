# Generated by Django 2.0.4 on 2018-04-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(help_text='Tax year the return was filed for')),
                ('wages', models.DecimalField(decimal_places=2, help_text='Wages, salaries and tips', max_digits=10)),
                ('interest', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Interest, taxable and tax-exempt combined', max_digits=10)),
                ('profit', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Business income (or loss)', max_digits=10)),
                ('dividends', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Ordinary and qualified dividends', max_digits=10)),
                ('capital_gains', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Capital gains (or loss)', max_digits=10)),
                ('royalties', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text='Rental real estate, royalties, partnerships, etc', max_digits=10)),
                ('income', models.DecimalField(decimal_places=2, help_text='Total reported income including other fields', max_digits=10)),
                ('agi', models.DecimalField(decimal_places=2, help_text='Adjusted gross income after non-taxable income removed', max_digits=10, verbose_name='adjusted gross income')),
                ('taxable_income', models.DecimalField(decimal_places=2, help_text='Taxable income after itemized deductions', max_digits=10)),
                ('federal_tax', models.DecimalField(decimal_places=2, help_text='Total amount owed or paid in Federal taxes', max_digits=10)),
                ('local_tax', models.DecimalField(decimal_places=2, help_text='Total amount owed or paid in state and local taxes', max_digits=10)),
            ],
        ),
    ]