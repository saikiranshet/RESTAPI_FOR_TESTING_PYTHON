import requests


class APICaller:
    def __init__(self, base_url, headers) -> None:
        self.base_url = base_url
        self.headers = headers

    def get(
        self,
        url_offset,
        err_key: str = "message",
        error: str = "Failed to make GET request",
        skip_err=False,
    ):
        url = f"{self.base_url}{url_offset}"
        response = requests.get(url, headers=self.headers, timeout=30)
        res = None
        if "application/json" in response.headers.get("Content-Type", ""):
            res = response.json()
        if not skip_err and response.status_code >= 400:
            message = error
            if isinstance(res, dict):
                message = res.get(err_key, error)
            raise Exception(message)
        return res
