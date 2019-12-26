from alpine:latest

# Install Python3 on alpine
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Set Working Directory and install requirements
WORKDIR /app

COPY ./requirements.txt /app

RUN pip3 --no-cache-dir install -r requirements.txt

# Copy app source, expose port & run
COPY ./src/ /app

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["main.py"]
