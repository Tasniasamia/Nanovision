# Generated by Django 4.1.5 on 2023-05-04 11:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_full_name', models.CharField(max_length=500)),
                ('c_short_name', models.CharField(max_length=500)),
                ('logo', models.ImageField(upload_to='media /company/logo/')),
                ('location', models.TextField(max_length=800)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('short_name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=25)),
                ('number_of_class', models.PositiveIntegerField()),
                ('payment_system', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=50)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=30)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Feese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_time', models.TimeField()),
                ('e_time', models.TimeField(null=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
            ],
        ),
        migrations.CreateModel(
            name='Office_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=150)),
                ('name_english', models.CharField(max_length=150, null=True)),
                ('date_of_bath', models.DateField(null=True)),
                ('father_name', models.CharField(max_length=250, null=True)),
                ('mother_name', models.CharField(max_length=250, null=True)),
                ('present_address', models.TextField(max_length=500, null=True)),
                ('cell_number_1', models.CharField(max_length=15)),
                ('cell_number_2', models.CharField(max_length=15)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discount', models.FloatField(default=0)),
                ('name_english', models.CharField(max_length=150, null=True)),
                ('name_bangla', models.CharField(max_length=250, null=True)),
                ('nich_name', models.CharField(max_length=250, null=True)),
                ('date_of_bath', models.DateField(null=True)),
                ('blood_group', models.CharField(max_length=5, null=True)),
                ('father_name', models.CharField(max_length=250, null=True)),
                ('mother_name', models.CharField(max_length=250, null=True)),
                ('father_occupation', models.CharField(max_length=250, null=True)),
                ('present_address', models.TextField(max_length=500, null=True)),
                ('cell_number_student', models.CharField(max_length=15)),
                ('cell_number_guardian', models.CharField(max_length=15)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
                ('course_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NV_control.course_batch')),
                ('course_day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NV_control.course_day')),
                ('course_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course_feese')),
                ('course_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NV_control.course_time')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('reveive_by', models.CharField(max_length=80)),
                ('payment_id', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.student_user')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Necessary_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mandatory', models.BooleanField(default=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.course')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Help_Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('l_education', models.CharField(max_length=255)),
                ('degination', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Deactive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('c_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_active')),
            ],
        ),
        migrations.AddField(
            model_name='company_active',
            name='c_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NV_control.company_name'),
        ),
    ]