class Dress():
    def __init__(self, style, size, color):
        self.style = style
        self.size = size
        self.color = color

    def embrace(self):
        print('EMBRACE THIS SEASON')    
        
    # def __init__():



if __name__ == "__main__":

    dress = Dress(style = "Empire", size = "M", color = "Pink")
    print(type(dress))  
    print(dress.size)
    print(dress.color) 
    print(dress.embrace())

    dress = Dress(style = "A-line", size = "S", color = "Yellow")
    print(type(dress))  
    print(dress.size)
    print(dress.color)  
    print(dress.embrace())  