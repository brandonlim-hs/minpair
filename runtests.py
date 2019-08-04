#!/usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
import nose


def start(argv=None):
    sys.exitfunc = lambda: sys.stderr.write("Shutting down...\n")

    if argv is None:
        argv = [
            "nosetests", "--verbose", "--with-coverage",
            "--cover-package=minimal_pairs", "--cover-erase",
            "--cover-branches", "--cover-xml", "--with-xunit",
        ]

    nose.run_exit(argv=argv, defaultTest=os.path.abspath(
        os.path.dirname(__file__)))


if __name__ == "__main__":
    start(sys.argv)
