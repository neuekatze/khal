a = "* a e ï i o ö u ü ä ë"

a = a.split()

b = "a e ï i o ö u ü ä"

b = b.split()
inp = (int(input("A: ")), int(input("b: ")))

def finding(x):
    if (((x//10)+1) == x%10):
        return a[x//10] + "ë"
    return a[x//10] + b[x%10]

print(finding(inp[0]), finding(inp[1]))
