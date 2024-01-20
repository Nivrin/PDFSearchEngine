FROM python:3.11.4

WORKDIR .

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]