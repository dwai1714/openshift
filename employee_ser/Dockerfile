FROM python:2-onbuild
# get ContainerPilot release
ENV CONTAINERPILOT_VERSION 2.4.1
RUN export CP_SHA1=198d96c8d7bfafb1ab6df96653c29701510b833c \
    && curl -Lso /tmp/containerpilot.tar.gz \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/containerpilot-${CONTAINERPILOT_VERSION}.tar.gz" \
    && echo "${CP_SHA1}  /tmp/containerpilot.tar.gz" | sha1sum -c \
    && tar zxf /tmp/containerpilot.tar.gz -C /bin \
    && rm /tmp/containerpilot.tar.gz

# add ContainerPilot configuration
COPY containerpilot.json /etc/containerpilot.json
ENV CONTAINERPILOT=file:///etc/containerpilot.json

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

EXPOSE 8080
#COPY ./app /app
CMD /bin/containerpilot python employee_ser.py
#CMD ["python", "email_ser.py"]
#EXPOSE 9001
