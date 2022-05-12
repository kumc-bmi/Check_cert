
class service:
    def __init__(self, cname, port):
        self.cname = cname
        self.port = port
        self.failing = False
        self.type = "web"


def check_date(service, OpenSSL, ssl, datetime):
    cert = ssl.get_server_certificate((service.cname, service.port))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    
    today = datetime.datetime.today()

    date_format, encoding = "%Y%m%d%H%M%SZ", "ascii"
    cert_date = datetime.datetime.strptime(x509.get_notAfter()
                                           .decode(encoding), date_format)

    if cert_date < today + datetime.timedelta(days=30):
        service.failing = True


def main(list_of_servs, which_certs, environ, OpenSSL, ssl, datetime, pd, regex, logging):
    
    list_of_servs = list_of_servs[1:len(list_of_servs)-1]
    print(list_of_servs)
    cnames = list_of_servs.split(',')

    services = []

    for i in cnames:
        this = service(i, 443)
        services.append(this)

    print('------')
    for i in services:
        print('checking ' + i.cname)
        check_date(i, OpenSSL, ssl, datetime)
        if i.failing == True:
            logging.info(i.cname + ' will expire within 30 days')
        else:
            logging.info(i.cname + ' server is safe')
    print('------')

    # ensure non-zero exit if any were failing    
    for i in services:
        assert i.failing == False


if __name__ == "__main__":    
    def _server_status():
        '''
        # https://www.madmode.com/2019/python-eng.html
        '''
        # pip3 install pyopenSSL --user
        import OpenSSL
        import ssl
        import datetime
        import logging
        from os import environ
        import pandas as pd
        from sys import argv, stderr
        from pathlib2 import Path
        import regex

        logging.basicConfig(level=logging.DEBUG, stream= stderr)

        if len(argv[1]) != 3:
            print(argv)
            logging.error("""Wrong format or arguments :
             please try like 'python3 cert_scanner.py [list_of_servers_separated_by_commas_no_double_quotes] which_certs""")

        [list_of_servs, which_certs] = argv[1:]
        print("The value is %s",list_of_servs)
        main(list_of_servs, which_certs, environ, OpenSSL, ssl, datetime, pd, regex, logging)

    _server_status()
