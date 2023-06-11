-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2023 at 05:28 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelm`
--

-- --------------------------------------------------------

--
-- Table structure for table `custom`
--

CREATE TABLE `custom` (
  `clname` varchar(50) NOT NULL,
  `clno` bigint(20) NOT NULL,
  `claadhar` int(12) NOT NULL,
  `clemail` varchar(100) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `noofadul` int(13) NOT NULL,
  `noofchildren` int(14) NOT NULL,
  `roomno` int(30) NOT NULL,
  `hallno` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `ecode` int(12) NOT NULL,
  `ename` varchar(40) NOT NULL,
  `dept` varchar(20) NOT NULL,
  `eno` bigint(20) NOT NULL,
  `eaadhar` int(12) NOT NULL,
  `eemail` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `hallno` int(13) NOT NULL,
  `event` varchar(100) NOT NULL,
  `cusadhaar` int(90) NOT NULL,
  `ecode` int(12) NOT NULL,
  `roomrent` int(15) NOT NULL,
  `total` int(50) NOT NULL,
  `days` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `roomno` int(30) NOT NULL,
  `cusadhaar` int(90) NOT NULL,
  `roomtypr` varchar(20) NOT NULL,
  `ecode` int(12) NOT NULL,
  `roomrent` int(15) NOT NULL,
  `total` int(50) NOT NULL,
  `days` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `custom`
--
ALTER TABLE `custom`
  ADD PRIMARY KEY (`claadhar`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`ecode`),
  ADD UNIQUE KEY `eaadhar` (`eaadhar`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
