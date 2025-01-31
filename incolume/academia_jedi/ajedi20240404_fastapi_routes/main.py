"""Module."""

from fastapi import APIRouter, FastAPI

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D103, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300

# @asynccontextmanager
# async def lifespan(_: FastAPI):
#     yield

test_router = APIRouter()


app = FastAPI()  # FastAPI(lifespan=lifespan)


@test_router.get('/posts')
async def posts():
    return {'posts': 'test'}


# app.include_router(items_router)
# app.include_router(automations_router)
# app.include_router(test_router)
#
# app.state.limiter = limiter
#
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get('/')
def read_root():
    return 'Server is running.'
