import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('abstract_submission_deadline', models.DateTimeField()),
                ('paper_submission_deadline', models.DateTimeField()),
                ('review_deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('paper_file_path', models.TextField(null=True)),
                ('status', models.TextField(default='Not Submitted')),
                ('abstract_file_path', models.TextField()),
                ('upload_date', models.DateTimeField(default=datetime.datetime(
                    2019, 5, 30, 9, 39, 26, 161362, tzinfo=utc))),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('password', models.TextField()),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submits',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField(default=datetime.datetime(
                    2019, 5, 30, 9, 39, 26, 161860, tzinfo=utc))),
                ('submit_status', models.TextField(default='abstract_pending')),
                ('is_scheduled', models.BooleanField(default=False)),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
                ('conference', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Conference')),
                ('paper', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Paper', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('chair', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Chair')),
                ('conference', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Conference')),
                ('paper', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Creates',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('chair', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Chair')),
                ('conference', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text_abstract', models.TextField(null=True)),
                ('review_text_paper', models.TextField(null=True)),
                ('paper', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Paper')),
                ('reviewer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Reviewer')),
            ],
            options={
                'unique_together': {('paper', 'reviewer')},
            },
        ),
        migrations.CreateModel(
            name='Assigns',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('chair', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Chair')),
                ('conference', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Conference')),
                ('paper', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Paper')),
                ('reviewer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='main.Reviewer')),
            ],
            options={
                'unique_together': {('paper', 'reviewer')},
            },
        ),
    ]
