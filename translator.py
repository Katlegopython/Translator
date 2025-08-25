# Simple dictionary-based translator

translations = {
    "hello": "hallo",
    "how": "hoe",
    "are": "is",
    "you": "jy",
    "goodbye": "",
    "thanks": "totsiens",
    "yes": "ja",
    "no": "nee"
}

# Ask user for a word
word = input("Enter a word to translate (English to Afrikaans): ").lower()

# Translate using dictionary
if word in translations:
    print("🌍 Translation:", translations[word])
else:
    print("❌ Sorry, I don't know that word yet.")
