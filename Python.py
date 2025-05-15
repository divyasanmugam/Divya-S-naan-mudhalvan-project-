from textblob import TextBlob

text = input("Enter a social media message: ")
blob = TextBlob(text)
print(f"Polarity: {blob.polarity}")
print(f"Subjectivity: {blob.subjectivity}")
