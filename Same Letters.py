def shomar (st,a):
  n=0
  for i in st:
    if i==a:
      n+=1
  return n

def bh (k1,k2):
  for i in k1:
    j=1
    if shomar(k1,i)==shomar(k2,i):
      pass
    else:
      j=0
      break
  if j==1:
    return 'Yes'
  else:
    return 'No'
