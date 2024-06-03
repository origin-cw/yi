import torch


print('Torch Version:',torch.__version__)
print('CUDA GPU check:',torch.cuda.is_available())
print('CUDA GPU num:', torch.cuda.device_count())



if(torch.cuda.is_available()):
  print('CUDA GPU num:', torch.cuda.device_count())
  n=torch.cuda.device_count()
while n > 0:
  print('CUDA GPU name:', torch.cuda.get_device_name(n-1))
  n -= 1



print(torch.__version__) #查看torch版本

print(torch.version.cuda)#查看cuda版本

print(torch.backends.cudnn.version())#查看cudnn版本


