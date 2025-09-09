from unittest.mock import patch

import pytest


def test_unstable_success(client):
    """Test /unstable endpoint success case."""

    with patch("random.choice", return_value=True):
        response = client.get("/v1/unstable")
        assert response.status_code == 200
        data = response.json()
        assert data["STATUS"] == "success"
        assert "TIMESTAMP" in data


def test_unstable_failure(client):
    """Test /unstable endpoint failure case."""

    with patch("random.choice", return_value=False):
        response = client.get("/v1/unstable")
        assert response.status_code == 500


@pytest.mark.asyncio
async def test_slow_endpoint(client):
    """Test /slow endpoint."""

    with patch("asyncio.sleep") as mockSleep:
        response = client.get("/v1/slow")
        assert response.status_code == 200
        data = response.json()
        assert "MESSAGE" in data
        assert data["DELAY_SECONDS"] == 5
        assert "TIMESTAMP" in data
        mockSleep.assert_called_once_with(5)
