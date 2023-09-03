# Generated by Django 4.1.5 on 2023-05-20 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NV_control', '0004_company_expense_catagory_company_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_user',
            name='student_id',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company_expense',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='NV_control.company_expense_catagory'),
        ),
    ]