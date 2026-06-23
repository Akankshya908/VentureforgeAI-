from utils.gemini_client import ask_gemini

def analyze_competitors(startup_idea: str):

    prompt = f"""
    You are a startup analyst.

    Analyze competitors for:

    {startup_idea}

    Return:

    1. Top 5 Competitors

    For each competitor:
    - Company Name
    - Strengths
    - Weaknesses

    Then provide:

    - Market Gaps
    - Differentiation Opportunities
    - Competitive Advantage Suggestions
    """

    return ask_gemini(prompt)