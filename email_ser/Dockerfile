FROM python:2-onbuild

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD mkdir /tmp
#CMD mkdir /config
#COPY settings.py /config/settings.py
#COPY wsgi.ini /config/wsgi.ini
#CMD python api_prod.py
#CMD ls -la
#ENV  EVE_SETTINGS=/config/settings.py
#CMD uwsgi --ini /config/wsgi.ini
#CMD gunicorn api:app -b 0.0.0.0:8000
#CMD ls; echo $EVE_SETTINGS

EXPOSE 9008
#EXPOSE 8080
#COPY ./app /app
CMD ["python", "email_ser.py"]

