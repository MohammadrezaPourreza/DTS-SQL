def sql_generation_prompt_token_counter(question, database_schema, query, tokenizer):
    user_message = f"""Given the following SQL tables, your job is to generate the Sqlite SQL query given the user's question.
    Put your answer inside the ```sql and ``` tags.
    {database_schema}
    ###
    Question: {question}
    """
    assitant_message = f"""
    ```sql
    {query} ;
    ```
    <|EOT|>
    """
    messages = [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": assitant_message},
    ]
    return len(tokenizer.apply_chat_template(messages, tokenize=True))


def schema_linking_prompt_token_counter(
    question, database_schema, correct_tables, correct_columns, tokenizer
):
    user_message = f"""Given the following SQL tables, your job is to determine the column names and table that the question is referring to.
{database_schema}
###
Question: {question}
"""
    assitant_message = f"""
Columns: {correct_columns}
Tables: {correct_tables}
 ;
"""
    messages = [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": assitant_message},
    ]
    return len(tokenizer.apply_chat_template(messages, tokenize=True))
