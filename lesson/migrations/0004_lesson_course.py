# Generated by Django 4.2.6 on 2023-10-17 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_photo'),
        ('lesson', '0003_alter_lesson_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='курс'),
            preserve_default=False,
        ),
    ]
