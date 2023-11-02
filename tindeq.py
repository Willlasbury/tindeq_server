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
            y = str.split(' ')
            # print(y)
            nums = []
            for num in y:
                b = int(num)
                nums.append(b)
            nums = bytes(nums)
            print('nums: ', nums)

            data_struct = struct.Struct("<fl")
            info_struct = struct.Struct("<bb")
            kind, size = info_struct.unpack(nums[:2])
            print('kind, size', kind, size)
            for x,s  in data_struct.iter_unpack(nums[2:]):
                print('x, s: ', x, s)
                

            print('\ntest\n')
            # print('last', self.data)
            # return self.data
            return 'hi'
        except:
            print('\nerror\n')
            return HTTPException(status_code=400, detail='some error')