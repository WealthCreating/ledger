# Generated by Django 2.0.5 on 2018-10-04 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_exclude_accounts_from_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, help_text='Date of credit score report')),
                ('score', models.PositiveSmallIntegerField(help_text='Credit score between 0 and 850')),
                ('source', models.CharField(choices=[('Experian', 'Experian'), ('Equifax', 'Equifax'), ('TransUnion', 'TransUnion')], help_text='The credit bureau that generated the report', max_length=255)),
                ('preferred', models.BooleanField(default=True, help_text='If this score should be used over others in the month')),
                ('memo', models.CharField(blank=True, help_text='A short memo or note about the credit score', max_length=255, null=True)),
            ],
            options={
                'db_table': 'credit_scores',
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
        ),
    ]