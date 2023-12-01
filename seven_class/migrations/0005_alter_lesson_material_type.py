# Generated by Django 4.2.7 on 2023-11-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven_class', '0004_lesson_material_type_alter_lesson_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='material_type',
            field=models.CharField(blank=True, choices=[('image', 'Изображение'), ('docx', 'Документ (docx)'), ('pdf', 'Документ (pdf)'), ('presentation', 'Презентация'), ('youtube', 'Видео (YouTube)'), ('text', 'Текст')], max_length=20, null=True),
        ),
    ]
