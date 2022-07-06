height = int(input("Enter the height of the triangle: "))

for row in range(height):
    if (row != height - 1):  # every other row
        print(" "*(height - row) + "/" + " " *
              (2*row) + "\\" + " "*(height-row))
    else:  # this is the last row
        print(" "*(height - row) + "/" + "_" *
              (2*row) + "\\" + " "*(height-row))
