import struct
import json

class TindeqHandler:
    def __init__ (self):
        self.data = None

    @classmethod
    def handleData(self, str):
        try:
            # convert data into an array
            nums = str.split(' ')
            print('bytes: ', nums)
            self.data = struct.Struct.unpack("<fl", nums)
            
            print('last', self.data)
            return self.data
        except:
            return 400