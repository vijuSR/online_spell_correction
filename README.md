# online_spell_correction
Personalized online spell correction and auto-completion.

Typical spell correction solutions used in production systems consist of large indexed lookup tables based on a global model trained across many users over a large scale web corpus or a query log.For search over personal corpora, such as email, this global solution is not sufficient, as it ignores the user’s personal lexicon. Without personalization, global spelling fails to correct tail queries drawn from a user’s own, often idiosyncratic, lexicon. Personalization using existing algorithms is difficult due to resource constraints and unavailability of sufficient data to build per-user models [1].  

It works by augmenting the Levenshtein distance. It is a basic implementation based on the algorithms defined in the paper referenced below.

## Getting Started
1. Language requirement: Python3 (developed using python3.6)  
1. ### Get the code:
    - Using SSH: `git clone git@github.com:vijuSR/online_spell_correction.git`  
    OR  
    - Using HTTP: `git clone https://github.com/vijuSR/online_spell_correction.git`

1. ### Setup the Virtual Environment (Recommended):
    - Create the virtual environment
        - `python3 -m venv </path/to/venv>`  
    - Activate your virtual-environment
        - Linux: `source </path/to/venv>/bin/activate`
        - Windows: `cd </path/to/venv>` then `.\Scripts\activate`  
    - Install the requirements
        - `cd <root-dir-of-project>`
        - `pip install -I -r requirements.txt`

        #### That's all for the setup ! :smiley: 
        
## Run
- The Lexicon
        - `cd <root-dir-of-project>`: you can see a file named lexicon.json, it contains all the candidates that are to be ranked for a given user query input.
        - Change the content of the "lexicon.json" as required. Currently it contains a sample lexicon for dynasore names.

- `cd <root-dir-of-project>`
- `python3 routes.py`

## References:
1. Gupta, J. P., Qin, Z., Bendersky, M., & Metzler, D. (2019). Personalized Online Spell Correction for Personal Search.
