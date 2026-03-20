from openai import OpenAI
import re

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def generate_summary(data):

    prompt = f"""
Create a professional resume summary based on this information.

Name: {data['name']}
Skills: {data['skills']}
Education: {data['education']}
Experience: {data['experience']}

Write 3-4 lines of professional resume summary.
Do NOT use markdown symbols like ** or *.
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content

    # Remove markdown characters
    summary = re.sub(r'\*+', '', summary)

    return summary