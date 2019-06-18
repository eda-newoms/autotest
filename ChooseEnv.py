import ReadConfig2;

#Choose environment: 25, 26, Test, Prod environment
config = ReadConfig2.ReadConfig();
config.environment='25';

url=config.GetConfig('endpointUrl');
user= config.GetConfig('account');
pwd=config.GetConfig('pwd');
