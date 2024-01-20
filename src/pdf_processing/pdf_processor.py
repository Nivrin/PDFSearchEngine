from pathlib import Path
import re

import fitz
import spacy


def extract_text_from_pdf(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    if not pdf_path.is_file():
        raise ValueError(f"Invalid file path: {pdf_path}")

    cv_pdf = fitz.open(pdf_path)
    extracted_text = ""

    for page in cv_pdf:
        extracted_text += page.get_text()

    return extracted_text


def filter_text(text: str) -> str:
    if not text:
        raise ValueError("Input text is empty. Provide non-empty text for processing.")

    original_text = text
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', original_text)
    cleaned_text = cleaned_text.lower()
    cleaned_text = ' '.join(cleaned_text.split())

    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        raise ValueError("Spacy model 'en_core_web_sm' not found. Make sure to install "
                         "it using `python -m spacy download en_core_web_sm`.")

    doc = nlp(cleaned_text)

    filtered_cleaned_text = ' '.join([token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']])

    return filtered_cleaned_text


def create_inverted_index_from_filtered_text(filtered_text: str, document_id: int) -> list[tuple[str, int]]:
    terms = filtered_text.split()
    inverted_index_data = [(term, document_id) for term in terms]
    return  inverted_index_data
