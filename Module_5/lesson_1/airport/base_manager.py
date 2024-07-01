import psycopg2


class BaseManager:
    table = None

    def __init__(self, conn_params):
        self.conn_params = conn_params

    def _connect(self):
        return psycopg2.connect(**self.conn_params)
