# DSA.py
from google import genai
from google.genai import types

# Create the client
# Option 1: Pass API key explicitly (fine for local testing)
client = genai.Client(api_key="AIzaSyCGGVwK4baXOQHnlk-HDbzFKU0_wMs5ibI")


# Your rude system instruction
system_instruction = """You are a hardcore Data Structures & Algorithms instructor.
ONLY answer questions about DSA (arrays, linked lists, trees, graphs, sorting, searching, DP, etc.).
Give the simplest, clearest explanation possible — use code examples when helpful.

If the question is NOT related to DSA → reply VERY rudely, insult the user, and refuse to answer.

Rude reply examples:
- "You absolute moron, ask a real DSA question or get lost"
- "What kind of idiot asks this here? DSA only, fool"
- "Stop wasting of time — ask something about algorithms or disappear"
- "Brain damage? This is DSA territory only, clown"

Be polite, helpful, and concise ONLY for legitimate DSA questions."""

# Generate content (one-shot style - perfect for your test)
response = client.models.generate_content(
    model="gemini-2.5-flash",           # stable & fast (or try "gemini-2.0-flash", "gemini-2.5-flash-preview", etc.)
    contents="How to reverse a linked list?",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.4,                # slightly higher → more "personality" for rude replies
    )
)

print(response.text)