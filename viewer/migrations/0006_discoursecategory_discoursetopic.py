# Generated by Django 3.1 on 2020-12-04 14:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewer', '0005_actiontype_sessionactions_snapshotactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscourseTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(15, 'Discourse Topic Title must be longer than 15 characters')])),
                ('discourse_topic_id', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'viewer_discoursetopic',
            },
        ),
        migrations.CreateModel(
            name='DiscourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('discourse_category_id', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'viewer_discoursecategory',
            },
        ),
    ]
