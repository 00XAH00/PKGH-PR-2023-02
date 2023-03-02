FROM python:3.11

#
WORKDIR /app

ARG Production

EXPOSE 5478

ENV PYTHONPATH=/app

COPY ../backend/poetry.lock ../backend/pyproject.toml /app/
#
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
#
COPY ../backend/ /app
COPY ./backend/.env /app/.env

#
CMD ["poetry", "run", "python3", "src/main.py"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
