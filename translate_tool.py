# Install the googletrans library if you haven't already
# Run this in your terminal: pip install googletrans==4.0.0-rc1

from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(input_text, target_language):
    try:
        # Translate the text
        translated = translator.translate(input_text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to display available languages
def display_languages():
    print("Supported languages for translation:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

# Main program
def main():
    print("Welcome to the Language Translation Tool")
    display_languages()

    # Get user input for the text to translate and the target language
    input_text = input("\nEnter the text you want to translate: ")
    target_language = input("Enter the target language code (e.g., 'fr' for French, 'es' for Spanish, 'de' for German): ")

    # Translate the text and display the result
    translated_text = translate_text(input_text, target_language)
    print(f"\nTranslated text: {translated_text}")

if __name__ == "__main__":
    main()
