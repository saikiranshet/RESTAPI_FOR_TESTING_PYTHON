from ..utils.request_gen import APICaller
from ..utils.routes import USER_INFO
from ..utils import DATA
import pytest

class TestUserInfo:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_object(self, get_api_obj: APICaller):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.GET_INFO
        data = get_api_obj.get(url_offset)
        first_item = data[0]
        id_name = (first_item['id'], first_item['name'])
        expected = ('1', 'Google Pixel 6 Pro')
        assert id_name == expected, f"Expected {expected}, but got {id_name}"


    @pytest.mark.smoke
    @pytest.mark.regression
    def test_object_with_particularid(self, get_api_obj):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.GET_PARTICULAR_ID
        data = get_api_obj.get(url_offset)
        third_item = data[0]
        id_name = (third_item['id'], third_item['name'])
        expected = ('3','Apple iPhone 12 Pro Max')
        assert id_name == expected, f"Expected {expected}, but got {id_name}"

    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_object_with_particularids(self, get_api_obj: APICaller):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.GET_PARTICULAR_ID
        data = get_api_obj.get(url_offset)
        id_name_pairs = [(item['id'], item['name']) for item in data if item['id'] in ['3', '5', '10']]
        expected_pairs = [
              ('3', 'Apple iPhone 12 Pro Max'),
               ('5', 'Samsung Galaxy Z Fold2'),
             ('10', 'Apple iPad Mini 5th Gen')
            ]       
        for id_name, expected in zip(id_name_pairs, expected_pairs):
             assert id_name == expected, f"Expected {expected}, but got {id_name}"

           
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_object_with_objectvalue(self, get_api_obj: APICaller):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.GET_PARTICULAR_VAL
        data = get_api_obj.get(url_offset)
        id_value = data['id']
        assert id_value == '7', f"Expected '7', but got {id_value}"

    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_object_post_api(self, get_api_obj: APICaller):
        """
        This test is to fetch info
        """
        url_offset = USER_INFO.POST_URL
        data = get_api_obj.post(url_offset)
        

     
