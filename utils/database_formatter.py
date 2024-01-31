import sqlite3


def get_table_schema(db_uri: str, table_name: str) -> str:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    cursor.execute(f"PRAGMA foreign_key_list({table_name});")
    foreign_keys = cursor.fetchall()
    cursor.execute(f"PRAGMA index_list({table_name});")
    primary_key_indices = cursor.fetchall()
    primary_key_columns = []
    for index_info in primary_key_indices:
        index_name = index_info[1]
        cursor.execute(f"PRAGMA index_info({index_name});")
        index_columns = cursor.fetchall()
        primary_key_columns.extend(column[2] for column in index_columns)
    conn.close()
    schema_str = f"CREATE TABLE {table_name} (\n"
    for column in columns:
        column_name = column[1]
        data_type = column[2]
        schema_str += f"  {column_name} {data_type}"
        if column_name in primary_key_columns:
            schema_str += " PRIMARY KEY"
        for foreign_key in foreign_keys:
            if column_name == foreign_key[3]:
                schema_str += f" REFERENCES {foreign_key[2]}({foreign_key[4]})"

        schema_str += ",\n"
    schema_str = schema_str.rstrip(",\n")
    schema_str += "\n);"
    return schema_str


def get_table_schema_with_samples(
    db_uri: str, table_name: str, sample_limit: int = 3
) -> str:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()

    # Fetch table schema
    cursor.execute(f"PRAGMA table_info(`{table_name}`);")
    columns = cursor.fetchall()
    cursor.execute(f"PRAGMA foreign_key_list(`{table_name}`);")
    foreign_keys = cursor.fetchall()
    cursor.execute(f"PRAGMA index_list(`{table_name}`);")
    primary_key_indices = cursor.fetchall()
    primary_key_columns = []

    for index_info in primary_key_indices:
        index_name = index_info[1]
        cursor.execute(f"PRAGMA index_info(`{index_name}`);")
        index_columns = cursor.fetchall()
        primary_key_columns.extend(column[2] for column in index_columns)

    # Construct CREATE TABLE statement
    schema_str = f"CREATE TABLE `{table_name}` (\n"
    for column in columns:
        column_name = column[1]
        data_type = column[2]
        schema_str += f"  {column_name} {data_type}"
        if column_name in primary_key_columns:
            schema_str += " PRIMARY KEY"
        for foreign_key in foreign_keys:
            if column_name == foreign_key[3]:
                schema_str += f" REFERENCES {foreign_key[2]}({foreign_key[4]})"

        schema_str += ",\n"
    schema_str = schema_str.rstrip(",\n")
    schema_str += "\n);\n"

    # Fetch sample data
    cursor.execute(f"SELECT * FROM `{table_name}` LIMIT {sample_limit};")
    sample_rows = cursor.fetchall()

    # Format sample rows for display
    if len(sample_rows) > 0:
        schema_str += f"Sample rows from `{table_name}`:\n"
        for row in sample_rows:
            formatted_row = ", ".join(str(item) for item in row)
            schema_str += f"{formatted_row}\n"

    conn.close()
    return schema_str


def get_all_table_names(db_uri: str) -> list[str]:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    conn.close()
    return [table_name[0] for table_name in table_names]


def get_number_of_columns(db_uri: str, given_tables: list[str]) -> list[int]:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    number_of_columns = []
    for given_table in given_tables:
        for table_name in table_names:
            if table_name[0] == given_table:
                cursor.execute(f"PRAGMA table_info({table_name[0]});")
                columns = cursor.fetchall()
                number_of_columns.append(len(columns))
                break
    conn.close()
    return number_of_columns

def get_all_column_names(db_uri: str, given_tables: list[str]) -> list[list[str]]:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    column_names = []
    for given_table in given_tables:
        for table_name in table_names:
            if table_name[0] == given_table:
                cursor.execute(f"PRAGMA table_info({table_name[0]});")
                columns = cursor.fetchall()
                column_names.append([column[1] for column in columns])
                break
    conn.close()
    return column_names

def get_all_primary_keys(db_uri: str, given_tables: list[str]) -> list[list[str]]:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    primary_keys = []
    for given_table in given_tables:
        for table_name in table_names:
            if table_name[0] == given_table:
                cursor.execute(f"PRAGMA table_info({table_name[0]});")
                columns = cursor.fetchall()
                primary_keys.append([column[1] for column in columns if column[5] == 1])
                break
    conn.close()
    return primary_keys


def get_table_representation(db_uri: str, given_tables: list[str]) -> list[str]:
    conn = sqlite3.connect(db_uri)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    table_schema = []
    for table_name in table_names:
        cursor.execute(f"PRAGMA table_info({table_name[0]});")
        columns = cursor.fetchall()
        table_schema.append({"table_name": table_name[0], "columns": columns})
    representations = []
    for given_table in given_tables:
        reperesentation = ""
        for table in table_schema:
            if table["table_name"] == given_table:
                reperesentation += (
                    f"Table {table['table_name']} has the following columns: ["
                )
                for column in table["columns"]:
                    reperesentation += f"{column[1]}, "
                reperesentation = reperesentation.rstrip(", ")
                reperesentation += "]\n"
                break
        representations.append(reperesentation)
    conn.close()
    return representations
