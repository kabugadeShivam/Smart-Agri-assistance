from utils.gemini_ai import client


def generate_scheme_advice(profile, matched_schemes):

    context = ""

    for scheme in matched_schemes:

        context += f"""
Scheme Name: {scheme.get('Scheme_Name','')}

Type: {scheme.get('Type','')}

State: {scheme.get('State','')}

Crop: {scheme.get('Crop','')}

Eligibility:
{scheme.get('Eligibility','')}

Benefits:
{scheme.get('Benefit','')}

Subsidy:
{scheme.get('Subsidy','')}

Documents:
{scheme.get('Required_Documents','')}

Apply:
{scheme.get('Apply_At','')}

Website:
{scheme.get('Official_Website','')}

---------------------------------------
"""

    prompt = f"""
You are an expert Government Agriculture Scheme Advisor.

Farmer Profile

State : {profile["state"]}

Crop : {profile["crop"]}

Land : {profile["land"]} acres

Category : {profile["category"]}

Need : {profile["need"]}

The following schemes were retrieved.

{context}

Generate a professional recommendation.

Format:

🏆 Top Eligible Schemes

✅ Why Eligible

💰 Benefits & Subsidy

📄 Documents Required

📝 Application Process

⭐ Priority Order

Keep the explanation simple.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text