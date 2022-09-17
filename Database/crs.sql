-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2021 at 05:25 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crs`
--

-- --------------------------------------------------------

--
-- Table structure for table `adm_location`
--

CREATE TABLE `adm_location` (
  `id` bigint(20) NOT NULL,
  `pincode` int(11) NOT NULL,
  `l_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adm_location`
--

INSERT INTO `adm_location` (`id`, `pincode`, `l_name`) VALUES
(1, 390009, 'Vadodara'),
(2, 390002, 'Surat'),
(3, 390004, 'Ahmedabad');

-- --------------------------------------------------------

--
-- Table structure for table `adm_login`
--

CREATE TABLE `adm_login` (
  `id` bigint(20) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adm_login`
--

INSERT INTO `adm_login` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `adm_vehicles`
--

CREATE TABLE `adm_vehicles` (
  `id` bigint(20) NOT NULL,
  `vehicle_brand` varchar(30) NOT NULL,
  `l_name` varchar(100) NOT NULL,
  `vehicle_name` varchar(100) NOT NULL,
  `vehicle_image` varchar(200) NOT NULL,
  `price_per_day` int(11) NOT NULL,
  `fuel_type` varchar(100) NOT NULL,
  `seating_capacity` varchar(100) NOT NULL,
  `aircondition` varchar(100) NOT NULL,
  `airbag` varchar(100) NOT NULL,
  `vehicle_no` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adm_vehicles`
--

INSERT INTO `adm_vehicles` (`id`, `vehicle_brand`, `l_name`, `vehicle_name`, `vehicle_image`, `price_per_day`, `fuel_type`, `seating_capacity`, `aircondition`, `airbag`, `vehicle_no`) VALUES
(5, 'Hyundai', 'Vadodara', 'i-20', '/media/i20_39OjuVC.jpg', 50, 'Diesel', 'three', 'yes', 'yes', 'GJ06Au1645'),
(6, 'hyundai', 'Vadodara', 'alcazar', '/media/alcazar_M7WZN8Q.jpg', 40, 'Petrol', 'two', 'yes', 'yes', 'GJ06AU1645'),
(7, 'Hyundai', 'Vadodara', 'tucson', '/media/tucson.jpg', 55, 'Diesel', 'four', 'yes', 'yes', 'gj06lk5442'),
(8, 'TATA', 'Surat', 'Mercedes', '/media/venue.jpg', 60, 'Diesel', 'five', 'yes', 'yes', 'GJ06az1613');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'user', '0001_initial', '2021-07-27 15:33:53.475328'),
(2, 'adm', '0001_initial', '2021-07-27 15:40:10.138481'),
(3, 'contenttypes', '0001_initial', '2021-07-27 15:40:10.839251'),
(4, 'auth', '0001_initial', '2021-07-27 15:40:27.571035'),
(5, 'admin', '0001_initial', '2021-07-27 15:40:33.439897'),
(6, 'admin', '0002_logentry_remove_auto_add', '2021-07-27 15:40:33.692222'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2021-07-27 15:40:33.810904'),
(8, 'contenttypes', '0002_remove_content_type_name', '2021-07-27 15:40:35.559257'),
(9, 'auth', '0002_alter_permission_name_max_length', '2021-07-27 15:40:36.744650'),
(10, 'auth', '0003_alter_user_email_max_length', '2021-07-27 15:40:38.432940'),
(11, 'auth', '0004_alter_user_username_opts', '2021-07-27 15:40:38.662335'),
(12, 'auth', '0005_alter_user_last_login_null', '2021-07-27 15:40:40.291846'),
(13, 'auth', '0006_require_contenttypes_0002', '2021-07-27 15:40:40.396840'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2021-07-27 15:40:40.553665'),
(15, 'auth', '0008_alter_user_username_max_length', '2021-07-27 15:40:42.538439'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2021-07-27 15:40:45.314273'),
(17, 'auth', '0010_alter_group_name_max_length', '2021-07-27 15:40:47.900830'),
(18, 'auth', '0011_update_proxy_permissions', '2021-07-27 15:40:48.047436'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2021-07-27 15:40:51.886266'),
(20, 'sessions', '0001_initial', '2021-07-27 15:40:52.636743'),
(21, 'user', '0002_alter_booking_from_date', '2021-08-07 11:27:04.546416'),
(22, 'user', '0003_alter_booking_to_date', '2021-08-07 11:38:31.913622'),
(23, 'adm', '0002_auto_20210808_1053', '2021-08-08 05:23:34.684254'),
(24, 'user', '0004_post', '2021-08-08 07:05:45.800063'),
(25, 'user', '0005_auto_20210809_1604', '2021-08-09 10:35:07.049964'),
(26, 'user', '0006_booking_additional_charge', '2021-08-12 14:33:56.582323');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_booking`
--

CREATE TABLE `user_booking` (
  `id` bigint(20) NOT NULL,
  `booking_number` varchar(100) NOT NULL,
  `email_id` varchar(254) NOT NULL,
  `veh_id` int(11) NOT NULL,
  `from_date` datetime(6) NOT NULL,
  `to_date` datetime(6) NOT NULL,
  `from_destination` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `total_price` int(11) NOT NULL,
  `diff_amount` double DEFAULT NULL,
  `refund_price` double DEFAULT NULL,
  `additional_charge` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_booking`
--

INSERT INTO `user_booking` (`id`, `booking_number`, `email_id`, `veh_id`, `from_date`, `to_date`, `from_destination`, `status`, `total_price`, `diff_amount`, `refund_price`, `additional_charge`) VALUES
(123, '2679509663393', 'deepak.rj.dr@gmail.com', 5, '2021-08-11 16:04:00.000000', '2021-08-13 16:04:00.000000', 'location', 'complete', 2400, NULL, NULL, 200),
(124, '5669183011761', 'deepak.rj.dr@gmail.com', 5, '2021-08-16 16:05:00.000000', '2021-08-18 16:05:00.000000', 'location', 'complete', 2400, NULL, NULL, NULL),
(125, '2611296445701', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 23:10:00.000000', '2021-08-14 23:10:00.000000', 'location', 'payment pending', 1200, NULL, NULL, NULL),
(126, '8724715838418', 'deepak.rj.dr@gmail.com', 6, '2021-08-11 23:10:00.000000', '2021-08-12 23:10:00.000000', 'location', 'payment pending', 960, NULL, NULL, NULL),
(127, '3110048876396', 'deepak.rj.dr@gmail.com', 8, '2021-08-11 23:29:00.000000', '2021-08-13 23:29:00.000000', 'location', 'complete', 2880, 1728, 1152, NULL),
(128, '5691754944972', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 14:56:00.000000', '2021-08-31 14:56:00.000000', 'location', 'payment pending', 21600, NULL, NULL, NULL),
(129, '2636230501262', 'deepak.rj.dr@gmail.com', 6, '2021-08-13 17:44:00.000000', '2021-08-14 17:44:00.000000', 'location', 'payment pending', 960, NULL, NULL, NULL),
(130, '3406295600821', 'deepak.rj.dr@gmail.com', 5, '2021-08-14 19:03:00.000000', '2021-08-15 19:03:00.000000', 'location', 'cancelled', 1200, 360, 840, NULL),
(131, '6211821875551', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:49:00.000000', '2021-08-14 20:49:00.000000', 'location', 'payment pending', 1200, NULL, NULL, NULL),
(132, '9353983985936', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:49:00.000000', '2021-08-14 20:49:00.000000', 'location', 'payment pending', 1200, NULL, NULL, NULL),
(133, '2872105129771', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:49:00.000000', '2021-08-14 20:49:00.000000', 'location', 'payment pending', 1200, NULL, NULL, NULL),
(134, '2404231580749', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:49:00.000000', '2021-08-14 20:49:00.000000', 'location', 'payment pending', 1200, NULL, NULL, NULL),
(135, '6992856912253', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:50:00.000000', '2021-08-21 20:51:00.000000', 'location', 'payment pending', 9600, NULL, NULL, NULL),
(136, '5631698629138', 'deepak.rj.dr@gmail.com', 5, '2021-08-13 20:50:00.000000', '2021-08-21 20:51:00.000000', 'location', 'payment pending', 9600, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_post`
--

CREATE TABLE `user_post` (
  `id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_user`
--

CREATE TABLE `user_user` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `email_id` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `lic_no` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(10) NOT NULL,
  `country` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_user`
--

INSERT INTO `user_user` (`id`, `fullname`, `email_id`, `password`, `contact_no`, `lic_no`, `dob`, `address`, `city`, `country`) VALUES
(1, 'Deepak', 'deepak.rj.dr@gmail.com', '1234', '7567422168', 'DL123', '1998-06-15', '401 Shivalik Flats', 'Vadodara', 'India'),
(2, 'Janvi Assasani', 'janvi@gmail.com', '123', '8456789584', 'DL1234', '2000-01-09', 'ahmedabad', 'Ahmedabad', 'India');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adm_location`
--
ALTER TABLE `adm_location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adm_login`
--
ALTER TABLE `adm_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adm_vehicles`
--
ALTER TABLE `adm_vehicles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `user_booking`
--
ALTER TABLE `user_booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_post`
--
ALTER TABLE `user_post`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adm_location`
--
ALTER TABLE `adm_location`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `adm_login`
--
ALTER TABLE `adm_login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `adm_vehicles`
--
ALTER TABLE `adm_vehicles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `user_booking`
--
ALTER TABLE `user_booking`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- AUTO_INCREMENT for table `user_post`
--
ALTER TABLE `user_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
