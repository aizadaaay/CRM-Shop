# shop/migrations/0014_alter_покупатель_user.py

from django.db import migrations, models
from django.contrib.auth.models import User

def set_default_user(apps, schema_editor):
    UserModel = apps.get_model('auth', 'User')
    # Найдите первого пользователя
    first_user = UserModel.objects.first()
    if first_user:
        # Устанавливаем значение по умолчанию для всех существующих записей
        Покупатель = apps.get_model('shop', 'Покупатель')
        Покупатель.objects.filter(user__isnull=True).update(user=first_user)

class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.AlterField(
            model_name='покупатель',
            name='user',
            field=models.OneToOneField(on_delete=models.CASCADE, to='auth.User', default=None),
        ),
        migrations.RunPython(set_default_user),
    ]
