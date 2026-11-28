from tokenizer import count_tokens, get_token_ids, get_tokens

text = "Elephant is a huge animal"

print(
    "Token Count:",
    count_tokens(text)
)
print(get_token_ids(text))
print(get_tokens(text))