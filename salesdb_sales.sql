CREATE DATABASE IF NOT EXISTS salesdb;

USE salesdb;

DROP TABLE IF EXISTS `sales`;

CREATE TABLE `sales` (
  `Date` date DEFAULT NULL,
  `StoreID` int DEFAULT NULL,
  `TotalItems` int DEFAULT NULL,
  `TotalAmount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
