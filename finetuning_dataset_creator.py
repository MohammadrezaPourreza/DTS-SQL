import pandas as pd
from tqdm import tqdm
from utils.database_formatter import get_table_schema_with_samples, get_all_table_names
from utils.sql_regularizator import format_and_lowercase_sql_query
from utils.prompts import (
    sql_generation_prompt_token_counter,
    schema_linking_prompt_token_counter,
)
from transformers import AutoTokenizer
from sql_metadata import Parser

BASE_DATABASES_DIR = "datasets/database"
MODEL_NAME = "deepseek-ai/deepseek-coder-6.7b-instruct"
CONTEXT_WINDOW = 3000
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def load_spider_train_set():
    df1 = pd.read_json("datasets/train_others.json")
    df2 = pd.read_json("datasets/train_spider.json")
    df = pd.concat([df1, df2])
    df = df.reset_index(drop=True)
    return df


def load_spider_dev_set():
    df = pd.read_json("spider-syn/dev.json")
    return df


def create_sql_generation_correct_tables(dataset, question, query, db_uri):
    correct_tables = Parser(query).tables
    correct_columns = Parser(query).columns
    database_schema_filtered = ""
    for table in correct_tables:
        database_schema_filtered += get_table_schema_with_samples(db_uri, table)
        database_schema_filtered += "\n"
    database_schema = ""
    all_tables = get_all_table_names(db_uri)
    for table in all_tables:
        database_schema += get_table_schema_with_samples(db_uri, table)
        database_schema += "\n"
    if (
        schema_linking_prompt_token_counter(question, database_schema, correct_tables, correct_columns, tokenizer)
        <= CONTEXT_WINDOW
    ):
        dataset.append(
            {
                "db_id": db_uri.split("/")[-1].split(".")[0],
                "question": question,
                "query": query,
                "filtered_database_schema": database_schema_filtered,
                "database_schema": database_schema,
                "correct_tables": ", ".join(correct_tables),
                "correct_columns": ", ".join(correct_columns),
            }
        )
    return dataset


def create_full_sql_generation(
    dataset, question, query, db_uri, full_finetuning_errors
):
    database_schema = ""
    all_tables = get_all_table_names(db_uri)
    for table in all_tables:
        database_schema += get_table_schema_with_samples(db_uri, table)
        database_schema += "\n"
    if (
        sql_generation_prompt_token_counter(question, database_schema, query, tokenizer)
        <= CONTEXT_WINDOW
    ):
        dataset.append(
            {
                "db_id": db_uri.split("/")[-1].split(".")[0],
                "question": question,
                "query": query,
                "database_schema": database_schema,
            }
        )
    else:
        full_finetuning_errors += 1
    return dataset, full_finetuning_errors


if __name__ == "__main__":
    # Load Spider train set
    df = load_spider_train_set()
    df = df.sample(frac=1).reset_index(drop=True)
    finetuning_dataset = []
    filtered_finetuning_dataset = []
    full_finetuning_errors = 0
    filtered_finetuning_errors = 0
    for index, row in tqdm(df.iterrows(), total=len(df)):
        db_id = row["db_id"]
        question = row["question"]
        query = row["query"]
        query = format_and_lowercase_sql_query(query)
        db_uri = f"{BASE_DATABASES_DIR}/{db_id}/{db_id}.sqlite"
        all_tables = get_all_table_names(db_uri)
        try:
            filtered_finetuning_dataset = create_sql_generation_correct_tables(
                filtered_finetuning_dataset, question, query, db_uri
            )
        except Exception:
            filtered_finetuning_errors += 1
        finetuning_dataset, full_finetuning_errors = create_full_sql_generation(
            finetuning_dataset, question, query, db_uri, full_finetuning_errors
        )
    # Save finetuning dataset
    print(f"Full finetuning set errors: {full_finetuning_errors}")
    print(f"Filtered finetuning set errors: {filtered_finetuning_errors}")
    df = pd.DataFrame(finetuning_dataset)
    df.to_csv("training/full_finetuning_dataset.csv", index=False)
    df = pd.DataFrame(filtered_finetuning_dataset)
    df.to_csv("training/filtered_finetuning_dataset.csv", index=False)
    # Load Spider dev set
    df = load_spider_dev_set()
    validation_dataset = []
    validation_dataset_fromatted = []
    filtered_validation_dataset = []
    validation_set_errors = 0
    validation_set_formatted_errors = 0
    filtered_validation_set_errors = 0
    for index, row in tqdm(df.iterrows(), total=len(df)):
        db_id = row["db_id"]
        question = row["SpiderSynQuestion"]
        query = row["query"]
        formatted_query = format_and_lowercase_sql_query(query)
        db_uri = f"{BASE_DATABASES_DIR}/{db_id}/{db_id}.sqlite"
        try:
            filtered_validation_dataset = create_sql_generation_correct_tables(
                filtered_validation_dataset, question, formatted_query, db_uri
            )
        except Exception:
            filtered_validation_set_errors += 1
        validation_dataset_fromatted, validation_set_formatted_errors = create_full_sql_generation(
            validation_dataset_fromatted,
            question,
            formatted_query,
            db_uri,
            validation_set_formatted_errors,
        )
        validation_dataset, validation_set_errors = create_full_sql_generation(
            validation_dataset, question, query, db_uri, validation_set_errors
        )
    print(f"Filtered validation set errors: {filtered_validation_set_errors}")
    print(f"Validation set formatted errors: {validation_set_formatted_errors}")
    print(f"Validation set errors: {validation_set_errors}")
    # Save validation dataset
    df = pd.DataFrame(validation_dataset)
    df.to_csv("validation/spider_syn_dataset.csv", index=False)
    df = pd.DataFrame(validation_dataset_fromatted)
    df.to_csv("validation/spider_syn_dataset_formatted.csv", index=False)
    df = pd.DataFrame(filtered_validation_dataset)
    df.to_csv("validation/filtered_spider_syn_dataset", index=False)
