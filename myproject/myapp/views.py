from django.shortcuts import render
from myapp.tasks import example_task


def my_view(request):

    result = example_task.delay()
    print(f"Task ID: {result.id}")

    return render(request, 'my_template.html', {'result_id': result.id})
