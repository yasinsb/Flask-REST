class Device:
    def __init__(self, name, conn):
        self.name = name
        self.conn = conn
    
    def __str__(self):
        return f"{self.name!r} is connected with {self.conn!r}"



class Printer(Device):
    def __init__(self, name, conn, pages_left):
        super().__init__(name, conn)
        self.pages_left = pages_left

    def __str__(self):
        return F"{super().__str__()} and has {self.pages_left} pages left"


printer = Printer('Printer 1', 'USB', 100)

print(printer)


