import torch
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(torch.device("cuda"))
    print(os.path.dirname(__file__)+"/.env.closeai")