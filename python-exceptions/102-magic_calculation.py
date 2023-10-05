#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(94, 103):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result = result + a ** b / i
        except:
            result = a + b        
        finally:
            return result
