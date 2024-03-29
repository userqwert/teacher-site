# Generated by Django 4.2.7 on 2024-02-05 15:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Який клас додається')),
                ('img_sub', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Картинка чи фото для класу')),
            ],
            options={
                'verbose_name': 'Клас',
                'verbose_name_plural': 'Класи',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Тема уроку')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Текс для читача')),
                ('imgforles', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Заставка до уроку')),
                ('les_img', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Картинка для ознайомлення')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='lesson_files/', verbose_name='ПДФ Файл')),
                ('presentation', models.URLField(blank=True, null=True, verbose_name='Презентація')),
                ('youtube_video_url', models.URLField(blank=True, null=True, verbose_name='Відео з YouTube')),
                ('docx_file', models.URLField(blank=True, null=True, verbose_name='DOCX Файл')),
                ('google_form', models.URLField(blank=True, null=True, verbose_name='Форма для тестів')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='work_classes.workclass')),
            ],
        ),
    ]
