FROM python:3.9-slim-buster

WORKDIR /app

# COPY requirements.txt ./requirements.txt
# RUN pip3 install pip --upgrade && pip3 install -r requirements.txt

COPY Pipfile ./Pipfile
RUN pip3 install pip --upgrade && pip3 install pipenv
ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv install --skip-lock

COPY . .

EXPOSE 8501

# CMD streamlit run main.py
CMD pipenv run streamlit run main.py
