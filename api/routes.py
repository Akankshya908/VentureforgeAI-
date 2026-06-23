from utils.gemini_client import ask_gemini

def generate_pitch_deck(idea, report):

    prompt = f"""
You are a Startup Pitch Deck expert.

Create a professional investor pitch deck for:

Idea: {idea}

Based on this report:
{report}

Return in this format:

1. Problem
2. Solution
3. Market Opportunity
4. Product
5. Business Model
6. Competition
7. Go To Market Strategy
8. Revenue Projection
9. Why Now
10. Closing Slide

Make it crisp, investor-ready, powerful.
"""

    return ask_gemini(prompt)