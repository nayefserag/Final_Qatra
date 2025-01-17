# Generated by Django 4.2 on 2023-05-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Sginup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='البريد الألكتروني'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=255, verbose_name='كلمة المرور'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password_confirmation',
            field=models.CharField(max_length=255, verbose_name='تأكيد كلمة المرور '),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='رقم الهاتف'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='اسم المستخدم'),
        ),
    ]
