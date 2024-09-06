calls = 0
def count_calls ():
    global calls
    calls+=1
def string_info (n):
    print(n.upper(), n.lower(), len(n))
    count_calls()
def is_contains (a, b):
    c = (len(b))
    i = 0
    for j in range (i, c):
        if a.upper() == b[i].upper():
            result = True
            break
        else:
            result = False
        i+=1
    print(result)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)