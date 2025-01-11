from ..utils.request_gen import APICaller
from ..utils.routes import USER_INFO
from ..utils import DATA
import pytest


class TestUserInfo:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_fetch(self, get_api_obj: APICaller):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.GET_INFO
        data = get_api_obj.get(url_offset)
        print(data)
       
       