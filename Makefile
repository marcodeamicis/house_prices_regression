install:
	pip install pipenv && \
		pipenv install --dev --skip-lock

lint:
	flake8

test:
	pipenv run pytest --cov ./src/