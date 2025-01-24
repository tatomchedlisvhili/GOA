#1
def double_integer(i):
    return i*2

#2
def friend(x):
    name = []
    for i in x:
        if len(i) == 4:
            name.append(i)
    return name


#3
def grow(arr):
    num1 = 1
    for i in arr:
        num1 *= i
    return num1 
    
    
#4
def find_average(numbers):
    if numbers == [] :
        return 0
    else:
        return sum(numbers) / len(numbers)
    

#5
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague



#6
def double_char(s):
    result = ""
    for i in s:
        result = result + i*2
        
    return result

#7
def remove_url_anchor(url):
    result = ""
    for i in url:
        if i == "#":
            break
        else:
            result +=i
    return result

#8
def sum_cubes(n):
    result = 0
    for i in range(1,n+1):
        result = result + i**3
    return result