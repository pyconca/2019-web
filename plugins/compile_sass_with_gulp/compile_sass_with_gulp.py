

from nikola.plugin_categories import Task
from nikola import utils

from doit.action import CmdAction



class CompileSassWithGulp(Task):
    """Generate CSS out of Sass sources."""

    name = "build_sass_with_gulp"

    def gen_tasks(self):
        """Create tasks to invoke gulp to compile our SASS"""

        def create_cmd_string():
            return "npm run build"


        return {
            'basename': 'build_sass_with_gulp',
            'actions': [CmdAction(create_cmd_string)],
            'verbosity': 2,
            'uptodate': [False],
        }

