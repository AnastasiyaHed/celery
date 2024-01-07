from celery import shared_task
import time

@shared_task
def example_task():
    print("Выполнение примера задачи...")
    time.sleep(5)
    print("Пример выполненного задания.")
