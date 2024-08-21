import os

from configs import settings
from utils.lazy_property import LazyProperty as lazyproperty


class ConfigParser(object):

    def __init__(self):
        pass

    @lazyproperty
    def service_name(self):
        return os.getenv("SERVER_NAME", settings.SERVICE_NAME)

    @lazyproperty
    def host(self):
        return os.getenv("SERVICE_HOST", settings.SERVICE_HOST)

    @lazyproperty
    def port(self):
        return os.getenv("SERVICE_PORT", settings.SERVICE_PORT)

    @lazyproperty
    def service_workers(self):
        return os.getenv("SERVICE_WORKERS", settings.SERVICE_WORKERS)

    @lazyproperty
    def log_filepath(self):
        filepath = os.getenv("LOG_FILEPATH", settings.LOG_FILEPATH)
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        return os.path.join(filepath, 'service.log')

    @lazyproperty
    def log_level(self):
        return os.getenv("LOG_LEVEL", settings.LOG_LEVEL)

    @lazyproperty
    def model_filepath(self):
        return os.getenv("MODEL_FILEPATH", settings.MODEL_FILEPATH)
