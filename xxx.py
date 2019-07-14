import torch

a = torch.randn(10,3,5)
b = torch.split(a, 1, dim=0)
c = []
print("\n\n")
for x in b :
    x = torch.squeeze(x,0)
    c.append(x)
    


c = torch.stack(c,dim=0)

x = torch.tensor([1, 2, 3, 4])
#print(x)
#print(x.size())
x = torch.unsqueeze(x, 0)
x = torch.unsqueeze(x, 2)
#print(x)
#print(x.size())

a = torch.randn(10,3,1)
b = torch.randn(10,1,1)
c = torch.bmm(a,b)
#print(c.size())

a = torch.randn(10,3)
a = torch.unsqueeze(a,1)
#print(a.size())

length = [3,5,2,7,4]
mask = torch.zeros(5,7)
print(mask)
for id,x in enumerate(length) :
    mask[id,x:] = 1
print(mask)




