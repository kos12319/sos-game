import random
import numpy as np

def create_array(x,y):
  '''διμιουργία τυχαίου πίνακα'''
  l3=[]
  for j in range (0,x):
    l=[]
    l2=[]
    for i in range(0,y):
      a = random.randrange(2)
      l.append(a)
    for i in l:
      if i==1:
        l2.append("S")
      else:
        l2.append("O")
    print(l2)
    l3.append(l2)
  return l3


def count_sos(sos_array):
  '''καταμέτρηση sos σε παραλληλόγραμμο πίνακα'''
  x = len(sos_array)
  y = len(sos_array[0])
  #καταμέτηση οριζοντίων sos
  print('--rows--')
  counts_x = 0
  for j in range (0, x):
    row = "".join(sos_array[j])
    # print(row)
    counts_x += row.count('SOS')
  print(counts_x)
  #καταμέτρηση καθέτων sos
  print('--columns--')

  counts_y = 0
  for j in range(0, y):
    column = "".join(sos_array[i][j] for i in range(0, x))
    # print(column)
    counts_y += column.count('SOS')
  print(counts_y)
  # καταμέτρηση διαγώνιων πάνω αριστερά προς κάτω δεξιά sos
  print('--left-diagonals---')

  l_count = 0
  l4 = np.array(sos_array)
  l_diag = ["".join(list(l4.diagonal(i))) for i in range(-x+1, y)]
  # print(l_diag)
  l_count += sum(s.count('SOS') for s in l_diag)
  print(l_count)
  # καταμέτρηση διαγώνιων πάνω δεξιά προς κάτω αριστερά sos
  print('--right-diagonals--')

  r_count = 0
  l5 = l4[::-1]
  r_diag = ["".join(list(l5.diagonal(i))) for i in range(-x+1, y)]
  # print(r_diag)
  r_count += sum(s.count('SOS') for s in r_diag)
  print(r_count)
  #καταμέτρηση όλων
  print('--- total ---')
  total = sum([counts_x, counts_y, l_count, r_count])
  print(total)
  return total

#είσοδος διαστάσεων απο χρήστη
m=int(input("give  row dimensions: "))
n=int(input("give column dimensions: "))
  #επαναληψη 100 φορές και εύρεση μέσου όρου
total = 0
for i in range(0,100):
  sos_array = create_array(n,m)
  total += count_sos(sos_array)
print('total', total)
print('mean', total/100)
