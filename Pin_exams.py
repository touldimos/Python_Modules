default = ['Bsc', 'MSc']
for i, e in enumerate(zip(default, ['Geography', 'Geomatics']), start = 15):
    print(i, e)
    
plays = {
    'artist A':
        {'track A': 10, 'track B': 11},
    'artist B':
        {'track C': 4, 'track D': 7},}

plays['artist C'] = {'track D': 12, 'track E': 15}
del plays['artist B']
incr = plays['artist A']['track B'] - plays['artist A']['track A']
plays['artist A']['track x'] = plays['artist A'].pop('track A')

def translate(num, delimiter):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    result = []
    for i in range(len(num)):
        if len(num) == 0:
            result.append([])
        if num[i].isalpha() == False: 
            result.append(numbers[float(num[i])])
    seq = delimiter.join(result)
    print(seq)
    
translate('523c6v', '-')

def mylist_adder(el, lst = []):
    lst.append(el)
    return lst

l = mylist_adder(1, [])
s = mylist_adder(2, [])
t = mylist_adder(3, [])

print(l)
print(s)
print(t)

L = [["a", "this_one", "b"], ["c", "that_one", "d"]]
for i in range(len(L)):
    print(L[i][1])

def gcd(x, y, depth = 1):
    if y != 0:
        rem = x % y
        result = gcd(y, rem, depth + 1)
        return result
    else:
        tmp = x
        return tmp

def main():
    m = 9
    n = 3
    print("Finding gcd({}, {})".format(m, n))
    g = gcd(m, n)
    print("Greatest common divisor of {}, {} = {}".format(m, n, g))

main()