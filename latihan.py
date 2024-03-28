baris = 3
kolom = 4

for i in range (baris):
    for j in  range (kolom):
        print(i+1, end=" ")
    print()

baris = 3
kolom = 4

for i in range(baris):
    for j in range(kolom):
        print(j+1, end=" ")
    print()

baris = 3
kolom = 4

for i in range(baris):
    for j in range(kolom):
        print(j+1,end=" ")
    print()

print("=======================")

#No.1
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25
baris = 6
kolom = 6

for i in range(1, baris):
    for j in range(1, kolom):
        print(j*i,end=" ")
    print()

#No.2
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9
for i in range(1,6):
    for j in range(i, i+i):
        print(j, end=" ")
    print()

#No.3
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5
baris = 6
kolom = 7
for i in range(1, baris):
    for j in range(i, kolom - 1):
        print(j, end=" ")
    print()

#No.4
# 1 3 5 7 9
# 2 4 6 8 10
# 3 5 7 9 11
# 4 6 8 10 12
# 5 7 9 11 13
for i in range(1,6):
    a=i
    for j in range(1,6):
        print(a, end=" ")
        a+=2
    print()

#No.5
# 1 3 5 6 7
# 2 5 8 11 14
# 3 7 11 15 19
# 4 9 13 17 21
# 5 11 15 19 23
b=2
for i in range(1,6):
    a=i

    for j in range(5):
        print(a, end=" ")
        a+=b
    b+=1
    print()

#no.6
# + + + + 5
# + + + 4 5
# + + 3 4 5
# + 2 3 4 5
# 1 2 3 4 5
b = 5
k = 5
for i in range(b, 0, -1):
    print()
    for j in range(1, k +1):
        if j < i:
            print("+", end=" ")
        else:
            print(j, end=" ")

print()

#no. 7
# A B A B A
# B A B A B
# A B A B A
# B A B A B
b = 4
k = 5
kar = ['A', 'B']
for i in range(b):
    print()
    for j in range(k):
        print(kar[(i+j)%2], end=" ")

print()

# no.8
# S O S O S
# O S O S
# S O S
# O S
# S
b = 5
kar = ['S', 'O']
for i in range(b):
    print()
    for j in range(b-i):
        print(kar[(i+j)%2], end=" ")

print()



# no.9
a=1
b=1
c=0
for i in range (10):
    print("*"*a)
    c=a+b
    a=b
    b=c

#    jangan dengerin




