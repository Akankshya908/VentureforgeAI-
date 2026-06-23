from utils.gemini_client import ask_gemini


def generate_strategy(startup_idea: str) -> str:

    prompt = f"""
    You are a Startup Strategy Consultant.

    Analyze this idea:

    {startup_idea}

    Provide:

    1. Business Model (how it makes money)
    2. Pricing Strategy
    3. Go-To-Market Plan
    4. Growth Strategy
    5. Risks + Mitigation
    """

    return ask_gemini(prompt)