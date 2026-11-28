## Steps to Create and Execute

    1. Create a virtual environment
            - python -m venv venv
    2. Activate the virtual environment
            - venv\Scripts\activate
    3. Create a requirments.txt file 
                tiktoken
                sentence-transformers
                numpy
                scikit-learn
                pandas
    4. Execute the requirement file
            - pip install -r requirements.txt
    5. What Problem Are We Solving?
        Humans see:
                - I love AI
        Model sees:
                  [40, 3021, 15592] and Not words
        . Create a tokenizer.py
        . Create a testcase file to execute it test_tokenizer.py
        . Execute python test_tokenizer.py
        . u can try different models
    6. What Is an Embedding?
        Machine can't store:
                - I love AI
        It converts text into numbers.
                Example:               
                [0.23,
                0.81,
                -0.44,
                ...
                ]
        . Create a embedder.py
        . Create a testcase file to execute it test_embedder.py
        . Execute python test_embedder.py
    7. Similarity Search
        Now we compare vectors.
            Example
                Vector A
                    [1,2,3]
                Vector B
                    [1,2,4]
            Very similar.
                Vector C
                    [-10,4,99]
            Not similar.
        . Create a search.py
        . Create a testcase file to execute it test_similarity.py
        . Execute python test_similarity.py


## Semantic Search Engine

1. Create data.py
2. Create semantic_search.py
3. Create run_search.py