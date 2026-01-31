import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")
    
client = genai.Client(api_key=API_KEY)
# for model in client.models.list():
#     print(model.name)

SYSTEM_PROMPT = """
You are a Docker Study Helper.
Your job is to:
- Explain Docker concepts clearly
- Explain Docker commands with syntax
- Provide simple real-world examples
- Suggest best practices
- Correct misunderstandings politely

Always assume the user is learning Docker.
"""

def ask_docker_agent(user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            SYSTEM_PROMPT,
            user_input
        ]
    )
    return response.text


if __name__ == "__main__":
    user_input = input("You: ")
    answer = ask_docker_agent(user_input)
    print("\nAgent:", answer)

