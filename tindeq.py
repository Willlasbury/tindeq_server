import struct

class TindeqHandler:
    def __init__ (self, data):
        self.data = None

    def handleData(self, data):
        handler = struct.Struct("<fl")
        self.data = handler.unpack(data)
        print(self.data)
        return self.data