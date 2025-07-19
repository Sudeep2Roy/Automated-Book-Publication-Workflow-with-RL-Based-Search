import google.generativeai as genai

# Your Gemini API key
genai.configure(api_key="AIzaSyAAMbpx33u3VCCNEK9rNp7ff2E5UggcqEM")

# Correct Gemini Pro model initialization
model = genai.GenerativeModel(model_name="gemini-pro")

def spin_chapter(text):
    prompt = (
        "You are a creative fiction writer. Rewrite the following book chapter in a more engaging, "
        "modern, and vivid style while keeping the story intact.\n\n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    return response.text

def review_chapter(text):
    prompt = (
        "You are a fiction editor. Review the following rewritten chapter for grammar, clarity, flow, "
        "and tone. Suggest improvements or rewrite where necessary.\n\n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    return response.text
