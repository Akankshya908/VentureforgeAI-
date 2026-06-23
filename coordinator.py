from utils.gemini_client import ask_gemini


def build_startup_report(startup_idea: str):

    prompt = f"""
You are an AI Startup Analyst.

Return ONLY valid JSON (no extra text).

Schema:

{{
  "idea": "{startup_idea}",
  "research": {{
    "problem": "",
    "target_users": "",
    "market_need": "",
    "opportunities": ""
  }},
  "competitors": {{
    "top_competitors": [],
    "market_gaps": "",
    "differentiation": ""
  }},
  "product": {{
    "mvp_features": [],
    "user_journey": [],
    "tech_features": []
  }},
  "strategy": {{
    "business_model": "",
    "pricing": "",
    "go_to_market": ""
  }},
  "marketing": {{
    "positioning": "",
    "audience": "",
    "launch_plan": ""
  }}
}}

Make it detailed but strictly JSON only.
"""

    response = ask_gemini(prompt)

    return {
        "idea": startup_idea,
        "report": response,
        "mode": "structured-json-v1"
    }