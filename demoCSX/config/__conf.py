import os.path
import ConfigParser


def __loadConfig():
    cf=ConfigParser.SafeConfigParser()
    cf.read([
        '/etc/demoCSX.conf',
        os.path.expanduser('~/demoCSX.conf'),
        '/home/arkilic/python_packages/demo/demoCSX.conf'
    ])
    return cf


conf_dict = __loadConfig()

