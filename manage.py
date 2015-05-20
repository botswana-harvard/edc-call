#!/usr/bin/env python3
import os
import sys

SOURCE_DIR = os.path.expanduser('~/source')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contact.settings")

    sys.path.insert(1, os.path.join(SOURCE_DIR, 'edc-base/'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
