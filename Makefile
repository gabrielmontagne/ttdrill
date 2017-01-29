NAME := ttdrill
VERSION := 0.0.1
AUTHOR := Gabriel Montagné Láscaris-Comneno
AUTHOR_EMAIL := gabriel@tibas.london
YEAR := $(shell date +%Y)

init:
	pip3 install -r requirements.txt

test:
	nosetests

lint:
	@echo '---PEP8---'
	@pep8 -v $(NAME)
	@echo '---pylint---'
	@pylint $(NAME)
