
from cmath import atan
from socket import BTPROTO_RFCOMM

#Q7
def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False
#Q8
def is_odd(n):
    if(n % 2 == 1):
        return True
    else:
        return False
#Q10-11
def is_rightangled(a,b,c):
    at = a**2
    bt = b**2
    ct = c**2
    
    if(at+bt==ct or bt+ct==at or ct+at==bt):
        return True
    else:
        return False


print(is_even(2))#True
print(is_even(3))#False
print(is_odd(3))#True
print(is_odd(2))#False
print(is_rightangled(5,3,4))#true
#Coding Bat
def hello_name(name):
  s = "Hello "+ name+ "!"
  return(s)
def make_out_word(out, word):
  s = out[0:2]+word+out[2:4]
  return s
def first_two(str):
  s = str[0:2]
  return s
