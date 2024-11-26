import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# Senders information
SENDER_DETAILS = {
    "name": "Rahul T K",
    "email": "rahultk@gmail.com",
    "role": "Project Manager"
}

def log_feedback(client_name, original_response, feedback):
    """
    Log feedback on the response for future analysis and improvement.
    
    Parameters:
        client_name (str): The name of the client.
        original_response (str): The original generated response.
        feedback (str): Feedback or suggestions for improvement.
    """
    with open("response_feedback.log", "a") as log_file:
        log_file.write(f"Client: {client_name}\n")
        log_file.write(f"Original Response:\n{original_response}\n")
        log_file.write(f"Feedback:\n{feedback}\n\n")

def generate_response(client_details):
    """
    Generate a professional email response based on client details using OpenAI's GPT-3.5-turbo model.
    
    Parameters:
        client_details (dict): A dictionary containing client information.
    
    Returns:
        str: The generated email response.
    """
    # Construct the subject line dynamically based on project type
    subject_line = f"Web Development Project Inquiry - {client_details['project_type']}"
    
    prompt = f"""
    Write a professional and natural email response based on the following client details:
    
    Client Name: {client_details['client_name']}
    Client Email: {client_details['client_email']}
    Project Type: {client_details['project_type']}
    Budget: {client_details['budget']}
    Service Category: {client_details['service_category']}
    Additional Information: {client_details['additional_info']}
    
    Ensure the response:
    - Avoids overused phrases (e.g., "I hope this email finds you well").
    - Is human-like, professional, and contextually relevant.
    - Reflects empathy and understanding of the client's requirements.
    Include the sender's details in the email:
    Sender Name: {SENDER_DETAILS['name']}
    Sender Email: {SENDER_DETAILS['email']}
    Sender Role: {SENDER_DETAILS['role']}
    Start the email with the following subject line: "{subject_line}"
    """
    
    try:
                
        # Call OpenAI API to generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional assistant specializing in client communications."},
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
        "service_category": "Web Development",
        "additional_info": "I need 4 dynamic pages for a real estate web application: apartments, houses, business centres, and land. Filters for 'for sale' and 'for rent' must be connected. Functionality only; design will be handled separately."
    }
     # Generate the  response and display it
    response = generate_response(client_details)
    print("Generated Response:\n")
    print(response)

    feedback = "Add a more detailed timeline and milestones in the response."
    log_feedback(client_details['client_name'], response, feedback)

