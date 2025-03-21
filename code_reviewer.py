# code_reviewer.py

import openai
import os

# Set your OpenAI API Key (replace with your key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get feedback on code
def get_code_review(code: str):
    prompt = f"Please review the following Python code for quality and security issues:\n\n{code}\n\nProvide suggestions for improvement, bug fixes, and potential security concerns."
    response = openai.Completion.create(
        model="gpt-4",  # Or "gpt-3.5-turbo" for cheaper model
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Sample Python code for review
    code_to_review = """
def vulnerable_function(password):
    if password == 'password123':
        print("Access granted")
    else:
        print("Access denied")
    """
    
    review = get_code_review(code_to_review)
    print("Code Review Feedback:\n", review)
