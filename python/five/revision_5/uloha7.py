def len_int(ntica):
    vystup = ()
    for item in ntica:
        if type(item) == int:
            vystup = vystup + (item,)


    return vystup


print(len_int((1, 5.55, 4, "a")))