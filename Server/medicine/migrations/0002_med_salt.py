# Generated by Django 4.0.3 on 2022-04-07 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med_salt',
            fields=[
                ('salt_uid', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=20)),
                ('salt_qty', models.DecimalField(decimal_places=3, max_digits=5)),
                ('salt_qty_type', models.CharField(max_length=20)),
                ('salt_desc', models.TextField()),
                ('med_uid', models.ForeignKey(db_column='med_uid', on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
    ]
