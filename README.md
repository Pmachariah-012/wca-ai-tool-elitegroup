# wca-ai-tool-elitegroup
AI-powered CV reviewer tool using Python and API.
# WCA AI CV Reviewer Tool

##  Project Overview
The **CV Reviewer Tool** is a Python-based application designed to provide professional, automated feedback on resumes. By leveraging AI API integration and advanced prompt engineering, the tool analyzes CV content to help users improve their professional presentation.

This project was developed as part of the **Elite Group** collaboration, focusing on technical implementation, ethical AI use, and structured data output.

---

##  Features
* **R-T-C-C-O Prompting:** Utilizes a robust prompt framework (Role, Task, Context, Constraints, Output) for high-accuracy reviews.
* **JSON Data Formatting:** All reviews are parsed into JSON for clean, structured, and readable output.
* **CLI Interface:** Simple command-line operations for user input and processing.
* **Personalized Feedback:** Tailors suggestions based on specific user career goals and background.

---

##  Project Structure
* `prompts.py`: The engine of the tool, containing the R-T-C-C-O logic.
* `main.py`: Handles the API communication, user input, and script execution.
* `README.md`: Documentation and project guide.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mylneas1/wca-ai-tool-elitegroup.git](https://github.com/mylneas1/wca-ai-tool-elitegroup.git)
   cd wca-ai-tool-elitegroup
import requests
import json
from prompts import CV_REVIEW_PROMPT  # <--- Step 1: Import your prompt

# AI API config
API_URL ="curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
API_KEY = "AIzaSyAFkgo2DT1HUMzd6AFP8yUNli6Skqn2vNU"

def connect_to_ai(prompt):
    # Connect to AI API
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4o-mini", # Or "gpt-4" as you have in your image
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status() 
        # Properly parsing the JSON response
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error connecting to AI API: {e}"

def handle_request(cv_text):
    # Step 2: Use the imported prompt and inject the CV text
    # This replaces the {cv_text} placeholder in prompts.py with the user's input
    full_prompt = CV_REVIEW_PROMPT.format(cv_text=cv_text)

    # Get AI response
    ai_response = connect_to_ai(full_prompt)
    return ai_response

def main():
    print("--- AI CV Reviewer Tool ---")
    # Instead of hardcoded text, let's use input() to meet the "User Input" requirement
    user_cv = input("Please paste the CV text you want to review: \n")
    
    if user_cv.strip():
        print("\nAnalyzing... Please wait.\n")
        feedback = handle_request(user_cv)
        print("CV Review Feedback:")
        print(feedback)
    else:
        print("No CV text provided. Exiting.")
# conclusion
the cv reviewer works with different cv
it analyses only cv


if __name__ == "__main__":
    main()
