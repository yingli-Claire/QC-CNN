import torch 

print(torch.version.__version__)
print(torch.cuda.is_available())

a=torch.ones(3,3)
print(a)

b=torch.ones(3,3)
print(b)

print(a+b)

a=a.to('cuda')
b=b.to('cuda')
print(a+b)

a=a.to('cpu')
#print(a+b)

