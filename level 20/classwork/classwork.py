def string_to_number(s):
    return int(s)


def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"
    


def make_upper_case(s):
    return s.upper()


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    


def make_negative( number ):
    if number < 0:
        return number
    else:
        return -number
    

def square_sum(numbers):
    result = 0
    
    for i in numbers:
        result += i ** 2
        
    return result