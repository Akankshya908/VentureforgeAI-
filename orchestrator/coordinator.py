from utils.gemini_client import ask_gemini


def build_startup_report(startup_idea: str):

    prompt = f"""
You are an AI Startup Multi-Agent System.

Analyze this idea and generate structured output:

IDEA: {startup_idea}

Return EXACT JSON with keys:

1. research:
- problem
- target_users
- market_need
- opportunities

2. competitors:
- top_competitors (list)
- market_gaps
- differentiation

3. product:
- mvp_features
- user_journey
- tech_features

4. strategy:
- business_model
- pricing
- go_to_market

5. marketing:
- positioning
- audience
- launch_plan

Make it detailed, startup-ready, and structured.
"""

    response = ask_gemini(prompt)

    return {
        "idea": startup_idea,
        "ai_generated_report": response,
        "mode": "single-call-multi-agent"
    }