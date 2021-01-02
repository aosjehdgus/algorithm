n = 10

# 2진수
b = bin(n)
print(b)              # 출력 값 : 0b1010
# 8진수
o = oct(n)
print(o)              # 출력 값 : 0o12
# 16진수
h = hex(n)
print(h)              # 출력 값 : 0xa

# 출력 값은 모두 str 타입으로 출력된다.

n = 10

# 2진수
b = format(n, 'b')
print(b)              # 출력 값 : 1010
# 8진수
o = format(n, 'o')
print(o)              # 출력 값 : 12
# 16진수
x = format(n, 'x')
print(x)              # 출력 값 : a

# 출력 값은 모두 str 타입으로 출력된다.

x = format(n, 'x')
print(x.upper())              # 출력 값 : A


b = int('0b1010', 2)    # 10의  2진수  대입  # 출력 값 : 10
print(b)

o = int('0o12', 8)      # 10의  8진수  대입  # 출력 값 : 10
print(o)

h = int('0xa', 16)      # 10의  16진수 대입  # 출력 값 : 10
print(h)


# 10진수 -> 2진수  
b_10 = "{0:#b}".format(10)              # 출력 값 : 0b1010
print(b_10)
# 10진수 -> 8진수
o_10 = "{0:#o}".format(10)              # 출력 값 : 0o12
print(o_10)
# 10진수 -> 16진수
x_10 = "{0:#x}".format(10)              # 출력 값 : 0xa
print(x_10)

# 2진수 ->  8진수
o_2 = "{0:#o}".format(0b1010)           # 출력 값 : 0o12
pr`int(o_2)
# 2진수 ->  10진수
d_2 = "{0:#d}".format(0b1010)           # 출력 값 : 10
print(d_2)
# 2진수 ->  16진수
x_2 = "{0:#x}".format(0b1010)           # 출력 값 : 0xa
print(x_2)

# 8진수 ->  2진수
o_8 = "{0:#b}".format(0o12)             # 출력 값 : 0b1010
print(o_8)
# 8진수 ->  10진수
d_8 = "{0:#d}".format(0o12)             # 출력 값 : 10
print(d_8)
# 8진수 ->  16진수
x_8 = "{0:#x}".format(0o12)             # 출력 값 : 0xa
print(x_8)

# 16진수 ->  2진수
o_16 = "{0:#b}".format(0xa)             # 출력 값 : 0b1010
print(o_16)
# 16진수 ->  10진수
d_16 = "{0:#d}".format(0xa)             # 출력 값 : 10
print(d_16)
# 16진수 ->   8진수
x_16 = "{0:#o}".format(0xa)             # 출력 값 : 0o12
print(x_16)


# 2진수 -> 8진수
o_2 = oct(0b1010)
print(o_2)                                # 출력 값 : 0o12
# 2진수 -> 16진수
h_2 = hex(0b1010)
print(h_2)                                # 출력 값 : 0xa
# 2진수 -> 10진수
s_2 = str(0b1010)
print(s_2)                                # 출력 값 : 10

# 8진수 -> 2진수
o_8 = bin(0o12)
print(o_8)                                # 출력 값 : 0b1010
# 8진수 -> 16진수
h_8 = hex(0o12)
print(h_8)                                # 출력 값 : 0xa
# 8진수 -> 10진수
s_8 = str(0o12)
print(s_8)                                # 출력 값 : 10
 
# 16진수 -> 2진수
o_16 = bin(0xa)
print(o_16)                               # 출력 값 : 0b1010
# 16진수 -> 8진수
h_16 = oct(0xa)
print(h_16)                               # 출력 값 : 0o12
# 16진수 -> 10진수
s_16 = str(0xa)
print(s_16)                               # 출력 값 : 10




