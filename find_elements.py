def find_elements(p,find):
   i=o
   while i<=len(p):
      if p[i] == find:
         return i
      i = i + 1
   return -1

#  otra version
   i = 0
   for e in p:
      if e == find:
         return i
      i = i + 1
   return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1                                                                                                                                                                       
~                      
