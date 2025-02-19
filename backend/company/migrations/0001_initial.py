# Generated by Django 4.0.3 on 2022-05-04 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('com_uid', models.AutoField(primary_key=True, serialize=False)),
                ('com_name', models.CharField(max_length=20)),
                ('com_licence_no', models.CharField(max_length=20)),
                ('com_address', models.CharField(max_length=50)),
                ('com_contact_no', models.CharField(max_length=15)),
                ('com_email', models.EmailField(max_length=254)),
                ('com_description', models.TextField()),
                ('com_joindate', models.DateField(auto_now_add=True)),
                ('com_account_no', models.CharField(max_length=20)),
                ('bank_uid', models.ForeignKey(db_column='bank_uid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank.bank')),
            ],
        ),
    ]
