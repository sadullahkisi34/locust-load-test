from locust import HttpUser, task, between

class N11SearchUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def search_bilgisayar(self):
        headers = {
            "authority": "www.n11.com",
            "method": "GET",
            "path": "/arama?q=bilgisayar",
            "scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Connection": "keep-alive",
            "Referer": "https://www.n11.com/",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"macOS"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

            
            "Cookie": (
                "n11_cookie_ver_1=true; "
                "rememberMe=true; "
                "mf_auth_cookie=1955652269-gtKoFrFhMHpKBxgfXflHLoXvvhAWYHsD-DZuUTHeUX3udODgquaKeIlmKp1cuUfgo; "
                "mf_refresh_token=1955652269-gtKoFrFhMHpKBxgfXflHLoXvvhAWYHsD-DZuUTHeUX3udODgquaKeIlmKp1cuUfgo; "
                "sgmdn_2789236=1; "
                "ttcsid=1754137370391::aiS0nwBestva2DUGkG3A.1.1754138088097"
            )
        }

        with self.client.get("/arama?q=bilgisayar", headers=headers, name="Arama: bilgisayar", catch_response=True) as response:
            if response.status_code == 200 and "ürün" in response.text.lower():
                response.success()
            else:
                response.failure(f"Status: {response.status_code} - içerik boş veya engellendi")