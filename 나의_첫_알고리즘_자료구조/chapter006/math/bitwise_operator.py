bin_num = 0b01110111
print(format(bin_num&11110000,'#b'))    #0b1110000

x1 = 3

# x1를 2배하고 싶다.
print(x1<<1)    #6

# x1를 2^n하고 싶다. (2배는 2^1)
print(x1<<2)    #4배 12
print(x1<<3)    #8배 24
print(x1<<4)    #16배 48

x2 = 48

# x2를 /2하고 싶다.
print(x2>>1)    #24

# x1를 2^-n하고 싶다. *정수몫
print(x2>>2)    #12
print(x2>>3)    #6
print(x2>>4)    #3
print(x2>>5)    #1 (2^5 = 32 , 48//32 = 1
print(x2>>6)    #0 (2^5 =  64, 48//64 = 0


x3 = 3
x4 = 4

print(x3 & 1)   #홀수 1
print(x4 & 1)   #짝수 0

print(format(1<<4,"#b"))        #0b10000
print(format((1<<4)-1,"#b"))    #0b1111