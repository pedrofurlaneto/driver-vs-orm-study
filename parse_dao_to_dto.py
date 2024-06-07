import psycopg

def parse_DAO_to_DTO_list(session: psycopg.Cursor): 
    entity_list = []

    metadata = [description[0] for description in session.description]
    for values in session.fetchall():
        entity_list.append(dict(zip(metadata, values)))

    return entity_list
