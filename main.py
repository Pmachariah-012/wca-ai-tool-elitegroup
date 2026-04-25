import requests
from prompts import CV_REVIEW_PROMPT

API_KEY = "AIzaSyAfkgo2DT1NUNzd6AFPByUNli6Shqn2vNU"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

def main():
    user_cv = input("Paste CV and hit Enter: ")
    
    # Send request to Gemini
    payload = {"contents": [{"parts": [{"text": CV_REVIEW_PROMPT.format(cv_text=user_cv)}]}]}
    response = requests.post(URL, json=payload)
    
    # Print result
    if response.status_code == 200:
        print(response.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    main()