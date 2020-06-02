FROM alpine:3.10.3

LABEL maintainer.name="Munis Isazade" \
      maintainer.email="munisisazade@gmail.com"

WORKDIR /code

COPY . .

RUN apk update --no-cache \
&& apk upgrade --no-cache \
&& apk add --no-cache python3 \
&& python3 -m venv .venv \
&& . .venv/bin/activate \
&& pip install --no-cache-dir -U pip \
&& pip install --no-cache-dir -r requirements.txt \
&& rm -f requirements.txt

ENV PATH="/code/.venv/bin:$PATH"

EXPOSE 5052

CMD [".venv/bin/python","-u","run.py"]
