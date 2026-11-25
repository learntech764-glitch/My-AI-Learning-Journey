## My understanding 

 - reference video : 
                1. https://www.youtube.com/watch?v=vZRE_jhA3Qc&t=2s
                2. https://www.youtube.com/watch?v=jXzLYFLzdl4
                3. https://www.youtube.com/channel/UCbb3yjpby3NDps6n4Xq3W5A/videos
                4. https://www.youtube.com/watch?v=URucTTDWgI0&list=PLWSlr9idVBc0&index=4

    # 1. What is LLM?
        - Large Language Model
        - AI trained on vast text data to learn the patterns of human language and generate responses.
        - LLM is a pattern matcher
        - Ingest data -> Train Model -> Fine Tune(3 steps)
        - given sequence of words its job is to predicting the next word
        - because it doesnt truly understand anything it can just confidently make stuff up that is called hallucinations
    
    # 2.Why ChatGPT Understands You?
        - An untamed data forest
        - Common Craw -archiving the internent(2.7 B webpages)
        - the great data cleanup 
        - url filtering(exclude undesirable domains like malware and spam) - > text extraction(remove ads and navigation menus from HTML) -> Language filter(Keep pages in the desired language say English) -> Deduplication (remove duplicate pages and low quality text.)-> PII removal(Filter out personally identifiable information)
        - left with 44 terabyte library
        - 44 TB high quality text
    
    # 3. Tokenization
        A) The AI's Reading problem
            - human types hello - > computer sees UTF-8 binary code
        B) From Bits to A smarter grouping (bytes)
            -start with bits -> group into 8s and - > form a byte
            8 groups of 0s and 1s is 256 symbols 
        C) Byte Pair encoding
            - finds the frequent consequitive sysmbol and merge them into a new single sysmbol
            - find common pair -> mint new symbol -> replace pair -> repeat
            - output is vocabulary of 100,277
        D) Tokens in Action
            - "Hello World"
            - GPT-4 Tokenizer ->2 tokens "Hello" and " world"(with space)
            if we use "helloworld" then we get "hello" or "wo" or "rld"

NOTE : 1 token ~ 4 characters
3/4 of a word
100 tokens ~ 75 words

## How LLMs Actually Work?
    - Refer excel "How LLM works.xlsx"

## What is Context Window?
    - Input tokens+ Output tokens
    - Amount of info u pass to LLM model
    - each LLM model has a context window limit
    - LLM does not remember the context ( we need to create temprary storage and pass as user role and assistant role
    user : A
    Assistant:B

    user : (history -> A,B)+C(new input)
    Assistant :D

    user : (history -> A,B,C,D)+E(new input)
    Assistant :F
    
    ) .. token increases with the history
    - prompt does not train the LLM
    - if u pass entire history as input to LLM then context window will get occupied ? no best apprach is summarize the context
    (
        user : (summarize history -> A,B,C,D)+E(new input)
      Assistant :F

    )
    - if LLm model has limited info then it will halucinate

## Why does the LLM model hallucinate
   - The task of LLM is to predict next token
   - not to validte the info
   - so the highliy probable next token is picked as a response 
   - And LLm gives a confident response


   NOTE LLM does not contains latest information. It will have the vocab it was traied on . So inorder to get the latest information there is an orchestration which gets the intent and decides that it has to search web and then passes the input+ the search result to LLMM to get the response