from fastapi import FastAPI, APIRouter


from starlette.staticfiles import StaticFiles


app = FastAPI()

router = APIRouter()


@router.get("/")
async def api_root():
    return {"message": "Hello World"}


app.include_router(router, prefix="/api")
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
