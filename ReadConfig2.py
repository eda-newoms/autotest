import os
import configparser

path=os.path.split(__file__)[0];
file=os.path.join(path,'envConfig.ini');
cf=configparser.ConfigParser();
cf.read(file);

class ReadConfig:
    environment = 'Default';

    def GetConfig(self,name=''):
        conf = cf.get(self.environment,name);
        return conf;
