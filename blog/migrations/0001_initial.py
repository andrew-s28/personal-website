# Generated by Django 4.2.11 on 2024-05-26 04:52

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tinymce/')),
            ],
            options={
                'verbose_name': 'Uploaded image',
                'verbose_name_plural': 'Uploaded images',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='picture_lead')),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('title',), unique=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
