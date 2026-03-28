import torch
import multiprocessing as mp


def main():
    queue = mp.Queue()

    tensor = torch.rand((1<<28))

    print("is_shared:",tensor.is_shared())
    
    print("send to a queue")
    queue.put(tensor)

    tensor = queue.get()

    print("is_shared:",tensor.is_shared())

    input("press enter to continue")


if __name__ == "__main__":
    main()
