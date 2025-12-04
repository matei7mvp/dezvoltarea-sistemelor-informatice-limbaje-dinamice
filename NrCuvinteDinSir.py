import string

# Numarul de cuvinte din sir
s = "Acestaa este un sir de caractere, " \
    "cu adevarat un sir de caractere!!!"

print(len(s.split()))


# Cuvinte de lungime para / impara

# impare
[print(x) for x in s.split() if (len(x) % 2)]

# pare
cuvinte = [c.strip(string.punctuation) for c in s.split()]
print([c for c in cuvinte if not len(c) % 2])
