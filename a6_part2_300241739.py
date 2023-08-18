class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self,P1,P2,color):
        ''' (Rectangle,Point,Point,Color) -> None
        initialize the rectangles bottem left point,top right point and color '''
        self.point1=P1
        self.point2=P2
        self.color=color

    def get_bottom_left(self):
        '''
        (Rectangle) -> Tuple
        returns the (x,y) of the bottom left point
        '''
        return self.point1

    def get_top_right(self):
        '''
        (Rectangle) -> Tuple
        returns the (x,y) of the top right point
        '''
        return self.point2

    def get_color(self):
        '''
        (Rectangle) -> string
        returns the color of the rectangle object
        '''
        return self.color

    def reset_color(self,color):
        '''
        (Rectangle,string) -> None
        changes the rectangle object's color
        '''
        self.color=color

    def get_perimeter(self):
        '''
        (Rectangle) -> int
        finds the perimeter of the rectangle object
        '''
        bottemleftvalues=self.point1.get()
        x1value=bottemleftvalues[0]
        y1value=bottemleftvalues[1]
        topright=self.point2.get()
        x2value= topright[0]
        y2value=topright[1]
        return 2*x2value - 2*x1value + 2*y2value - 2*y1value

    def get_area(self):
        '''
        (Rectangle) -> int
        returns the area of the rectangle object
        '''
        bottemleftvalues = self.point1.get()
        topright = self.point2.get()
        bottemleftvalues=self.point1.get()
        x1value=bottemleftvalues[0]
        y1value=bottemleftvalues[1]
        topright=self.point2.get()
        x2value= topright[0]
        y2value=topright[1]
        x = x2value - x1value
        y = y2value - y1value
        return x*y

    def move(self,dx,dy):
        '''
        (Rectangle,movemnet value, Mouvement value) -> None
        Moves the coordinates of the rectangle object by specified amount.
        '''
        self.point1.move(dx,dy)
        self.point2.move(dx,dy)

    def intersects(self,rectangle2):
        '''
        (Rectangle, Rectangle) -> Boolean
        checks if both objects intersect intersect
        '''

        P0 = self.point1.get() #(X1,Y1)
        P1 = self.point2.get()#(X2,Y2)
        P2 = rectangle2.point1.get() #(x1,y1)
        P3 = rectangle2.point2.get()#(x2,y2)
        if P2[0]>P1[0] or P3[0]<P0[0] or P2[1]>P1[1] or P3[1]<P0[1]:
            return False
        else:
            return True

    def contains(self,x,y):
        '''
        (Rectangle, Rectangle) -> Boolean
        checks if there is a point that is contained insi
        '''
        rec1p1 = self.point1.get() #(X1,y1)
        rec1p2 = self.point2.get()#(X2,Y2)
        if rec1p1[0]<=x and x<=rec1p2[0] and rec1p1[1]<=y and y<=rec1p2[1]:
            return True
        else:
            return False

    def __eq__(self, rec2):
        '''
        (Rectangle,Rectangle)->bool
        Returns True if self and other have the same coordinates and color
        '''
        if (self.point1==rec2.point1 and self.point2==rec2.point2 and self.color ==rec2.color):
            return True
        else:
            return False

    def __repr__(self):
        '''(rectangle)->str
        Returns canonical string representation Rectangle(Point(),Point(),Color)'''
        return 'Rectangle(' + str(self.point1) + "," + str(self.point2) + "," + '"'+str(self.color)+'"' + ')'

    def __str__(self):
        '''(rectangle)->str
        Returns nice string representation Rectangle(Point(),Point(),Color).
        '''
        return ("I am a "+ str(self.color) +" rectangle with bottom left corner at "+str(self.point1.get())+" and top right corner at " +str(self.point2.get())+".")


class Canvas:
    def __init__(self,space=[]):
        ''' (Canvas,space=[]) -> None
        initialize the canvas empty if there isn't a specified rectangle
        '''
        self.canvas=space

    def add_one_rectangle(self,rectangle):
        '''
        (Canvas, Rectangle) -> list
        returns the added Canvas list with the object
        '''
        return self.canvas.append(rectangle)

    def count_same_color(self,color):
        '''
        (Canvas, string) -> int
        returns the number of color that are the same as requested on the canvas
        '''
        totaltimes=0
        for i in range(0,len(self.canvas)):
            rect=self.canvas[i]
            if color == rect.get_color():
                totaltimes+=1
        return totaltimes

    def total_perimeter(self):
        '''
        (Canvas) -> int
        returns the total perimeter of the list
        '''
        rectanglecounter=0
        for i in range(0,len(self.canvas)):
            rectangle=self.canvas[i]
            rectanglecounter += rectangle.get_perimeter()
        return rectanglecounter


    def min_enclosing_rectangle(self):
        '''
        (Canvas) -> Rectangle
        returns a rectangle object that inecapsulates all of the rectangles in the list
        '''
        X1 = 0
        X2 = 0
        Y1 = 0
        Y2 = 0
        for i in range(0,len(self.canvas)):
            rectangle1=self.canvas[i]
            rec1P1=(rectangle1.get_bottom_left()).get()
            rec1P2=(rectangle1.get_top_right()).get()
            if rec1P1[0]<X1:
                X1=rec1P1[0]
            if rec1P2[0] > X2:
                X2 = rec1P2[0]
            if rec1P1[1] < Y1:
                Y1=rec1P1[1]
            if rec1P2[1] > Y2:
                Y2=rec1P2[1]
        return Rectangle(Point(X1,Y1),Point(X2,Y2),"'red'")

    def common_point(self):
        '''
        (Canvas) -> Boolean
        Checks if there is a common point between all the rectangles and returns a boolean of wheter it does or not
        '''
        iscount = 0
        rectangle1 = self.canvas[0]
        for j in range(0,len(self.canvas)):
            rectangle2= self.canvas[j]
            if rectangle1.intersects(rectangle2):
                iscount+=1
        if len(self.canvas) == iscount:
            return True
        else:
            return False
    def __len__(self):
        '''
        (Canvas) -> int
        calculates and returns the lenght of the list
        '''
        return len(self.canvas)

    def __repr__(self):
        '''(rectangle)->str
        Returns canonical string representation Rectangle(Point(),Point(),Color)'''
        return "Canvas ("+str(self.canvas)+")"

