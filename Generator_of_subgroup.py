p = 3 * (2 ** 30) + 1
g = 0

for i in range(2,p):

    if g != 0:
        break

    result = (i ** 1024) % p

    if result != 1:
        continue

    else:
        candidate = i

        for j in range(2,1024+1):

            check = (candidate ** j) % p

            if check != 1:
                continue

            else:

                if j < 1024:
                    break

                else:
                    g = candidate
                    print("Our generator will be:", g)