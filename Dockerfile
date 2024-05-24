FROM python:3.9

RUN mkdir /salary_watcher

WORKDIR salary_watcher

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev,test --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY . .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]