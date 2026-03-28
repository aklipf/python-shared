import torch

import multiprocessing as mp

from monitoring import Monitoring

def main():
    monitor = Monitoring()
    queue = mp.Queue()

    tensor = torch.zeros((1<<30,),dtype=torch.uint8)

    monitor.info()
    print(f"is_shared: {tensor.is_shared()}")


    print("send to a queue")
    queue.put(tensor)
    tensor = queue.get()

    monitor.info()
    print(f"is_shared: {tensor.is_shared()}")

if __name__ == "__main__":
    main()
