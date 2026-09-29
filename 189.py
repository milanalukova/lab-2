n = int(input())

last_one = n % 10 
last_two = n % 100

if last_two >= 11 and last_two <= 14:
    word = "hryven"
elif last_one == 1:
    word = "hryvnia"
elif last_one >= 2 and last_one <= 4:
    word = "hryvni"
else:
    word = "hryven"

print(n, word)