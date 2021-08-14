from math import gcd

def mixed_fraction(s):
  
  """ FAILED ATTEMPT - PASSED THE TESTS BUT FAILED SUBMISSION
  
  Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

  [sign]a b/c

  where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

  If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

  Division by zero should raise an error (preferably, the standard zero division error of your language).
  
  
  WORKING SOLUTION:
  
  from fractions import Fraction

  def mixed_fraction(string):
    frac = Fraction(*map(int, string.split("/")))
    if frac.denominator == 1:
        return f"{frac.numerator}"
    whole = int(
        abs(frac.numerator) / frac.denominator * (1 if frac.numerator > 0 else -1)
    )
    frac = abs(frac - whole) if whole else frac - whole
    return f"{whole} {frac}" if whole else f"{frac}"
  
  """
    
    s_split = s.split("/")
    # a/b
    a = int(s_split[0])
    b = int(s_split[-1])
    a_abs = abs(a)
    b_abs = abs(b)
    
    if a == 0 and b != 0:
        return '0'
    elif b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    
    int_div = a_abs // b_abs
    mod = a_abs % b_abs
    _gcd = int(gcd(a_abs, b_abs))
    
    if mod == 0:
        return str(int_div)
    elif (b_abs > a_abs) and (b < a):
        return "{}/{}".format(int(a/_gcd), abs(int((b/_gcd))))
    elif b_abs > a_abs:
        return "{}/{}".format(int(a/_gcd), int(b/_gcd)) 
    else:
        if (a < 0 or b < 0) is not (a < 0 and b < 0):
            return "{} {}/{}".format(int_div*-1, abs(int(mod/_gcd)), abs(int(b/_gcd)))
        else:
            return "{} {}/{}".format(int_div, abs(int(mod/_gcd)), abs(int(b/_gcd)))
