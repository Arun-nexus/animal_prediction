import os
import asyncio
from groq import AsyncGroq

api_key = os.getenv("groq_api_key")
client = AsyncGroq(api_key=api_key)

async def call_groq(prompt: str):
    try:
        stream = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
            stream=True  )

        full_res = ""
        async for chunk in stream:

            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                full_res += content

        return full_res

    except Exception as e:
        return f"\n error: {str(e)}"


async def test():
    prompt = "Explain WebSockets in simple terms for a beginner."
    result = await call_groq(prompt)
    print(result)


if __name__ == "__main__":
    asyncio.run(test())