FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENV DB_USERNAME=${{ vars.DB_USERNAME}}
ENV DB_PASSWORD=${{ secrets.DB_PASSWORD}}
ENV DB_NAME=${{ vars.DB_NAME}}
ENV HOST_SERVER=${{ vars.HOST_SERVER}}
ENV DB_SERVER_PORT=${{ vars.DB_SERVER_PORT}}
ENV SSL_MODE=${{ vars.SSL_MODE}}
ENV PGADMIN_DEFAULT_EMAIL=${{ vars.PGADMIN_DEFAULT_EMAIL}}
ENV PGADMIN_DEFAULT_PASSWORD=${{ secrets.PGADMIN_DEFAULT_PASSWORD}}
ENV SECRET_KEY=${{ vars.SECRET_KEY}}
ENV ALGORITHM=${{ vars.ALGORITHM}}

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]