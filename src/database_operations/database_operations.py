import sqlite3


def insert_document_to_db(conn, file_path, text_content):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO documents (file_path, text_content, time_created) VALUES (?, ?, CURRENT_TIMESTAMP)",
                   (file_path, text_content))
        conn.commit()
        document_id = cursor.lastrowid

        return document_id

    except sqlite3.IntegrityError:
        cursor.execute("UPDATE documents SET text_content = ?, time_created = CURRENT_TIMESTAMP WHERE file_path = ?",
                       (text_content, file_path))

        conn.commit()
        cursor.execute("SELECT document_id FROM documents WHERE file_path = ?", (file_path,))

        document_id = cursor.fetchone()[0]

        update_inverted_index_for_document(conn, document_id)

        return document_id


def update_inverted_index_for_document(conn, document_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inverted_index WHERE document_id = ?", (document_id,))
    conn.commit()


def insert_inverted_index_to_db(conn, inverted_index_data):
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO inverted_index (term, document_id) VALUES (?, ?)",
                       inverted_index_data)
    conn.commit()

# def get_all_documents(conn):
#     cursor = conn.cursor()
#     cursor.execute("SELECT file_path, time_created FROM documents")