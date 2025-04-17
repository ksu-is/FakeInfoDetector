import re
from urllib.parse import urlparse

def is_url(input_text):
    url_pattern = re.compile(r'https?://\S+')
    return re.match(url_pattern, input_text) is not None

def check_fake_keywords(text):
    fake_keywords = [
        "clickbait",
        "shocking",
        "you won't believe",
        "miracle",
        "unbelievable",
        "secret",
        "cure",
        "exposed",
        "banned"
    ]
    for keyword in fake_keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def check_trusted_domain(url):
    trusted_domains = [
        "bbc.com",
        "npr.org",
        "reuters.com",
        "apnews.com",
        "nytimes.com",
        "theguardian.com"
    ]
    try:
        domain = urlparse(url).netloc
        for trusted in trusted_domains:
            if trusted in domain:
                return True
        return False
    except:
        return False

def main():
    print("Welcome to the FakeInfoDetector!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a URL or article text: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if is_url(user_input):
            print("You entered a URL.")
            
            if check_trusted_domain(user_input):
                print("✅ This URL is from a trusted news source.")
            else:
                print("⚠️ This URL is not from a recognized trusted source.")
        else:
            print("You entered article text.")

        if check_fake_keywords(user_input):
            print("⚠️ Warning: This might be fake news based on the wording.")
        else:
            print("✅ This doesn't look suspicious (but always double-check the source).")

        print("\n")  # adds space between checks

if __name__ == "__main__":
    main()