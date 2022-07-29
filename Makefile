install:
	pip install pipenv && \
		pipenv install --dev --skip-lock

lint:
	pipenv run flake8 ./src/

test:
	pipenv run pytest --cov ./src/
