
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0009_auto_20180721_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myjob',
            name='own',
        ),
        migrations.RemoveField(
            model_name='myjob',
            name='user',
        ),
        migrations.AddField(
            model_name='job',
            name='job_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_jobs', to='its_login_register.User'),
        ),
        migrations.DeleteModel(
            name='Myjob',
        ),
    ]
