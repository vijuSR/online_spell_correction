# online_spell_correction
Personalized online spell correction and auto-completion.

It works by augmenting the Levenshtein distance.
It is a basic implementation based on the algorithms defined in the paper referenced below.

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
        - `pip install --upgrade -I -r requirements.txt`
    - The Lexicon
        - `cd <root-dir-of-project>`: you can see a file named lexicon.json, it contains all the candidates that are to be ranked for a given user query input.
        - Open the "lexicon.json" and fill it as instructed inside file.

        #### That's all for the setup ! :smiley: 
        
## Run
- `cd <root-dir-of-project>`
- `python3 routes.py`

## References:
- Gupta, J. P., Qin, Z., Bendersky, M., & Metzler, D. (2019). Personalized Online Spell Correction for Personal Search.
