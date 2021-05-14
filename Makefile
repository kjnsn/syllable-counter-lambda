package: setup nltk_data
	pipenv lock -r > requirements.txt

setup:
	pipenv install

nltk_data: update_nltk_data

update_nltk_data: setup
	mkdir -p nltk_data/tokenizers
	pipenv run python -m textblob.download_corpora
	cp -rv ~/nltk_data/tokenizers/punkt ./nltk_data/tokenizers/
	find nltk_data -type f ! -name '*english*' -name '*.pickle' -exec rm '{}' \; # Remove everything that isn't the english file

test: 
	pipenv run python -m unittest discover . "*_test.py"

.PHONY: package install
