import openai
import time
from colorama import Fore

# Set up the OpenAI API client
openai.api_key = "INPUT_YOUR_API_KEY"

open__x = f"[+] Hey, I'm Open-X By @LeeTxHacker And I'm A Chat_Bot AI Made Using The API Of CHAT-GPT By Open-AI\n\n"

def get_response(prompt):
    model_engine = "text-davinci-002"
    prompt = f"{open__x}\n\nUser: {prompt}\n\nAI:"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def main():
    print(f"{open__x}")
    while True:
        openx_user_int = input("\n[+] You: ")
        if openx_user_int.lower() in ["bye", "goodbye", "exit"]:
            print(f"{Fore.RED}[+] Open-X: Goodbye!")
            break

        try:
            response = get_response(openx_user_int)
        except openai.error.APIError as open_x_error:
            print(f"{Fore.RED}[+] Open-X: Sorry, Can't Create Response: Error - {open_x_error}")
            continue

        print(f"[+] Open-X: {response}")

        time.sleep(1)

if __name__ == "__main__":
    main()
