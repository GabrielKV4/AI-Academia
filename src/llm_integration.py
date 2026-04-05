import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Missing OPENAI_API_KEY in environment variables.")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt, temperature=0.3):
    try:
        start_time = time.time()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise academic summarization assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
        )

        if not response or not hasattr(response, "choices") or not response.choices:
            return "ERROR: Invalid response from LLM."

        content = response.choices[0].message.content

        if not content or not content.strip():
            return "ERROR: LLM returned an empty response."

        if not content or not content.strip():
            return "ERROR: LLM returned an empty response."
        # Timeout error
        if time.time() - start_time > 15:
            raise RuntimeError("LLM Request has timed out.")
        return response.choices[0].message.content.strip()

    # Provides clear error message
    except Exception as e:
        return f"ERROR: LLM request failed - {str(e)}"
