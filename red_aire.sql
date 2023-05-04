-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2023 at 06:05 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `red_aire`
--

-- --------------------------------------------------------

--
-- Table structure for table `accesorioprimaria`
--

CREATE TABLE `accesorioprimaria` (
  `id_accesorioPrimaria` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `fk_Primaria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `accesorioprimaria`
--

INSERT INTO `accesorioprimaria` (`id_accesorioPrimaria`, `tipo`, `fk_Primaria`) VALUES
(1, 'Valve, Ball, Reduced trim, Beta = 0.9', 1),
(2, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 1),
(3, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 2),
(4, 'Tee, Run, Screwed', 3),
(5, 'Tee, Run, Screwed', 4),
(6, 'Tee, Run, Screwed', 5),
(7, 'Tee, Run, Screwed', 6),
(8, 'Tee, Run, Screwed', 6);

-- --------------------------------------------------------

--
-- Table structure for table `accesoriosecundaria`
--

CREATE TABLE `accesoriosecundaria` (
  `id_accesorioSecundaria` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `fk_Secundaria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `accesoriosecundaria`
--

INSERT INTO `accesoriosecundaria` (`id_accesorioSecundaria`, `tipo`, `fk_Secundaria`) VALUES
(1, 'Contraction', 1),
(2, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 1),
(3, 'Valve, Ball, Reduced trim, Beta = 0.9', 1),
(4, 'Tee, Run, Screwed', 2),
(5, 'Tee, Run, Screwed', 3),
(6, 'Tee, Run, Screwed', 4),
(7, 'Tee, Run, Screwed', 4),
(8, 'Contraction', 5),
(9, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 5),
(10, 'Valve, Ball, Reduced trim, Beta = 0.9', 5),
(11, 'Tee, Run, Screwed', 6),
(12, 'Tee, Run, Screwed', 7),
(13, 'Tee, Run, Screwed', 8),
(14, 'Tee, Run, Screwed', 9),
(15, 'Tee, Run, Screwed', 10),
(16, 'Tee, Run, Screwed', 11),
(17, 'Tee, Run, Screwed', 11),
(18, 'Contraction', 12),
(19, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 12),
(20, 'Valve, Ball, Reduced trim, Beta = 0.9', 12),
(21, 'Tee, Run, Screwed', 13),
(22, 'Tee, Run, Screwed', 14),
(23, 'Tee, Run, Screwed', 15),
(24, 'Tee, Run, Screwed', 16),
(25, 'Tee, Run, Screwed', 17),
(26, 'Tee, Run, Screwed', 18),
(27, 'Tee, Run, Screwed', 18),
(28, 'Contraction', 19),
(29, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 19),
(30, 'Valve, Ball, Reduced trim, Beta = 0.9', 19),
(31, 'Tee, Run, Screwed', 20),
(32, 'Tee, Run, Screwed', 21),
(33, 'Tee, Run, Screwed', 22),
(34, 'Tee, Run, Screwed', 22),
(35, 'Contraction', 23),
(36, 'Elbow, 90°, Long-radius (R/D = 1.5), All types', 23),
(37, 'Valve, Ball, Reduced trim, Beta = 0.9', 23),
(38, 'Tee, Run, Screwed', 24),
(39, 'Tee, Run, Screwed', 25),
(40, 'Tee, Run, Screwed', 25);

-- --------------------------------------------------------

--
-- Table structure for table `tuberiaprimaria`
--

CREATE TABLE `tuberiaprimaria` (
  `id_Primaria` int(11) NOT NULL,
  `coor_inicial` varchar(100) NOT NULL,
  `coor_final` varchar(100) NOT NULL,
  `material` varchar(100) NOT NULL,
  `deltaP_max` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `tuberiaprimaria`
--

INSERT INTO `tuberiaprimaria` (`id_Primaria`, `coor_inicial`, `coor_final`, `material`, `deltaP_max`) VALUES
(1, '(0,0,0)', '(2000,0,0)', 'Stainless Steel', '2'),
(2, '(2000,0,0)', '(2000,4000,0)', 'Stainless Steel', '2'),
(3, '(2000,4000,0)', '(5500,4000,0)', 'Stainless Steel', '2'),
(4, '(5500,4000,0)', '(8500,4000,0)', 'Stainless Steel', '2'),
(5, '(8500,4000,0)', '(11500,4000,0)', 'Stainless Steel', '2'),
(6, '(11500,4000,0)', '(14500,4000,0)', 'Stainless Steel', '2');

-- --------------------------------------------------------

--
-- Table structure for table `tuberiasecundaria`
--

CREATE TABLE `tuberiasecundaria` (
  `id_Secundaria` int(11) NOT NULL,
  `coor_inicial` varchar(100) NOT NULL,
  `coor_final` varchar(100) NOT NULL,
  `material` varchar(100) NOT NULL,
  `deltaP_max` varchar(100) NOT NULL,
  `fk_Primaria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `tuberiasecundaria`
--

INSERT INTO `tuberiasecundaria` (`id_Secundaria`, `coor_inicial`, `coor_final`, `material`, `deltaP_max`, `fk_Primaria`) VALUES
(1, '(2000,4000,0)', '(2000,4000,2500)', 'Stainless steel', '2', 2),
(2, '(2000,4000,2500)', '(2000,4000,5000)', 'Stainless steel', '2', 2),
(3, '(2000,4000,5000)', '(2000,4000,7500)', 'Stainless steel', '2', 2),
(4, '(2000,4000,7500)', '(2000,4000,10000)', 'Stainless steel', '2', 2),
(5, '(5500,4000,0)', '(5500,4000,1400)', 'Stainless steel', '2', 3),
(6, '(5500,4000,1400)', '(5500,4000,2800)', 'Stainless steel', '2', 3),
(7, '(5500,4000,2800)', '(5500,4000,4200)', 'Stainless steel', '2', 3),
(8, '(5500,4000,4200)', '(5500,4000,5600)', 'Stainless steel', '2', 3),
(9, '(5500,4000,5600)', '(5500,4000,7000)', 'Stainless steel', '2', 3),
(10, '(5500,4000,7000)', '(5500,4000,8400)', 'Stainless steel', '2', 3),
(11, '(5500,4000,8400)', '(5500,4000,9800)', 'Stainless steel', '2', 3),
(12, '(8500,4000,0)', '(8500,4000,1400)', 'Stainless steel', '2', 4),
(13, '(8500,4000,1400)', '(8500,4000,2800)', 'Stainless steel', '2', 4),
(14, '(8500,4000,2800)', '(8500,4000,4200)', 'Stainless steel', '2', 4),
(15, '(8500,4000,4200)', '(8500,4000,5600)', 'Stainless steel', '2', 4),
(16, '(8500,4000,5600)', '(8500,4000,7000)', 'Stainless steel', '2', 4),
(17, '(8500,4000,7000)', '(8500,4000,8400)', 'Stainless steel', '2', 4),
(18, '(8500,4000,8400)', '(8500,4000,9800)', 'Stainless steel', '2', 4),
(19, '(11500,4000,0)', '(11500,4000,2500)', 'Stainless steel', '2', 5),
(20, '(11500,4000,2500)', '(11500,4000,5000)', 'Stainless steel', '2', 5),
(21, '(11500,4000,5000)', '(11500,4000,7500)', 'Stainless steel', '2', 5),
(22, '(11500,4000,7500)', '(11500,4000,10000)', 'Stainless steel', '2', 5),
(23, '(14500,4000,0)', '(14500,4000,500)', 'Stainless steel', '2', 6),
(24, '(14500,4000,500)', '(14500,4000,5500)', 'Stainless steel', '2', 6),
(25, '(14500,4000,5500)', '(14500,4000,10000)', 'Stainless steel', '2', 6);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accesorioprimaria`
--
ALTER TABLE `accesorioprimaria`
  ADD PRIMARY KEY (`id_accesorioPrimaria`),
  ADD KEY `fk_Primaria` (`fk_Primaria`);

--
-- Indexes for table `accesoriosecundaria`
--
ALTER TABLE `accesoriosecundaria`
  ADD PRIMARY KEY (`id_accesorioSecundaria`),
  ADD KEY `fk_Secundaria` (`fk_Secundaria`);

--
-- Indexes for table `tuberiaprimaria`
--
ALTER TABLE `tuberiaprimaria`
  ADD PRIMARY KEY (`id_Primaria`);

--
-- Indexes for table `tuberiasecundaria`
--
ALTER TABLE `tuberiasecundaria`
  ADD PRIMARY KEY (`id_Secundaria`),
  ADD KEY `fk_Primaria` (`fk_Primaria`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accesorioprimaria`
--
ALTER TABLE `accesorioprimaria`
  MODIFY `id_accesorioPrimaria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `accesoriosecundaria`
--
ALTER TABLE `accesoriosecundaria`
  MODIFY `id_accesorioSecundaria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `tuberiaprimaria`
--
ALTER TABLE `tuberiaprimaria`
  MODIFY `id_Primaria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tuberiasecundaria`
--
ALTER TABLE `tuberiasecundaria`
  MODIFY `id_Secundaria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accesorioprimaria`
--
ALTER TABLE `accesorioprimaria`
  ADD CONSTRAINT `accesorioprimaria_ibfk_1` FOREIGN KEY (`fk_Primaria`) REFERENCES `tuberiaprimaria` (`id_Primaria`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `accesoriosecundaria`
--
ALTER TABLE `accesoriosecundaria`
  ADD CONSTRAINT `accesoriosecundaria_ibfk_1` FOREIGN KEY (`fk_Secundaria`) REFERENCES `tuberiasecundaria` (`id_Secundaria`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tuberiasecundaria`
--
ALTER TABLE `tuberiasecundaria`
  ADD CONSTRAINT `tuberiasecundaria_ibfk_1` FOREIGN KEY (`fk_Primaria`) REFERENCES `tuberiaprimaria` (`id_Primaria`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
