import re

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

def main():
    print("Welcome to the FakeInfoDetector!")
    user_input = input("Please enter a URL or article text: ")
    
    if is_url(user_input):
        print("You entered a URL.")
    else:
        print("You entered article text.")

    if check_fake_keywords(user_input):
        print("⚠️ Warning: This might be fake news based on the wording.")
    else:
        print("✅ This doesn't look suspicious (but always double-check the source).")

if __name__ == "__main__":
    main()