from unittest.mock import mock_open, patch


def test_get_orders_empty(client):
    """Test GET /orders with empty CSV."""

    csvHeader = "ORDER_ID,CUSTOMER_NAME,PRODUCT,QUANTITY,PRICE,ORDER_DATE\n"
    with (
        patch("pathlib.Path.mkdir"),
        patch("pathlib.Path.exists", return_value=True),
        patch("builtins.open", mock_open(read_data=csvHeader)),
    ):
        response = client.get("/v1/orders")
        assert response.status_code == 200
        assert response.json() == []


def test_get_orders_with_data(client):
    """Test GET /orders with sample data."""

    csvData = """ORDER_ID,CUSTOMER_NAME,PRODUCT,QUANTITY,PRICE,ORDER_DATE
123,John Doe,Laptop,1,999.99,2024-01-15T10:30:00"""

    with (
        patch("pathlib.Path.mkdir"),
        patch("pathlib.Path.exists", return_value=True),
        patch("builtins.open", mock_open(read_data=csvData)),
    ):
        response = client.get("/v1/orders")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["CUSTOMER_NAME"] == "John Doe"
        assert data[0]["PRODUCT"] == "Laptop"


def test_create_order(client):
    """Test POST /orders."""

    orderData = {
        "CUSTOMER_NAME": "Test Customer",
        "PRODUCT": "Test Product",
        "QUANTITY": 2,
        "PRICE": 50.0,
    }

    with (
        patch("pathlib.Path.mkdir"),
        patch("pathlib.Path.exists", return_value=True),
        patch("builtins.open", mock_open()),
    ):
        response = client.post("/v1/orders", json=orderData)
        assert response.status_code == 200
        data = response.json()
        assert data["CUSTOMER_NAME"] == "Test Customer"
        assert data["PRODUCT"] == "Test Product"
        assert "ORDER_ID" in data
        assert "ORDER_DATE" in data


def test_create_order_validation(client):
    """Test POST /orders with invalid data."""

    invalidData = {"CUSTOMER_NAME": "", "PRODUCT": "Test Product", "QUANTITY": -1, "PRICE": 0}

    response = client.post("/v1/orders", json=invalidData)
    assert response.status_code == 422
