from fastapi import APIRouter


router = APIRouter(prefix="/demo")


@router.get("/")
async def demo():
    return "hello world"
