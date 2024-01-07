from __future__ import absolute_import, unicode_literals
# Загрузить модуль с задачами, чтобы Celery обнаружил их
from . import tasks

__all__ = ('tasks',)