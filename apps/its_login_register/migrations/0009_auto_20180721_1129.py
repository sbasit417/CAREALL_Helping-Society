

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0008_myjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myjob',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='myjob',
            name='user_id',
        ),
        migrations.AddField(
            model_name='myjob',
            name='own',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='own', to='its_login_register.Job'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myjob',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_user', to='its_login_register.User'),
        ),
    ]
