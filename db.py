from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import DictCursor, LoggingConnection
from contextlib import contextmanager
import os


env = os.getenv('EVENTBOOKER_ENV', 'development')


def get_password():
    with open('secret') as f:
        return f.read().strip()


setting = {
    'development':  {
        'dbname': 'eventbooker_dev',
        'user': 'postgres',
        'host': 'localhost',
        'password': ''
    },
    'production':  {
        'dbname': 'eventbooker',
        'user': 'postgres',
        'host': 'db',
        'password': get_password() if env == 'production' else ''
    }
}[env]


import logging

import sqlalchemy as sa
import psycopg2.extras

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()


import psycopg2.extensions
import logging


class LoggingCursor(DictCursor):

    def execute(self, sql, args=None):
        logger = logging.getLogger('sql_debug')
        logger.info(self.mogrify(sql, args))

        try:
            super(LoggingCursor, self).execute(sql, args)
        except Exception, exc:
            logger.error("%s: %s" % (exc.__class__.__name__, exc))
            raise

pool = ThreadedConnectionPool(1, 20,
                              dbname=setting['dbname'],
                              user=setting['user'],
                              host=setting['host'],
                              password=setting['password']
                              )


@contextmanager
def get_cursor():
    con = pool.getconn()
    try:
        yield con.cursor(cursor_factory=LoggingCursor)
    finally:
        pool.putconn(con)
