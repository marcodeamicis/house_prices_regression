install:
	pip install pipenv && \
		pipenv install --dev --skip-lock

lint:
	flake8 src

test:
	pipenv run pytest --cov ./src/