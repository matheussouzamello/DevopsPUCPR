import unittest
from unittest.mock import patch

from app import create_app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_returns_application_metadata(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["status"], "ok")
        self.assertIn("project", payload)
        self.assertIn("version", payload)

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_about_endpoint(self):
        response = self.client.get("/about")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["stack"], "Flask")
        self.assertEqual(payload["container"], "Docker")

    def test_home_contains_default_name_and_version(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["project"], "DevOps Somativa 1")
        self.assertEqual(payload["version"], "1.0.0")

    def test_create_app_reads_environment_variables(self):
        with patch.dict(
            "os.environ",
            {"APP_NAME": "Meu Projeto", "APP_VERSION": "2.1.3"},
            clear=False,
        ):
            app = create_app()

        self.assertEqual(app.config["APP_NAME"], "Meu Projeto")
        self.assertEqual(app.config["APP_VERSION"], "2.1.3")

    def test_unknown_route_returns_404(self):
        response = self.client.get("/nao-existe")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
