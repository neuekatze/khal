import random

v = "b c ç č d đ f g j k l ļ m n ň p r s š t ţ v w x y z ž ż"""

v = v.split()

root = random.choice(v) + "-" + random.choice(v)

print(root, root.upper())
