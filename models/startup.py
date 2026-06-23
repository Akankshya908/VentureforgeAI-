from __future__ import annotations

from pydantic import BaseModel, Field


class StartupIdea(BaseModel):
    """User-provided startup idea input."""

    idea: str = Field(..., min_length=5, description="Plain-language description of the startup idea")


class StartupReport(BaseModel):
    """Combined report produced by the coordinator after running all agents."""

    research: str
    competitors: str
    strategy: str
    product_plan: str
    marketing_plan: str
    pitchdeck: str

