#!/usr/bin/env python
import sys
import traceback
from os.path import abspath, dirname, join

from django.core.management import execute_manager

try:
    from settings import active as settings
except ImportError, e:
    print '\033[1;33m'
    print "Apparently you don't have the file settings/active.py yet."
    print "Create it containing and try again"
    print "original traceback:"
    print "=" * 20
    print
    traceback.print_exc(e)
    sys.exit(1)

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

if __name__ == "__main__":
    execute_manager(settings)
