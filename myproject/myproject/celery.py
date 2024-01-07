from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения Django settings module для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Создайте экземпляр Celery и настройте его, используя настройки Django.
app = Celery('myproject')

# Загрузите модули задач из всех зарегистрированных конфигураций приложений Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживайте задачи из всех установленных конфигураций приложений Django.
app.autodiscover_tasks()
