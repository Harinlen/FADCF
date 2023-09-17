# -*- coding: utf-8 -*-
import pickle
import multiprocessing


class MemoryProxy:
    def __init__(self, data, lock: multiprocessing.Lock):
        self.__data = data
        self.__lock = lock

    def set(self, key: str, item):
        with self.__lock:
            self.__data[key] = item
            return item

    def get(self, key: str):
        return self.__data[key]


class Memory:
    def __init__(self):
        self.__data = dict()
        self.__proxy = multiprocessing.Manager().dict(self.__data)
        self.__lock = multiprocessing.Lock()

    def get_proxy(self) -> MemoryProxy:
        return MemoryProxy(self.__data, self.__lock)

    def dump(self, file):
        # Dump the memory dict pool to the file.
        with self.__lock:
            pickle.dump(self.__data, file)
