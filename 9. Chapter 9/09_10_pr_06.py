with open("log.txt") as f:
    content = f.read()
print(content)
if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")