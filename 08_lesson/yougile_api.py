import requests


class YougileProjects:
    def __init__(self, url, token, company_id):
        self.url = url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "yougile-id": company_id
        }

    def create_project(self, title, users=None):
        payload = {
            "title": title,
            "users": users if users is not None else {}
        }
        return requests.post(
            f"{self.url}/projects", json=payload, headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.url}/projects/{project_id}", headers=self.headers
        )

    def update_project(self, project_id, title):
        payload = {"title": title}
        return requests.put(
            f"{self.url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
