package: setup update_nltk
	zip -r9 package.zip .

setup:
	pip install -t . -r requirements.txt

update_nltk:
	mkdir -p nltk_data/tokenizers
	python -m textblob.download_corpora
	cp -rv ~/nltk_data/tokenizers/punkt ./nltk_data/tokenizers/

test:
	python -m unittest discover . "*_test.py"

.PHONY: package install
