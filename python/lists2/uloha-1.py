list_points = []
point = 0

def sort_points(list_points):
    min=max=list_points[0]
    
    for i in list_points:

        if min>i:
            min = i

        if max<i:
            max=i

    print(f"Minimum value is: {min}\nMaximum value is: {max}")


while True:
    point = int(input("Write point (-1 to stop adding): "))
    if point == -1:
        break
    list_points.append(point)

sort_points(list_points)