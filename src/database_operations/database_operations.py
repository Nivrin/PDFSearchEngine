def insert_document_to_db(conn, file_path, text_content):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO documents (file_path, text_content) VALUES (?, ?)", (file_path, text_content))
    conn.commit()

    return cursor.lastrowid


def insert_inverted_index_to_db(conn, inverted_index_data):
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO inverted_index (term, document_id) VALUES (?, ?)",
                       inverted_index_data)
    conn.commit()
