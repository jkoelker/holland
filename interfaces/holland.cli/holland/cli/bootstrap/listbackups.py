from cement.core.namespace import CementNamespace, register_namespace

listbackups = CementNamespace(
    label = 'listbackups',
    controller='ListBackupsController',
    description='List available backups',
    )

register_namespace(listbackups)
