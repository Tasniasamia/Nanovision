# Generated by Django 4.1.5 on 2023-05-21 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NV_control', '0005_student_user_student_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Student_Waiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('remarks', models.TextField(max_length=750)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='NV_control.student_user')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Student_Submited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('document', models.ManyToManyField(to='NV_control.course_necessary_document')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.student_user')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Student_Penalti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('remarks', models.TextField(max_length=750)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='NV_control.student_user')),
            ],
        ),
    ]
