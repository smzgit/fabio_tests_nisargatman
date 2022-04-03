from flask import Flask
import  configparser
import logging
def getLogger():
    LOG = logging.getLogger("VectorAI_ASSG_Logs -> ")
    LOG.setLevel(level=logging.INFO)
    fh = logging.StreamHandler()
    fh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d) - %(message)s')
    fh.setFormatter(fh_formatter)
    LOG.addHandler(fh)
    return LOG
#initialize Flask application
app = Flask(__name__)
LOG = getLogger()
conifg = configparser.ConfigParser()
conifg.read('/app/wiki_app/postgres_db.ini')
global conifg_dict
conifg_dict={}
conifg=conifg['postgres']
conifg_dict['user'] =conifg.get('user','-')
conifg_dict['password'] =conifg.get('password','-')
conifg_dict['host'] =conifg.get('host','-')
conifg_dict['port'] =conifg.get('port','-')
conifg_dict['database'] =conifg.get('database','-')


