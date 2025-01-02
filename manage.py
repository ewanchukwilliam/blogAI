#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogai.settings")
    try:
        import subprocess
        import threading

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        def run_tailwind():
            subprocess.run(["python", "manage.py", "tailwind", "start"])
        threading.Thread(target=run_tailwind, daemon=True).start()
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
