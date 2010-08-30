from doctest import DocFileSuite
import unittest

def test_suite( ):
    suite = [DocFileSuite('../../docs/readme.txt'),
             DocFileSuite('../../docs/issue.txt'),
             DocFileSuite('../../docs/observation.txt'),
             DocFileSuite('../../docs/action.txt'),
            ]
    return unittest.TestSuite(suite)
