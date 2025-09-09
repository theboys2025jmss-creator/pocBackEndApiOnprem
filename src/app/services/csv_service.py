import csv
from datetime import datetime
from pathlib import Path
from typing import List
from uuid import uuid4

from ..core.config import settings
from ..core.logging import logger
from ..models.schemas import Order, OrderResponse


class CsvService:
    """Service for CSV file operations."""

    def __init__(self):
        """Initialize CSV service."""

        self.dataPath = Path(settings.DATA_PATH)
        self.ordersFile = self.dataPath / "orders.csv"

    def _ensureDataDirectory(self) -> None:
        """Ensure data directory exists."""

        self.dataPath.mkdir(parents=True, exist_ok=True)
        logger.info("data.directory.ensured", path=str(self.dataPath))

    def _ensureOrdersFile(self) -> None:
        """Ensure orders CSV file exists with headers."""

        if not self.ordersFile.exists():
            with open(self.ordersFile, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["ORDER_ID", "CUSTOMER_NAME", "PRODUCT", "QUANTITY", "PRICE", "ORDER_DATE"]
                )
            logger.info("orders.file.created", path=str(self.ordersFile))

    def getOrders(self) -> List[OrderResponse]:
        """Read all orders from CSV file."""

        self._ensureDataDirectory()
        self._ensureOrdersFile()
        orders = []
        try:
            with open(self.ordersFile, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    orders.append(
                        OrderResponse(
                            ORDER_ID=row["ORDER_ID"],
                            CUSTOMER_NAME=row["CUSTOMER_NAME"],
                            PRODUCT=row["PRODUCT"],
                            QUANTITY=int(row["QUANTITY"]),
                            PRICE=float(row["PRICE"]),
                            ORDER_DATE=row["ORDER_DATE"],
                        )
                    )
            logger.info("orders.read", count=len(orders))
            return orders
        except Exception as e:
            logger.error("orders.read.error", error=str(e))
            raise

    def addOrder(self, order: Order) -> OrderResponse:
        """Add new order to CSV file."""

        self._ensureDataDirectory()
        self._ensureOrdersFile()
        orderId = str(uuid4())
        orderDate = datetime.now().isoformat()

        try:
            with open(self.ordersFile, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        orderId,
                        order.CUSTOMER_NAME,
                        order.PRODUCT,
                        order.QUANTITY,
                        order.PRICE,
                        orderDate,
                    ]
                )

            orderResponse = OrderResponse(
                ORDER_ID=orderId,
                CUSTOMER_NAME=order.CUSTOMER_NAME,
                PRODUCT=order.PRODUCT,
                QUANTITY=order.QUANTITY,
                PRICE=order.PRICE,
                ORDER_DATE=orderDate,
            )

            logger.info("order.added", orderId=orderId, customer=order.CUSTOMER_NAME)
            return orderResponse
        except Exception as e:
            logger.error("order.add.error", error=str(e))
            raise


csvService = CsvService()
