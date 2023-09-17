# -*- coding: utf-8 -*-
import time
import kernel.mem as mem


class Task:
    def __init__(self):
        pass

    def __call__(self, mem_proxy: mem.MemoryProxy):
        pass


class TaskIdle(Task):
    def __call__(self, *args, **kwargs):
        time.sleep(0.1)


class Scheduler:
    def __init__(self):
        pass

    def execute(self):
        pass


class FifoScheduler(Scheduler):
    def __init__(self, tasks: list = None):
        super().__init__()
        # Create an idle task.
        if tasks is None:
            tasks = [TaskIdle()]
        self.__mem_proxy = mem.usr.get_proxy()
        self.__task_pool = tasks

    def execute(self):
        # Call all the tasks inside the function.
        for task in self.__task_pool:
            task(self.__mem_proxy)


def get_scheduler(*args, **kwargs) -> Scheduler:
    return FifoScheduler(*args, **kwargs)
