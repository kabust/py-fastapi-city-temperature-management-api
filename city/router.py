from fastapi import APIRouter


router = APIRouter()


@router.get("/cities/")
def get_cities():
    pass
