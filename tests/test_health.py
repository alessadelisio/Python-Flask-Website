class TestBaseAPI:
    def test_endpoint_should_work(self, fake_client):
        # ARRANGE: Already done by the fake_client

        # ACT
        response = fake_client.get("/health")

        # ASSERT
        assert response.status_code == 200
        assert response.json == {"status": "ok"}
