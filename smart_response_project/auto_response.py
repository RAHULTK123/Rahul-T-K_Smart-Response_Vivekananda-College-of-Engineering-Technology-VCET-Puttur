import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(client_details):
    """
    Generate a professional email response based on client details using OpenAI's GPT-3.5-turbo model.

    Parameters:
        client_details (dict): A dictionary containing client information.

    Returns:
        str: The generated email response.
    """
    prompt = f"""
    Write a professional and human-like email response based on the following details:
    Client Name: {client_details['client_name']}
    Client Email: {client_details['client_email']}
    Project Type: {client_details['project_type']}
    Budget: {client_details['budget']}
    Additional Information: {client_details['additional_info']}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error occurred while generating response: {e}"

if __name__ == "__main__":
    client_details = {
        "client_name": "Geminas Ket",
        "client_email": "GeminasKet@gmail.com",
        "project_type": "Content with Databases",
        "budget": "$100,000",
        "additional_info": "I need 4 dynamic pages for a real estate web application: apartments, houses, business centres, and land."
    }

    response = generate_response(client_details)
    print("Generated Response:\n")
    print(response)
