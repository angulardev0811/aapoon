# Generated by Django 2.2.9 on 2020-02-02 15:13

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_card_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_section_subscribe',
            field=wagtail.core.fields.RichTextField(default='Input here...'),
        ),
    ]