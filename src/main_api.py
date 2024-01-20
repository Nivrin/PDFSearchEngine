from pathlib import Path
from pdf_processing.pdf_processor import extract_text_from_pdf, filter_text, create_inverted_index_from_filtered_text
from database_operations.database_operations import insert_document_to_db, insert_inverted_index_to_db
import sqlite3


def process_pdf(file_path: str):
    data_directory = Path(__file__).parent.parent / 'data'
    pdf_path = Path(file_path)
    database_path = data_directory / 'search_engine.db'

    with sqlite3.connect(database_path) as conn:
        extracted_text = extract_text_from_pdf(pdf_path)
        filtered_text = filter_text(extracted_text)

        document_id = insert_document_to_db(conn, str(pdf_path), filtered_text)

        inverted_index_data = create_inverted_index_from_filtered_text(filtered_text, document_id)
        insert_inverted_index_to_db(conn, inverted_index_data)


def main():
    data_directory = Path(__file__).parent.parent / 'data'
    database_path = data_directory / 'search_engine.db'
    process_pdf(Path(r"C:\Users\Lenovo-LPT-1\Desktop\private\cv\geodata\Niv Rimon - Software Developer CV2.pdf"))

    print("done")


if __name__ == '__main__':
    main()
