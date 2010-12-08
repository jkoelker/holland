import os
from holland.core.config import get_holland_config 

dcf = get_holland_config().cli()
config_prefix = os.path.dirname(dcf.filename)
dcf['config_source'] = ['defaults']
dcf['app_name'] = 'holland' # name for cli like /etc/<app_name>
dcf['app_egg_name'] = 'holland.cli' # name from setup.py
dcf['app_module'] = 'holland.cli' # name of the library dir
dcf['enabled_plugins'] = [] # no default plugins, add via the config file
dcf['debug'] = False
dcf['plugin_config_dir'] = os.path.join(config_prefix, 'plugins.d')
dcf['log_to_console'] = True
dcf['output_handler'] = 'genshi'
dcf['show_plugin_load'] = False
dcf['config_files'] = [dcf.filename]

default_config = dcf

def get_default_config():
    """Return the default application config."""
    return default_config

def get_nose_config(prefix=None):
    if not prefix:
        from tempfile import mkdtemp
        prefix = mkdtemp()
        
    tcf = get_holland_config().cli()
    config_prefix = os.path.dirname(tcf.filename)
    tcf['config_files'] = [tcf.filename]
    tcf['config_source'] = ['defaults']
    tcf['app_name'] = 'holland'
    tcf['app_egg_name'] = 'holland.cli'
    tcf['app_module'] = 'holland.cli' 
    tcf['enabled_plugins'] = [] 
    tcf['debug'] = False
    tcf['datadir'] = '%s/data' % prefix
    tcf['tmpdir'] = '%s/tmp' % prefix
    tcf['log_file'] = '%s/log/%s.log' % (prefix, tcf['app_name'])
    tcf['plugin_config_dir'] = os.path.join(config_prefix, 'plugins.d')
    tcf['log_to_console'] = False
    tcf['output_engine'] = 'genshi'
    tcf['show_plugin_load'] = False
    return tcf
    
