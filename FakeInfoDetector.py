import re
from urllib.parse import urlparse

def is_url(input_text):
    url_pattern = re.compile(r'https?://\S+')
    return re.match(url_pattern, input_text) is not None

def check_fake_keywords(text):
    fake_keywords = [
        "clickbait", "shocking", "you won't believe", "miracle", "unbelievable",
        "secret", "cure", "exposed", "banned", "hoax", "scam", "fake", "fraud",
        "breaking", "shocking truth", "cover-up", "alternative facts",
        "deep state", "whistleblower", "urgent"
    ]
    for keyword in fake_keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def check_trusted_domain(url):
    trusted_domains = [
        "bbc.com", "npr.org", "reuters.com", "apnews.com", "nytimes.com", "theguardian.com",
        "washingtonpost.com", "forbes.com", "pbs.org", "cbsnews.com", "abcnews.go.com",
        "nbcnews.com", "bloomberg.com", "usatoday.com"
    ]
    try:
        domain = urlparse(url).netloc
        for trusted in trusted_domains:
            if trusted in domain:
                return True
        return False
    except:
        return False

def check_news():
    user_input = input("Enter a URL or article text: ")

    is_url_input = is_url(user_input)
    trusted = False
    suspicious = check_fake_keywords(user_input)

    if is_url_input:
        print("You entered a URL.")
        trusted = check_trusted_domain(user_input)
        if trusted:
            print("✅ This URL is from a trusted news source.")
        else:
            print("⚠️ This URL is not from a recognized trusted source.")
    else:
        print("You entered article text.")

    if suspicious:
        print("⚠️ Warning: This might be fake news based on the wording.")
    else:
        print("✅ This doesn't look suspicious (but always double-check the source).")

    print()

def main():
    print("Welcome to the FakeInfoDetector!")

    while True:
        print("==== Main Menu ====")
        print("1. Check a URL or article text")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")

        if choice == "1":
            check_news()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1 or 2.\n")

if __name__ == "__main__":
    main()