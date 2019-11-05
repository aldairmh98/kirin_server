from watchdog.events import FileSystemEventHandler
import logging
import winsound
from git import Repo

class my_LoggingEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def on_moved(self, event):
        super(my_LoggingEventHandler, self).on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("mi %s: from %s to %s", what, event.src_path,
                     event.dest_path)

    def on_created(self, event):
        super(my_LoggingEventHandler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("mui Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        super(my_LoggingEventHandler, self).on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        logging.info("mi Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(my_LoggingEventHandler, self).on_modified(event)
        repo = Repo('.')
        branch = repo.active_branch
        if branch.name in ['master', 'develop', 'hotfix', 'release']:
            duration = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)

