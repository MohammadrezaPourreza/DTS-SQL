import re
from sqlglot.tokens import Tokenizer, TokenType

KEYWORDS = [
    TokenType.SELECT,
    TokenType.FROM,
    TokenType.WHERE,
    TokenType.ORDER_BY,
    TokenType.GROUP_BY,
    TokenType.JOIN,
    TokenType.UNION,
    TokenType.INTERSECT,
    TokenType.EXCEPT,
    TokenType.HAVING,
    TokenType.IN,
    TokenType.NOT,
    TokenType.LIMIT,
    TokenType.DESC,
    TokenType.ASC,
    TokenType.DISTINCT,
    TokenType.LIKE,
    TokenType.BETWEEN,
    TokenType.STAR,
    TokenType.R_PAREN,
    TokenType.L_PAREN,
    TokenType.COMMA,
    TokenType.GT,
    TokenType.GTE,
    TokenType.LTE,
    TokenType.EQ,
    TokenType.NEQ,
    TokenType.LT,
    TokenType.AND,
    TokenType.OR,
    TokenType.ON,
    TokenType.SEMICOLON,
    TokenType.PLUS,
]

tokenizer = Tokenizer()


def format_and_lowercase_sql_query(query):
    tokens = tokenizer.tokenize(query)
    for token in tokens:
        if token.token_type not in KEYWORDS:
            if (
                query[query.find(token.text) - 1] != "'"
                and query[query.find(token.text) - 1] != '"'
            ):
                query = query.replace(token.text, token.text.lower())
        else:
            query = query.replace(token.text, token.text.upper())

    def format_aggregation_functions(match):
        function_name = match.group(1).upper()  # Aggregation function name in lowercase
        arguments = match.group(2)  # Arguments inside the parentheses
        return f"{function_name}({arguments})"

    agg_func_pattern = r"\b(COUNT|SUM|AVG|MIN|MAX)\s*\(\s*([^)]*?)\s*\)"
    formatted_query = re.sub(
        agg_func_pattern, format_aggregation_functions, query, flags=re.IGNORECASE
    )
    return formatted_query
