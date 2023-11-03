import struct
from fastapi import HTTPException
# from session import Session



class TindeqHandler:
    def __init__(self, session):
        self.session = session


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
            kind, size = info_struct.unpack(nums[:2])
            # get weight and time from rest of list
            for weight, useconds  in data_struct.iter_unpack(nums[2:]):
                self.session.log_force_sample(time=useconds, weight=weight)

            # grab average data
            mean = self.session.mean()

            # clear weight before next read
            self.session.clear()

            return mean
        except:
            print('\nerror\n')
            return HTTPException(status_code=400, detail='some error')
        
    def handleCFT(self, time, weight):
        pass