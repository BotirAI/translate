# Generated by Django 4.0.1 on 2022-01-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translateapi', '0003_rename_to_id_translate_to_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='translate',
            name='izox',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]