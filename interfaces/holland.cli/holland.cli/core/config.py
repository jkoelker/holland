"""
This is the applications default configuration.  You can feel free to alter
this file to your needs, however it should be noted that all these variables
are overridden by settings in /etc/holland.cli/holland.cli.conf and/or
~/.holland.cli.conf (by default) and therefore, any default configurations
you want to make obvious to your users should be set in your default config
file as packaged with the software.
"""

import os
from configobj import ConfigObj

from cement.core.exc import CementConfigError
    
# This is a sane default for development/no config    
prefix = os.path.join(os.environ['HOME'], '.holland.cli')
  

dcf = ConfigObj() # default config
dcf['config_source'] = ['defaults']
dcf['app_name'] = 'holland.cli' # name for cli like /etc/<app_name>
dcf['app_egg_name'] = 'holland.cli' # name from setup.py
dcf['app_module'] = 'holland.cli' # name of the library dir

dcf['enabled_plugins'] = [] # no default plugins, add via the config file
dcf['debug'] = False
dcf['datadir'] = os.path.join(prefix, 'data')
dcf['tmpdir'] = os.path.join(prefix, 'tmp')
dcf['log_file'] = os.path.join(prefix, 'log', dcf['app_name'])
dcf['plugin_config_dir'] = os.path.join(prefix, 'etc', 'plugins.d')
dcf['log_to_console'] = True
dcf['output_handler'] = 'genshi'
dcf['show_plugin_load'] = False

# By default look in /etc and ~/ for config files.  Developers for non *nix 
# audiences will want to change this.
dcf['config_files'] = [
    os.path.join('/etc', dcf['app_name'], '%s.conf' % dcf['app_name']),
    os.path.join(prefix, 'etc', '%s.conf' % dcf['app_name']),
    os.path.join(os.environ['HOME'], '.%s.conf' % dcf['app_name']),
    ]

default_config = dcf

def get_default_config():
    """Return the default application config."""
    return default_config

def get_nose_config(prefix=None):
    if not prefix:
        from tempfile import mkdtemp
        prefix = mkdtemp()
        
    tcf = ConfigObj() # test config
    tcf['config_files'] = [os.path.abspath('./config/holland.cli.conf-test')]
    tcf['config_source'] = ['defaults']
    tcf['app_name'] = 'holland.cli'
    tcf['app_egg_name'] = 'holland.cli'
    tcf['app_module'] = 'holland.cli' 
    tcf['enabled_plugins'] = [] 
    tcf['debug'] = False
    tcf['datadir'] = '%s/data' % prefix
    tcf['tmpdir'] = '%s/tmp' % prefix
    tcf['log_file'] = '%s/log/%s.log' % (prefix, tcf['app_name'])
    tcf['plugin_config_dir'] = './config/plugins.d' 
    tcf['log_to_console'] = False
    tcf['output_engine'] = 'genshi'
    tcf['show_plugin_load'] = False
    return tcf
    