from doctest import DocFileSuite
import unittest
import os

def tearDown(test):
    if os.path.exists('Data.fs'):
        os.remove('Data.fs')

def test_suite( ):
    suite = [DocFileSuite('../../docs/readme.txt', tearDown=tearDown),
             DocFileSuite('../../docs/core.txt', tearDown=tearDown),
             DocFileSuite('../../docs/database.txt', tearDown=tearDown),
             DocFileSuite('../../docs/issue.txt', tearDown=tearDown),
             DocFileSuite('../../docs/observation.txt', tearDown=tearDown),
             DocFileSuite('../../docs/action.txt', tearDown=tearDown),
            ]
    return unittest.TestSuite(suite)
