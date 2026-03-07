def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r   
    print("Circle points are:")
    while x <= y:
        
        print(xc + x, yc + y)
        print(xc - x, yc + y)
        print(xc + x, yc - y)
        print(xc - x, yc - y)
        print(xc + y, yc + x)
        print(xc - y, yc + x)
        print(xc + y, yc - x)
        print(xc - y, yc - x)
        print("------------------")
       
        if p < 0:
            
            x += 1
            p = p + 2*x + 3
        else:
            p = p + 2*(x - y) + 5
            y -= 1
            x += 1
# Example
midpoint_circle(0, 0, 5)
