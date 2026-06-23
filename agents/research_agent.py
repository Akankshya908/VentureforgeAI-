from utils.gemini_client import ask_gemini

def run_research(startup_idea: str):

    prompt = f"""
    Analyze startup idea:

    {startup_idea}

    Return:

    1. Problem
    2. Target Users
    3. Market Need
    4. Opportunities
    """

    return ask_gemini(prompt)