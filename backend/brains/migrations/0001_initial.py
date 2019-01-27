# Generated by Django 2.1.5 on 2019-01-27 16:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_admin', models.UUIDField(editable=False)),
                ('party_name', models.CharField(max_length=100)),
                ('party_code', models.IntegerField(unique=True)),
                ('party_playlist_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100)),
                ('user_access_token', models.CharField(max_length=100)),
                ('user_party', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brains.Parties')),
            ],
        ),
        migrations.AddField(
            model_name='tracks',
            name='track_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brains.Users'),
        ),
    ]
