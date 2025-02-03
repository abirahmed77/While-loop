num = 1654

count = 0

while num > 0:
    num = num // 10
    count = count + 1
    
print(f"The number has {count} digits")