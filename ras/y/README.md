1. Run modify_rasa_hf.py file to place /hugging_face folder in the sitepackages/rasa/nlu/utils/


2.
Download infic bert from https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/models/indic-bert-v1.tar.gz
Extract and copy its folder path
Place the folder path in config_transformers.py

rasa train -c config_transformers.py