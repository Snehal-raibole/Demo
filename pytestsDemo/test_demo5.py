import pytest
from pytestsDemo.test_log import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExecute2(BaseClass):
    def test_userprofile(self, dataload):
        log = self.get_logger()
        log.info(dataload[0])
        log.info(dataload[2])


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

