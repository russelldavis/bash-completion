import pytest


@pytest.mark.pre_commands(
    "PKG_DBDIR=$PWD/dbtools/db",
)
class TestPortupgrade(object):

    @pytest.mark.complete("portupgrade ")
    def test_1(self, completion):
        assert completion.list == "a b-c-d".split()
        assert completion.line.endswith(" ")
