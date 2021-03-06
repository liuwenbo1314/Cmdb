# Generated by Django 2.2.1 on 2019-12-30 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=32, verbose_name='单位,集团下属机构名字')),
                ('address', models.TextField(verbose_name='所在地')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='中文名')),
                ('QQ', models.CharField(max_length=32, verbose_name='QQ号')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Company')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
