from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TasksRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи📜"]
)


@router.post("", summary="Добавление новой задачи", response_model=STaskId)
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("", summary="Вернуть все задачи", response_model=list[STask])
async def get_task():
    tasks = await TasksRepository.find_all()
    return tasks
