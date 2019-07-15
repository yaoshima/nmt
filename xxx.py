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
#print(mask)
for id,x in enumerate(length) :
    mask[id,x:] = 1
#print(mask)
    
x = torch.tensor([1, 2, 3, 4])
x = x.unsqueeze(1)
#print(x.size())

pad_token = "?"
s = [['a','b','c','d'],['a','b'],['a','b','c']]
longest_len = max(map(len,s))
print(longest_len)
not_the_longest = [ss for ss in s if len(ss) < longest_len]
print(not_the_longest)
for x in not_the_longest :
        #while(len(s) != longest_len) :
            #s.append(pad_token)
        padded_num = longest_len - len(x)
        sa = [pad_token * padded_num]
        print(sa)
        x.extend( [pad_token] * padded_num )
print(s)




