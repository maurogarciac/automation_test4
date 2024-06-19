import requests

from config.settings import Urls


class TestApi:

    def test_1(self) -> None:
        url: str = Urls.API
        response = requests.get(url)

        # Verify status code
        assert response.status_code == 200 

        # Verify headers
        assert response.headers["Content-Type"] == "application/json; charset=UTF-8"

        # Verify response structure
        data: dict = response.content()
        assert "id" in data
        assert "title" in data
        assert "author" in data