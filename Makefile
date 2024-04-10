.PHONY: build
build:
	pip install -r requirements.txt

.PHONY: start
start:
	python3 app/run.py