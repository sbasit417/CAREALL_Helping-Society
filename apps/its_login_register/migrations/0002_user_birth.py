
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
