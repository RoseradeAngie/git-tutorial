
def is_pdrom(h):

   for n in h:

       if h == h[::-1]:
           return True
       else:
           return False


print (is_pdrom("545"))

