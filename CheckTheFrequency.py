test_dict = {"Guddu" : 3, "Gamerz" : 6, "is" : 3, "the" : 3, "best" : 4, "gaming" : 0, "channel" : 1, "ever" : 1}

print("The original dictionary : " + str(test_dict))


K = 3

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is = " + str(res))