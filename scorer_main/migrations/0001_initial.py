# Generated by Django 2.0.1 on 2018-01-25 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_data', models.TextField(null=True)),
                ('match1_data', models.TextField(null=True)),
                ('practice_noshow', models.NullBooleanField()),
                ('match1_noshow', models.NullBooleanField()),
                ('match2_data', models.NullBooleanField()),
                ('match3_data', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Scorekeeper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privilege', models.CharField(choices=[('AD', 'Admin'), ('SC', 'Score Keeper')], max_length=2)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorer_main.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('json_shema', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('team_number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('admin', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='scorekeeper',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorer_main.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorer_main.Season'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorer_main.Event'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorer_main.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='scorekeeper',
            unique_together={('user', 'event')},
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('team', 'event')},
        ),
    ]