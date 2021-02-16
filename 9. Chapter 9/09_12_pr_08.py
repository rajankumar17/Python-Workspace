with open("this.txt") as f:
    content = f.read()
print(content)
with open("copy.txt", 'w') as f:
    f.write(content)
print(content)