import struct
import json
from fastapi import HTTPException
class TindeqHandler:
    def __init__ (self):
        self.data = None

    @classmethod
    def handleData(self, str):
        try:
            # convert data into an array
            arr = str.split(' ')
            
            # turn data from stings to ints
            nums = []
            for num in arr:
                b = int(num)
                nums.append(b)

            # create a byte array 
            nums = bytes(nums)

            # create struct objects to translate data 
            data_struct = struct.Struct("<fl")
            info_struct = struct.Struct("<bb")

            # get type of response and the data size from first two indexes
            kind, size = info_struct.unpack(nums[:2])

            # get weight and time from rest of list
            for weight,useconds  in data_struct.iter_unpack(nums[2:]):
                print('weight, useconds: ', weight, useconds)
                
            return 'hi'
        except:
            print('\nerror\n')
            return HTTPException(status_code=400, detail='some error')