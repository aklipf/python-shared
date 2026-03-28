import torch
import psutil

import multiprocessing as mp


def main():
    p = psutil.Process()
    queue = mp.Queue()

    tensor = torch.zeros((1<<30,),dtype=torch.uint8)


    print(f"is_shared: {tensor.is_shared()}")
    before = p.memory_info().shared


    print("send to a queue")
    queue.put(tensor)
    tensor = queue.get()


    after = p.memory_info().shared
    print(f"is_shared: {tensor.is_shared()}")
    shared_mem_diff = after-before
    print(f"shared memory: {shared_mem_diff>>20}Mb")

if __name__ == "__main__":
    main()
