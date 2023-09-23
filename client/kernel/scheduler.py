# -*- coding: utf-8 -*-
import time
import importlib
from typing import Tuple, List
from kernel.exception import LogSchedulerLoadFailError
from kernel.mem import MemoryProxy


class Task:
    def __init__(self):
        pass

    def __call__(self, mem_proxy: MemoryProxy):
        pass


class TaskIdle(Task):
    def __call__(self, *args, **kwargs):
        time.sleep(0.1)


class Scheduler:
    def __init__(self, mem_proxy: MemoryProxy, tasks: list):
        self.tasks = tasks
        self.mem_proxy = mem_proxy

    def execute(self):
        pass


class FifoScheduler(Scheduler):
    def __init__(self, mem_proxy: MemoryProxy, tasks: list):
        super().__init__(mem_proxy, tasks)

    def execute(self):
        # Call all the tasks inside the function.
        for task in self.tasks:
            task(self.mem_proxy)


SCHEDULER_MAP = {
    '': FifoScheduler, # Default uses FIFO scheduler
    'fifo': FifoScheduler
}


def get_scheduler(mem_proxy: MemoryProxy) -> Scheduler:
    # Read the scheduler settings from usr directory.
    def __get_user_setting():
        # Set the default tasks and scheduler.
        usr_tasks = [TaskIdle()]
        usr_scheduler_type = FifoScheduler
        # Try to load user scheduler setting.
        try:
            usr_settings = importlib.import_module('usr.scheduler')
        except ModuleNotFoundError:
            return usr_tasks, usr_scheduler_type
        # Read the task setting.
        if hasattr(usr_settings, 'tasks'):
            usr_tasks = usr_settings.tasks
        if hasattr(usr_settings, 'method'):
            # Check the target type.
            setting_type = usr_settings.method
            if (isinstance(setting_type, type) and
                    issubclass(setting_type, Scheduler)):
                usr_scheduler_type = setting_type
            elif isinstance(setting_type, str):
                setting_type = setting_type.lower()
                if setting_type not in SCHEDULER_MAP:
                    raise LogSchedulerLoadFailError(
                        'Failed to find "{}" scheduler'.format(setting_type))
                usr_scheduler_type = SCHEDULER_MAP[setting_type]
            else:
                raise LogSchedulerLoadFailError(
                    'Unknown scheduler type setting "{}"'.format(
                        str(setting_type)))
        return usr_tasks, usr_scheduler_type

    tasks, scheduler_type = __get_user_setting()
    # Construct the scheduler.
    return scheduler_type(mem_proxy=mem_proxy, tasks=tasks)
