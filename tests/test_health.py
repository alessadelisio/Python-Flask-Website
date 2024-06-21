class TestBaseAPI:
    """Test suite for the 'health' endpoint"""

    def test_endpoint_should_work(self, fake_client):
        """Funtion test to check the 'health'
        endpoint with a successful GET request."""

        # ARRANGE: Already done by the fake_client

        # ACT
        response = fake_client.get("/health")

        # ASSERT
        assert response.status_code == 200  # noqa: PLR2004
        assert response.json == {"status": "ok"}
