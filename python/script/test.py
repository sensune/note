
def sum(i):
    if i == 1:
        return 1
    return i+sum(i-1)
print(sum(100))

#1-2+3-4+5...-100
re = 0
for i in range(1,100):
    if i%2 == 0:
        re-=i
    else:
        re+=i
print(re)