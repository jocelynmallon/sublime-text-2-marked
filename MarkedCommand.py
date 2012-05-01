import os
import subprocess

import sublime
import sublime_plugin
 

class MarkedCommand(sublime_plugin.WindowCommand):  
    def run(self):  
        filename = self.window.active_view().file_name()
        subprocess.call(['open', '-a', 'Marked', filename])
