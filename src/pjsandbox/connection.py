#from settings import CONNECTIONS_FILE
from .settings import CONNECTIONS_FILE
import configparser
from clickhouse_driver import connect, Client
from pandas import DataFrame

config = configparser.ConfigParser()
config.read(CONNECTIONS_FILE)

class clickhouse_client:
    def execute(query: str):
        try :
            with Client(**config['clickhouse_client']) as clickhouse_clt:
                res = clickhouse_clt.execute("SELECT toYear(date) AS year, round(avg(price)) AS price FROM uk_price_paid GROUP BY year ORDER BY year")
                if res[0] is not None: column_indexlist = range(len(res[0]))
                return res, column_indexlist
        except:
            print('error executing query against clickhouse db')

""" result_list, len_result_list = clickhouse_client.execute(query='')
for row in result_list:
    print(row[0]) """

#class connection:


""" # Connection.py from clickhouse_driver
    Represents connection between client and ClickHouse server.

    :param host: host with running ClickHouse server.
    :param port: port ClickHouse server is bound to.
                 Defaults to ``9000`` if connection is not secured and
                 to ``9440`` if connection is secured.
    :param database: database connect to. Defaults to ``'default'``.
    :param user: database user. Defaults to ``'default'``.
    :param password: user's password. Defaults to ``''`` (no password).
    :param client_name: this name will appear in server logs.
                        Defaults to ``'python-driver'``.
    :param connect_timeout: timeout for establishing connection.
                            Defaults to ``10`` seconds.
    :param send_receive_timeout: timeout for sending and receiving data.
                                 Defaults to ``300`` seconds.
    :param sync_request_timeout: timeout for server ping.
                                 Defaults to ``5`` seconds.
    :param compress_block_size: size of compressed block to send.
                                Defaults to ``1048576``.
    :param compression: specifies whether or not use compression.
                        Defaults to ``False``. Possible choices:

                            * ``True`` is equivalent to ``'lz4'``.
                            * ``'lz4'``.
                            * ``'lz4hc'`` high-compression variant of
                              ``'lz4'``.
                            * ``'zstd'``.

    :param secure: establish secure connection. Defaults to ``False``.
    :param verify: specifies whether a certificate is required and whether it
                   will be validated after connection.
                   Defaults to ``True``.
    :param ssl_version: see :func:`ssl.wrap_socket` docs.
    :param ca_certs: see :func:`ssl.wrap_socket` docs.
    :param ciphers: see :func:`ssl.wrap_socket` docs.
    :param keyfile: see :func:`ssl.wrap_socket` docs.
    :param certfile: see :func:`ssl.wrap_socket` docs.
    :param server_hostname: Hostname to use in SSL Wrapper construction.
                            Defaults to `None` which will send the passed
                            host param during SSL initialization. This param
                            may be used when connecting over an SSH tunnel
                            to correctly identify the desired server via SNI.
    :param alt_hosts: list of alternative hosts for connection.
                      Example: alt_hosts=host1:port1,host2:port2.
    :param settings_is_important: ``False`` means unknown settings will be
                                  ignored, ``True`` means that the query will
                                  fail with UNKNOWN_SETTING error.
                                  Defaults to ``False``.
    :param tcp_keepalive: enables `TCP keepalive <https://tldp.org/HOWTO/
                          TCP-Keepalive-HOWTO/overview.html>`_ on established
                          connection. If is set to ``True``` system keepalive
                          settings are used. You can also specify custom
                          keepalive setting with tuple:
                          ``(idle_time_sec, interval_sec, probes)``.
                          Defaults to ``False``.
    :param client_revision: can be used for client version downgrading.
                          Defaults to ``None``.
    """






""" # HOW TO HANDLE PASSWORDS ON WINDOWS ... NEED A KEYSTORE Volt like PASSBOLT (passbolt.com)
import configparser
from getpass import getpass
import keyring

INSTANCE = "sqlserver"
config = configparser.ConfigParser()
config.read(r'..\config.ini')

server = config[INSTANCE]["server"]
port = config[INSTANCE]["port"]
ssl = config[INSTANCE]["ssl"]
user = config[INSTANCE]["user"]
# interact with Windows Credential Manager through the keyring library
password = keyring.get_password(INSTANCE, user)
if not password:
    password = getpass(f"Please insert password for user '{user}' and instance '{INSTANCE}':")
keyring.set_password(INSTANCE, user, password)
config[INSTANCE]["password"] = password
print(config[INSTANCE]["password"]) """

