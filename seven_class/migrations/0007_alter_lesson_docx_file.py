# Generated by Django 4.2.7 on 2023-11-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven_class', '0006_delete_materialtype_remove_lesson_material_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='docx_file',
            field=models.URLField(blank=True, null=True),
        ),
    ]