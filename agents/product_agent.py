from utils.gemini_client import ask_gemini


def create_product_plan(startup_idea: str) -> str:

    prompt = f"""
    You are a Senior Product Manager.

    For the startup idea below, design a product plan:

    Idea: {startup_idea}

    Provide:

    1. MVP Features (minimum viable product)
    2. User Journey (step-by-step flow)
    3. Key Features (must-have)
    4. Tech Features (AI/ML/API usage)
    5. UX Suggestions

    Make it practical and startup-ready.
    """

    return ask_gemini(prompt)