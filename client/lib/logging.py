# -*- coding: utf-8 -*-
import os
import sys
import traceback
from io import StringIO
from kernel.exception import RuntimeLogError, CriticalLogError
from datetime import datetime
from kernel.paths import DIR_STORAGE, ensure_dir
from kernel.mem import MemoryProxy

LOG_TO_CONSOLE = False

LOG_DIR = os.path.join(DIR_STORAGE, 'logs')
LOG_ERRORS = os.path.join(LOG_DIR, 'errors.txt')
LOG_WARNING = os.path.join(LOG_DIR, 'warnings.txt')
LOG_INFO = os.path.join(LOG_DIR, 'info.txt')


def open_log(path: str):
    return open(path, 'a')


class LogBuffer:
    def __init__(self, log_path: str, buf_size: int):
        self.log_path = log_path
        if LOG_TO_CONSOLE:
            return
        self.buffer = ['' for _ in range(buf_size)]
        self.buffer_pos = 0

    def flush(self):
        # Check pointer position.
        if LOG_TO_CONSOLE or self.buffer_pos == 0:
            return
        # Write the content line by line.
        with open_log(self.log_path) as log_file:
            if self.buffer_pos == len(self.buffer):
                print(*self.buffer, sep='\n', end='\n', file=log_file)
            else:
                print(*self.buffer[:self.buffer_pos], sep='\n', end='\n',
                      file=log_file)
        self.buffer_pos = 0

    @staticmethod
    def timestamp_text(timestamp: datetime):
        return '[{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}]'.format(
            timestamp.year, timestamp.month, timestamp.day,
            timestamp.hour, timestamp.minute, timestamp.second)

    def write_line(self, *objects, sep=' '):
        def __write_log(file, end):
            print(LogBuffer.timestamp_text(datetime.now()), *objects,
                  sep=sep, end=end, file=file)
        if LOG_TO_CONSOLE:
            __write_log(None, '\n')
            return

        # Flush the buffer when it is full.
        if self.buffer_pos == len(self.buffer):
            self.flush()
        # Write the content to the line buffer.
        with StringIO() as string_file:
            __write_log(string_file, '')
            # Save the buffer to list.
            self.buffer[self.buffer_pos] = string_file.getvalue()
            self.buffer_pos += 1


LOG_BUF_LIMIT = 128
info_buffer = LogBuffer(LOG_INFO, LOG_BUF_LIMIT)
warning_buffer = LogBuffer(LOG_WARNING, LOG_BUF_LIMIT)


def logging_start(mem_proxy: MemoryProxy):
    # Use console when debug mode enabled.
    global LOG_TO_CONSOLE
    LOG_TO_CONSOLE = mem_proxy.get('conf').DEBUG
    if LOG_TO_CONSOLE:
        return
    # Ensure directory exist.
    ensure_dir(LOG_DIR, 'Failed to create log directory.')
    # Ensure the file exist.
    open_log(LOG_ERRORS).close()
    open_log(LOG_WARNING).close()
    open_log(LOG_INFO).close()


def error(*objects, sep=' ', end='\n'):
    def __write_log(file):
        print(LogBuffer.timestamp_text(datetime.now()), *objects,
              sep=sep, end=end, file=file)

    if LOG_TO_CONSOLE:
        __write_log(sys.stderr)
        return

    # Error message needs to be written as soon as possible.
    with open_log(LOG_ERRORS) as error_log_file:
        __write_log(error_log_file)


def info(*objects, sep=' '):
    info_buffer.write_line(*objects, sep=sep)


def warning(*objects, sep=' '):
    warning_buffer.write_line(*objects, sep=sep)


def flush():
    info_buffer.flush()
    warning_buffer.flush()


def runtime_error_dump(exc: RuntimeLogError):
    # Print the exception in error log.
    error(*traceback.format_exception(exc), sep='')


def critical_error_dump(exc: CriticalLogError):
    # Print the critical error info.
    error(str(exc))
