# Generated by Django 5.1.4 on 2025-01-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_groups_user_user_permissions_alter_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
