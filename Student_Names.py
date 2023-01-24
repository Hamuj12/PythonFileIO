# s = open('studentnames.txt', 'r')
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# print(s.readline().rstrip('\n'))
# s.close()

s = open('studentnames.txt', 'r')
n = 0
for line in s:
    print(line.rstrip('\n'))
    n += 1

print('There were', n-1, 'students in the file.')
s.close()