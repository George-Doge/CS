def mocnina(ciselko):
    navratny_tuple = ()
    for i in range(ciselko+1):
        navratny_tuple = navratny_tuple + (i**2,)
        #print(i, ":", i**2)


    return navratny_tuple


print(mocnina(9))
