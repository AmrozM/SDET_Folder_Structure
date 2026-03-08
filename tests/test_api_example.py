import requests
#headers = {"x-api-key": "reqres-free-v1"}

def test_check_api_request():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data)>0
    assert data[0]["username"] == "Bret","Username does not match"
    assert data[0]["id"] == 1
    assert "email" in data[0]
    assert data[0]["address"]["city"] == "Gwenborough", "City name does not match"