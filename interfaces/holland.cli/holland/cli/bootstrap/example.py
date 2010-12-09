
from cement.core.hook import define_hook
from cement.core.namespace import CementNamespace, register_namespace

define_hook('my_example_hook')

# Setup the 'example' namespace object
example = CementNamespace(
    label='example', 
    controller='ExampleController',
    description='Example Plugin for holland.cli',
    provider='holland.cli'
    )

# Example namespace default configurations, overwritten by the [example] 
# section of the applications config file(s).  Once registered, this dict is
# accessible as:
#
#   from cement.core.namespace import get_config
#   example_config = get_config('example')
#
# Or simply as:
#
#   root_config = get_config()
#   root_config['example']
#
example.config['foo'] = 'bar'

# Example namespace options.  These options show up under:
#
#   $ holland.cli example --help
#
example.options.add_option('-F', '--foo', action='store',
    dest='foo', default=None, help='Example Foo Option'
    )

# Officialize and register the namespace
register_namespace(example)

