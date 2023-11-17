from fastapi import APIRouter

from tindeq import TindeqHandler
from schemas.req.tindeqData import TindeqData
from schemas.res.weightRes import WeightRes


router = APIRouter(prefix="/tindeq")

tindeq = TindeqHandler()

@router.get("/test")
async def root():
    return {"message": "Hello World"}

# todo: add response schema
@router.post("")
async def getTindeqData(data: TindeqData):
    try:
        res = tindeq.handleData(data.bytes)
        return res
    except:
        return 'error'