-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2023 at 02:22 AM
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

-- --------------------------------------------------------

--
-- Table structure for table `accesoriosecundaria`
--

CREATE TABLE `accesoriosecundaria` (
  `id_accesorioSecundaria` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `fk_Secundaria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

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
  MODIFY `id_accesorioPrimaria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accesoriosecundaria`
--
ALTER TABLE `accesoriosecundaria`
  MODIFY `id_accesorioSecundaria` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tuberiaprimaria`
--
ALTER TABLE `tuberiaprimaria`
  MODIFY `id_Primaria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tuberiasecundaria`
--
ALTER TABLE `tuberiasecundaria`
  MODIFY `id_Secundaria` int(11) NOT NULL AUTO_INCREMENT;

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
