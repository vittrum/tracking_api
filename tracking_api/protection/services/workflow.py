from protection.models import Task


def report_work_start(task: Task) -> bool:
    try:
        task.state = 'worker started'
        task.save()
        print('worker approved the task!')
        return True
    except RuntimeError:
        print('Task is not approved by worker!')
        return False


def report_work_end(task: Task) -> bool:
    try:
        task.state = 'worker ended'
        task.save()
        print('worker approved the task!')
        return True
    except RuntimeError:
        print('Task is not ended by worker!')
        return False


def approve_task(task: Task) -> bool:
    try:
        task.state = 'worker ended'
        task.save()
        print('client approved the task!')
        return True
    except RuntimeError:
        print('Client not performed a task!')
        return False


