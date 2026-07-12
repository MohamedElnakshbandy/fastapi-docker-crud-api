from fastapi import APIRouter
from celery.result import AsyncResult

from app.celery_app import celery_app
from app.tasks import slow_add

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/slow-add")
def submit_slow_add(x: int, y: int):
    task = slow_add.delay(x, y)

    return {
        "task_id": task.id,
        "status": "submitted"
    }


@router.get("/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(
        task_id,
        app=celery_app
    )

    response = {
        "task_id": task_id,
        "status": task_result.status
    }

    if task_result.successful():
        response["result"] = task_result.result
    elif task_result.failed():
        response["error"] = str(task_result.result)

    return response