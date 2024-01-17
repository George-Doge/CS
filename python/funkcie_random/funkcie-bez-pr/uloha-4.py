import time as tm

'''
Vyriesil som to tak, ze som vsetko premenil na minuty.
pre kontrolu mozte zakomentovat 'time = cas()' a dat tam
premennu 'time = "hh:mm"'.
'''

def cas():
    time = tm.asctime()
    time = time[11:19]
    return time

def odporucanie():
    time = cas()
    print(f"Teraz je {time}.")
    time = time[0:5]

    hours = int(time[0:2])
    hours *= 60

    minutes = int(time[3:5])
    minutes += hours

    if minutes >= 6*60 and minutes <= 7*60:
        print("Odporucam aby si vstal")

    elif minutes > 7*60 and minutes <= 450:
        print("Odporucam, aby si sa isiel naranajkovat")

    elif minutes >= 12*60 and minutes <= 14*60:
        print("Odporucam, aby si obedoval")

    elif minutes >= 22*60 and minutes <= 23*60:
        print("Odporucam ist spat")

    elif minutes > 23*60 or minutes <= 5*60:
        print("Chod uz spat, zaspis na hodine")

odporucanie()