FROM python:3.11-slim

ENV PYTHONUNBUFFERED=True
ENV APP_HOME=/app
WORKDIR ${APP_HOME}

COPY .github/workflows/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY .github/workflows/*.py ./
COPY .github/workflows/index.html ./index.html
COPY .github/workflows/app.js ./app.js
COPY .github/workflows/index.css ./index.css

CMD exec uvicorn main:app --host 0.0.0.0 --port $PORT
