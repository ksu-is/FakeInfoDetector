import re

def is_url(input_text):
    url_pattern = re.compile(r'https?://\S+')
    return re.match(url_pattern, input_text) is not None

def main():
    print("Welcome to the FakeInfoDetector!")
    user_input = input("Please enter a URL or article text: ")
    
    if is_url(user_input):
        print("You entered a URL.")
    else:
        print("You entered article text.")

if __name__ == "__main__":
    main()