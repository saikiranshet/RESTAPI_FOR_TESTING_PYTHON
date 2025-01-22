# RESTAPI_FOR_TESTING_PYTHON

#list OF API's which are available for testing

You can find the FreeAPI document here in the link 
  https://restful-api.dev/

**List Of API's Used For Testing**
1. GET API - https://api.restful-api.dev/objects
2. GET API - https://api.restful-api.dev/objects?id=3&id=5&id=10
3. GET API - https://api.restful-api.dev/objects/7
4. POST API - https://api.restful-api.dev/objects
5. PUT API - https://api.restful-api.dev/objects
6. PATCH API - https://api.restful-api.dev/objects/7
7. DELETE API -  https://api.restful-api.dev/objects/6


*Environment Variables*
BASE_URL= 'https://api.restful-api.dev'

*Execute - To execute the test suite*

pytest -vs --html=reports/report.html


*To execute the test using markers*

pytest -vsm "smoke" --html=reports/report.html
pytest -vsm "regression" --html=reports/report.html


Jenkins URL - http://13.60.94.126:8080/
EC2 machine instance is set