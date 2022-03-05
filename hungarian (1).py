import numpy as np

A = np.random.randint(10,size=(20, 20))

def stp1_a(zm, mzm):
  min_x = [99999, -1]
  for i in range(zm.shape[0]): 
    if np.sum(zm[i] == True) > 0 and min_x[0] > np.sum(zm[i] == True):
      min_x = [np.sum(zm[i] == True), i]
    
  index = np.where(zm[min_x[1]] == True)[0][0]
  zm[:, index] = False
  zm[min_x[1], :] = False
  mzm.append((min_x[1], index))

def stp_2(A):
  
  Ac = A
  Acb = (Ac == 0)
  Acbc = Acb.copy()
  mzm = []
  while (True in Acbc):
	  stp1_a(Acbc, mzm)
  mzr = []
  mzc = []
  for i in range(len(mzm)):
    mzr.append(mzm[i][0])
    mzc.append(mzm[i][1])
  nmr = list(set(range(Ac.shape[0])) - set(mzr))
  mc = []
  boo = True
  while boo:
    boo = False
    for i in range(len(nmr)):
      ra = Acb[nmr[i], :]
      for j in range(ra.shape[0]):
        if ra[j] == True and j not in mc:
          mc.append(j)
          boo = True
    for x, y in mzm:
      if x not in nmr and y in mc:
        nmr.append(x)
        boo = True
  xr = list(set(range(A.shape[0])) - set(nmr))
  return(mzm, xr, mc)

def stp_3(A, cr, cc):
  Ac = A
  non_zero_element = []
  for x in range(len(Ac)):
    if x not in cr:
      for i in range(len(Ac[x])):
        if i not in cc:
          non_zero_element.append(Ac[x][i])
  q= min(non_zero_element)
  for x in range(len(Ac)):
    if x not in cr:
      for i in range(len(Ac[x])):
        if i not in cc:
          Ac[x, i] = Ac[x, i] - q
  for x in range(len(cr)):  
    for y in range(len(cc)):
      Ac[cr[x], cc[y]] = Ac[cr[x], cc[y]] + q
  return Ac

def the_hungarian(A): 
  l = A.shape[0]
  Ac = A
  for i in range(A.shape[0]): 
    Ac[i] = Ac[i] - np.min(Ac[i])
  for j in range(A.shape[1]): 
    Ac[:,j] = Ac[:,j] - np.min(Ac[:,j])
  count = 0
  while count < l:
    a, mr, mc = stp_2(Ac)
    count = len(mr) + len(mc)
    if count < l:
      Ac = stp_3(Ac, mr, mc)
  return a

def ans_calculation(A, pp):
  total = 0
  final = np.zeros((A.shape[0], A.shape[1]))
  for i in range(len(pp)):
    total += A[pp[i][0], pp[i][1]]
    final[pp[i][0], pp[i][1]] = A[pp[i][0], pp[i][1]]
  return total, final

ap = the_hungarian(A.copy())
a, AA = ans_calculation(A, ap)
print(f"Answer: {a:.0f}\n{AA}")
