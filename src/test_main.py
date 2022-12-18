from .main import *

def test_getcarcolor():
    response=getcarcolor(4284078)
    assert response.error_code=="ok"
