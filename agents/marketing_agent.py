from utils.gemini_client import ask_gemini


def create_marketing_plan(startup_idea: str) -> str:

    prompt = f"""
    You are a Marketing Expert for startups.

    Idea: {startup_idea}

    Create:

    1. Brand Positioning
    2. Target Audience
    3. Social Media Strategy
    4. Viral Marketing Ideas
    5. Launch Plan (Day 1 to Day 7)
    """

    return ask_gemini(prompt)