import json
from pathlib import Path
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field

GOALS_FILE = Path("data/goals.json")


class Goal(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
    title: str
    description: str = ""
    status: str = "pending"


def load_goals(path: Path = GOALS_FILE) -> List[Goal]:
    return [Goal(**d) for d in json.loads(path.read_text())] if path.exists() else []


def save_goals(goals: List[Goal], path: Path = GOALS_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([g.model_dump() for g in goals], indent=2))


def create_goal(title: str, description: str = "", path: Path = GOALS_FILE) -> Goal:
    goals = load_goals(path)
    goal = Goal(title=title, description=description)
    goals.append(goal)
    save_goals(goals, path)
    return goal


def update_goal(
    goal_id: str,
    *,
    title: str | None = None,
    description: str | None = None,
    status: str | None = None,
    path: Path = GOALS_FILE,
) -> Goal | None:
    goals = load_goals(path)
    for g in goals:
        if g.id == goal_id:
            if title is not None:
                g.title = title
            if description is not None:
                g.description = description
            if status is not None:
                g.status = status
            save_goals(goals, path)
            return g
    return None


def delete_goal(goal_id: str, path: Path = GOALS_FILE) -> bool:
    goals = load_goals(path)
    new_goals = [g for g in goals if g.id != goal_id]
    if len(new_goals) == len(goals):
        return False
    save_goals(new_goals, path)
    return True
