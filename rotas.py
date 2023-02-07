from fastapi import APIRouter

from controllers import answer_controllers as answer

router = APIRouter()

router.include_router(answer.router, prefix = '/answer')