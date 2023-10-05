#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(94, 103):
        try:
            i > a
        except:
            print("Too far")
            result = result + a ** b / i
            break
        result = a + b        
    finally:
        return result
