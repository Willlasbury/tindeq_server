import struct
from fastapi import HTTPException
# from session import Session

class TindeqHandler:

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

            # get type of response (see tindeq api) and the data size from first two indexes
            type, size = info_struct.unpack(nums[:2])

            # returns type of measurement and dict of weight:time
            return {type, data_struct.iter_unpack(nums[2:])}
        except:
            print('\nerror\n')
            return HTTPException(status_code=400, detail='some error')
        
    def handleCFT(self, time, weight):
        pass