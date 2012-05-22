import os, sys
import subprocess
import sublime_plugin 

class MarkedCommand(sublime_plugin.WindowCommand):  
    def run(self):  
        filename = self.window.active_view().file_name()

        proc_env = os.environ.copy()
        for k, v in proc_env.iteritems():
            proc_env[k] = os.path.expandvars(v).encode(sys.getfilesystemencoding())

        subprocess.call(['open', '-a', 'Marked', filename], env=proc_env)
