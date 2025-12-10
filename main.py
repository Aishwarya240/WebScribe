# WebScribe - URL Summarizer
# Author: Aishwarya Patil

import re
from colorama import Fore, Style, init
from yaspin import yaspin
from newspaper import Article
from ollama import Client

# Initialize colorama
init(autoreset=True)

# Initialize Ollama client
client = Client()

# URL validation regex
url_pattern = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


def is_valid_url(url):
    return re.match(url_pattern, url) is not None


def fetch_text(url):
    with yaspin(text="Fetching and extracting article...", color="cyan") as spinner:
        try:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text
            if len(text.split()) < 50:
                spinner.fail("❌")
                return None
            spinner.ok("✅")
            return text
        except Exception as e:
            spinner.fail("❌")
            print(Fore.RED + f"Error fetching URL: {e}")
            return None


def summarize_text(text, language="English"):
    with yaspin(text="Summarizing with Llama 2...", color="green") as spinner:
        try:
            prompt = f"Summarize this text in a concise, human-friendly manner in {language}:\n{text}"
            response = client.chat(
                model="llama2",
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response.message.content  # updated Ollama API
            spinner.ok("✅")
            return summary
        except Exception as e:
            spinner.fail("❌")
            print(Fore.RED + f"Error summarizing text: {e}")
            return None


def estimate_reading_time(text):
    words = len(text.split())
    time_minutes = max(1, words // 200)  # average reading speed 200 wpm
    return words, time_minutes


def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to WebScribe - AI Web Summarizer!\n")

    while True:
        url = input(Fore.MAGENTA + "Enter a URL to summarize (or type 'exit' to quit): " + Style.RESET_ALL).strip()
        if url.lower() == "exit":
            print(Fore.CYAN + "Goodbye! Thanks for using WebScribe.")
            break
        if not is_valid_url(url):
            print(Fore.RED + "Please enter a valid URL.")
            continue

        text = fetch_text(url)
        if not text:
            print(Fore.RED + "[ERROR] Could not extract enough text from the webpage.")
            continue

        # Show word count and reading time
        total_words, total_time = estimate_reading_time(text)
        print(Fore.YELLOW + f"\nOriginal article has ~{total_words} words (~{total_time} min reading time).")

        # Optionally choose summary language
        lang = input(
            Fore.MAGENTA + "Enter summary language (default: English): " + Style.RESET_ALL).strip() or "English"

        summary = summarize_text(text, language=lang)
        if summary:
            summary_words, summary_time = estimate_reading_time(summary)
            print(Fore.GREEN + "\n----- WebScribe Summary -----\n")
            print(Fore.WHITE + summary)
            print(Fore.YELLOW + f"\nSummary has ~{summary_words} words (~{summary_time} min reading time).")
        else:
            print(Fore.RED + "Failed to generate summary.")


if __name__ == "__main__":
    main()
