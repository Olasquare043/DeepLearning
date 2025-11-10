import torch
print(torch.__version__)
print("CUDA available:", torch.cuda.is_available())


# trying tensor
x= torch.tensor([7,2,3,5])
print(x)