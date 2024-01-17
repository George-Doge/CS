import time as t

def cas():
    time = t.asctime()
    time = time[11:16]
    print(f"Teraz je {time}.")

cas()