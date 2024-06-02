import google.generativeai as genai

# GOOGLE_API_KEY= <API Key>
# genai.configure(api_key=GOOGLE_API_KEY)

def get_response_from_model(code, API_KEY):
    generation_config = {
    "temperature": 0.1,
    "max_output_tokens": 5000
    }
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config)


    prompt_parts = [f'''Convert the following java code into equivalent python code: {code}
        #Keep the output logic similar to the input logic.#
        #Keep the method implementation similar to the input.#
        ''']
    response = model.generate_content(prompt_parts)
    output=response.text
    output=remove_first_and_last_line(output)
    return output

######################################
def remove_first_and_last_line(text):
    # Split the string into lines
    lines = text.split('\n')
    
    # Check if there are more than two lines to remove first and last lines
    if len(lines) > 2:
        # Slice the list to remove the first and last lines
        lines = lines[1:-1]
    
    # Join the remaining lines back into a single string
    result = '\n'.join(lines)
    return result
