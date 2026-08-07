import os
import traceback

from dotenv import load_dotenv
from google import genai

from utils.ai_engine.prompt_builder import build_prompt
from utils.auth import current_farmer
from utils.farmer_memory import save_memory

# =====================================================
# Load Environment
# =====================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

# =====================================================
# Gemini Client
# =====================================================

client = genai.Client(api_key=API_KEY)

# Working model
MODEL_NAME = "models/gemini-3.5-flash"

# =====================================================
# Generate AI Response
# =====================================================

def generate_answer(question: str):

    try:

        print("\n==============================")
        print("STEP 1 : Building Prompt")
        print("==============================")

        prompt = build_prompt(question)

        print("✅ Prompt Built Successfully")
        print(f"Prompt Length : {len(prompt)} characters")

        print("\n==============================")
        print("STEP 2 : Sending Request to Gemini")
        print("==============================")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        print("✅ Gemini Response Received")

        if hasattr(response, "text") and response.text:

            answer = response.text

            print("\n==============================")
            print("STEP 3 : Saving Conversation")
            print("==============================")

            try:

                save_memory(
                    farmer_id=current_farmer(),
                    question=question,
                    ai_response=answer
                )

                print("✅ Conversation Saved")

            except Exception as memory_error:

                print("❌ Memory Save Error")
                traceback.print_exc()

            return answer

        else:

            print("❌ Empty Response Returned")

            return "⚠ Gemini returned an empty response."

    except Exception:

        print("\n==============================")
        print("❌ FULL ERROR TRACEBACK")
        print("==============================")

        traceback.print_exc()

        return f"""
# ❌ AI Error

The complete error has been printed in the terminal.

Please copy the **entire traceback** from the terminal and send it to ChatGPT.

Current Model:
{MODEL_NAME}
"""