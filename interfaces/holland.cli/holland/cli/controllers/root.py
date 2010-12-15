"""
This is the RootController for the holland.cli application.  This can be used
to expose commands to the root namespace which will be accessible under:

    $ holland.cli --help
  
"""

from cement.core.controller import CementController, expose
from cement.core.namespace import get_config
from cement.core.log import get_logger
from cement import namespaces

from holland.cli.core.exc import HollandCliArgumentError

log = get_logger(__name__)
config = get_config()

class RootController(CementController):
    @expose('holland.cli.templates.root.error', is_hidden=True)
    def error(self, errors=[]):
        """
        This can be called when catching exceptions giving the developer a 
        clean way of presenting errors to the user.
        
        Required Arguments:
        
            errors
                A list of tuples in the form of [('ErrorCode', 'Error message')].
        
        
        The best way to use this is with an 'abort' function... something like:
        
        .. code-block:: python
        
            from cement.core.controller import run_controller_command
            
            def abort(errors):
                run_controller_command('root', 'error', errors=errors)
            
            errors = []
            # do something, if error
            errors.append(('MyErrorCode', 'My Error Message'))
            
            abort(errors)
            
            # continue work (no errors)
            
        """
        return dict(errors=errors)
    
    @expose(is_hidden=True)
    def nosetests(self):
        """This method is added for nose testing."""
        pass
        
    @expose(is_hidden=True)
    def default(self):
        """
        This is the default command method.  If no commands are passed to
        holland.cli, this one will be executed.  By default it raises an
        exception.
        
        """
        namespaces['root'].options.print_help()
        raise HollandCliArgumentError, "A command is required."
    
    @expose('holland.cli.templates.root.cmd1')
    def cmd1(self):
        """This is an example 'root' command."""
        foo = 'bar'
        items = ['one', 'two', 'three']
        return dict(foo=foo, items=items)
    
    @expose()
    def cmd1_help(self):
        """This is an example 'root' -help command.  It should be replaced."""
        foo = 'In holland.cli.controllers.root.cmd1_help()'
        return dict(foo=foo)
    
    @expose('holland.cli.templates.root.get-started')
    def get_started(self):
        features = [
            'Multiple Configuration file parsing (default: /etc, ~/)',
            'Command line argument and option parsing',
            'Dual Console/File Logging Support',
            'Full Internal and External (3rd Party) Plugin support',
            'Basic "hook" support',
            'Full MVC support for advanced application design',
            'Text output rendering with Genshi templates',
            'Json output rendering allows other programs to access your CLI-API',
            ]
        
        genshi_link = "http://genshi.edgewall.org/wiki/Documentation/text-templates.html"
        return dict(config=config, features=features, genshi_link=genshi_link)
