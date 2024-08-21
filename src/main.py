import uvicorn

from server import serving, config


# logging.getLogger("uvicorn.error").disabled = True
# logging.getLogger("uvicorn.access").disabled = True


def main():
    uvicorn.run(
        serving.app,
        host=config.host,
        port=config.port,
        workers=config.service_workers)


if __name__ == '__main__':
    main()
