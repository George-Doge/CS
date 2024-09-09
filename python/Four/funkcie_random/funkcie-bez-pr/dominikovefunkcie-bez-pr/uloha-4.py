import time as tm

def cas():
    time = tm.asctime()
    time = time[11:16]
    return time

def odporucanie():
    time = cas()
    print(f"Je {time}.")
    time = time[0:5]

    hours = int(time[0:2])
    hours *= 60

    minutes = int(time[3:5])
    minutes += hours

    if minutes >= 6*60 and minutes <= 7*60:
        print("Vstavaj!!!")

    elif minutes > 7*60 and minutes <= 450:
        print("Cas na ranajky!")

    elif minutes >= 12*60 and minutes <= 14*60:
        print("Obed caka !")

    elif minutes >= 22*60 and minutes <= 23*60:
        print("Uz chod spat!")

    elif minutes > 23*60 or minutes <= 5*60:
        print("Uz vazne chod spat!")

odporucanie()