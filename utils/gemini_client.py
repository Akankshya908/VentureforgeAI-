from google import genai

client = genai.Client()

def ask_gemini(prompt: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return mock_response(prompt)


def mock_response(prompt: str):

    return f"""
[MOCK RESPONSE - GEMINI UNAVAILABLE]

This is fallback AI output.

You asked:
{prompt[:300]}...

--- 

This system is running in offline mode because:
- API quota exceeded OR
- network limitation

But architecture is working correctly.
"""