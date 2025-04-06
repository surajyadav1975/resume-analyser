from openai import OpenAI
import os

# Initialize OpenAI client using API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gpt_feedback(resume_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume analyst."},
                {"role": "user", "content": f"Analyze this resume:\n{resume_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
