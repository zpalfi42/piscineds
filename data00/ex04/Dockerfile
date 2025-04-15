FROM postgres:16.4-alpine3.20

# Install Python
RUN apk add --no-cache python3 py3-pip gcc musl-dev postgresql-dev python3-dev libffi-dev linux-headers

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./scripts/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN apk del gcc musl-dev postgresql-dev python3-dev

# Set default command (optional, PostgreSQL command is inherited)
CMD ["postgres"]