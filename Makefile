package: setup update_nltk
	pipenv lock -r > requirements.txt

setup:
	pipenv install

update_nltk:
	mkdir -p nltk_data/tokenizers
	pipenv run python -m textblob.download_corpora
	cp -rv ~/nltk_data/tokenizers/punkt ./nltk_data/tokenizers/

test:
	pipenv run python -m unittest discover . "*_test.py"

.PHONY: package install
