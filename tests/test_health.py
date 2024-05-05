class TestBaseAPI:
    def test_endpoint_should_work(self, fake_client):
        response = fake_client.get("/health")

        assert response.status_code == 200
        assert response.json == {"status": "ok"}
