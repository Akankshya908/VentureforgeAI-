from __future__ import annotations

from google import genai

from utils.gemini_client import get_gemini_client


def generate_pitchdeck(startup_idea: str) -> str:
    """Generate a pitch deck outline for the startup idea."""

    client: genai.Client = get_gemini_client()

    prompt: str = (
        "You are a pitch deck agent. Create a pitch deck outline for the following startup idea.\n\n"
        f"Startup idea: {startup_idea}\n\n"
        "Include slide-by-slide content with:\n"
        "- Slide title\n"
        "- Key bullet points\n"
        "- A short 'speaker note'\n\n"
        "Cover: problem, solution, market, product, business model, traction assumptions, "
        "go-to-market, competition, team placeholders, financial highlights placeholders, ask.\n"
        "Return in a clear numbered list of slides."
    )

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return getattr(response, "text", str(response))

