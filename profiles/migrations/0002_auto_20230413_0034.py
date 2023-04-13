# Generated by Django 3.2.18 on 2023-04-13 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_about_me_public',
            new_name='is_about_me',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_branch_of_military_served_public',
            new_name='is_branch_of_military_served',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_fullname_public',
            new_name='is_fullname',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_length_of_service_public',
            new_name='is_length_of_service',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_linkedin_public',
            new_name='is_linkedin',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_past_deployments_public',
            new_name='is_past_deployments',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_preferred_display_name_public',
            new_name='is_preferred_display_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_profile_picture_public',
            new_name='is_profile_picture',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_rank_public',
            new_name='is_rank',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_user_email_public',
            new_name='is_user_email',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_user_phone_public',
            new_name='is_user_phone',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
