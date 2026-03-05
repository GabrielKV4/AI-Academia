import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def call_llm(prompt, temperature=0.3):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a precise academic summarization assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("LLM ERROR:", e)
        return "LLM generation failed."