-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 06, 2015 at 10:54 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `webprog`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `find_all`()
BEGIN
 SELECT id, name 
 FROM animals; 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `find_by_id`(IN a_id INT(11),OUT a_name VARCHAR(20))
BEGIN
 	SELECT name INTO a_name FROM animals
 	WHERE id = a_id;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `animals`
--

CREATE TABLE IF NOT EXISTS `animals` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `animals`
--

INSERT INTO `animals` (`id`, `name`) VALUES
(1, 'Kingfisher'),
(2, 'Rat'),
(3, 'Cat'),
(4, 'Ant'),
(5, 'Dog'),
(6, 'cat'),
(7, 'elephant'),
(8, 'tiger'),
(9, 'cheetah'),
(10, 'fox'),
(11, 'rabbit'),
(12, 'sheep'),
(13, 'Cougar'),
(14, 'Snake'),
(15, 'shark');

-- --------------------------------------------------------

--
-- Table structure for table `spotted`
--

CREATE TABLE IF NOT EXISTS `spotted` (
  `animal` varchar(20) NOT NULL DEFAULT '',
  `count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `spotted`
--

INSERT INTO `spotted` (`animal`, `count`) VALUES
('200', 0),
('cheetah', 1),
('Dog', 1),
('elephant', 2),
('Kingfisher', 111),
('Rat', 22),
('shark', 4),
('sheep', 10);

-- --------------------------------------------------------

--
-- Table structure for table `temp`
--

CREATE TABLE IF NOT EXISTS `temp` (
  `TempId` int(11) DEFAULT NULL,
  `Role` varchar(255) DEFAULT NULL,
  `ChangeDate` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `spotted`
--
ALTER TABLE `spotted`
 ADD PRIMARY KEY (`animal`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
