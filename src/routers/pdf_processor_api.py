from pathlib import Path
import sqlite3

from fastapi import APIRouter

from ..database_operations.database_operations import insert_document_to_db, \
    insert_inverted_index_to_db
from ..models.pdf_models import PDF
from ..pdf_processing.pdf_processor import extract_text_from_pdf, filter_text, \
    create_inverted_index_from_filtered_text


router = APIRouter()


def process_pdf_logic(pdf_path: Path, conn: sqlite3.Connection):
    extracted_text = extract_text_from_pdf(pdf_path)
    filtered_text = filter_text(extracted_text)

    document_id = insert_document_to_db(conn, str(pdf_path), filtered_text)

    inverted_index_data = create_inverted_index_from_filtered_text(filtered_text, document_id)
    insert_inverted_index_to_db(conn, inverted_index_data)


@router.post("/pdf/process-pdf")
async def process_pdf(pdf: PDF):
    data_directory = Path(__file__).parent.parent.parent / 'data'
    database_path = data_directory / 'search_engine.db'
    pdf_path = pdf.path

    with sqlite3.connect(database_path) as conn:
        process_pdf_logic(pdf_path, conn)
