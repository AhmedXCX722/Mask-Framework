import requests
from colorama import Fore, Style, init

# Initialize Colorama for Windows support
init(autoreset=True)

# Function to shorten a URL using TinyURL API
def shorten_url(long_url):
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(Fore.RED + "Error shortening URL" + Fore.RESET)
        return None

# Banner and style elements
def print_banner():
    print(Fore.YELLOW + """
                           __  __           _    
                          |  \/  |         | |   
                          | \  / | ___   __| | __
                          | |\/| |/ _ \ / _` |/ /
                          | |  | | (_) | (_|   < 
                          |_|  |_|\___/ \__,_|\_\
""" + Fore.RESET)

def print_line():
    print(Fore.BLUE + "============================================================================" + Fore.RESET)

def print_bio():
    print(Fore.CYAN + """
[---]                  The Best Mask Framework                  [---]
[---]                Created by: AKA_Sla7er (AKA)               [---]
[---]                      Version: 1.0.0                       [---]
[---]          Homepage: https://aka7-org.github.io/home/       [---]
                   Welcome to the Mask Framework Tool
""" + Fore.RESET)

# Main function to run the tool
def run_mask_framework():
    # Print Banner, Line, and Bio
    print_banner()
    print_line()
    print_bio()
    print_line()

    # User input for phishing URL
    real_phishing_url = input(Fore.GREEN + "Enter the phishing URL you want to mask: " + Fore.RESET)
    
    # Shorten the phishing URL
    short_url = shorten_url(real_phishing_url)
    
    if short_url:
        print(Fore.YELLOW + f"Shortened phishing URL: {short_url}" + Fore.RESET)
    else:
        print(Fore.RED + "Failed to generate a shortened URL." + Fore.RESET)

# Entry point for the script
if __name__ == "__main__":
    run_mask_framework()
