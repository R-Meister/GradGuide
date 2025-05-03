from pdfminer.high_level import extract_text
import re

# Define your custom stopwords
custom_stopwords = {
    'the', 'and', 'is', 'in', 'to', 'of', 'a', 'with', 'that', 'for', 'on',
    'this', 'by', 'it', 'an', 'as', 'are', 'was', 'at', 'be', 'from'
}

def clean_and_tokenize(text):
    # Convert to lowercase
    text = text.lower()
    # Remove non-alphabetic characters
    words = re.findall(r'\b[a-z]+\b', text)
    # Filter out stopwords
    filtered_words = [word for word in words if word not in custom_stopwords]
    return filtered_words

def parse_pdf(file_path):
    # Extract raw text from PDF
    text = extract_text(file_path)
    # Clean and tokenize text
    tokens = clean_and_tokenize(text)
    return tokens

# Example usage
if __name__ == "__main__":
    pdf_file = "/Users/ramanmendiratta/Desktop/raman_resume.pdf"  # Replace with your PDF file path
    parsed_tokens = parse_pdf(pdf_file)
    print("Extracted Tokens (without stopwords):")
    print(parsed_tokens)
