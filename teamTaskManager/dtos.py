class TaskDTO(object):

    def __init__(self, task_id, name, additional_info, priority, is_completed):
        self.task_id = task_id
        self.name = name
        self.additional_info = additional_info
        self.priority = priority
        self.is_completed = is_completed


class WorkerDTO(object):

    def __init__(self, worker_id, first_name, last_name, role, is_busy):
        self.worker_id = worker_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.is_busy = is_busy
