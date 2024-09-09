import time as tm

def cas():
    time = tm.asctime()
    time = time[11:19]
    print(f"Teraz je {time}.")

cas()