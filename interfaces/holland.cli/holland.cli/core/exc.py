"""holland.cli exception classes."""

class Holland.cliError(Exception):
    """Generic errors."""
    def __init__(self, value, code=1):
        Exception.__init__(self)
        self.msg = value
        self.code = code
    
    def __str__(self):
        return self.msg
        
    def __unicode__(self):
        return unicode(self.msg)
                
class Holland.cliConfigError(Holland.cliError):
    """Config parsing and setup errors."""
    def __init__(self, value):
        code = 10
        Holland.cliError.__init__(self, value, code)

class Holland.cliRuntimeError(Holland.cliError):
    """Runtime errors."""
    def __init__(self, value):
        code = 20
        Holland.cliError.__init__(self, value, code)

class Holland.cliArgumentError(Holland.cliError):
    """Argument errors."""
    def __init__(self, value):
        code = 40
        Holland.cliError.__init__(self, value, code)
