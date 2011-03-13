"""holland.cli controller."""

from cement.core.namespace import get_config
from cement.core.log import get_logger
from cement.core.controller import CementController, expose
from cement.core.hook import run_hooks

log = get_logger(__name__)
config = get_config()

class ListBackupsController(CementController):
    @expose('holland.cli.templates.listbackups.cmd', namespace='root')
    def cmd(self):
        print 'cmd'

    @expose(namespace='listbackups')
    def hozer(self):
        print 'hozer'

    @expose(namespace='listbackups')
    def default(self):
        print 'default'
