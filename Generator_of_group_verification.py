g = 713377 # The generator
p = 3 * (2 ** 30) + 1 # The modulo
elements = []

for i in range(1,1025):

    result = (g ** i) % p
    elements.append(result)

print("The elements are:")
print(elements)
print("")

if len(elements) == len(set(elements)):
    print("No value is repeated")