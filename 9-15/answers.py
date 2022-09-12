
#Chapter 7 Question 7
from cmath import atan
from socket import BTPROTO_RFCOMM


def is_even(n):
    if(n % 2 == 0):
        return True
    else:
        return False

def is_odd(n):
    if(n % 2 == 1):
        return True
    else:
        return False
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