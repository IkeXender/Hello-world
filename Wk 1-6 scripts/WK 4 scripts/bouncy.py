bounciness = 0.6

height = float(input("Enter the initial height: "))

bounces = int(input("Enter the number of bounces: "))

distance = height

for count in range(bounces):
    height = height * bounciness
    distance = distance + height

    if count < bounces - 1:
        distance = distance + height

print("Total distance traveled:", distance)
