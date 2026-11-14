
def rectangle_area_perimeter(l, b):
    a = l * b
    p = 2 * (l + b)
    return a, p 

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter) 