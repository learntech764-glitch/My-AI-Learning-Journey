import tiktoken

#encoding = tiktoken.get_encoding("cl100k_base")
#encoding=tiktoken.encoding_for_model("gpt-5.x")
encoding=tiktoken.encoding_for_model("gpt-3.5-turbo")
def count_tokens(text: str) -> int:
    tokens = encoding.encode(text)
    return len(tokens)

# token IDs
def get_token_ids(text: str) -> list[int]:
    tokens = encoding.encode(text)
    return tokens

# tokens
def get_tokens(text: str) -> list[str]:
    tokens = encoding.encode(text)
    return [encoding.decode([token]) for token in tokens]