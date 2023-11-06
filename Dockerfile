FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENV DB_USERNAME=${{ env.DB_USERNAME}}
ENV DB_PASSWORD=${{ secrets.DB_PASSWORD}}
ENV DB_NAME=${{ env.DB_NAME}}
ENV HOST_SERVER=${{ env.HOST_SERVER}}
ENV DB_SERVER_PORT=${{ env.DB_SERVER_PORT}}
ENV SSL_MODE=${{ env.SSL_MODE}}
ENV PGADMIN_DEFAULT_EMAIL=${{ env.PGADMIN_DEFAULT_EMAIL}}
ENV PGADMIN_DEFAULT_PASSWORD=${{ secrets.PGADMIN_DEFAULT_PASSWORD}}
ENV SECRET_KEY=${{ env.SECRET_KEY}}
ENV ALGORITHM=${{ env.ALGORITHM}}

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]