def spam_can(amount: int, salt: int):
    a_spam_can = "SPAM is {0:d} grams with {1:d} gram salt.".format(amount, salt)
    return a_spam_can


msg = spam_can(salt=350, amount=9)
print(msg)




