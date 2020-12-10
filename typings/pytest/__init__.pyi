"""
This type stub file was generated by pyright.
"""

from _pytest import __version__
from _pytest.assertion import register_assert_rewrite
from _pytest.compat import _setup_collect_fakemodule
from _pytest.config import ExitCode, UsageError, cmdline, hookimpl, hookspec, main
from _pytest.debugging import pytestPDB as __pytestPDB
from _pytest.fixtures import fillfixtures as _fillfuncargs, fixture, yield_fixture
from _pytest.freeze_support import freeze_includes
from _pytest.main import Session
from _pytest.mark import MARK_GEN as mark, param
from _pytest.nodes import Collector, File, Item
from _pytest.outcomes import exit, fail, importorskip, skip, xfail
from _pytest.python import Class, Function, Instance, Module, Package
from _pytest.python_api import approx, raises
from _pytest.recwarn import deprecated_call, warns
from _pytest.warning_types import PytestAssertRewriteWarning, PytestCacheWarning, PytestCollectionWarning, PytestConfigWarning, PytestDeprecationWarning, PytestExperimentalApiWarning, PytestUnhandledCoroutineWarning, PytestUnknownMarkWarning, PytestWarning

"""
pytest: unit and functional testing with Python.
"""
set_trace = __pytestPDB.set_trace
