import sys
from pkg_resources import get_distribution

from cement.core.exc import CementArgumentError, CementConfigError
from cement.core.exc import CementRuntimeError
from cement.core.log import get_logger
from cement.core.app_setup import lay_cement
from cement.core.command import run_command

from holland.cli.core.config import get_default_config
from holland.cli.core.exc import HollandCliArgumentError, HollandCliConfigError
from holland.cli.core.exc import HollandCliRuntimeError

from holland.core.util.bootstrap import bootstrap as holland_bootstrap

VERSION = get_distribution('holland.cli').version
BANNER = """
Holland Backup v%s
Copyright (c) 2008-2010 Rackspace US, Inc.
More info available at http://hollandbackup.org

[[[[[[[]]]]]]] [[[[[[[]]]]]]]
[[[[[[[]]]]]]]       [[[[[[[]]]]]]]
[[[[[[[]]]]]]] [[[[[[[]]]]]]]
[[[[[[[]]]]]]] [[[[[[[]]]]]]]

""" % VERSION

def main(args=None):
    try:
        if not args:
            args = sys.argv

        holland_bootstrap()
            
        lay_cement(config=get_default_config(), banner=BANNER, args=args, 
                   version=VERSION)
    
        log = get_logger(__name__)
        log.debug("Cement Framework Initialized!")

        if not len(args) > 1:
            args.append('default')
        
        run_command(args[1])
            
    except CementArgumentError, e:
        # Display the apps exception names instead for the Cement exceptions.
        print("HollandCliArgumentError > %s" % e)
        sys.exit(e.code)
    except CementConfigError, e:
        print("HollandCliConfigError > %s" % e)
        sys.exit(e.code)
    except CementRuntimeError, e:
        print("HollandCliRuntimeError > %s" % e)
        sys.exit(e.code)
    except HollandCliArgumentError, e:
        print("HollandCliArgumentError > %s" % e)
        sys.exit(e.code)
    except HollandCliConfigError, e:
        print("HollandCliConfigError > %s" % e)
        sys.exit(e.code)
    except Holland.cliRuntimeError, e:
        print("HollandCliRuntimeError > %s" % e)
        sys.exit(e.code)
    sys.exit(0)
   
def nose_main(args, test_config):
    """
    This function provides an alternative to main() that is more friendly for 
    nose tests as it doesn't catch any exceptions.
    
    Required Arguments:
        
        args
            The args to pass to lay_cement
        
        test_config
            A test config to pass to lay_cement
    
    Usage:
    
    .. code-block:: python
    
        from holland.cli.core.appmain import nose_main
        from holland.cli.core.config import get_nose_config
        
        args = [__file__, 'nosetests', '--quiet']
        (res_dict, output_text) = nose_main(args, get_nose_config())
        
    """
    
    lay_cement(config=test_config, banner=BANNER, args=args)
    log = get_logger(__name__)
    log.debug("Cement Framework Initialized!")

    if not len(args) > 1:
        args.append('default')

    (res, output_txt) = run_command(args[1])
    return (res, output_txt)
         
if __name__ == '__main__':
    main()
    
