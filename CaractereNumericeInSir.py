# Cate caractere numerice exista in sir?
s = "10n3scu 10n 112233"

print(len([x for x in s if x.isdigit()]))


# Care sunt caracterele numerice din sir?
[print(x) for x in s if x.isdigit()]

# Sau
print("".join([x for x in s if x.isdigit()]))

# Sau
[print(x, end="") for x in s if x.isdigit()]


# Caractere numerice unice din sir
print(set([x for x in s if x.isdigit()]))

# Sau
print({x for x in s if x.isdigit()})


# Inlocuire caractere numerice cu *
print("".join([x if not x.isdigit() else "*" for x in s]))


# Frecventa de aparitie cifre
print([(c, s.count(c)) for c in  {x for x in s if x.isdigit()}])








