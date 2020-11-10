-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for codekid
DROP DATABASE IF EXISTS `codekid`;
CREATE DATABASE IF NOT EXISTS `codekid` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `codekid`;

-- Dumping structure for table codekid.data
DROP TABLE IF EXISTS `data`;
CREATE TABLE IF NOT EXISTS `data` (
  `number` varchar(50) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `explanation` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table codekid.data: ~7 rows (approximately)
DELETE FROM `data`;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` (`number`, `name`, `explanation`) VALUES
	('1', 'Capture', ' :Beschrijf de requirements, geef een eenduidige definitie van het probleem. '),
	('2', 'Contemplate', ' :Analyseer het probleem: welke data is nodig. Welke oplossingsstrategieën zijn er, welke deelproblemen zijn te onderkennen.'),
	('3', 'Contract', ' :Bepaal de interface, beschrijf input- en outputdata (inhoud en structuur).'),
	('4', 'Compose', ' :Deel het probleem eventueel op in deelproblemen. Herhaal de zeven stappen voor elk nieuw deelprobleem.'),
	('5', 'Chart', ' :Gebruik de drie besturingsstructuren om de volgorde van de instructies de beschrijven.'),
	('6', 'Code', ' :Codeer de besturing in een programmeertaal.'),
	('7', 'Check', ' :Test de code conform de requirements. Ga indien nodig terug naar stap 1.');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;

-- Dumping structure for table codekid.score
DROP TABLE IF EXISTS `score`;
CREATE TABLE IF NOT EXISTS `score` (
  `name` varchar(255) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table codekid.score: ~4 rows (approximately)
DELETE FROM `score`;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
INSERT INTO `score` (`name`, `score`, `datetime`) VALUES
	('Julean ', 7, '2020-10-23 15:51:30'),
	('Max', 7, '2020-10-23 15:51:52'),
	('Eva', 7, '2020-10-23 15:52:04'),
	('Cynthia', 7, '2020-10-23 15:52:23');
/*!40000 ALTER TABLE `score` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
