"""
Functions to support bootstrapping.

These functions should only be called when starting up a holland session.
They initialize things like logging and the config system.
"""
import os
import sys
import logging
import warnings
from holland.core.plugin import add_plugin_dir
from holland.core.config import get_holland_config, setup_config as _setup_config
from holland.core.log import setup_console_logging, setup_file_logging, clear_root_handlers
from holland.core.spool import spool

LOGGER = logging.getLogger(__name__)

def setup_config(config_file):
    try:
        _setup_config(config_file)
    except IOError, e:
        LOGGER.error("Failed to load holland config: %s", e)
        sys.exit(os.EX_CONFIG)

def log_warnings(message, category, filename, lineno, file=None, line=None):
    WARNLOG = logging.getLogger("Python")
    logging.debug("message=%s message=%r category=%r", message, message, category)
    warning_string = warnings.formatwarning(message,
                                            category,
                                            filename,
                                            lineno)
    if category == DeprecationWarning:
        WARNLOG.debug("%s", warning_string)
    else:
        WARNLOG.debug(warning_string)
        WARNLOG.warn("%s", message)

def setup_logging():
    clear_root_handlers()
    hollandcfg = get_holland_config()
    log_level = hollandcfg.lookup('logging.level')

    if hollandcfg.lookup('logging.filename'):
        setup_file_logging(filename=hollandcfg.lookup('logging.filename'),
                           level=log_level)

    # Monkey patch in routing warnings through logging
    old_showwarning = warnings.showwarning
    warnings.showwarning = log_warnings

def setup_umask():
    hollandcfg = get_holland_config()
    os.umask(hollandcfg.lookup('holland.umask'))

def setup_path():
    hollandcfg = get_holland_config()
    if hollandcfg.lookup('holland.path'):
        os.putenv('PATH', hollandcfg.lookup('holland.path'))
        os.environ['PATH'] = hollandcfg.lookup('holland.path')

def setup_plugins():
    hollandcfg = get_holland_config()
    map(add_plugin_dir, hollandcfg.lookup('holland.plugin-dirs'))

def bootstrap(config_file=None):
    if config_file is None:
        config_file = os.getenv('HOLLAND_CONFIG',
                                '/etc/holland/holland.conf')
    # Setup the configuration
    setup_config(config_file)
    # Setup logging per config
    setup_logging()
    # use umask setting
    setup_umask()
    # configure our PATH
    setup_path()
    # Setup plugin directories
    setup_plugins()
    # Setup spool
    spool.path = get_holland_config().lookup('holland.backup-directory')
