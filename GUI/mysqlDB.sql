-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: meminfo
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `coach`
--

DROP TABLE IF EXISTS `coach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coach` (
  `coa_phone` int(11) NOT NULL,
  `coa_name` varchar(50) DEFAULT NULL,
  `coa_info` text,
  `coa_pic_path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`coa_phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coach`
--

LOCK TABLES `coach` WRITE;
/*!40000 ALTER TABLE `coach` DISABLE KEYS */;
INSERT INTO `coach` VALUES (20000,'马老师',NULL,NULL),(20001,'秦老师',NULL,NULL),(20002,'刘老师',NULL,NULL),(20003,'方老师',NULL,NULL);
/*!40000 ALTER TABLE `coach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mem_class`
--

DROP TABLE IF EXISTS `mem_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mem_class` (
  `mem_phone` int(11) NOT NULL,
  `mem_name` varchar(50) NOT NULL,
  `mem_coa_name` varchar(50) DEFAULT NULL,
  `year` int(11) NOT NULL,
  `week` int(11) NOT NULL,
  `ctime` varchar(200) DEFAULT NULL,
  `coa_eval` text,
  PRIMARY KEY (`mem_phone`,`mem_name`,`year`,`week`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mem_class`
--

LOCK TABLES `mem_class` WRITE;
/*!40000 ALTER TABLE `mem_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `mem_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mem_info`
--

DROP TABLE IF EXISTS `mem_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mem_info` (
  `mem_phone` int(11) NOT NULL,
  `mem_name` varchar(50) NOT NULL,
  `mem_parent` varchar(50) DEFAULT NULL,
  `mem_gender` varchar(50) DEFAULT NULL,
  `mem_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`mem_phone`,`mem_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mem_info`
--

LOCK TABLES `mem_info` WRITE;
/*!40000 ALTER TABLE `mem_info` DISABLE KEYS */;
INSERT INTO `mem_info` VALUES (10000,'马小跳','马天笑','男',1),(10010,'夏林果','夏雪宜','女',2),(10086,'陆漫漫','陆振华','女',3);
/*!40000 ALTER TABLE `mem_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-11 16:52:39
