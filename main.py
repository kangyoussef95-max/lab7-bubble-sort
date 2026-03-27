def bubble_sort(x : list):
    for i in range(len(x)):
     if x == x.sort():
         return x
     else:
           for j in range(0, len(x) - i - 1):
              if x[j] > x[j + 1]:
                  x[j], x[j + 1] = x[j + 1], x[j]
           return x
     