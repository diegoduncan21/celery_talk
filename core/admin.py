from django.contrib import admin

from djcelery.models import TaskMeta


class TaskMetaAdmin(admin.ModelAdmin):
    list_display = [
        'task_id',
        'status',
        'result',
        'date_done',
        'traceback',
        'hidden',
    ]


admin.site.register(TaskMeta, TaskMetaAdmin)
