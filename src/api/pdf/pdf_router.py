from pathlib import Path
import sqlite3

from fastapi import APIRouter, HTTPException
from ...database_operations.database_operations import (insert_document_to_db,
                                                                         insert_inverted_index_to_db)
from ...pdf_processing.pdf_processor import (extract_text_from_pdf, filter_text,
                                                              create_inverted_index_from_filtered_text)
from ..pdf.pdf_models import PDF


router = APIRouter()


def process_pdf_logic(pdf_path: Path, conn: sqlite3.Connection):
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        filtered_text = filter_text(extracted_text)

        document_id = insert_document_to_db(conn, str(pdf_path), filtered_text)

        inverted_index_data = create_inverted_index_from_filtered_text(filtered_text, document_id)
        insert_inverted_index_to_db(conn, inverted_index_data)

    except Exception as e:
        # Handle the exception here, you might want to log it or take specific actions
        raise HTTPException(status_code=500, detail=f"Failed to process PDF: {e}")


@router.post("/pdf/process-pdf")
async def process_pdf(pdf: PDF):
    try:
        data_directory = Path(__file__).parent.parent.parent.parent / 'data'
        database_path = data_directory / 'search_engine.db'
        pdf_path = pdf.path

        with sqlite3.connect(database_path) as conn:
            process_pdf_logic(pdf_path, conn)
        return {"message": "PDF processed successfully",
                "Errorcode": HTTPException(status_code=200)}

    except Exception as e:
        return {"message": f"Failed to process PDF request: {e}",
                "Errorcode": HTTPException(status_code=500)}
