#lens functions example

s = "chapman"
len_s = len(s)
print(s[0:len_s])

print()
for c in s:
    print(c)

print()
for idx in range(len(s)):
    print(s[idx])

print()

idx = 0
while idx < len(s):
    print(s[idx])
    idx += 1
    
print()
letter = 'a'
for char in s:
    if char in letter:
        print(char)

print()
idx = 0
while idx < len(s):
    if s[idx] == "a":
        a_num = idx
        print(a_num)
        break
    idx += 1
