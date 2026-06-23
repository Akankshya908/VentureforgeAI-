from fastapi import APIRouter
from orchestrator.coordinator import build_startup_report

router = APIRouter()


@router.post("/generate-report")
def generate_report(data: dict):

    idea = data.get("idea")

    if not idea:
        return {
            "status": "error",
            "message": "Idea is required"
        }

    result = build_startup_report(idea)

    return result