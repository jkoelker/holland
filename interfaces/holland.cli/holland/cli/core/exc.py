"""holland.cli exception classes."""

class HollandCliError(Exception):
    """Generic errors."""
    def __init__(self, value, code=1):
        Exception.__init__(self)
        self.msg = value
        self.code = code
    
    def __str__(self):
        return self.msg
        
    def __unicode__(self):
        return unicode(self.msg)
                
class HollandCliConfigError(HollandCliError):
    """Config parsing and setup errors."""
    def __init__(self, value):
        code = 10
        HollandCliError.__init__(self, value, code)

class HollandCliRuntimeError(HollandCliError):
    """Runtime errors."""
    def __init__(self, value):
        code = 20
        HollandCliError.__init__(self, value, code)

class HollandCliArgumentError(HollandCliError):
    """Argument errors."""
    def __init__(self, value):
        code = 40
        HollandCliError.__init__(self, value, code)
