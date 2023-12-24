# Generated by Django 5.0 on 2023-12-24 16:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StrtatupMangaerProfile',
            new_name='StartupManagerProfile',
        ),
        migrations.CreateModel(
            name='InvestorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inverstor_phone_number', models.CharField(max_length=10)),
                ('specialization', models.CharField(max_length=255)),
                ('inverstor_avatar', models.ImageField(default='iamges/default.jpg', upload_to='images/')),
                ('inverstor_birth_day', models.DateField()),
                ('inverstor_x_link', models.URLField()),
                ('inverstor_bio', models.TextField()),
                ('inverstor_city', models.CharField(max_length=255)),
                ('inverstor_LinkedIn', models.URLField()),
                ('invested_campany', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=56)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='InverstorProfile',
        ),
    ]