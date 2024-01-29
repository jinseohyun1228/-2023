import string

def ciper(a_string,key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt= ''

    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 36
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


x1 = "DFRGRD34FFG!!"
y1 = ciper(x1,4)

print(y1)