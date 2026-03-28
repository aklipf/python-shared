import psutil

from enum import Enum

class Unit(Enum):
    B = 0
    KB = 10
    MB = 20
    GB = 30

class Monitoring:
    def __init__(self):
        self.process = psutil.Process()

    def num_file_descriptor(self) -> int:
        return self.process.num_fds()

    def shared_memory(self, unit:Unit=Unit.MB) -> int:
        return self.process.memory_info().shared>>unit.value

    def info(self):
        print("Monitoring")
        print(f"- file desciptor: {self.num_file_descriptor()}")
        print(f"- shared memory: {self.shared_memory()}Mb")

