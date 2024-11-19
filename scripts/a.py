a = "* a e ï i o ö u ü ä"

a = a.split()

b = "a e ï i o ö u ü ä ë"

b = b.split()
inp = (int(input("A: ")), int(input("b: ")))

def finding(x):
    if (((x//10)-1) == x%10):
        return "ë" + b[x%10]
    return a[x//10] + b[x%10]

for i in range(inp[0], inp[1] - 1):
    print(finding(i) + ", ", end="")

print(finding(inp[0]), finding(inp[1]))
