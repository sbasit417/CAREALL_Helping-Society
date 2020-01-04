

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0007_auto_20180720_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
