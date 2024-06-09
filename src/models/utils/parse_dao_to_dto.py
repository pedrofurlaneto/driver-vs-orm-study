import psycopg

def parse_DAO_to_DTO_list(description, rows): 
    entity_list = []

    metadata = [description[0] for description in description]
    for values in rows:
        entity_list.append(dict(zip(metadata, values)))

    return entity_list
