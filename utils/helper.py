from fuzzywuzzy import process
from langchain.embeddings import OpenAIEmbeddings
from sql_metadata import Parser
from typing import Any, Tuple, List
from dotenv import load_dotenv
from numpy import dot
from numpy.linalg import norm


def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:
    return dot(a, b) / (norm(a) * norm(b))


load_dotenv()


def find_closest_match(table_name: str, all_tables: list[str]) -> Any:
    closest_match = process.extractOne(table_name, all_tables)
    if closest_match:
        return closest_match[0]
    else:
        return None


def find_correct_tables_and_columns(
    query: str,
    all_tables: list[str],
) -> Tuple[list[str], list[str]]:
    correct_tables = Parser(query).tables
    correct_columns = Parser(query).columns
    for i, table in enumerate(correct_tables):
        closest_match = find_closest_match(table, all_tables)
        if closest_match:
            correct_tables[i] = closest_match
    return correct_tables, correct_columns


def find_table_embedding(
    table_representations: list[str],
) -> list[list[float]]:
    # embeddings = HuggingFaceEmbeddings()
    embeddings = OpenAIEmbeddings()
    table_embeddings = embeddings.embed_documents(table_representations)
    return table_embeddings


def rank_the_tables(
    table_embedding: list[float],
    tables: List[Tuple[str, list[float]]],
) -> list[str]:
    table_rankings = []
    for table_name, table_embedding in tables:
        table_rankings.append(
            (table_name, cosine_similarity(table_embedding, table_embedding))
        )
    table_rankings.sort(key=lambda x: x[1], reverse=True)
    return [table_name for table_name, _ in table_rankings]
