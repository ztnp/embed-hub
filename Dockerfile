FROM python:3.10.12-slim AS builder

RUN mkdir /install

WORKDIR /install

COPY ./requirements.txt .

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --prefix="/install" -r requirements.txt

FROM python:3.10.12-slim AS final

COPY --from=builder /install /usr/local

RUN mkdir /app

WORKDIR /app

COPY ./bin/entrypoint.sh .

RUN chmod +x /app/entrypoint.sh

COPY ./src /app

ENTRYPOINT ["/app/entrypoint.sh"]