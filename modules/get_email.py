import modules.config as config
import requests
import json

# SET PROMPT
def set_prompt(text):
  return f'''
    Extract and normalize 1 email address from the following Shopee chat or note into a standard format (e.g., user@gmail.com).

    Instructions:
    1. Detect both standard email formats and obscured/obfuscated emails (e.g., using 'at', 'dot', extra spaces, or substitute symbols).
    2. If no email address is found, return an empty string ("").

    Text:
    {text}
  '''

# GET EMAIL
def get_email(text):
  response=requests.post(
    url='https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent',
    headers={"Content-Type": "application/json", "X-goog-api-key": config.api_gemini_key},
    json={
      "contents": [{"parts": [{"text": set_prompt(text=text)}]}],
      "generationConfig":{
        "responseMimeType": "application/json",
        "responseSchema": {"type": "OBJECT", "properties": {"email": {"type": "STRING"}}, "required": ["email"]},
        "thinkingConfig": {"thinkingLevel": "minimal"}
      }
    }
  )
  prompt_response=response.json()["candidates"][0]["content"]["parts"][0]["text"]
  return str(json.loads(prompt_response)['email']).lower()