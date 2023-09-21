-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 22, 2022 at 06:09 AM
-- Server version: 8.0.26
-- PHP Version: 7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wae_pre`
--

-- --------------------------------------------------------

--
-- Table structure for table `Activity_activity`
--

CREATE TABLE `Activity_activity` (
  `id` bigint NOT NULL,
  `SourceID` int NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `Comment` varchar(250) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `RelatedTo` varchar(100) NOT NULL,
  `Emp` int NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Description` longtext NOT NULL,
  `From` varchar(10) NOT NULL,
  `To` varchar(10) NOT NULL,
  `Time` varchar(10) NOT NULL,
  `Allday` varchar(200) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `Host` varchar(100) NOT NULL,
  `Participants` varchar(250) NOT NULL,
  `Document` varchar(250) NOT NULL,
  `Repeated` varchar(100) NOT NULL,
  `Priority` varchar(100) NOT NULL,
  `ProgressStatus` varchar(100) NOT NULL,
  `leadType` varchar(50) NOT NULL,
  `Type` varchar(20) NOT NULL,
  `SourceType` varchar(20) NOT NULL,
  `Status` int NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Activity_activity`
--

INSERT INTO `Activity_activity` (`id`, `SourceID`, `Subject`, `Comment`, `Name`, `RelatedTo`, `Emp`, `Title`, `Description`, `From`, `To`, `Time`, `Allday`, `Location`, `Host`, `Participants`, `Document`, `Repeated`, `Priority`, `ProgressStatus`, `leadType`, `Type`, `SourceType`, `Status`, `CreateDate`, `CreateTime`) VALUES
(1, 39, 'Groffers Stove', 'Needs to take a follow up on call for OPS fields.', '', '', 98, '', '', '2022-10-10', '2022-10-10', '11:00 AM', '', '', '', '', '', '', '', '', '', 'Followup', 'Lead', 0, '2022-10-07', '6:17:36 PM'),
(2, 0, '', '', '', 'hi', 1, 'test', 'test', '', '2022-10-17', '03:03 PM', '', '', '', '', '', '', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-10-10', '3:02:44 PM'),
(3, 11, '', '', '', 'hi', 1, 'New Event', 'Testing', '2022-10-31', '2022-10-31', '03:25 PM', '', 'Delhi', 'Host', 'Rahul', '', 'Daily', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-10-31', '3:21:34 PM'),
(4, 11, '', '', '', 'hi', 1, 'New Event 2', 'Tesintg', '2022-10-13', '2022-10-13', '3:26 PM', '', 'Delhi', 'Host', 'Ashutosh', '', 'Monthly', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-10-31', '3:21:34 PM'),
(5, 91, 'Humdard', 'Need a discussion', '', '', 1, '', '', '2022-11-21', '2022-11-21', '9:00 AM', '', '', '', '', '', '', '', '', '', 'Followup', 'Lead', 0, '2022-11-02', '6:36:52 PM'),
(6, 15, '', '', '', 'hi', 107, 'Next visit', 'wertyu', '2022-11-04', '2022-11-04', '03:13 PM', '', 'Office', 'VISION', 'Yes', '', 'Daily', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-11-03', '1:10:11 PM'),
(7, 15, '', '', '', 'hi', 107, 'TO DO LIST', 'DFGHJKL', '2022-11-04', '2022-11-05', '6:16 PM', '', 'HJK', 'FGHJKL', 'FDGHJKL', '', 'Daily', 'low', 'WIP', '', 'Task', 'Opportunity', 0, '2022-11-03', '1:10:11 PM'),
(8, 16, '', '', '', 'hi', 107, 'rtyujkl', 'ghjk', '2022-11-04', '2022-11-04', '01:28 PM', '', 'hjk', 'bnm', 'nm,', '', 'Daily', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-11-03', '1:21:19 PM'),
(9, 16, '', '', '', 'hi', 107, 'rtyujkl', 'ghjk', '2022-11-04', '2022-11-04', '001:28 PM', '', 'hjk', 'bnm', 'nm,', '', 'Daily', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-11-03', '1:21:19 PM'),
(10, 16, '', '', '', 'hi', 107, 'TO DO LIST', 'sedftgyhujikl', '2022-11-04', '2022-11-12', '1:31 PM', '', 'HJK', 'FGHJKL', 'FDGHJKL', '', 'Yearly', 'low', 'WIP', '', 'Task', 'Opportunity', 0, '2022-11-03', '1:21:19 PM'),
(11, 33, '', '', '', 'hi', 1, 'tesat', 'test', '2022-11-21', '2022-11-25', '1:42 AM', '', 'delhi', '', '', '', 'Once', 'low', 'WIP', '', 'Task', 'Opportunity', 0, '2022-11-21', '9:56:02 AM'),
(12, 33, '', '', '', 'hi', 1, 'title', 'desccru', '2022-11-22', '2022-11-26', '02:50 PM', '', 'loaccdh', '', '', '', 'Once', 'low', 'WIP', '', 'Event', 'Opportunity', 0, '2022-11-21', '9:56:02 AM');

-- --------------------------------------------------------

--
-- Table structure for table `Activity_chatter`
--

CREATE TABLE `Activity_chatter` (
  `id` bigint NOT NULL,
  `Message` varchar(250) NOT NULL,
  `SourceID` varchar(10) NOT NULL,
  `SourceType` varchar(20) NOT NULL,
  `Emp` varchar(10) NOT NULL,
  `Emp_Name` varchar(50) NOT NULL,
  `Mode` varchar(50) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Activity_chatter`
--

INSERT INTO `Activity_chatter` (`id`, `Message`, `SourceID`, `SourceType`, `Emp`, `Emp_Name`, `Mode`, `UpdateDate`, `UpdateTime`) VALUES
(1, 'Needs to take a follow up on call for OPS fields.', '39', 'Lead', '98', 'Samay', 'Call', '2022-10-07', '6:17:36 PM'),
(2, 'Hi, everyone the needs to be complete before due date with out any delay the message needs to be communicated to one and all.', '6', 'Opportunity', '98', 'Samay', '', 'Oct 07, 2022', '6:51 PM'),
(3, 'TEST', '6', 'Opportunity', '1', 'sriram', '', 'Oct 11, 2022', '4:23 PM'),
(4, 'Need a discussion', '91', 'Lead', '1', 'sriram', 'Call', '2022-11-02', '6:36:52 PM'),
(5, 'I hope this stage has been completed', '13', 'Opportunity', '1', 'sriram', '', 'Nov 03, 2022', '10:07 AM'),
(6, 'I hope this stage has been completed', '13', 'Opportunity', '1', 'sriram', '', 'Nov 03, 2022', '10:07 AM'),
(7, 'sdfghjkl,.', '16', 'Opportunity', '107', 'Farooq', '', 'Nov 03, 2022', '1:26 PM');

-- --------------------------------------------------------

--
-- Table structure for table `Activity_maps`
--

CREATE TABLE `Activity_maps` (
  `id` bigint NOT NULL,
  `Lat` varchar(100) NOT NULL,
  `Long` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Emp_Id` varchar(10) NOT NULL,
  `Emp_Name` varchar(50) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Attachment_attachment`
--

CREATE TABLE `Attachment_attachment` (
  `id` bigint NOT NULL,
  `File` varchar(150) NOT NULL,
  `LinkType` varchar(100) NOT NULL,
  `LinkID` int NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL,
  `Caption` varchar(500) NOT NULL,
  `FileName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Attachment_attachment`
--

INSERT INTO `Attachment_attachment` (`id`, `File`, `LinkType`, `LinkID`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `Caption`, `FileName`) VALUES
(1, '/static/image/Attachment/contact-person_h15bKeb.png', 'Opportunity', 1, '2022-09-28', '3:21:33 PM', '2022-09-28', '3:21:33 PM', 'New Caption', ''),
(2, '/static/image/Attachment/contact-person2_r00RS80.png', 'Opportunity', 1, '2022-09-28', '3:21:33 PM', '2022-09-28', '3:21:33 PM', 'New Caption', ''),
(3, '/static/image/Attachment/contact-person_dB3vV45.png', 'Opportunity', 1, '2022-09-28', '3:45:49 PM', '2022-09-28', '3:45:49 PM', 'New Caption', ''),
(4, '/static/image/Attachment/contact-person2_EhDvI5j.png', 'Opportunity', 1, '2022-09-28', '3:45:49 PM', '2022-09-28', '3:45:49 PM', 'New Caption', ''),
(7, '/static/image/Attachment/contact-person_JFis2eN.png', 'Opportunity', 2, '2022-09-28', '6:47:11 PM', '2022-09-28', '6:47:11 PM', 'New Caption', ''),
(8, '/static/image/Attachment/contact-person2_YzFzEQ0.png', 'Opportunity', 2, '2022-09-28', '6:47:11 PM', '2022-09-28', '6:47:11 PM', 'New Caption', ''),
(9, '/static/image/Attachment/bridge-logo_0Vg6og3.png', 'Opportunity', 2, '2022-09-28', '6:47:11 PM', '2022-09-28', '6:47:11 PM', 'New Caption', ''),
(10, '/static/image/Attachment/contact-person_kREHFzS.png', 'Quotation', 3, '2022-09-29', '2:54:14 PM', '2022-09-29', '2:54:14 PM', 'Adhar Card', ''),
(11, '/static/image/Attachment/contact-person2_zvYTB51.png', 'Quotation', 3, '2022-09-29', '2:54:14 PM', '2022-09-29', '2:54:14 PM', 'New Caption', ''),
(12, '/static/image/Attachment/contact-person_rPzw9SE.png', 'Project', 4, '2022-09-29', '5:32:13 PM', '2022-09-29', '5:32:13 PM', '', ''),
(13, '/static/image/Attachment/contact-person2_fYNF6t0.png', 'Project', 8, '2022-09-30', '12:27:06 PM', '2022-09-30', '12:27:06 PM', '', ''),
(17, '/static/image/Attachment/iner-box2_1z3X2GB.png', 'Project', 16, '2022-09-30', '3:21:46 PM', '2022-09-30', '3:21:46 PM', 'New Caption', ''),
(18, '/static/image/Attachment/invoices_0Yc2i3w.png', 'Project', 16, '2022-09-30', '3:21:46 PM', '2022-09-30', '3:21:46 PM', 'New Caption', ''),
(19, '/static/image/Attachment/opportunity_Lu0tyBV.png', 'Project', 16, '2022-09-30', '3:23:08 PM', '2022-09-30', '3:23:08 PM', 'New Caption', ''),
(35, '/static/image/Attachment/bann-img2_pbMUFOd.png', 'Project', 11, '2022-09-30', '3:45:33 PM', '2022-09-30', '3:45:33 PM', 'New Caption', ''),
(36, '/static/image/Attachment/bridge-logo_mtmKVtL.png', 'Project', 11, '2022-09-30', '3:45:33 PM', '2022-09-30', '3:45:33 PM', 'New Caption', ''),
(37, '/static/image/Attachment/bridge-logo2_JATmlD2.png', 'Project', 11, '2022-09-30', '3:45:33 PM', '2022-09-30', '3:45:33 PM', 'New Caption', ''),
(38, '/static/image/Attachment/contact-person2_i6kXkiC.png', 'Project', 11, '2022-09-30', '3:46:55 PM', '2022-09-30', '3:46:55 PM', 'asdf', ''),
(39, '/static/image/Attachment/contact-person2_azmUhQY.png', 'Project', 11, '2022-09-30', '3:48:29 PM', '2022-09-30', '3:48:29 PM', 'asdf', ''),
(40, '/static/image/Attachment/Capture_8iQk0mF.PNG', 'Project', 12, '2022-09-30', '4:12:29 PM', '2022-09-30', '4:12:29 PM', 'Adhar Card', ''),
(41, '/static/image/Attachment/contact-person_OmQ0TJQ.png', 'Project', 12, '2022-09-30', '4:12:29 PM', '2022-09-30', '4:12:29 PM', 'New Caption', ''),
(43, '/static/image/Attachment/graph2_ZUeez1B.JPG', 'Project', 13, '2022-09-30', '6:18:50 PM', '2022-09-30', '6:18:50 PM', '', ''),
(44, '/static/image/Attachment/graph3_PPGRg68.JPG', 'Project', 13, '2022-09-30', '6:18:50 PM', '2022-09-30', '6:18:50 PM', '', ''),
(45, '/static/image/Attachment/graph4_8PQUKrL.JPG', 'Project', 13, '2022-09-30', '6:18:50 PM', '2022-09-30', '6:18:50 PM', '', ''),
(46, '/static/image/Attachment/Capture_XjIQMbA.PNG', 'Order', 1, '2022-10-3', '10:19:03 AM', '2022-10-3', '10:19:03 AM', 'Adhar Card', ''),
(47, '/static/image/Attachment/contact-person_w4OPxOd.png', 'Lead', 34, '2022-10-3', '10:22:08 AM', '2022-10-3', '10:22:08 AM', 'Adhar Card', ''),
(48, '/static/image/Attachment/contact-person2_kK7UtuG.png', 'Lead', 34, '2022-10-3', '10:22:08 AM', '2022-10-3', '10:22:08 AM', 'Adhar Card', ''),
(49, '/static/image/Attachment/Bridge-%20Document%20(B2B).xlsx', 'Lead', 35, '2022-10-03', '11:20:11 AM', '2022-10-03', '11:20:11 AM', 'Standalone Document', ''),
(50, '/static/image/Attachment/WIN_20220816_11_11_32_Pro.jpg', 'Lead', 35, '2022-10-3', '11:28:48 AM', '2022-10-3', '11:28:48 AM', 'Image', ''),
(54, '/static/image/Attachment/SALE%20Module%20Discussion%20(2).xlsx', 'Project', 15, '2022-10-03', '2:47:55 PM', '2022-10-03', '2:47:55 PM', '', ''),
(55, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1).xlsx', 'Project', 15, '2022-10-03', '2:47:55 PM', '2022-10-03', '2:47:55 PM', '', ''),
(56, '/static/image/Attachment/14.09.2022_15.50.04_REC.mp4', 'Project', 15, '2022-10-03', '2:47:55 PM', '2022-10-03', '2:47:55 PM', '', ''),
(57, '/static/image/Attachment/WhatsApp%20Image%202022-09-12%20at%209.31.40%20PM.jpeg', 'Project', 15, '2022-10-03', '2:47:55 PM', '2022-10-03', '2:47:55 PM', '', ''),
(58, '/static/image/Attachment/Screen%20Shot%202022-09-08%20at%203.45.17%20PM.png', 'Project', 15, '2022-10-03', '2:47:55 PM', '2022-10-03', '2:47:55 PM', '', ''),
(60, '/static/image/Attachment/Quotation.pdf', 'Project', 17, '2022-10-03', '3:52:11 PM', '2022-10-03', '3:52:11 PM', '', ''),
(61, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1)%20(1)_GRHEcYJ.xlsx', 'Opportunity', 3, '2022-10-03', '4:09:40 PM', '2022-10-03', '4:09:40 PM', 'Projection Doc', ''),
(62, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)%20(1).xlsx', 'Opportunity', 3, '2022-10-03', '4:24:24 PM', '2022-10-03', '4:24:24 PM', 'Projection Doc', ''),
(63, '/static/image/Attachment/BingWallpaper.exe', 'Quotation', 4, '2022-10-03', '4:29:40 PM', '2022-10-03', '4:29:40 PM', '', ''),
(64, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1)%20(1)_GRHEcYJ_EAzc0No.xlsx', 'Lead', 36, '2022-10-03', '4:59:57 PM', '2022-10-03', '4:59:57 PM', 'Project Doc Sales', ''),
(65, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1)_rGeVMyM.xlsx', 'Project', 18, '2022-10-03', '5:22:39 PM', '2022-10-03', '5:22:39 PM', '', ''),
(66, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)%20(1)_Kq0SH04.xlsx', 'Project', 18, '2022-10-03', '5:22:39 PM', '2022-10-03', '5:22:39 PM', 'NA', ''),
(67, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1)_7sD6jdN.xlsx', 'Project', 19, '2022-10-03', '5:22:39 PM', '2022-10-03', '5:22:39 PM', '', ''),
(68, '/static/image/Attachment/14.09.2022_15.50.04_REC_vjs9Idy.mp4', 'Project', 19, '2022-10-03', '5:22:39 PM', '2022-10-03', '5:22:39 PM', '', ''),
(69, '/static/image/Attachment/Bridge-%20Document%20(B2B)%20(1)_rGeVMyM_0m7K0Wl.xlsx', 'Opportunity', 4, '2022-10-03', '5:35:57 PM', '2022-10-03', '5:35:57 PM', 'Water Plant Doc', ''),
(70, '/static/image/Attachment/Bridge_Field_Details_(B2C)%20(3).xlsx', 'Project', 20, '2022-10-06', '2:56:10 PM', '2022-10-06', '2:56:10 PM', '', ''),
(71, '/static/image/Attachment/Print_BHUBANESWAR(BBS)_BALASORE(BLS)_6609933272.pdf', 'Lead', 38, '2022-10-6', '3:10:49 PM', '2022-10-6', '3:10:49 PM', '', ''),
(72, '/static/image/Attachment/item_import%20(1).xlsx', 'Opportunity', 5, '2022-10-06', '3:11:49 PM', '2022-10-06', '3:11:49 PM', 'Import', ''),
(73, '/static/image/Attachment/Bridge_Field_Details_(B2C)%20(4).xlsx', 'Order', 2, '2022-10-07', '11:58:36 AM', '2022-10-07', '11:58:36 AM', 'Quotation', ''),
(74, '/static/image/Attachment/Quotation_j872rRV.pdf', 'Order', 2, '2022-10-07', '11:58:36 AM', '2022-10-07', '11:58:36 AM', 'Quotation', ''),
(75, '/static/image/Attachment/Capture_GaB5vVm.PNG', 'Order', 3, '2022-10-07', '1:14:38 PM', '2022-10-07', '1:14:38 PM', 'Capture', ''),
(76, '/static/image/Attachment/Quotation_qOYWPLa.pdf', 'Order', 4, '2022-10-07', '3:40:41 PM', '2022-10-07', '3:40:41 PM', 'OPS Quote', ''),
(77, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_qS01vA5.xlsx', 'Lead', 39, '2022-10-07', '6:12:43 PM', '2022-10-07', '6:12:43 PM', 'Doc.', ''),
(78, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_UrQpWsN.xlsx', 'Opportunity', 6, '2022-10-07', '6:48:29 PM', '2022-10-07', '6:48:29 PM', 'Sales Doc.', ''),
(79, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_xudwJIC.xlsx', 'Quotation', 8, '2022-10-07', '7:02:33 PM', '2022-10-07', '7:02:33 PM', '', ''),
(80, '/static/image/Attachment/Quotation_Hcu1mYz.pdf', 'Lead', 40, '2022-10-10', '5:11:08 PM', '2022-10-10', '5:11:08 PM', 'Quote', ''),
(81, '/static/image/Attachment/document%20(2).doc', 'Opportunity', 7, '2022-10-10', '5:37:08 PM', '2022-10-10', '5:37:08 PM', 'Doc', ''),
(82, '/static/image/Attachment/document%20(2)_7L8DDV4.doc', 'Quotation', 10, '2022-10-10', '5:57:33 PM', '2022-10-10', '5:57:33 PM', 'Doc', ''),
(83, '/static/image/Attachment/document%20(2)_mCz6KPC.doc', 'Quotation', 11, '2022-10-10', '5:57:33 PM', '2022-10-10', '5:57:33 PM', 'Doc', ''),
(84, '/static/image/Attachment/document%20(2)_hFcxw3E.doc', 'Quotation', 12, '2022-10-10', '5:57:33 PM', '2022-10-10', '5:57:33 PM', 'Doc', ''),
(85, '/static/image/Attachment/document%20(2)_7Umm3Ke.doc', 'Quotation', 13, '2022-10-10', '5:57:33 PM', '2022-10-10', '5:57:33 PM', 'Doc', ''),
(86, '/static/image/Attachment/document%20(2)_ry1gFhr.doc', 'Quotation', 14, '2022-10-10', '6:09:54 PM', '2022-10-10', '6:09:54 PM', 'Doc', ''),
(87, '/static/image/Attachment/document%20(2)_4QU9yHG.doc', 'Quotation', 15, '2022-10-10', '6:15:00 PM', '2022-10-10', '6:15:00 PM', 'Doc', ''),
(88, '/static/image/Attachment/Bridge%20-%20Features.docx', 'Project', 25, '2022-10-11', '6:19:37 PM', '2022-10-11', '6:19:37 PM', '', ''),
(89, '/static/image/Attachment/Sick%20lift%20flow%20chart-FINAL%20REV.pdf', 'Order', 10, '2022-10-13', '4:54:28 PM', '2022-10-13', '4:54:28 PM', '', ''),
(90, '/static/image/Attachment/LeadExcelSheet.xlsx', 'Lead', 41, '2022-10-14', '6:17:30 PM', '2022-10-14', '6:17:30 PM', 'Doc', ''),
(91, '/static/image/Attachment/Capture_yT9NqcC.PNG', 'Lead', 43, '2022-10-17', '2:20:17 PM', '2022-10-17', '2:20:17 PM', 'asdASD', ''),
(92, '/static/image/Attachment/Ellipse1_jfRUpPi.png', 'Lead', 44, '2022-10-17', '3:51:08 PM', '2022-10-17', '3:51:08 PM', 'asdfasdf', 'Ellipse1.png'),
(93, '/static/image/Attachment/dash-logo_awUTSB4.JPG', 'Opportunity', 11, '2022-10-17', '5:30:29 PM', '2022-10-17', '5:30:29 PM', 'New Caption', 'dash-logo.JPG'),
(94, '/static/image/Attachment/contact-person2_o1eAPqW.png', 'Quotation', 36, '2022-10-17', '5:33:54 PM', '2022-10-17', '5:33:54 PM', 'adsadf', ''),
(95, '/static/image/Attachment/orders_kCnTs59.png', 'Lead', 44, '2022-10-17', '5:34:39 PM', '2022-10-17', '5:34:39 PM', 'New Caption', 'orders.png'),
(96, '/static/image/Attachment/graph3_lsCbn6d.JPG', 'Lead', 44, '2022-10-17', '5:35:59 PM', '2022-10-17', '5:35:59 PM', 'Adhar Card', ''),
(97, '/static/image/Attachment/opportunity_s88HF2z.png', 'Lead', 44, '2022-10-17', '5:41:58 PM', '2022-10-17', '5:41:58 PM', 'New Caption', 'opportunity.png'),
(98, '/static/image/Attachment/contact-person2_w7KHGGg.png', 'Opportunity', 11, '2022-10-17', '5:42:13 PM', '2022-10-17', '5:42:13 PM', 'asdf', 'contact-person2.png'),
(99, '/static/image/Attachment/indologo.png', 'Lead', 46, '2022-10-18', '2:28:32 PM', '2022-10-18', '2:28:32 PM', 'test', 'indologo.png'),
(100, '/static/image/Attachment/logos_youtube-icon.png', 'Lead', 46, '2022-10-18', '2:28:32 PM', '2022-10-18', '2:28:32 PM', 'test', 'logos_youtube-icon.png'),
(101, '/static/image/Attachment/quotation_gD7FUo2.png', 'Lead', 52, '2022-10-18', '3:37:42 PM', '2022-10-18', '3:37:42 PM', 'Adhar Card', 'quotation.png'),
(102, '/static/image/Attachment/iner-box1_2tPbkRE.png', 'Lead', 53, '2022-10-18', '3:40:36 PM', '2022-10-18', '3:40:36 PM', 'Adhar Card', 'iner-box1.png'),
(103, '/static/image/Attachment/1170_6TWV0io', 'Lead', 68, '2022-10-18', '11:49 AM', '2022-10-18', '11:49 AM', '', '1170'),
(104, '/static/image/Attachment/1666093894.4226031video.mp4', 'Lead', 69, '18-10-2022', '11:49 AM', '18-10-2022', '11:49 AM', 'test', '1666093894.4226031video.mp4'),
(105, '/static/image/Attachment/1666094047.415474video.mp4', 'Lead', 70, '18-10-2022', '11:49 AM', '18-10-2022', '11:49 AM', 'test', '1666094047.415474video.mp4'),
(106, '/static/image/Attachment/826709', 'Lead', 71, '2022-10-18', '11:49 AM', '2022-10-18', '11:49 AM', '', '826709'),
(107, '/static/image/Attachment/826709_Yk9TLNb', 'Lead', 72, '2022-10-18', '11:49 AM', '2022-10-18', '11:49 AM', '', '826709'),
(109, '/static/image/Attachment/826707.jpg', 'Lead', 74, '2022-10-18', '11:49 AM', '2022-10-18', '11:49 AM', '', '826707.jpg'),
(111, '/static/image/Attachment/1088_6slmOjx', 'Lead', 77, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', '1088'),
(113, '/static/image/Attachment/1666157982.827039video.mp4', 'Lead', 80, '19-10-2022', '11:49 AM', '19-10-2022', '11:49 AM', 'test', '1666157982.827039video.mp4'),
(114, '/static/image/Attachment/1666158270.570078video.mp4', 'Lead', 81, '19-10-2022', '11:49 AM', '19-10-2022', '11:49 AM', 'test', '1666158270.570078video.mp4'),
(115, '/static/image/Attachment/peakpx(1).jpg', 'Lead', 82, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', 'peakpx(1).jpg'),
(116, '/static/image/Attachment/images%20(1)_1662926193274.jpeg', 'Lead', 83, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', 'images (1)_1662926193274.jpeg'),
(117, '/static/image/Attachment/IMG_20221018_230052.jpg', 'Lead', 84, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', 'IMG_20221018_230052.jpg'),
(118, '/static/image/Attachment/1666159615.9326282video.mp4', 'Lead', 85, '19-10-2022', '11:49 AM', '19-10-2022', '11:49 AM', 'test', '1666159615.9326282video.mp4'),
(119, '/static/image/Attachment/VID-20221018-WA0005.mp4', 'Lead', 86, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', 'VID-20221018-WA0005.mp4'),
(120, '/static/image/Attachment/1666161065.289279image.jpg', 'Lead', 87, '19-10-2022', '11:49 AM', '19-10-2022', '11:49 AM', 'test', '1666161065.289279image.jpg'),
(121, '/static/image/Attachment/1666161162.550095image.jpg', 'Lead', 88, '19-10-2022', '11:49 AM', '19-10-2022', '11:49 AM', 'test', '1666161162.550095image.jpg'),
(122, '/static/image/Attachment/indologo_U2XZmeb.png', 'Lead', 88, '2022-10-19', '12:07:04 PM', '2022-10-19', '12:07:04 PM', 'test', 'indologo.png'),
(123, '/static/image/Attachment/logos_youtube-icon_ALT0Pt9.png', 'Lead', 88, '2022-10-19', '12:07:04 PM', '2022-10-19', '12:07:04 PM', 'testfd', 'logos_youtube-icon.png'),
(124, '/static/image/Attachment/indologo_Emj4X9w.png', 'Lead', 89, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', 'bjnkm', 'indologo.png'),
(125, '/static/image/Attachment/Group%20238290.png', 'Lead', 89, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', 'bjnkm', 'Group 238290.png'),
(126, '/static/image/Attachment/IMG_20221018_230117.jpg', 'Lead', 90, '2022-10-19', '11:49 AM', '2022-10-19', '11:49 AM', '', 'IMG_20221018_230117.jpg'),
(127, '/static/image/Attachment/quotation_gD7FUo2_BIvMEXd.png', 'Project', 28, '2022-11-02', '11:30:30 AM', '2022-11-02', '11:30:30 AM', '', ''),
(128, '/static/image/Attachment/ce749ccf-a15c-46e3-8430-ed74573d29b1.jpg', 'Project', 29, '02-11-2022', '11:51:40 AM', '02-11-2022', '11:51:40 AM', '', 'ce749ccf-a15c-46e3-8430-ed74573d29b1.jpg'),
(129, '/static/image/Attachment/Cinntra-%20Bridge%20Sales%20Application-%20User%20Manual.docx', 'Lead', 91, '2022-11-02', '10:55 AM', '2022-11-02', '10:55 AM', 'Data File', 'Cinntra- Bridge Sales Application- User Manual.docx'),
(130, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_UrQpWsN_MdkYryd.xlsx', 'Lead', 91, '2022-11-02', '10:55 AM', '2022-11-02', '10:55 AM', 'Data File', 'SALE Module Discussion (2)_UrQpWsN.xlsx'),
(131, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_ziHSDUo.xlsx', 'Project', 30, '2022-11-02', '6:48:25 PM', '2022-11-02', '6:48:25 PM', '', ''),
(133, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)%20(1)_C3FtP8U.xlsx', 'Lead', 92, '2022-11-03', '10:55 AM', '2022-11-03', '10:55 AM', 'Sales Documents', 'SALE Module Discussion (2) (1).xlsx'),
(134, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_UrQpWsN_BmiyL73.xlsx', 'Opportunity', 14, '2022-11-03', '11:27:39 AM', '2022-11-03', '11:27:39 AM', 'Sales Doc', 'SALE Module Discussion (2)_UrQpWsN.xlsx'),
(135, '/static/image/Attachment/iTunes%20Library.itl', 'Project', 34, '2022-11-04', '1:09:06 PM', '2022-11-04', '1:09:06 PM', '', ''),
(136, '/static/image/Attachment/data_import.xlsx', 'Quotation', 71, '2022-11-7', '12:31:11 PM', '2022-11-7', '12:31:11 PM', 'dfghjkl', 'data_import.xlsx'),
(137, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_UrQpWsN_dQJWENX.xlsx', 'Lead', 96, '2022-11-07', '05:52 AM', '2022-11-07', '05:52 AM', 'Projection Doc', 'SALE Module Discussion (2)_UrQpWsN.xlsx'),
(138, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_QJjNjcf.xlsx', 'Project', 36, '2022-11-07', '3:24:52 PM', '2022-11-07', '3:24:52 PM', '', ''),
(139, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)%20(1)%20(1).xlsx', 'Opportunity', 26, '2022-11-07', '3:28:51 PM', '2022-11-07', '3:28:51 PM', 'Sales Doc.', 'SALE Module Discussion (2) (1) (1).xlsx'),
(140, '/static/image/Attachment/SALE%20Module%20Discussion%20(2)_UrQpWsN_VXbVXiA.xlsx', 'Quotation', 72, '2022-11-07', '3:33:33 PM', '2022-11-07', '3:33:33 PM', 'Projection Doc', 'SALE Module Discussion (2)_UrQpWsN.xlsx'),
(141, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf', 'Order', 55, '2022-11-08', '12:17:02 PM', '2022-11-08', '12:17:02 PM', 'test', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(142, '/static/image/Attachment/order.html', 'Order', 55, '2022-11-08', '12:17:02 PM', '2022-11-08', '12:17:02 PM', 'test', 'order.html'),
(143, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_1MniQ4d.pdf', 'Order', 56, '2022-11-08', '2:35:45 PM', '2022-11-08', '2:35:45 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(144, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_Vd4BXN2.pdf', 'Order', 57, '2022-11-08', '2:38:23 PM', '2022-11-08', '2:38:23 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(145, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_7lplfrj.pdf', 'Order', 58, '2022-11-08', '3:16:15 PM', '2022-11-08', '3:16:15 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(146, '/static/image/Attachment/SALE%20Module%20Discussion.xlsx', 'Order', 59, '2022-11-08', '3:25:42 PM', '2022-11-08', '3:25:42 PM', '', 'SALE Module Discussion.xlsx'),
(147, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_zMoUxao.pdf', 'Order', 60, '2022-11-08', '3:58:39 PM', '2022-11-08', '3:58:39 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(148, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_40p9Gg3.pdf', 'Order', 61, '2022-11-08', '4:06:08 PM', '2022-11-08', '4:06:08 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(149, '/static/image/Attachment/Order_vision.html', 'Order', 62, '2022-11-08', '4:09:38 PM', '2022-11-08', '4:09:38 PM', '', 'Order_vision.html'),
(150, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_DBw7pcZ.pdf', 'Order', 63, '2022-11-08', '4:23:38 PM', '2022-11-08', '4:23:38 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(151, '/static/image/Attachment/IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022_tYmVGOV.pdf', 'Order', 66, '2022-11-08', '5:29:16 PM', '2022-11-08', '5:29:16 PM', '', 'IGNOU-Date-Sheet-Dec-2022-Updated-on-1st-Nov-2022.pdf'),
(152, '/static/image/Attachment/Order_vision_8U713kh.html', 'Order', 67, '2022-11-08', '5:45:17 PM', '2022-11-08', '5:45:17 PM', '', 'Order_vision.html'),
(153, '/static/image/Attachment/order_k51eD4Y.html', 'Order', 68, '2022-11-08', '5:49:24 PM', '2022-11-08', '5:49:24 PM', '', 'order.html'),
(154, '/static/image/Attachment/order_ilIbNm8.html', 'Order', 69, '2022-11-08', '5:51:32 PM', '2022-11-08', '5:51:32 PM', '', 'order.html'),
(155, '/static/image/Attachment/Screenshot_20221105-223952_PhonePe.jpg', 'Lead', 97, '2022-11-09', '01:51 PM', '2022-11-09', '01:51 PM', '', 'Screenshot_20221105-223952_PhonePe.jpg'),
(156, '/static/image/Attachment/20221031_214355.jpg', 'Lead', 98, '2022-11-09', '09:24 AM', '2022-11-09', '09:24 AM', '', '20221031_214355.jpg'),
(157, '/static/image/Attachment/dash-logo.png', 'Project', 37, '2022-11-11', '3:19:33 PM', '2022-11-11', '3:19:33 PM', '', ''),
(158, '/static/image/Attachment/data_import_2nxMqqV.xlsx', 'Project', 37, '14-11-2022', '10:29:31 AM', '14-11-2022', '10:29:31 AM', '', 'data_import.xlsx'),
(159, '/static/image/Attachment/indologo_aSFBwYH.png', 'Project', 38, '2022-11-14', '12:19:30 PM', '2022-11-14', '12:19:30 PM', '', ''),
(163, '/static/image/Attachment/dash-logo_zIdsaVu.png', 'Project', 44, '14-11-2022', '3:13:17 PM', '14-11-2022', '3:13:17 PM', '', 'dash-logo.png'),
(164, '/static/image/Attachment/dash-logo_naBSQX8.png', 'Project', 44, '14-11-2022', '3:35:40 PM', '14-11-2022', '3:35:40 PM', '', 'dash-logo.png'),
(165, '/static/image/Attachment/dash-logo_rLCoIFo.png', 'Project', 47, '14-11-2022', '6:40:40 PM', '14-11-2022', '6:40:40 PM', 'testing cinntra', 'dash-logo.png'),
(166, '/static/image/Attachment/Bizz%20Analyst%20Features.xlsx', 'Lead', 100, '2022-11-15', '11:30 AM', '2022-11-15', '11:30 AM', '', 'Bizz Analyst Features.xlsx'),
(167, '/static/image/Attachment/Required%20fields.docx', 'Project', 48, '2022-11-15', '11:25:30 AM', '2022-11-15', '11:25:30 AM', '', ''),
(168, '/static/image/Attachment/todyas%20taks.txt', 'Project', 48, '15-11-2022', '11:37:33 AM', '15-11-2022', '11:37:33 AM', 'Adhar Card', 'todyas taks.txt'),
(169, '/static/image/Attachment/Quotation_GaRY9Wi.pdf', 'Opportunity', 29, '2022-11-15', '11:57:59 AM', '2022-11-15', '11:57:59 AM', 'Quote', 'Quotation.pdf'),
(170, '/static/image/Attachment/order_CI75qMM.html', 'Opportunity', 32, '2022-11-17', '10:20:50 AM', '2022-11-17', '10:20:50 AM', 'New Caption', 'order.html'),
(171, '/static/image/Attachment/quotation.html', 'Opportunity', 32, '2022-11-17', '10:20:50 AM', '2022-11-17', '10:20:50 AM', 'New Caption', 'quotation.html'),
(172, '/static/image/Attachment/order_lgkBfPL.html', 'Opportunity', 33, '2022-11-17', '10:24:18 AM', '2022-11-17', '10:24:18 AM', 'New Caption', 'order.html'),
(173, '/static/image/Attachment/quotation_s4gQr10.html', 'Opportunity', 33, '2022-11-17', '10:24:18 AM', '2022-11-17', '10:24:18 AM', 'New Caption', 'quotation.html'),
(174, '/static/image/Attachment/IMG-20221117-WA0001.jpg', 'Opportunity', 34, '2022-11-17', '11:26 AM', '2022-11-17', '11:26 AM', '', 'IMG-20221117-WA0001.jpg'),
(175, '/static/image/Attachment/IMG-20221117-WA0001_SfbxA4Q.jpg', 'Opportunity', 35, '2022-11-17', '11:29 AM', '2022-11-17', '11:29 AM', '', 'IMG-20221117-WA0001.jpg'),
(176, '/static/image/Attachment/IMG-20221117-WA0000.jpg', 'Lead', 101, '2022-11-17', '06:40 AM', '2022-11-17', '06:40 AM', '', 'IMG-20221117-WA0000.jpg'),
(177, '/static/image/Attachment/IMG-20221117-WA0001_FKKcd0J.jpg', 'Lead', 102, '2022-11-17', '06:40 AM', '2022-11-17', '06:40 AM', '', 'IMG-20221117-WA0001.jpg'),
(178, '/static/image/Attachment/IMG-20221117-WA0002.jpg', 'Lead', 102, '2022-11-17', '06:40 AM', '2022-11-17', '06:40 AM', '', 'IMG-20221117-WA0002.jpg'),
(179, '/static/image/Attachment/IMG-20221116-WA0002.jpg', 'Lead', 103, '2022-11-17', '06:40 AM', '2022-11-17', '06:40 AM', '', 'IMG-20221116-WA0002.jpg'),
(180, '/static/image/Attachment/IMG-20221116-WA0002_M57Hoel.jpg', 'Lead', 103, '2022-11-17', '06:40 AM', '2022-11-17', '06:40 AM', '', 'IMG-20221116-WA0002.jpg'),
(181, '/static/image/Attachment/indologo_30D7CXn.png', 'Lead', 103, '2022-11-17', '12:42:01 PM', '2022-11-17', '12:42:01 PM', 'xaz', 'indologo.png'),
(182, '/static/image/Attachment/Group%20238285.svg', 'Lead', 103, '2022-11-17', '3:33:03 PM', '2022-11-17', '3:33:03 PM', 'testtg', 'Group 238285.svg'),
(183, '/static/image/Attachment/1088_6slmOjx_kOtnkap', 'Quotation', 80, '2022-11-21', '3:50:18 PM', '2022-11-21', '3:50:18 PM', '', '1088_6slmOjx'),
(184, '/static/image/Attachment/826709_1sWUCZA', 'Quotation', 80, '2022-11-21', '3:50:18 PM', '2022-11-21', '3:50:18 PM', '', '826709'),
(185, '/static/image/Attachment/1088_6slmOjx_0vaS50H', 'Quotation', 81, '2022-11-21', '3:55:08 PM', '2022-11-21', '3:55:08 PM', '', '1088_6slmOjx'),
(186, '/static/image/Attachment/826709_QJMUQKa', 'Quotation', 81, '2022-11-21', '3:55:08 PM', '2022-11-21', '3:55:08 PM', '', '826709');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add chatter', 7, 'add_chatter'),
(26, 'Can change chatter', 7, 'change_chatter'),
(27, 'Can delete chatter', 7, 'delete_chatter'),
(28, 'Can view chatter', 7, 'view_chatter'),
(29, 'Can add lead item', 8, 'add_leaditem'),
(30, 'Can change lead item', 8, 'change_leaditem'),
(31, 'Can delete lead item', 8, 'delete_leaditem'),
(32, 'Can view lead item', 8, 'view_leaditem'),
(33, 'Can add source', 9, 'add_source'),
(34, 'Can change source', 9, 'change_source'),
(35, 'Can delete source', 9, 'delete_source'),
(36, 'Can view source', 9, 'view_source'),
(37, 'Can add type', 10, 'add_type'),
(38, 'Can change type', 10, 'change_type'),
(39, 'Can delete type', 10, 'delete_type'),
(40, 'Can view type', 10, 'view_type'),
(41, 'Can add lead', 11, 'add_lead'),
(42, 'Can change lead', 11, 'change_lead'),
(43, 'Can delete lead', 11, 'delete_lead'),
(44, 'Can view lead', 11, 'view_lead'),
(45, 'Can add employee', 12, 'add_employee'),
(46, 'Can change employee', 12, 'change_employee'),
(47, 'Can delete employee', 12, 'delete_employee'),
(48, 'Can view employee', 12, 'view_employee'),
(49, 'Can add targetyr', 13, 'add_targetyr'),
(50, 'Can change targetyr', 13, 'change_targetyr'),
(51, 'Can delete targetyr', 13, 'delete_targetyr'),
(52, 'Can view targetyr', 13, 'view_targetyr'),
(53, 'Can add targetqty', 14, 'add_targetqty'),
(54, 'Can change targetqty', 14, 'change_targetqty'),
(55, 'Can delete targetqty', 14, 'delete_targetqty'),
(56, 'Can view targetqty', 14, 'view_targetqty'),
(57, 'Can add target', 15, 'add_target'),
(58, 'Can change target', 15, 'change_target'),
(59, 'Can delete target', 15, 'delete_target'),
(60, 'Can view target', 15, 'view_target'),
(61, 'Can add branch', 16, 'add_branch'),
(62, 'Can change branch', 16, 'change_branch'),
(63, 'Can delete branch', 16, 'delete_branch'),
(64, 'Can view branch', 16, 'view_branch'),
(65, 'Can add company', 17, 'add_company'),
(66, 'Can change company', 17, 'change_company'),
(67, 'Can delete company', 17, 'delete_company'),
(68, 'Can view company', 17, 'view_company'),
(69, 'Can add branch', 18, 'add_branch'),
(70, 'Can change branch', 18, 'change_branch'),
(71, 'Can delete branch', 18, 'delete_branch'),
(72, 'Can view branch', 18, 'view_branch'),
(73, 'Can add line', 19, 'add_line'),
(74, 'Can change line', 19, 'change_line'),
(75, 'Can delete line', 19, 'delete_line'),
(76, 'Can view line', 19, 'view_line'),
(77, 'Can add opp item', 20, 'add_oppitem'),
(78, 'Can change opp item', 20, 'change_oppitem'),
(79, 'Can delete opp item', 20, 'delete_oppitem'),
(80, 'Can view opp item', 20, 'view_oppitem'),
(81, 'Can add opportunity', 21, 'add_opportunity'),
(82, 'Can change opportunity', 21, 'change_opportunity'),
(83, 'Can delete opportunity', 21, 'delete_opportunity'),
(84, 'Can view opportunity', 21, 'view_opportunity'),
(85, 'Can add stage', 22, 'add_stage'),
(86, 'Can change stage', 22, 'change_stage'),
(87, 'Can delete stage', 22, 'delete_stage'),
(88, 'Can view stage', 22, 'view_stage'),
(89, 'Can add static stage', 23, 'add_staticstage'),
(90, 'Can change static stage', 23, 'change_staticstage'),
(91, 'Can delete static stage', 23, 'delete_staticstage'),
(92, 'Can view static stage', 23, 'view_staticstage'),
(93, 'Can add bp addresses', 24, 'add_bpaddresses'),
(94, 'Can change bp addresses', 24, 'change_bpaddresses'),
(95, 'Can delete bp addresses', 24, 'delete_bpaddresses'),
(96, 'Can view bp addresses', 24, 'view_bpaddresses'),
(97, 'Can add bp branch', 25, 'add_bpbranch'),
(98, 'Can change bp branch', 25, 'change_bpbranch'),
(99, 'Can delete bp branch', 25, 'delete_bpbranch'),
(100, 'Can view bp branch', 25, 'view_bpbranch'),
(101, 'Can add bp currency', 26, 'add_bpcurrency'),
(102, 'Can change bp currency', 26, 'change_bpcurrency'),
(103, 'Can delete bp currency', 26, 'delete_bpcurrency'),
(104, 'Can view bp currency', 26, 'view_bpcurrency'),
(105, 'Can add bp department', 27, 'add_bpdepartment'),
(106, 'Can change bp department', 27, 'change_bpdepartment'),
(107, 'Can delete bp department', 27, 'delete_bpdepartment'),
(108, 'Can view bp department', 27, 'view_bpdepartment'),
(109, 'Can add bp employee', 28, 'add_bpemployee'),
(110, 'Can change bp employee', 28, 'change_bpemployee'),
(111, 'Can delete bp employee', 28, 'delete_bpemployee'),
(112, 'Can view bp employee', 28, 'view_bpemployee'),
(113, 'Can add bp position', 29, 'add_bpposition'),
(114, 'Can change bp position', 29, 'change_bpposition'),
(115, 'Can delete bp position', 29, 'delete_bpposition'),
(116, 'Can view bp position', 29, 'view_bpposition'),
(117, 'Can add business partner', 30, 'add_businesspartner'),
(118, 'Can change business partner', 30, 'change_businesspartner'),
(119, 'Can delete business partner', 30, 'delete_businesspartner'),
(120, 'Can view business partner', 30, 'view_businesspartner'),
(121, 'Can add activity', 31, 'add_activity'),
(122, 'Can change activity', 31, 'change_activity'),
(123, 'Can delete activity', 31, 'delete_activity'),
(124, 'Can view activity', 31, 'view_activity'),
(125, 'Can add chatter', 32, 'add_chatter'),
(126, 'Can change chatter', 32, 'change_chatter'),
(127, 'Can delete chatter', 32, 'delete_chatter'),
(128, 'Can view chatter', 32, 'view_chatter'),
(129, 'Can add maps', 33, 'add_maps'),
(130, 'Can change maps', 33, 'change_maps'),
(131, 'Can delete maps', 33, 'delete_maps'),
(132, 'Can view maps', 33, 'view_maps'),
(133, 'Can add countries', 34, 'add_countries'),
(134, 'Can change countries', 34, 'change_countries'),
(135, 'Can delete countries', 34, 'delete_countries'),
(136, 'Can view countries', 34, 'view_countries'),
(137, 'Can add states', 35, 'add_states'),
(138, 'Can change states', 35, 'change_states'),
(139, 'Can delete states', 35, 'delete_states'),
(140, 'Can view states', 35, 'view_states'),
(141, 'Can add industries', 36, 'add_industries'),
(142, 'Can change industries', 36, 'change_industries'),
(143, 'Can delete industries', 36, 'delete_industries'),
(144, 'Can view industries', 36, 'view_industries'),
(145, 'Can add payment terms types', 37, 'add_paymenttermstypes'),
(146, 'Can change payment terms types', 37, 'change_paymenttermstypes'),
(147, 'Can delete payment terms types', 37, 'delete_paymenttermstypes'),
(148, 'Can view payment terms types', 37, 'view_paymenttermstypes'),
(149, 'Can add address extension', 38, 'add_addressextension'),
(150, 'Can change address extension', 38, 'change_addressextension'),
(151, 'Can delete address extension', 38, 'delete_addressextension'),
(152, 'Can view address extension', 38, 'view_addressextension'),
(153, 'Can add app slave', 39, 'add_appslave'),
(154, 'Can change app slave', 39, 'change_appslave'),
(155, 'Can delete app slave', 39, 'delete_appslave'),
(156, 'Can view app slave', 39, 'view_appslave'),
(157, 'Can add document lines', 40, 'add_documentlines'),
(158, 'Can change document lines', 40, 'change_documentlines'),
(159, 'Can delete document lines', 40, 'delete_documentlines'),
(160, 'Can view document lines', 40, 'view_documentlines'),
(161, 'Can add quotation', 41, 'add_quotation'),
(162, 'Can change quotation', 41, 'change_quotation'),
(163, 'Can delete quotation', 41, 'delete_quotation'),
(164, 'Can view quotation', 41, 'view_quotation'),
(165, 'Can add address extension', 42, 'add_addressextension'),
(166, 'Can change address extension', 42, 'change_addressextension'),
(167, 'Can delete address extension', 42, 'delete_addressextension'),
(168, 'Can view address extension', 42, 'view_addressextension'),
(169, 'Can add document lines', 43, 'add_documentlines'),
(170, 'Can change document lines', 43, 'change_documentlines'),
(171, 'Can delete document lines', 43, 'delete_documentlines'),
(172, 'Can view document lines', 43, 'view_documentlines'),
(173, 'Can add order', 44, 'add_order'),
(174, 'Can change order', 44, 'change_order'),
(175, 'Can delete order', 44, 'delete_order'),
(176, 'Can view order', 44, 'view_order'),
(177, 'Can add department', 45, 'add_department'),
(178, 'Can change department', 45, 'change_department'),
(179, 'Can delete department', 45, 'delete_department'),
(180, 'Can view department', 45, 'view_department'),
(181, 'Can add tax', 46, 'add_tax'),
(182, 'Can change tax', 46, 'change_tax'),
(183, 'Can delete tax', 46, 'delete_tax'),
(184, 'Can view tax', 46, 'view_tax'),
(185, 'Can add item', 47, 'add_item'),
(186, 'Can change item', 47, 'change_item'),
(187, 'Can delete item', 47, 'delete_item'),
(188, 'Can view item', 47, 'view_item'),
(189, 'Can add category', 48, 'add_category'),
(190, 'Can change category', 48, 'change_category'),
(191, 'Can delete category', 48, 'delete_category'),
(192, 'Can view category', 48, 'view_category'),
(193, 'Can add notification', 49, 'add_notification'),
(194, 'Can change notification', 49, 'change_notification'),
(195, 'Can delete notification', 49, 'delete_notification'),
(196, 'Can view notification', 49, 'view_notification'),
(197, 'Can add corrigendum list', 50, 'add_corrigendumlist'),
(198, 'Can change corrigendum list', 50, 'change_corrigendumlist'),
(199, 'Can delete corrigendum list', 50, 'delete_corrigendumlist'),
(200, 'Can view corrigendum list', 50, 'view_corrigendumlist'),
(201, 'Can add cover detail', 51, 'add_coverdetail'),
(202, 'Can change cover detail', 51, 'change_coverdetail'),
(203, 'Can delete cover detail', 51, 'delete_coverdetail'),
(204, 'Can view cover detail', 51, 'view_coverdetail'),
(205, 'Can add critcal dates', 52, 'add_critcaldates'),
(206, 'Can change critcal dates', 52, 'change_critcaldates'),
(207, 'Can delete critcal dates', 52, 'delete_critcaldates'),
(208, 'Can view critcal dates', 52, 'view_critcaldates'),
(209, 'Can add documents', 53, 'add_documents'),
(210, 'Can change documents', 53, 'change_documents'),
(211, 'Can delete documents', 53, 'delete_documents'),
(212, 'Can view documents', 53, 'view_documents'),
(213, 'Can add lowest one', 54, 'add_lowestone'),
(214, 'Can change lowest one', 54, 'change_lowestone'),
(215, 'Can delete lowest one', 54, 'delete_lowestone'),
(216, 'Can view lowest one', 54, 'view_lowestone'),
(217, 'Can add payment instrument', 55, 'add_paymentinstrument'),
(218, 'Can change payment instrument', 55, 'change_paymentinstrument'),
(219, 'Can delete payment instrument', 55, 'delete_paymentinstrument'),
(220, 'Can view payment instrument', 55, 'view_paymentinstrument'),
(221, 'Can add technical opening', 56, 'add_technicalopening'),
(222, 'Can change technical opening', 56, 'change_technicalopening'),
(223, 'Can delete technical opening', 56, 'delete_technicalopening'),
(224, 'Can view technical opening', 56, 'view_technicalopening'),
(225, 'Can add tender', 57, 'add_tender'),
(226, 'Can change tender', 57, 'change_tender'),
(227, 'Can delete tender', 57, 'delete_tender'),
(228, 'Can view tender', 57, 'view_tender'),
(229, 'Can add tender opening', 58, 'add_tenderopening'),
(230, 'Can change tender opening', 58, 'change_tenderopening'),
(231, 'Can delete tender opening', 58, 'delete_tenderopening'),
(232, 'Can view tender opening', 58, 'view_tenderopening'),
(233, 'Can add tender submission', 59, 'add_tendersubmission'),
(234, 'Can change tender submission', 59, 'change_tendersubmission'),
(235, 'Can delete tender submission', 59, 'delete_tendersubmission'),
(236, 'Can view tender submission', 59, 'view_tendersubmission'),
(237, 'Can add ten item', 60, 'add_tenitem'),
(238, 'Can change ten item', 60, 'change_tenitem'),
(239, 'Can delete ten item', 60, 'delete_tenitem'),
(240, 'Can view ten item', 60, 'view_tenitem'),
(241, 'Can add work or item details', 61, 'add_workoritemdetails'),
(242, 'Can change work or item details', 61, 'change_workoritemdetails'),
(243, 'Can delete work or item details', 61, 'delete_workoritemdetails'),
(244, 'Can view work or item details', 61, 'view_workoritemdetails'),
(245, 'Can add address extension', 62, 'add_addressextension'),
(246, 'Can change address extension', 62, 'change_addressextension'),
(247, 'Can delete address extension', 62, 'delete_addressextension'),
(248, 'Can view address extension', 62, 'view_addressextension'),
(249, 'Can add document lines', 63, 'add_documentlines'),
(250, 'Can change document lines', 63, 'change_documentlines'),
(251, 'Can delete document lines', 63, 'delete_documentlines'),
(252, 'Can view document lines', 63, 'view_documentlines'),
(253, 'Can add invoice', 64, 'add_invoice'),
(254, 'Can change invoice', 64, 'change_invoice'),
(255, 'Can delete invoice', 64, 'delete_invoice'),
(256, 'Can view invoice', 64, 'view_invoice'),
(257, 'Can add campaign set', 65, 'add_campaignset'),
(258, 'Can change campaign set', 65, 'change_campaignset'),
(259, 'Can delete campaign set', 65, 'delete_campaignset'),
(260, 'Can view campaign set', 65, 'view_campaignset'),
(261, 'Can add campaign set members', 66, 'add_campaignsetmembers'),
(262, 'Can change campaign set members', 66, 'change_campaignsetmembers'),
(263, 'Can delete campaign set members', 66, 'delete_campaignsetmembers'),
(264, 'Can view campaign set members', 66, 'view_campaignsetmembers'),
(265, 'Can add campaign', 67, 'add_campaign'),
(266, 'Can change campaign', 67, 'change_campaign'),
(267, 'Can delete campaign', 67, 'delete_campaign'),
(268, 'Can view campaign', 67, 'view_campaign'),
(269, 'Can add project', 68, 'add_project'),
(270, 'Can change project', 68, 'change_project'),
(271, 'Can delete project', 68, 'delete_project'),
(272, 'Can view project', 68, 'view_project'),
(273, 'Can add addendum request', 69, 'add_addendumrequest'),
(274, 'Can change addendum request', 69, 'change_addendumrequest'),
(275, 'Can delete addendum request', 69, 'delete_addendumrequest'),
(276, 'Can view addendum request', 69, 'view_addendumrequest'),
(277, 'Can add attachment', 70, 'add_attachment'),
(278, 'Can change attachment', 70, 'change_attachment'),
(279, 'Can delete attachment', 70, 'delete_attachment'),
(280, 'Can view attachment', 70, 'view_attachment'),
(281, 'Can add client bank details', 71, 'add_clientbankdetails'),
(282, 'Can change client bank details', 71, 'change_clientbankdetails'),
(283, 'Can delete client bank details', 71, 'delete_clientbankdetails'),
(284, 'Can view client bank details', 71, 'view_clientbankdetails'),
(285, 'Can add customer code', 72, 'add_customercode'),
(286, 'Can change customer code', 72, 'change_customercode'),
(287, 'Can delete customer code', 72, 'delete_customercode'),
(288, 'Can view customer code', 72, 'view_customercode'),
(289, 'Can add customer group', 73, 'add_customergroup'),
(290, 'Can change customer group', 73, 'change_customergroup'),
(291, 'Can delete customer group', 73, 'delete_customergroup'),
(292, 'Can view customer group', 73, 'view_customergroup'),
(293, 'Can add customer zone', 74, 'add_customerzone'),
(294, 'Can change customer zone', 74, 'change_customerzone'),
(295, 'Can delete customer zone', 74, 'delete_customerzone'),
(296, 'Can view customer zone', 74, 'view_customerzone'),
(297, 'Can add cust code', 75, 'add_custcode'),
(298, 'Can change cust code', 75, 'change_custcode'),
(299, 'Can delete cust code', 75, 'delete_custcode'),
(300, 'Can view cust code', 75, 'view_custcode');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Branch_branch`
--

CREATE TABLE `Branch_branch` (
  `id` bigint NOT NULL,
  `companyId` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` varchar(250) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(35) NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `active` int NOT NULL,
  `timestamp` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpaddresses`
--

CREATE TABLE `BusinessPartner_bpaddresses` (
  `id` bigint NOT NULL,
  `BPID` varchar(50) NOT NULL,
  `BPCode` varchar(50) NOT NULL,
  `AddressName` varchar(100) NOT NULL,
  `Street` varchar(100) NOT NULL,
  `Block` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `ZipCode` varchar(100) NOT NULL,
  `Country` varchar(100) NOT NULL,
  `AddressType` varchar(100) NOT NULL,
  `RowNum` varchar(3) NOT NULL,
  `U_SHPTYP` varchar(100) NOT NULL,
  `U_COUNTRY` varchar(100) NOT NULL,
  `U_STATE` varchar(100) NOT NULL,
  `BillToRemark` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_bpaddresses`
--

INSERT INTO `BusinessPartner_bpaddresses` (`id`, `BPID`, `BPCode`, `AddressName`, `Street`, `Block`, `City`, `State`, `ZipCode`, `Country`, `AddressType`, `RowNum`, `U_SHPTYP`, `U_COUNTRY`, `U_STATE`, `BillToRemark`) VALUES
(4, '4', 'CS00004', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(5, '5', 'CS00005', 'Cinntra', 'dafdsf', '', 'City', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(12, '12', 'CS00012', 'Cinntra', 'dafdsf', '', 'Karol bagh', 'DL', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Delhi', 'Test Remark'),
(13, '13', 'CS00013', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(14, '14', 'CS00014', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(15, '15', 'CS00015', 'Ajanara Heights', 'Ajanara Heights, Crossing Republic', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_BillTo', '0', 'By Road', 'India', 'Uttar Pradesh', ''),
(16, '16', 'CS00016', 'Ajanara Enclave', 'Nana House, Ajanara Enclave, Hoshiarpur', '', 'Hoshiarpur', 'PB', '201301', 'IN', 'bo_BillTo', '0', 'By Courier', 'India', 'Punjab', 'NA'),
(17, '17', 'CS00017', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(18, '18', 'CS00018', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(19, '19', 'CS00019', 'Trends', 'Patel Nagar, Modinagar', '', 'Modinagar', 'UP', '201206', 'IN', 'bo_BillTo', '0', 'By Courier', 'India', 'Uttar Pradesh', ''),
(20, '20', 'CS00020', 'Haldiram & CO.', 'C-119, Sec-59, Hapur', '', 'Hapur', 'UP', '201301', 'IN', 'bo_BillTo', '0', 'By Courier', 'India', 'Uttar Pradesh', 'NA'),
(21, '21', 'CS00021', 'Groffers Stove', 'E-138, Sec-63, Noida', '', 'Noida', 'UP', '201301', 'IN', 'bo_BillTo', '0', '', 'India', 'Uttar Pradesh', 'NA'),
(22, '22', 'CS00022', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(23, '23', 'CS00023', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(24, '24', 'CS00024', 'IBM COMP LTD', '192, Basant Pur Saintli, Muradnagar', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_BillTo', '0', '', 'India', 'Uttar Pradesh', ''),
(25, '25', 'CS00025', 'Wipro Infotech ', 'Wipro Infotech Sec-63, Noida', '', 'Noida', 'UP', '201301', 'IN', 'bo_BillTo', '0', 'By Road', 'India', 'Uttar Pradesh', ''),
(26, '26', 'CS00026', 'Google Inc.', 'Ansari Nagar', '', 'New Delhi', 'GA', '201301', 'IN', 'bo_BillTo', '0', '', 'India', 'Goa', ''),
(27, '27', 'CS00027', 'FIncorp. Arch', 'E-121, FIncorp. Arch', '', 'Noida', 'UP', '201301', 'IN', 'bo_BillTo', '0', '', 'India', 'Uttar Pradesh', ''),
(28, '28', 'CS00028', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(29, '29', 'CS00029', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(30, '30', 'CS00030', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(31, '31', 'CS00031', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(32, '32', 'CS00032', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(33, '33', 'CS00033', 'Jyoti Pest Control', 'C-121, RDC, Ghaziabad', '', 'Ghaziabad', 'UP', '201001', 'IN', 'bo_BillTo', '0', 'By Road', 'India', 'Uttar Pradesh', ''),
(34, '34', 'CS00034', 'MASSAED India Pvt Ltd', 'Hyderabad', '', 'Santanu Sahu', 'TG', '500001', 'IN', 'bo_BillTo', '0', '', 'India', 'Telangana', ''),
(35, '35', 'CS00035', 'Dell Logistics', 'E-138, Dell Logistics', '', 'Noida', 'UP', '201301', 'IN', 'bo_BillTo', '0', '', 'India', 'Uttar Pradesh', ''),
(36, '36', 'CS00036', 'Humdard', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', '', 'Ghaziabad', 'UP', '201003', 'IN', 'bo_BillTo', '0', 'By Road', 'India', 'Uttar Pradesh', ''),
(37, '37', 'CS00037', 'ITC', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_BillTo', '0', 'By Road', 'India', 'Uttar Pradesh', ''),
(38, '38', 'CS00038', 'ITC', 'Ghaziabad', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_BillTo', '0', '', 'India', 'Uttar Pradesh', ''),
(39, '39', 'CS00039', 'ITC', 'Rajnagar Extension', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_BillTo', '0', 'By Courier', 'India', 'Uttar Pradesh', ''),
(40, '40', 'CS00040', 'MASSAED India Pvt Ltd', 'Hyderabad', '', 'Hyderabad', 'TG', '500001', 'IN', 'bo_BillTo', '0', '', 'India', 'Telangana', ''),
(41, '41', 'CS00041', 'testing billing', 'testing', '', 'Ashok Nagar', 'HR', '12342355', 'IN', 'bo_BillTo', '0', '', 'India', 'Haryana', ''),
(42, '43', 'CS00043', 'Shiv Lakhan Textiles', 'acbdefghijklmnopqrstuvwxyz acbdefghijklmnopqrstuvwxyz acbdefghijklmnopqrstuvwxyz', '', 'mumbai', 'MH', '110929', 'IN', 'bo_BillTo', '0', '', 'India', 'Maharashtra', 'acbdefghijklmnopqrstuvwxyz acbdefghijklmnopqrstuvwxyz acbdefghijklmnopqrstuvwxyz'),
(43, '44', 'CS00044', 'Textile Contractor Pvt Ltd', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', '', 'Bhubaneswar', 'OR', '265001', 'IN', 'bo_BillTo', '0', '', 'India', 'Odisha', ''),
(44, '45', 'CS00045', 'Shiv Lakhan Textiles', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(45, '46', 'CS00046', 'Shiv Lakhan Office', 'ewfdsa wqertyuio', '', 'Bhubaneswar', 'KA', '265001', 'IN', 'bo_BillTo', '0', '', 'India', 'Karnataka', ''),
(46, '47', 'CS00047', 'Lucky Traders', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_BillTo', '0', 'By Road', 'India', ' Uttar Pradesh', ''),
(47, '48', 'CS00048', 'ITC', 'test adress', '', 'Ghaziabad', 'UP', '110001', 'IN', 'bo_BillTo', '0', '', 'India', ' Uttar Pradesh', ''),
(48, '49', 'CS00049', 'Lucky Traders', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(49, '50', 'CS00050', 'Cinntra', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(50, '51', 'CS00051', 'Lux Co.', 'HNo. 192, Basant Pur Saintli, Muradnagar', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_BillTo', '0', 'By Road', 'India', ' Uttar Pradesh', ''),
(51, '52', 'CS00052', 'Ankur Santanu Bros & Co.', 'Shaheed Nagar', '', 'Bhubaneshwar', 'OR', '201301', 'IN', 'bo_BillTo', '0', 'By Courier', 'India', ' Odisha', 'wqasdfasdfasdf'),
(52, '53', 'CS00053', 'testing ', 'hdchccdcd', '', 'East Zone', 'DL', '34353432', 'IN', 'bo_BillTo', '0', 'By Sea', 'India', 'Delhi', 'remarks2'),
(53, '54', 'CS00054', 'Ankur Santanu Bros & Co.', 'dafdsf', '', 'Arif', 'JH', '110005', 'IN', 'bo_BillTo', '0', '', 'India', 'Jharkhand', ''),
(54, '55', 'CS00055', 'asdfadfa', 'tewe', '', 'dsfsdcsd', 'HR', '943453', 'IN', 'bo_BillTo', '0', '', 'India', 'Haryana', ''),
(55, '56', 'CS00056', 'Lucky Traders', 'new adas dasdasd asdas', '', 'Muradnagar', 'UP', '645654654555555555', 'IN', 'bo_BillTo', '0', 'By Road', 'India', ' Uttar Pradesh', 'fsd sdsedsffdfdsfd'),
(56, '57', 'CS00057', 'Ankur Santanu Bros & Co.', 'wecsdfsdfsdfdssdf', '', 'Bhubaneshwar', 'OR', '645654654555555552', 'IN', 'bo_BillTo', '0', 'By Air', 'India', ' Odisha', 'sdfsdfcsdcscdfsdfs'),
(57, '58', 'CS00058', 'Ankur Santanu Bros & Co.', 'nwe e shnasd adasdn auisda ', '', 'Bhubaneshwar', 'OR', '645653', 'IN', 'bo_BillTo', '0', 'By Road', 'India', ' Odisha', 'wsfdhisf sdjkfhs kfhsdkfhsjd sdjksdsd');

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpbranch`
--

CREATE TABLE `BusinessPartner_bpbranch` (
  `id` bigint NOT NULL,
  `BPID` varchar(4) NOT NULL,
  `RowNum` varchar(4) NOT NULL,
  `BPCode` varchar(100) NOT NULL,
  `BranchName` varchar(100) NOT NULL,
  `AddressName` varchar(100) NOT NULL,
  `AddressName2` varchar(100) NOT NULL,
  `AddressName3` varchar(100) NOT NULL,
  `BuildingFloorRoom` varchar(100) NOT NULL,
  `Street` varchar(100) NOT NULL,
  `Block` varchar(100) NOT NULL,
  `County` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `ZipCode` varchar(100) NOT NULL,
  `Country` varchar(100) NOT NULL,
  `AddressType` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Fax` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `TaxOffice` varchar(100) NOT NULL,
  `GSTIN` varchar(100) NOT NULL,
  `GstType` varchar(100) NOT NULL,
  `ShippingType` varchar(100) NOT NULL,
  `PaymentTerm` varchar(100) NOT NULL,
  `CurrentBalance` varchar(100) NOT NULL,
  `CreditLimit` varchar(100) NOT NULL,
  `Lat` varchar(100) NOT NULL,
  `Long` varchar(100) NOT NULL,
  `Status` int NOT NULL,
  `Default` int NOT NULL,
  `U_SHPTYP` varchar(100) NOT NULL,
  `U_COUNTRY` varchar(100) NOT NULL,
  `U_STATE` varchar(100) NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL,
  `BranchType` varchar(100) NOT NULL,
  `LandLine` varchar(100) NOT NULL,
  `ShipToRemark` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_bpbranch`
--

INSERT INTO `BusinessPartner_bpbranch` (`id`, `BPID`, `RowNum`, `BPCode`, `BranchName`, `AddressName`, `AddressName2`, `AddressName3`, `BuildingFloorRoom`, `Street`, `Block`, `County`, `City`, `State`, `ZipCode`, `Country`, `AddressType`, `Phone`, `Fax`, `Email`, `TaxOffice`, `GSTIN`, `GstType`, `ShippingType`, `PaymentTerm`, `CurrentBalance`, `CreditLimit`, `Lat`, `Long`, `Status`, `Default`, `U_SHPTYP`, `U_COUNTRY`, `U_STATE`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `BranchType`, `LandLine`, `ShipToRemark`) VALUES
(1, '4', '1', 'CS00004', 'Cinntra', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-09-28', '03:14:47 PM', '2022-09-28', '3:14:47 PM', '', '', ''),
(2, '5', '1', 'CS00005', 'Wepro', 'Cinntra', '', '', '', 'dafdsf', '', '', 'City', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-09-28', '06:31:29 PM', '2022-09-28', '6:31:29 PM', '', '', ''),
(3, '12', '1', 'CS00012', 'Testing Bp', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Karol bagh', 'DL', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Delhi', '2022-09-29', '03:07:44 PM', '2022-09-29', '3:07:44 PM', '', '', 'Test Remark'),
(4, '13', '1', 'CS00013', 'IBM', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '1234567891', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-09-29', '04:02:26 PM', '2022-09-29', '4:02:26 PM', '', '12345', ''),
(5, '14', '1', 'CS00014', 'Testing kithen', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-09-30', '04:53:49 PM', '2022-09-30', '4:53:49 PM', '', '', ''),
(6, '15', '1', 'CS00015', 'Ajanara Heights', 'Ajanara Heights', '', '', '', 'Ajanara Heights, Crossing Republic', '', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', 'Uttar Pradesh', '2022-10-03', '12:54:19 PM', '2022-10-03', '12:54:19 PM', '', '', ''),
(7, '16', '1', 'CS00016', 'Ajanara Enclave', 'Ajanara Enclave', '', '', '', 'Nana House, Ajanara Enclave, Hoshiarpur', '', '', 'Hoshiarpur', 'PB', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Courier', 'India', 'Punjab', '2022-10-03', '03:10:57 PM', '2022-10-03', '3:10:57 PM', '', '', 'NA'),
(8, '', '2', 'CS00016', 'Ajanara group', 'Ajanara group', '', '', '', 'E-567, Tiruvanantapuram, Kerala', '', '', 'Tiruvanantapuram', 'KL', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Kerala', '2022-10-03', '3:20:16 PM', '2022-10-03', '3:20:16 PM', 'Real Estate', '', ''),
(9, '17', '1', 'CS00017', 'Cinntra Test', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-03', '04:58:49 PM', '2022-10-03', '4:58:49 PM', '', '', ''),
(10, '18', '1', 'CS00018', 'Cinntra Test 2', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-03', '05:01:28 PM', '2022-10-03', '5:01:28 PM', '', '', ''),
(11, '19', '1', 'CS00019', 'Trends', 'Trends', '', '', '', 'Patel Nagar, Modinagar', '', '', 'Modinagar', 'UP', '201206', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Courier', 'India', 'Uttar Pradesh', '2022-10-03', '05:17:09 PM', '2022-10-03', '5:17:09 PM', '', '', ''),
(12, '20', '1', 'CS00020', 'Haldiram & CO.', 'Haldiram & CO.', '', '', '', 'C-119, Sec-59, Hapur', '', '', 'Hapur', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Courier', 'India', 'Uttar Pradesh', '2022-10-06', '02:50:39 PM', '2022-10-06', '2:50:39 PM', '', '', 'NA'),
(13, '21', '1', 'CS00021', 'Groffers Stove', 'Groffers Stove', '', '', '', 'E-138, Sec-63, Noida', '', '', 'Noida', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Uttar Pradesh', '2022-10-07', '06:23:46 PM', '2022-10-07', '6:23:46 PM', '', '', 'NA'),
(14, '22', '1', 'CS00022', 'Nimbus Post', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-10', '12:04:38 PM', '2022-10-10', '12:04:38 PM', '', '', ''),
(15, '23', '1', 'CS00023', 'popup', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-10', '02:49:51 PM', '2022-10-10', '2:49:51 PM', '', '', ''),
(16, '24', '1', 'CS00024', 'IBM COMP LTD', 'IBM COMP LTD', '', '', '', '192, Basant Pur Saintli, Muradnagar', '', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Uttar Pradesh', '2022-10-10', '05:25:17 PM', '2022-10-10', '5:25:17 PM', '', '', ''),
(17, '25', '1', 'CS00025', 'Wipro Infotech', 'Wipro Infotech ', '', '', '', 'Wipro Infotech Sec-63, Noida', '', '', 'Noida', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', 'Uttar Pradesh', '2022-10-10', '06:38:23 PM', '2022-10-10', '6:38:23 PM', '', '', ''),
(18, '26', '1', 'CS00026', 'Google Inc.', 'Google Inc.', '', '', '', 'Ansari Nagar', '', '', 'New Delhi', 'GA', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Goa', '2022-10-11', '11:19:45 AM', '2022-10-11', '11:19:45 AM', '', '', ''),
(19, '27', '1', 'CS00027', 'FIncorp. Arch', 'FIncorp. Arch', '', '', '', 'E-121, FIncorp. Arch', '', '', 'Noida', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Uttar Pradesh', '2022-10-11', '11:19:53 AM', '2022-10-11', '11:19:53 AM', '', '', ''),
(20, '28', '1', 'CS00028', 'Dell', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-11', '12:31:17 PM', '2022-10-11', '12:31:17 PM', '', '', ''),
(21, '29', '1', 'CS00029', 'New BP', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-11', '04:15:13 PM', '2022-10-11', '4:15:13 PM', '', '', ''),
(22, '30', '1', 'CS00030', 'NEw bp 2', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-11', '04:18:46 PM', '2022-10-11', '4:18:46 PM', '', '', ''),
(23, '31', '1', 'CS00031', 'New bp 3', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-11', '04:21:26 PM', '2022-10-11', '4:21:26 PM', '', '', ''),
(24, '32', '1', 'CS00032', 'asdf', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-10-11', '05:30:25 PM', '2022-10-11', '5:30:25 PM', '', '', ''),
(25, '33', '1', 'CS00033', 'Jyoti Pest Control', 'Jyoti Pest Control', '', '', '', 'C-121, RDC, Ghaziabad', '', '', 'Ghaziabad', 'UP', '201001', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', 'Uttar Pradesh', '2022-10-11', '06:06:06 PM', '2022-10-11', '6:06:06 PM', '', '', ''),
(26, '34', '1', 'CS00034', 'qwdqdqwd', 'MASSAED India Pvt Ltd', '', '', '', 'Hyderabad', '', '', 'Santanu Sahu', 'TG', '500001', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Telangana', '2022-10-11', '06:35:13 PM', '2022-10-11', '6:35:13 PM', '', '', ''),
(27, '35', '1', 'CS00035', 'Dell Logistics', 'Dell Logistics', '', '', '', 'E-138, Dell Logistics', '', '', 'Noida', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Uttar Pradesh', '2022-10-12', '10:47:22 AM', '2022-10-12', '10:47:22 AM', '', '', ''),
(28, '36', '1', 'CS00036', 'Humdard', 'Humdard', '', '', '', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', '', '', 'Ghaziabad', 'UP', '201003', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', 'Uttar Pradesh', '2022-11-02', '06:07:54 PM', '2022-11-02', '6:07:54 PM', '', '', ''),
(29, '37', '1', 'CS00037', 'ITC', 'ITC', '', '', '', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', '', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', 'Uttar Pradesh', '2022-11-03', '10:59:30 AM', '2022-11-03', '10:59:30 AM', '', '', ''),
(30, '38', '1', 'CS00038', 'Loco Treatment', 'ITC', '', '', '', 'Ghaziabad', '', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Uttar Pradesh', '2022-11-03', '11:04:43 AM', '2022-11-03', '11:04:43 AM', '', '', ''),
(31, '39', '1', 'CS00039', 'Apco Water Architecture', 'ITC', '', '', '', 'Rajnagar Extension', '', '', 'Ghaziabad', 'UP', '201006', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Courier', 'India', 'Uttar Pradesh', '2022-11-03', '11:10:38 AM', '2022-11-03', '11:10:38 AM', '', '', ''),
(32, '40', '1', 'CS00040', 'AGON IT SOLUTION 1233', 'MASSAED India Pvt Ltd', '', '', '', 'Hyderabad', '', '', 'Hyderabad', 'TG', '500001', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Telangana', '2022-11-03', '12:52:28 PM', '2022-11-03', '12:52:28 PM', '', '', ''),
(33, '41', '1', 'CS00041', 'adgfg', 'testing billing', '', '', '', 'testing', '', '', 'Ashok Nagar', 'HR', '12342355', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Haryana', '2022-11-03', '06:10:38 PM', '2022-11-03', '6:10:38 PM', '', '', ''),
(34, '43', '1', 'CS00043', 'Shiv Lakhan Textiles', 'Shiv Lakhan Textiles', '', '', '', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', '', '', 'mumbai', 'MH', '110929', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Maharashtra', '2022-11-04', '12:56:38 PM', '2022-11-04', '12:56:38 PM', '', '', 'qweqweqe'),
(35, '', '2', 'CS00043', 'Shiv Lakhan Office', 'Shiv Lakhan Office', '', '', '', 'Shaheed Nagar', '', '', 'Bhubaneswar', 'OR', '265001', 'IN', 'bo_ShipTo', '23456765432', '', 'Shiv@cinntra.com', '', '23145', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Odisha', '2022-11-04', '1:04:23 PM', '2022-11-04', '1:04:23 PM', 'Corporate Office', '67896789 678', ''),
(36, '44', '1', 'CS00044', 'Textile Contractor Pvt Ltd', 'Textile Contractor Pvt Ltd', '', '', '', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', '', '', 'Bhubaneswar', 'OR', '265001', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Odisha', '2022-11-04', '01:23:00 PM', '2022-11-04', '1:23:00 PM', '', '', ''),
(37, '45', '1', 'CS00045', 'asdfas', 'Shiv Lakhan Textiles', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-11-04', '04:15:08 PM', '2022-11-04', '4:15:08 PM', '', '', ''),
(38, '46', '1', 'CS00046', 'qweqweqweqweqweqw', 'wqerqwerqwerqwer', '', '', '', 'sadfdfasfasdfasdf', '', '', 'delhi', 'DL', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Delhi', '2022-11-04', '05:31:56 PM', '2022-11-04', '5:31:56 PM', '', '', ''),
(39, '', '2', 'CS00046', 'ghfds', 'ghfds', '', '', '', 'east delhi', '', '', 'delhi', 'DL', '110095', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Delhi', '2022-11-04', '8:01:23 PM', '2022-11-04', '8:01:23 PM', '', '', ''),
(40, '47', '1', 'CS00047', 'Lucky Traders', 'Lucky Traders', '', '', '', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', '', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', ' Uttar Pradesh', '2022-11-07', '03:17:58 PM', '2022-11-07', '3:17:58 PM', '', '', ''),
(41, '', '2', 'CS00047', 'Bhumesh', 'Bhumesh', '', '', '', 'Hno. 234, Plot no. 26, Sarsa Colony, Bhuvneshwar', '', '', 'Bhuvneshwar', 'UP', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Uttar Pradesh', '2022-11-07', '4:01:42 PM', '2022-11-07', '4:01:42 PM', 'Branch Office', '', ''),
(42, '48', '1', 'CS00048', 'test company', 'ITC', '', '', '', 'test adress', '', '', 'Ghaziabad', 'UP', '110001', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', ' Uttar Pradesh', '2022-11-08', '05:47:13 PM', '2022-11-08', '5:47:13 PM', '', '', ''),
(43, '49', '1', 'CS00049', 'eqasdfdasf', 'Lucky Traders', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-11-08', '06:21:21 PM', '2022-11-08', '6:21:21 PM', '', '', ''),
(44, '', '3', 'CS00043', 'dfghjkl.', 'dfghjkl.', '', '', '', 'Hyderabad', '', '', 'Hyderabad', 'UP', '500001', 'IN', 'bo_ShipTo', '08018762164', '', 'giet11aei014@gmail.com', '', '', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Uttar Pradesh', '2022-11-10', '10:48:05 AM', '2022-11-10', '10:48:05 AM', 'Factory', 'India', ''),
(45, '50', '1', 'CS00050', 'NEw com', 'Cinntra', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-11-11', '05:38:09 PM', '2022-11-11', '5:38:09 PM', '', '', ''),
(46, '51', '1', 'CS00051', 'Lux Co.', 'Lux Co.', '', '', '', 'HNo. 192, Basant Pur Saintli, Muradnagar', '', '', 'Muradnagar', 'UP', '201206', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', ' Uttar Pradesh', '2022-11-14', '06:39:36 PM', '2022-11-14', '6:39:36 PM', '', '', ''),
(47, '52', '1', 'CS00052', 'Ankur Santanu Bros & Co.', 'Ankur Santanu Bros & Co.', '', '', '', 'Shaheed Nagar', '', '', 'Bhubaneshwar', 'OR', '201301', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', ' Odisha', '2022-11-15', '11:11:38 AM', '2022-11-15', '11:11:38 AM', '', '', ''),
(48, '', '2', 'CS00052', 'Supertech Pvt Ltd', 'Supertech Pvt Ltd', '', '', '', 'Sasri Street', '', '', 'Gudari', 'OR', '765026', 'IN', 'bo_ShipTo', '08018762190', '', 'shantanu150@gmail.com', '', '09AGCC8931819', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Odisha', '2022-11-15', '11:22:06 AM', '2022-11-15', '11:22:06 AM', 'Factory', 'India', ''),
(49, '53', '1', 'CS00053', 'werdgfff', 'testing ', '', '', '', 'hdchccdcd', '', '', 'East Zone', 'DL', '34353432', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Sea', 'India', 'Delhi', '2022-11-15', '11:08:11 AM', '2022-11-15', '11:08:11 AM', '', '', 'remarks2'),
(50, '54', '1', 'CS00054', 'dfggfd', 'Ankur Santanu Bros & Co.', '', '', '', 'dafdsf', '', '', 'Arif', 'JH', '110005', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Jharkhand', '2022-11-15', '11:31:02 AM', '2022-11-15', '11:31:02 AM', '', '', ''),
(51, '55', '1', 'CS00055', 'sxgcgvhjb ', 'asdfadfa', '', '', '', 'tewe', '', '', 'dsfsdcsd', 'HR', '943453', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, '', 'India', 'Haryana', '2022-11-15', '12:00:02 PM', '2022-11-15', '12:00:02 PM', '', '', ''),
(52, '', '2', 'CS00055', 'reaer', 'reaer', '', '', '', 'fdsdf', '', '', 'trersrt', 'GA', '32424234', 'IN', 'bo_ShipTo', '4342', '', 'test@ff.vl', '', '534323454532', '', '', '', '', '', '', '', 1, 0, '', ' India', ' Goa', '2022-11-15', '2:48:57 PM', '2022-11-15', '2:48:57 PM', '', '45453', ''),
(53, '55', '3', 'CS00055', '', 'test', '', '', '', 'test', '', '', '', 'GA', '235689', 'IN', 'bo_ShipTo', '935488675', '', 'testing@gmail.com', '', 'TESY45466', '', '', '', '', '', '15.299326499999998', '74.12399599999999', 1, 0, '', 'India', 'Goa', '2022-11-15', '03:26 pm', '2022-11-15', '03:26 pm', 'Corporate Office', '2356896', ''),
(54, '56', '1', 'CS00056', 'naya company', 'Lucky Traders', '', '', '', 'new adas dasdasd asdas', '', '', 'Muradnagar', 'UP', '645654654555555555', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', ' Uttar Pradesh', '2022-11-16', '15:45:13', '2022-11-16', '15:45:13', '', '', 'fsd sdsedsffdfdsfd'),
(55, '57', '1', 'CS00057', 'firse new', 'Ankur Santanu Bros & Co.', '', '', '', 'wecsdfsdfsdfdssdf', '', '', 'Bhubaneshwar', 'OR', '645654654555555552', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Air', 'India', ' Odisha', '2022-11-16', '15:54:06', '2022-11-16', '15:54:06', '', '', 'sdfsdfcsdcscdfsdfs'),
(56, '58', '1', 'CS00058', 'new partner ha', 'Ankur Santanu Bros & Co.', '', '', '', 'nwe e shnasd adasdn auisda ', '', '', 'Bhubaneshwar', 'OR', '645653', 'IN', 'bo_ShipTo', '', '', '', '', '', '', '', '', '', '', '', '', 1, 1, 'By Road', 'India', ' Odisha', '2022-11-17', '17:17:33', '2022-11-17', '17:17:33', '', '', 'wsfdhisf sdjkfhs kfhsdkfhsjd sdjksdsd'),
(57, '', '2', 'CS00058', 'New Branchs', 'New Branchs', '', '', '', 'sdhfskjdfhjskdfjhksfsd dsfsdffs', '', '', 'Mumbai', 'B', '645653', 'AT', 'bo_ShipTo', '9902342224', '', 'sdsadada@sdaa.caa', '', '52342342', '', '', '', '', '', '', '', 1, 0, '', ' Austria', ' Burgenland', '2022-11-18', '10:40:48', '2022-11-18', '10:40:48', 'Branch Office', '0923521442433', ''),
(58, '58', '3', 'CS00058', 'naya branch', 'naya branch', '', '', '', 'New Delhi area India ', '', 'AF', '', 'BAL', '801503', 'AF', 'bo_ShipTo', '9905645678', '', '', '', '', '', 'Head Office', '', '', '', '', '', 1, 0, '', 'Afghanistan', 'Balkh', '2022-11-18', '13:07:38', '2022-11-18', '13:07:38', 'Head Office', '06122281420', '');

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpcurrency`
--

CREATE TABLE `BusinessPartner_bpcurrency` (
  `id` bigint NOT NULL,
  `CurrCode` varchar(20) NOT NULL,
  `CurrName` varchar(50) NOT NULL,
  `DocCurrCod` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpdepartment`
--

CREATE TABLE `BusinessPartner_bpdepartment` (
  `id` bigint NOT NULL,
  `Code` varchar(4) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Description` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpemployee`
--

CREATE TABLE `BusinessPartner_bpemployee` (
  `id` bigint NOT NULL,
  `Title` varchar(100) NOT NULL,
  `FirstName` varchar(100) NOT NULL,
  `MiddleName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Position` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `MobilePhone` varchar(100) NOT NULL,
  `Fax` varchar(100) NOT NULL,
  `E_Mail` varchar(100) NOT NULL,
  `Remarks1` varchar(100) NOT NULL,
  `InternalCode` varchar(100) NOT NULL,
  `DateOfBirth` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Profession` varchar(100) NOT NULL,
  `CardCode` varchar(100) NOT NULL,
  `U_BPID` int NOT NULL,
  `U_BRANCHID` varchar(100) NOT NULL,
  `U_NATIONALTY` varchar(100) NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL,
  `LandlineNo` varchar(100) NOT NULL,
  `LinkProfile` varchar(100) NOT NULL,
  `Alternateno` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_bpemployee`
--

INSERT INTO `BusinessPartner_bpemployee` (`id`, `Title`, `FirstName`, `MiddleName`, `LastName`, `Position`, `Address`, `MobilePhone`, `Fax`, `E_Mail`, `Remarks1`, `InternalCode`, `DateOfBirth`, `Gender`, `Profession`, `CardCode`, `U_BPID`, `U_BRANCHID`, `U_NATIONALTY`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `LandlineNo`, `LinkProfile`, `Alternateno`) VALUES
(4, '', 'Rahulak', '', '', 'Designation', '', '9560763295', '', 'rahul@gmail.com', '', '4', '', '', 'Sales', 'CS00004', 4, '1', '', '2022-09-28', '03:14:47 PM', '2022-09-28', '3:14:47 PM', '', '', ''),
(5, '', 'Rahul', '', '', '', '', '9560763295', '', 'rahul@gmail.com', '', '5', '', '', '', 'CS00005', 5, '2', '', '2022-09-28', '06:31:29 PM', '2022-09-28', '6:31:29 PM', '', '', ''),
(12, '', 'Rahul', '', '', '', '', '9560763295', '', 'rahul@gmail.com', '', '12', '', '', '', 'CS00012', 12, '3', '', '2022-09-29', '03:07:44 PM', '2022-09-29', '3:07:44 PM', '', '', ''),
(13, '', 'Rahul', '', '', '', 'Cinntra', '9560763295', '', 'rahul@gmail.com', '', '13', '', '', 'Commercial', 'CS00013', 13, '4', '', '2022-09-29', '04:02:26 PM', '2022-09-29', '4:02:26 PM', '', '', ''),
(14, '', 'Arif', '', '', '', '', '9711767677', '', '', '', '14', '', '', '', 'CS00014', 14, '5', '', '2022-09-30', '04:53:49 PM', '2022-09-30', '4:53:49 PM', '', '', ''),
(15, '', 'Abishek', '', '', 'Developer', 'Cinntra', '1234512345', '', 'rahul@gmail.com', '', '15', '', '', 'Finance', 'CS00012', 12, '1', 'Indian', '2022-09-30', '4:56:48 PM', '2022-09-30', '4:56:48 PM', '12322112', 'linkdingprod', ''),
(16, '', 'Ankit Verma', '', '', '', '', '9879868968', '', 'ankitverma@gmail.com', '', '16', '', '', '', 'CS00015', 15, '6', '', '2022-10-03', '12:54:19 PM', '2022-10-03', '12:54:19 PM', '', '', ''),
(17, '', 'Abhinav Tyagi', '', '', '', '', '9797979766', '', 'abhinavtyagi@gmail.com', '', '17', '', '', '', 'CS00016', 16, '7', '', '2022-10-03', '03:10:57 PM', '2022-10-03', '3:10:57 PM', '', '', ''),
(18, '', 'Laksay Tyagi', '', '', 'Managing Director', 'Nana House, Ajanara Enclave, Hoshiarpur', '98765678998', '', 'lakshaytyagi@gmail.com', '', '18', '', '', 'Facility', 'CS00016', 16, '1', 'Indian', '2022-10-03', '3:20:16 PM', '2022-10-03', '3:20:16 PM', '', 'Twitter', ''),
(19, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '19', '', '', '', 'CS00017', 17, '9', '', '2022-10-03', '04:58:49 PM', '2022-10-03', '4:58:49 PM', '', '', ''),
(20, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '20', '', '', '', 'CS00018', 18, '10', '', '2022-10-03', '05:01:28 PM', '2022-10-03', '5:01:28 PM', '', '', ''),
(21, '', 'Ashok', '', '', '', '', '9876898076', '', 'ashokch@gmail.com', '', '21', '', '', '', 'CS00019', 19, '11', '', '2022-10-03', '05:17:09 PM', '2022-10-03', '5:17:09 PM', '', '', ''),
(22, '', 'Nitin Tyagi', '', '', '', '', '9879868687', '', 'nitintyagi@gmail.com', '', '22', '', '', '', 'CS00020', 20, '12', '', '2022-10-06', '02:50:39 PM', '2022-10-06', '2:50:39 PM', '', '', ''),
(23, '', 'Chandan Singh', '', '', '', '', '8979879797', '', 'chandansingh@gmail.com', '', '23', '', '', '', 'CS00021', 21, '13', '', '2022-10-07', '06:23:46 PM', '2022-10-07', '6:23:46 PM', '', '', ''),
(24, '', 'Rahul', '', '', '', '', '9560763295', '', 'rahul@gmail.com', '', '24', '', '', '', 'CS00022', 22, '14', '', '2022-10-10', '12:04:38 PM', '2022-10-10', '12:04:38 PM', '', '', ''),
(25, '', 'Abishek', '', '', 'Designation', 'dafdsf', '1234512345', '', 'rahul@gmail.com', '', '25', '', '', 'Sales', 'CS00022', 22, '1', 'Indian', '2022-10-10', '12:44:02 PM', '2022-10-10', '12:44:02 PM', '12322112', 'linkdingprod', ''),
(26, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '26', '', '', '', 'CS00023', 23, '15', '', '2022-10-10', '02:49:51 PM', '2022-10-10', '2:49:51 PM', '', '', '1231231123'),
(27, '', 'Rahul Akarniya', '', '', 'Sales Man', '', '7987987979', '', 'rahul.akarniya@cinntra.co.in', '', '27', '', '', '', 'CS00024', 24, '16', '', '2022-10-10', '05:25:17 PM', '2022-10-10', '5:25:17 PM', '01232-488162', '', ''),
(28, '', 'Bhoopi', '', '', '', '', '9798798780', '', '', '', '28', '', '', '', 'CS00025', 25, '17', '', '2022-10-10', '06:38:23 PM', '2022-10-10', '6:38:23 PM', '', '', ''),
(29, '', 'Santanu Sahu', '', '', '', '', '1231231212', '', '', '', '29', '', '', '', 'CS00026', 26, '18', '', '2022-10-11', '11:19:45 AM', '2022-10-11', '11:19:45 AM', '', '', ''),
(30, '', 'Ankit Sharma', '', '', '', '', '8018762164', '', 'ankit.sharma@gmail.com', '', '30', '', '', '', 'CS00027', 27, '19', '', '2022-10-11', '11:19:53 AM', '2022-10-11', '11:19:53 AM', '', '', '9990989704'),
(31, '', 'Rahul', '', '', '', '', '9560763295', '', 'rahul@gmail.com', '', '31', '', '', '', 'CS00028', 28, '20', '', '2022-10-11', '12:31:17 PM', '2022-10-11', '12:31:17 PM', '', '', ''),
(32, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '32', '', '', '', 'CS00029', 29, '21', '', '2022-10-11', '04:15:13 PM', '2022-10-11', '4:15:13 PM', '', '', ''),
(33, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '33', '', '', '', 'CS00030', 30, '22', '', '2022-10-11', '04:18:46 PM', '2022-10-11', '4:18:46 PM', '', '', ''),
(34, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '34', '', '', '', 'CS00031', 31, '23', '', '2022-10-11', '04:21:26 PM', '2022-10-11', '4:21:26 PM', '', '', ''),
(35, '', 'Rahul', '', '', '', '', '9560763295', '', '', '', '35', '', '', '', 'CS00032', 32, '24', '', '2022-10-11', '05:30:25 PM', '2022-10-11', '5:30:25 PM', '', '', ''),
(36, '', 'Abhi Tyagi', '', '', '', '', '7678858755', '', 'abhi.tyagi@gmail.com', '', '36', '', '', '', 'CS00033', 33, '25', '', '2022-10-11', '06:06:06 PM', '2022-10-11', '6:06:06 PM', '', '', ''),
(37, '', 'Santanu', '', '', '', '', '8018762164', '', 'giet11aei014@gmail.com', '', '37', '', '', '', 'CS00034', 34, '26', '', '2022-10-11', '06:35:13 PM', '2022-10-11', '6:35:13 PM', '', '', ''),
(38, '', 'qdfqfasdasdcsadf', '', '', 'sdfasfdasdfd', '', '9090909000', '', '', '', '38', '', '', '', 'CS00034', 34, '1', 'Indian', '2022-10-11', '6:36:20 PM', '2022-10-11', '6:36:20 PM', '', '', ''),
(39, '', 'rtyuio', '', '', 'sdfghjk', '', '3456456566', '', '', '', '39', '', '', '', 'CS00034', 34, '1', 'Indian', '2022-10-11', '6:37:33 PM', '2022-10-11', '6:37:33 PM', '', '', ''),
(40, '', 'Abishek', '', '', 'Designation', '', '1234512345', '', '', '', '40', '', '', 'Finance', 'CS00034', 34, '1', 'Indian', '2022-10-12', '10:04:01 AM', '2022-10-12', '10:04:01 AM', '', '', ''),
(41, '', 'Abishek', '', '', 'Designation', 'C-121, RDC, Ghaziabad', '1234512345', '', '', '', '41', '', '', 'Commercial', 'CS00033', 33, '25', 'Indian', '2022-10-12', '10:06:09 AM', '2022-10-12', '10:06:09 AM', '', '', ''),
(42, '', 'Ankur Tyagi Ji', '', '', '', '', '8285067282', '', 'ankur.tyagi@cinntra.com', '', '42', '', '', '', 'CS00035', 35, '27', '', '2022-10-12', '10:47:22 AM', '2022-10-12', '10:47:22 AM', '', '', ''),
(43, '', 'Abishek', '', '', 'Designation', 'E-138, Dell Logistics', '1234512345', '', '', '', '43', '', '', 'Sales', 'CS00035', 35, '27', 'Indian', '01-11-2022', '6:13:21 PM', '01-11-2022', '6:13:21 PM', '12322112', '', '1231231123'),
(44, '', 'Suresh Tyagi', '', '', '', '', '7428498286', '', 'suresh.tyagi@gmail.com', '', '44', '', '', '', 'CS00036', 36, '28', '', '2022-11-02', '06:07:54 PM', '2022-11-02', '6:07:54 PM', '', '', ''),
(45, '', 'Sudhir Kumar', '', '', '', '', '9879878678', '', 'sudhir.kumar@gmail.com', '', '45', '', '', '', 'CS00037', 37, '29', '', '2022-11-03', '10:59:30 AM', '2022-11-03', '10:59:30 AM', '', '', ''),
(46, '', 'Sudhir Kumar', '', '', '', '', '9879878678', '', 'sudhir.kumar@gmail.com', '', '46', '', '', '', 'CS00038', 38, '30', '', '2022-11-03', '11:04:43 AM', '2022-11-03', '11:04:43 AM', '', '', ''),
(47, '', 'Sudhir Kumar', '', '', '', '', '9879878678', '', 'sudhir.kumar@gmail.com', '', '47', '', '', '', 'CS00039', 39, '31', '', '2022-11-03', '11:10:38 AM', '2022-11-03', '11:10:38 AM', '', '', ''),
(48, '', 'Santanu', '', '', '', '', '08018762164', '', 'giet11aei014@gmail.com', '', '48', '', '', '', 'CS00040', 40, '32', '', '2022-11-03', '12:52:28 PM', '2022-11-03', '12:52:28 PM', '', '', ''),
(49, '', 'dfsgh', '', '', '', '', '8976565456', '', '', '', '49', '', '', '', 'CS00041', 41, '33', '', '2022-11-03', '06:10:38 PM', '2022-11-03', '6:10:38 PM', '', '', ''),
(51, '', 'Shiv', '', '', '', '', '9090909090', '', 'shiv@cinntra.com', '', '51', '', '', '', 'CS00043', 43, '34', '', '2022-11-04', '12:56:38 PM', '2022-11-04', '12:56:38 PM', '', '', ''),
(52, '', 'Ankur', '', '', 'Marketing', 'Shaheed Nagar', '0909876657', '', 'ankur@cinntra.com', '', '52', '', '', 'Admin', 'CS00043', 43, '35', 'Indian', '2022-11-04', '1:04:23 PM', '2022-11-04', '1:04:23 PM', '1234234324', '', '4543545566'),
(53, '', 'Srimaan', '', '', '', '', '8989898989', '', 'srimaan@cinntra.com', '', '53', '', '', '', 'CS00044', 44, '36', '', '2022-11-04', '01:23:00 PM', '2022-11-04', '1:23:00 PM', '', '', ''),
(54, '', 'Shiv', '', '', '', '', '9090909090', '', 'shiv@cinntra.com', '', '54', '', '', '', 'CS00045', 45, '37', '', '2022-11-04', '04:15:08 PM', '2022-11-04', '4:15:08 PM', '', '', ''),
(55, '', 'Srimaan', '', '', '', '', '8989898989', '', 'srimaan@cinntra.com', '', '55', '', '', '', 'CS00046', 46, '38', '', '2022-11-04', '05:31:56 PM', '2022-11-04', '5:31:56 PM', '', '', ''),
(56, '', 'Samarth Singh', '', '', '', '', '9898798797', '', 'luckysingh@gmail.com', '', '56', '', '', '', 'CS00047', 47, '40', '', '2022-11-07', '03:17:58 PM', '2022-11-07', '3:17:58 PM', '', '', ''),
(57, '', 'Samarth Singh', '', '', 'Sales Executive', 'Hno. 234, Plot no. 26, Sarsa Colony, Bhuvneshwar', '9087657890', '', '', '', '57', '', '', 'Facility', 'CS00047', 47, '41', 'Indian', '2022-11-07', '4:01:42 PM', '2022-11-07', '4:01:42 PM', '01232-488162', '', '7865890098'),
(59, '', 'Sudhir Kumar', '', '', '', '', '9879878678', '', 'sudhir.kumar@gmail.com', '', '59', '', '', '', 'CS00048', 48, '42', '', '2022-11-08', '05:47:13 PM', '2022-11-08', '5:47:13 PM', '', '', ''),
(60, '', 'Lucky Singh', '', '', '', '', '9898798797', '', 'luckysingh@gmail.com', '', '60', '', '', '', 'CS00049', 49, '43', '', '2022-11-08', '06:21:21 PM', '2022-11-08', '6:21:21 PM', '', '', ''),
(61, '', 'Rahul', '', '', 'Develope', 'noida - 1002', '9560763295', '', 'rahul@gmail.com', '', '61', '', '', '', 'CS00050', 50, '45', '', '2022-11-11', '05:38:09 PM', '2022-11-11', '5:38:09 PM', '', '', ''),
(62, '', 'AT', '', '', 'Sales and Quality Manager', '', '6789876567', '', 'at@gmail.com', '', '62', '', '', '', 'CS00051', 51, '46', '', '2022-11-14', '06:39:36 PM', '2022-11-14', '6:39:36 PM', '', '', ''),
(63, '', 'Ankur Sahu', '', '', 'CEO', '', '9310010422', '', 'Ankur@cinntra.com', '', '63', '', '', '', 'CS00052', 52, '47', '', '2022-11-15', '11:11:38 AM', '2022-11-15', '11:11:38 AM', '', '', ''),
(64, '', 'Santanu', '', '', 'IT Manager', 'Sasri Street', '8018762100', '', 'giet11aei014@gmail.com', '', '64', '', '', 'Sales', 'CS00052', 52, '48', 'Indian', '2022-11-15', '11:22:06 AM', '2022-11-15', '11:22:06 AM', '0124345304', 'http://103.234.187.197:4258/#/customer/details/CS00052', '1123121212'),
(65, '', 'Pankaj', '', '', 'dsfggfd', '', '9325878665', '', 'rahul11akarniya@gmail.com', '', '65', '', '', '', 'CS00053', 53, '49', '', '2022-11-15', '11:08:11 AM', '2022-11-15', '11:08:11 AM', '', '', ''),
(66, '', 'Ankur Sahu', '', '', 'Designation', '', '9310010422', '', 'Ankur@cinntra.com', '', '66', '', '', '', 'CS00054', 54, '50', '', '2022-11-15', '11:31:02 AM', '2022-11-15', '11:31:02 AM', '', '', ''),
(67, '', 'vjahdbkj', '', '', ' bdmbkj', '', '9876545609', '', '', '', '67', '', '', '', 'CS00055', 55, '51', '', '2022-11-15', '12:00:02 PM', '2022-11-15', '12:00:02 PM', '', '', ''),
(68, '', 'rearae', '', '', 'njynhbgvfc', 'dafdsf', '6543243212', '', 'rmktmy', '', '68', '', '', 'Sales', 'CS00054', 54, '50', 'Indian', '15-11-2022', '4:03:12 PM', '15-11-2022', '4:03:12 PM', '57858', 'nkhjhj', '9767877677'),
(69, '', 'Testh', '', '', 'Tesgbn', 'tewe', '9356865688', '', 'testing@gmail.com', '', '69', '', '', 'Sales', 'CS00055', 55, '51', 'Indian', '2022-11-15', '06:14 pm', '2022-11-15', '06:14 pm', '5555058088', 'sgytf.cibn', '85258458859'),
(70, '', 'Lucky Singh', '', '', 'tester', '', '9898798797', '', 'luckysingh@gmail.com', '', '70', '', '', '', 'CS00056', 56, '54', '', '2022-11-16', '15:45:13', '2022-11-16', '15:45:13', '', '', ''),
(71, '', 'Ankur Sahu', '', '', 'testerd', '', '9310010422', '', 'Ankur@cinntra.com', '', '71', '', '', '', 'CS00057', 57, '55', '', '2022-11-16', '15:54:06', '2022-11-16', '15:54:06', '', '', ''),
(72, '', 'Ankur Sahu', '', '', 'testerd', '', '9310010422', '', 'Ankur@cinntra.com', '', '72', '', '', '', 'CS00058', 58, '56', '', '2022-11-17', '17:17:33', '2022-11-17', '17:17:33', '', '', ''),
(73, '', 'Kumar', '', '', 'tester', 'nwe e shnasd adasdn auisda', '8210035397', '', 'nayauser@gmail.com', '', '73', '', '', 'Finance', 'CS00058', 58, '56', 'Indian', '2022-11-18', '10:40:48', '2022-11-18', '10:40:48', '06122281420', 'www.facebook.com', '9798775051'),
(74, '', 'Singh', '', '', 'Dveloer', 'NEW DLEEHI INDIA ', '9903432133', '', 'newrus@gmail.com', '', '74', '', '', 'Finance', 'CS00057', 57, '1', 'Indian', '2022-11-18', '12:23:34', '2022-11-18', '12:23:34', '06122281420', 'www.facebook.com', '06122281420');

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_bpposition`
--

CREATE TABLE `BusinessPartner_bpposition` (
  `id` bigint NOT NULL,
  `PositionID` varchar(4) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Description` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_businesspartner`
--

CREATE TABLE `BusinessPartner_businesspartner` (
  `id` bigint NOT NULL,
  `CardCode` varchar(100) NOT NULL,
  `CardName` varchar(100) NOT NULL,
  `Industry` varchar(100) NOT NULL,
  `CardType` varchar(100) NOT NULL,
  `Website` varchar(100) NOT NULL,
  `EmailAddress` varchar(100) NOT NULL,
  `Phone1` varchar(100) NOT NULL,
  `DiscountPercent` varchar(100) NOT NULL,
  `Currency` varchar(100) NOT NULL,
  `IntrestRatePercent` varchar(100) NOT NULL,
  `CommissionPercent` varchar(100) NOT NULL,
  `Notes` varchar(100) NOT NULL,
  `PayTermsGrpCode` varchar(100) NOT NULL,
  `CreditLimit` varchar(100) NOT NULL,
  `AttachmentEntry` varchar(100) NOT NULL,
  `SalesPersonCode` varchar(5) NOT NULL,
  `ContactPerson` varchar(100) NOT NULL,
  `U_LEADID` int NOT NULL,
  `U_LEADNM` varchar(150) NOT NULL,
  `BPAddresses` varchar(100) NOT NULL,
  `U_PARENTACC` varchar(100) NOT NULL,
  `U_BPGRP` varchar(100) NOT NULL,
  `U_CONTOWNR` varchar(100) NOT NULL,
  `U_RATING` varchar(100) NOT NULL,
  `U_TYPE` varchar(100) NOT NULL,
  `U_ANLRVN` varchar(100) NOT NULL,
  `U_CURBAL` varchar(100) NOT NULL,
  `U_ACCNT` varchar(100) NOT NULL,
  `U_INVNO` varchar(100) NOT NULL,
  `U_LAT` varchar(100) NOT NULL,
  `U_LONG` varchar(100) NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL,
  `bpsource` varchar(10) NOT NULL,
  `category` varchar(250) NOT NULL,
  `intProdCat` text CHARACTER SET utf8mb4 NOT NULL,
  `intProjCat` text CHARACTER SET utf8mb4 NOT NULL,
  `source` varchar(100) NOT NULL,
  `source_id` varchar(10) NOT NULL,
  `zone` varchar(100) NOT NULL,
  `CustomerStatus` varchar(100) NOT NULL,
  `CreatedBy` varchar(100) NOT NULL,
  `BPCustCode` varchar(100) NOT NULL,
  `U_Landline` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_businesspartner`
--

INSERT INTO `BusinessPartner_businesspartner` (`id`, `CardCode`, `CardName`, `Industry`, `CardType`, `Website`, `EmailAddress`, `Phone1`, `DiscountPercent`, `Currency`, `IntrestRatePercent`, `CommissionPercent`, `Notes`, `PayTermsGrpCode`, `CreditLimit`, `AttachmentEntry`, `SalesPersonCode`, `ContactPerson`, `U_LEADID`, `U_LEADNM`, `BPAddresses`, `U_PARENTACC`, `U_BPGRP`, `U_CONTOWNR`, `U_RATING`, `U_TYPE`, `U_ANLRVN`, `U_CURBAL`, `U_ACCNT`, `U_INVNO`, `U_LAT`, `U_LONG`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `bpsource`, `category`, `intProdCat`, `intProjCat`, `source`, `source_id`, `zone`, `CustomerStatus`, `CreatedBy`, `BPCustCode`, `U_Landline`) VALUES
(4, 'CS00004', 'Cinntra', '1', 'cCustomer', 'cinntra@.com', 'Deloitte@gmail.com', '1234512345', '', 'INR', '', '', 'Testing', '1', '', '', '89', 'Rahul', 33, 'ASDasd', '', '', '', 'Rahul', '', 'Contractor', '', '', '', 'GST11233', '28.7041', '77.1025', '2022-09-28', '03:14:47 PM', '2022-09-28', '3:14:47 PM', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Facebook', '2', 'East Zone', 'Prospect', '', '', ''),
(5, 'CS00005', 'Wepro', '1', 'cCustomer', 'Wepro@.com', 'wepro@gmail.com', '9090902311', '', 'INR', '', '', 'Testing', '1', '', '', '89', 'Rahul', 0, '', '', 'Cinntra', '', 'Rahul', '', 'MEP Consultant', '', '', '', 'GST1000', '28.7041', '77.1025', '2022-09-28', '06:31:29 PM', '2022-09-28', '6:31:29 PM', 'Self', 'Product', 'Drinking Water Fountains', '', '', '', 'North Zone', 'Prospect', '', '', ''),
(12, 'CS00012', 'Testing Bp', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '89', 'Rahul', 33, 'ASDasd', '', 'Wepro', '', 'Rahul', '', 'Kitchen Consultant', '', '', '', '', '28.7041', '77.1025', '2022-09-29', '03:07:44 PM', '2022-09-29', '3:07:44 PM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Facebook', '2', 'North Zone', 'Prospect', '', '', ''),
(13, 'CS00013', 'IBM', '1', 'cCustomer', '', '', '', '', 'INR', '', '', 'Remarks', '1', '', '', '89', 'Rahul', 33, 'ASDasd', '', '', '', 'Rahul', '', 'Project Management Consultant', '', '', '', '1000', '28.7041', '77.1025', '2022-09-29', '04:02:26 PM', '2022-09-29', '4:02:26 PM', 'Lead', 'Product', 'Water Coolers', '', 'Facebook', '2', 'East Zone', 'Prospect', '', '', ''),
(14, 'CS00014', 'Testing kithen', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '89', 'Arif', 33, 'ASDasd', '', 'Testing Bp', '', 'Arif', '', 'Kitchen Consultant', '', '', '', 'GST11233', '28.7041', '77.1025', '2022-09-30', '04:53:49 PM', '2022-09-30', '4:53:49 PM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Facebook', '2', 'West Zone', 'Prospect', '', '', ''),
(15, 'CS00015', 'Ajanara Heights', '1', 'cCustomer', 'www.ajanaraheights.com', 'support@ajanaraheights.com', '09867785798', '', 'INR', '', '', '', '1', '', '', '94', 'Ankit Verma', 35, 'Ajanara Enclave', '', '', '', 'Ankit Verma', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-03', '12:54:19 PM', '2022-10-03', '12:54:19 PM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Facebook', '2', 'North Zone', 'Prospect', '', '', ''),
(16, 'CS00016', 'Ajanara Enclave', '1', 'cCustomer', 'www.ajanaraenclave.com', 'support@ajanaraenclave.com', '08699978089', '', 'INR', '', '', 'NA', '3', '', '', '95', 'Abhinav Tyagi', 35, 'Ajanara Enclave', '', '', '', 'Abhinav Tyagi', '', 'Kitchen Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-03', '03:10:57 PM', '2022-10-03', '3:10:57 PM', 'Lead', 'Project', '', 'Water Treatment Plant', 'Facebook', '2', 'West Zone', 'Prospect', '', '', ''),
(17, 'CS00017', 'Cinntra Test', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '89', 'Rahul', 35, 'Ajanara Enclave', '', '', '', 'Rahul', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-03', '04:58:49 PM', '2022-10-03', '4:58:49 PM', 'Lead', 'Product', 'Water Coolers', '', 'Facebook', '2', 'North Zone', 'Prospect', '', '', ''),
(18, 'CS00018', 'Cinntra Test 2', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '89', 'Rahul', 35, 'Ajanara Enclave', '', '', '', 'Rahul', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-03', '05:01:28 PM', '2022-10-03', '5:01:28 PM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Facebook', '2', 'East Zone', 'Prospect', '', '', ''),
(19, 'CS00019', 'Trends', '6', 'cCustomer', 'www.trends.com', 'support@trends.com', '09899868663', '', 'INR', '', '', '', '2', '', '', '95', 'Ashok', 36, 'Trends', '', '', '', 'Ashok', '', 'Project Management Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-03', '05:17:09 PM', '2022-10-03', '5:17:09 PM', 'Lead', 'Project', '', 'Ultra Filtration Plant', 'Emailer', '7', 'North Zone', 'Prospect', '', '', ''),
(20, 'CS00020', 'Haldiram & CO.', '7', 'cCustomer', 'www.haldiram.com', 'support@haldiram.co.in', '09866876876', '', 'INR', '', '', 'NA', '2', '', '', '96', 'Nitin Tyagi', 38, 'Haldiram & CO.', '', '', '', 'Nitin Tyagi', '', 'Kitchen Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-06', '02:50:39 PM', '2022-10-06', '2:50:39 PM', 'Lead', 'Product', 'Water Coolers', '', 'Facebook', '2', 'North Zone', 'Prospect', '', '', ''),
(21, 'CS00021', 'Groffers Stove', '3', 'cCustomer', 'www.groffersstove.com', 'support@groffersstoves.com', '09879878866', '', 'INR', '', '', '', '-1', '', '', '98', 'Chandan Singh', 39, 'Groffers Stove', '', '', '', 'Chandan Singh', '', 'Kitchen Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-07', '06:23:46 PM', '2022-10-07', '6:23:46 PM', 'Lead', 'Product & Project', 'Drinking Water Stations,Water Softner,Reverse Osmosis Plant,Bottle Filling Stations,Drinking Water Fountains,Water Coolers,Water Chillers,Drinking Water Taps,Sewage Treatment Plant,Water Treatment Plant,Ozonators', '', 'Instagram', '4', 'North Zone', 'Prospect', '', '', ''),
(22, 'CS00022', 'Nimbus Post', '1', 'cCustomer', 'nimbus.com', 'nimnus@gmail.com', '1234512345', '', 'INR', '', '', 'Testing', '1', '', '', '99', 'Rahul', 0, '', '', '', '', 'Rahul', '', 'Client', '', '', '', 'GST11233', '28.7041', '77.1025', '2022-10-10', '12:04:38 PM', '2022-10-10', '12:04:38 PM', 'Self', 'Product', 'Bottle Filling Stations', '', '', '', 'North Zone', 'Prospect', '', '', ''),
(23, 'CS00023', 'popup', '2', 'cCustomer', 'cinntra@.com', '', '1234512345', '', 'INR', '', '', 'Testing', '1', '', '', '92', 'Rahul', 39, 'Groffers Stove', '', '', '', 'Rahul', '', 'Client', '', '', '', 'GST11233', '28.7041', '77.1025', '2022-10-10', '02:49:51 PM', '2022-10-10', '2:49:51 PM', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Instagram', '4', 'North Zone', 'Prospect', '1', '', ''),
(24, 'CS00024', 'IBM COMP LTD', '1', 'cCustomer', 'www.IBM.com', 'ankur.tyagi@cinntra.com', '09907987987', '', 'INR', '', '', '', '2', '', '', '101', 'Rahul Akarniya', 40, 'IBM COMP LTD', '', '', '', 'Rahul Akarniya', '', 'Project Management Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-10', '05:25:17 PM', '2022-10-10', '5:25:17 PM', 'Lead', 'Product & Project', 'Bottle Filling Stations,Drinking Water Fountains,Water Coolers,Water Treatment Plant,Sewage Treatment Plant,Reverse Osmosis Plant,Ultra Filtration Plant', '', 'Linkedin', '3', 'South Zone', 'Prospect', '1', '', ''),
(25, 'CS00025', 'Lagero Infotech', '1', 'cCustomer', 'www.wipro.com', 'nipun.dixit@cinntra.com', '08798798889', '', 'INR', '', '', '', '1', '', '', '101', 'Bhoopi', 0, '', '', '', '', 'Bhoopi', '', 'MEP Consultant', '', '', '', '', '28.7041', '77.1025', '2022-10-10', '06:38:23 PM', '2022-10-10', '6:38:23 PM', 'Self', 'Product & Project', 'Water Softner,Reverse Osmosis Plant,Effluent Treatment Plant,Ultra Filtration Plant,Sewage Treatment Plant,Water Treatment Plant', '', '', '', 'North Zone', 'Prospect', '1', '', ''),
(26, 'CS00026', 'Google Inc.', '1', 'cCustomer', '', '', '1231231231', '', 'INR', '', '', '', '1', '', '', '1', 'Santanu Sahu', 0, '', '', '', '', 'Santanu Sahu', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '11:19:45 AM', '2022-10-11', '11:19:45 AM', 'Self', 'Product & Project', 'Bottle Filling Stations,Water Coolers', '', '', '', 'North Zone', 'Prospect', '1', '', ''),
(27, 'CS00027', 'FIncorp. Arch', '7', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '1', 'Ankit Sharma', 0, '', '', '', '', 'Ankit Sharma', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '11:19:53 AM', '2022-10-11', '11:19:53 AM', 'Self', 'Product & Project', 'Drinking Water Fountains,Bottle Filling Stations', '', '', '', 'North Zone', 'Prospect', '1', '', ''),
(28, 'CS00028', 'Dell', '2', 'cCustomer', 'cinntra@.com', 'Deloitte@gmail.com', '1234512345', '', 'INR', '', '', 'Testing', '1', '', '', '102', 'Rahul', 0, '', '', '', '', 'Rahul', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '12:31:17 PM', '2022-10-11', '12:31:17 PM', 'Self', 'Product', 'Bottle Filling Stations', '', '', '', 'East Zone', 'Prospect', '1', 'CNTR/E10001', ''),
(29, 'CS00029', 'New BP', '2', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '99', 'Rahul', 40, 'IBM COMP LTD', '', 'Testing Bp', '', 'Rahul', '', 'Others', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '04:15:13 PM', '2022-10-11', '4:15:13 PM', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Linkedin', '3', 'East Zone', 'Prospect', '1', 'ARCH/E10001', ''),
(30, 'CS00030', 'NEw bp 2', '4', 'cCustomer', '', '', '', '', 'INR', '', '', '', '2', '', '', '94', 'Rahul', 40, 'IBM COMP LTD', '', 'Ajanara Enclave', '', 'Rahul', '', 'Architect', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '04:18:46 PM', '2022-10-11', '4:18:46 PM', 'Lead', 'Project', '', 'Sewage Treatment Plant', 'Linkedin', '3', 'East Zone', 'Prospect', '1', 'ARCH/E10002', ''),
(31, 'CS00031', 'New bp 3', '3', 'cCustomer', '', '', '', '', 'INR', '', '', '', '2', '', '', '90', 'Rahul', 39, 'Groffers Stove', '', '', '', 'Rahul', '', 'Facility Management', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '04:21:26 PM', '2022-10-11', '4:21:26 PM', 'Lead', 'Project', '', 'Sewage Treatment Plant', 'Instagram', '4', 'East Zone', 'Prospect', '1', 'ARCH/E10003', ''),
(32, 'CS00032', 'asdf', '2', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '93', 'Rahul', 40, 'IBM COMP LTD', '', '', '', 'Rahul', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '05:30:25 PM', '2022-10-11', '5:30:25 PM', 'Lead', 'Product & Project', '', '', 'Linkedin', '3', 'East Zone', 'Prospect', '1', 'CNTR/E10002', ''),
(33, 'CS00033', 'Jyoti Pest Control', '3', 'cCustomer', 'www.jyotipestcontrol.com', 'support@jyotipestcontrol.com', '6686879879', '', 'INR', '', '', '', '2', '', '', '1', 'Abhi Tyagi', 42, 'Pest Control', '', '', '', 'Abhi Tyagi', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '06:06:06 PM', '2022-10-11', '6:06:06 PM', 'Lead', 'Product & Project', 'Bottle Filling Stations,Drinking Water Fountains,Water Coolers', '', 'Emailer', '7', 'North Zone', 'Customer', '1', 'CLNT/N30001', ''),
(34, 'CS00034', 'qwdqdqwd', '2', 'cCustomer', '', 'giet11aei014@gmail.com', '08018762164', '', 'INR', '', '', '', '2', '', '', '1', 'Santanu', 0, '', '', '', '', 'Santanu', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-10-11', '06:35:13 PM', '2022-10-11', '6:35:13 PM', 'Self', 'Product & Project', 'Water Coolers', '', '', '', 'North Zone', 'Prospect', '1', 'CNTR/N30001', ''),
(35, 'CS00035', 'Dell Logistics', '1', 'cCustomer', 'www.delllogistics.com', 'support@dell.com', '9990989704', '', 'INR', '', '', '', '2', '', '', '1', 'Ankur Tyagi Ji', 0, '', '', '', '', 'Ankur Tyagi Ji', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-10-12', '10:47:22 AM', '2022-10-12', '10:47:22 AM', 'Self', 'Product & Project', 'Bottle Filling Stations,Drinking Water Fountains,Water Coolers,Water Chillers,Drinking Water Stations,Drinking Water Taps,Water Dispenser,Ozonators,Water Treatment Plant,Sewage Treatment Plant,Water Softner,Effluent Treatment Plant,Reverse Osmosis Plant,Ultra Filtration Plant', '', '', '', 'North Zone', 'Customer', '1', 'CLNT/N30006', ''),
(36, 'CS00036', 'Humdard', '3', 'cCustomer', 'www.humdard.com', 'kashif.naved@cinntra.com', '08077642734', '', 'INR', '', '', 'NA', '2', '', '', '1', 'Suresh Tyagi', 91, 'Humdard', '', '', '', 'Suresh Tyagi', '', 'Facility Management', '', '', '', '', '28.7041', '77.1025', '2022-11-02', '06:07:54 PM', '2022-11-02', '6:07:54 PM', 'Lead', 'Product & Project', 'Sewage Treatment Plant,Water Coolers', '', 'Facebook', '2', 'North Zone', 'Customer', '1', 'FMNC/N30001', ''),
(37, 'CS00037', 'ITC', '7', 'cCustomer', 'www.itc.com', 'nipun.dixit@cinntra.com', '08767898765', '', 'INR', '', '', '', '2', '', '', '106', 'Sudhir Kumar', 92, 'ITC', '', '', '', 'Sudhir Kumar', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-03', '10:59:30 AM', '2022-11-03', '10:59:30 AM', 'Lead', 'Project', '', 'Ultra Filtration Plant', 'Instagram', '4', 'North Zone', 'Customer', '106', 'CLNT/N30007', ''),
(38, 'CS00038', 'Loco Treatment', '7', 'cCustomer', 'www.locotreatment.com', 'support@locotreatment.com', '7896898768', '', 'INR', '', '', '', '3', '', '', '106', 'Sudhir Kumar', 92, 'ITC', '', '', '', 'Sudhir Kumar', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-11-03', '11:04:43 AM', '2022-11-03', '11:04:43 AM', 'Lead', 'Product & Project', 'Sewage Treatment Plant', '', 'Instagram', '4', 'North Zone', 'Prospect', '106', 'CNTR/N30002', ''),
(39, 'CS00039', 'Apco Water Architecture', '3', 'cCustomer', 'www.apco.com', 'support@apco.com', '08678979998', '', 'INR', '', '', '', '1', '', '', '106', 'Sudhir Kumar', 92, 'ITC', '', '', '', 'Sudhir Kumar', '', 'Architect', '', '', '', '', '28.7041', '77.1025', '2022-11-03', '11:10:38 AM', '2022-11-03', '11:10:38 AM', 'Lead', 'Project', '', 'Reverse Osmosis Plant', 'Instagram', '4', 'North Zone', 'Customer', '106', 'ARCH/N30001', ''),
(40, 'CS00040', 'AGON IT SOLUTION 1233', '1', 'cCustomer', '', 'giet11aei014@gmail.commmm', '8018762164', '', 'INR', '', '', '', '1', '', '', '107', 'Santanu', 0, '', '', '', '', 'Santanu', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-03', '12:52:28 PM', '2022-11-03', '12:52:28 PM', 'Lead', 'Product & Project', 'Bottle Filling Stations,Ultra Filtration Plant,Reverse Osmosis Plant', '', '', '', 'North Zone', 'Customer', '107', 'CLNT/N30008', ''),
(41, 'CS00041', 'adgfg', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '106', 'dfsgh', 0, '', '', '', '', 'dfsgh', '', 'Project Management Consultant', '', '', '', '', '28.7041', '77.1025', '2022-11-03', '06:10:38 PM', '2022-11-03', '6:10:38 PM', 'Self', 'Project', '', 'Sewage Treatment Plant', '', '', 'North Zone', 'Prospect', '1', 'PRMC/N30001', ''),
(43, 'CS00043', 'Shiv Lakhan Textiles', '6', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '107', 'Shiv', 93, 'Shiv Lakhan Textiles', '', '', '', 'Shiv', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-04', '12:56:38 PM', '2022-11-04', '12:56:38 PM', 'Lead', 'Product & Project', 'Reverse Osmosis Plant', '', 'Emailer', '7', 'West Zone', 'Customer', '107', 'CLNT/W20003', ''),
(44, 'CS00044', 'Textile Contractor Pvt Ltd', '7', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '107', 'Srimaan', 0, '', '', '', '', 'Srimaan', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-11-04', '01:23:00 PM', '2022-11-04', '1:23:00 PM', 'Self', 'Product & Project', 'Bottle Filling Stations,Ultra Filtration Plant', '', '', '', 'East Zone', 'Customer', '107', 'CNTR/E10003', ''),
(45, 'CS00045', 'asdfas', '1', 'cCustomer', 'asf', '', '', '', 'INR', '', '', '', '-1', '', '', '91', 'Shiv', 93, 'Shiv Lakhan Textiles', '', '', '', 'Shiv', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-04', '04:15:08 PM', '2022-11-04', '4:15:08 PM', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Emailer', '7', 'East Zone', 'Prospect', '1', 'CLNT/E10004', ''),
(46, 'CS00046', 'qweqweqweqweqweqw', '1', 'cCustomer', 'qweqwe', '', '0909009090', '', 'INR', '', '', '', '-1', '', '', '107', 'Srimaan', 0, '', '', '', '', 'Srimaan', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-04', '05:31:56 PM', '2022-11-04', '5:31:56 PM', 'Self', 'Product', 'Bottle Filling Stations', '', '', '', 'North Zone', 'Customer', '107', 'CLNT/N30009', ''),
(47, 'CS00047', 'Lucky Traders', '3', 'cCustomer', 'www.luckytraders.com', 'Lucky.singh@gmail.com', '09867789776', '', 'INR', '', '', '', '2', '', '', '106', 'Samarth Singh', 96, 'Lucky Traders', '', '', '', 'Samarth Singh', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-07', '03:17:58 PM', '2022-11-07', '3:17:58 PM', 'Lead', 'Product & Project', 'Ultra Filtration Plant,Drinking Water Taps', '', 'Whatsapp', '6', 'North Zone', 'Customer', '106', 'CLNT/N30010', ''),
(48, 'CS00048', 'test company', '3', 'cCustomer', '', '', '', '', 'INR', '', '', '', '3', '', '', '97', 'Sudhir Kumar', 92, 'ITC', '', 'Lucky Traders', '', 'Sudhir Kumar', '', 'Architect', '', '', '', '', '28.7041', '77.1025', '2022-11-08', '05:47:13 PM', '2022-11-08', '5:47:13 PM', 'Lead', 'Project', '', 'Water Treatment Plant', 'Instagram', '4', 'West Zone', 'Customer', '1', 'ARCH/W20001', ''),
(49, 'CS00049', 'eqasdfdasf', '2', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '91', 'Lucky Singh', 96, 'Lucky Traders', '', '', '', 'Lucky Singh', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-08', '06:21:21 PM', '2022-11-08', '6:21:21 PM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Whatsapp', '6', 'West Zone', 'Prospect', '1', 'CLNT/W20004', ''),
(50, 'CS00050', 'NEw com', '1', 'cCustomer', '', 'newcom@gmail.com', '', '', 'INR', '', '', '', '1', '', '', '106', 'Rahul', 0, '', '', 'Lucky Traders', '', 'Rahul', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-11', '05:38:09 PM', '2022-11-11', '5:38:09 PM', 'Self', 'Product', 'Bottle Filling Stations', '', '', '', 'North Zone', 'Customer', '1', 'CLNT/N30013', '123213124134234'),
(51, 'CS00051', 'Lux Co.', '3', 'cCustomer', 'www.lux.com', 'support@lux.com', '9876545678', '', 'INR', '', '', '', '2', '', '', '107', 'AT', 99, 'Lux Co.', '', '', '', 'AT', '', 'Client', '', '', '', '', '28.7041', '77.1025', '2022-11-14', '06:39:36 PM', '2022-11-14', '6:39:36 PM', 'Lead', 'Product & Project', 'Bottle Filling Stations,Drinking Water Fountains,Water Coolers,Water Chillers,Drinking Water Stations,Drinking Water Taps,Water Dispenser,Ozonators,Water Treatment Plant,Sewage Treatment Plant,Water Softner,Effluent Treatment Plant,Reverse Osmosis Plant,Ultra Filtration Plant', '', 'Facebook', '2', 'North Zone', 'Customer', '1', 'CLNT/N30012', '012148530'),
(52, 'CS00052', 'Ankur Santanu Bros & Co.', '1', 'cCustomer', 'www.nayan.co', 'Ankur@cinntra.com', '1231231212', '', 'INR', '', '', 'qwasdfasdfasdf', '2', '', '', '107', 'Ankur Sahu', 100, 'Ankur Santanu Bros & Co.', '', 'Textile Contractor Pvt Ltd', '', 'Ankur Sahu', '', 'Architect', '', '', '', '37AADCS0472N1Z1', '28.7041', '77.1025', '2022-11-15', '11:11:38 AM', '2022-11-15', '11:11:38 AM', 'Lead', 'Product & Project', 'Water Coolers,Water Softner,Ultra Filtration Plant', '', 'Website', '5', 'East Zone', 'Customer', '1', 'ARCH/E10004', '0123248530'),
(53, 'CS00053', 'werdgfff', '1', 'cCustomer', 'www.sjs.cm', 'dbsjjd@mailc.ci', '7654334567', '', 'INR', '', '', 'remarks1', '-1', '', '', '89', 'Pankaj', 97, 'testing ', '', '', '', 'Pankaj', '', 'Client', '', '', '', '345678944567', '28.7041', '77.1025', '2022-11-15', '11:08:11 AM', '2022-11-15', '11:08:11 AM', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Facebook', '2', 'North Zone', 'Prospect', '1', 'CLNT/N30014', '09876567898765'),
(54, 'CS00054', 'dfggfd', '1', 'cCustomer', '', '', '', '', 'INR', '', '', '', '1', '', '', '106', 'Ankur Sahu', 100, 'Ankur Santanu Bros & Co.', '', '', '', 'Ankur Sahu', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-11-15', '11:31:02 AM', '2022-11-15', '11:31:02 AM', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Website', '5', 'East Zone', 'Prospect', '1', 'CNTR/E10004', ''),
(55, 'CS00055', 'sxgcgvhjb ', '2', 'cCustomer', '', '', '', '', 'INR', '', '', '', '2', '', '', '89', 'vjahdbkj', 0, '', '', '', '', 'vjahdbkj', '', 'Contractor', '', '', '', '', '28.7041', '77.1025', '2022-11-15', '12:00:02 PM', '2022-11-15', '12:00:02 PM', 'Reference', 'Product & Project', 'Water Coolers,Drinking Water Fountains,Bottle Filling Stations', '', '', '', 'East Zone', 'Prospect', '1', 'CNTR/E10005', ''),
(56, 'CS00056', 'naya company', '2', 'cCustomer', 'www.nayasite.com', 'nayahai@gmail.com', '00691212231', '', 'INR', '', '', 'naya remarks added', '4', '', '', '106', 'Lucky Singh', 96, 'Lucky Traders', '', 'dfggfd', '', 'Lucky Singh', '', 'Kitchen Consultant', '', '', '', '7', '28.7041', '77.1025', '2022-11-16', '15:45:13', '2022-11-16', '15:45:13', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Whatsapp', '6', 'East Zone', 'Customer', '1', 'KTCL/E10001', '9908546345'),
(57, 'CS00057', 'firse new', '7', 'cCustomer', 'www.nayasite1.com', 'nayahai@gmail.co', '00691212230', '', 'INR', '', '', 'rafddsfdssdsdfdddsd', '1', '', '', '106', 'Ankur Sahu', 100, 'Ankur Santanu Bros & Co.', '', 'Ankur Santanu Bros & Co.', '', 'Ankur Sahu', '', 'Facility Management', '', '', '', '7345678998', '28.7041', '77.1025', '2022-11-16', '15:54:06', '2022-11-16', '15:54:06', 'Lead', 'Product', 'Drinking Water Fountains', '', 'Website', '5', 'East Zone', 'Prospect', '1', 'FMNC/E10001', '9908546344'),
(58, 'CS00058', 'new partner ha', '2', 'cCustomer', 'www.nayasite.com', 'nayahai@outlook.com', '00691212233', '', 'INR', '', '', 'new asda odasdjadahjd', '4', '', '', '106', 'Ankur Sahu', 100, 'Ankur Santanu Bros & Co.', '', 'firse new', '', 'Ankur Sahu', '', 'Architect', '', '', '', '7', '28.7041', '77.1025', '2022-11-17', '17:17:33', '2022-11-17', '17:17:33', 'Lead', 'Product', 'Bottle Filling Stations', '', 'Website', '5', 'West Zone', 'Prospect', '1', 'ARCH/W20002', '9908546344'),
(59, '', 'xgjvjvjvhf', '1', 'cCustomer', 'www.ggggg.com', 'asgutg@fadf.df', '889652147', '', 'INR', '', '', 'the new rules ', '1', 'North Zone', '', '107', 'Tesgg', 100, 'Ankur Santanu Bros & Co.', '', 'test company', '', 'Tesgg', '', 'CLient', '', '', '', '23654', '30.7333', '76.7794', '2022-11-18', '10:13:35', '2022-11-18', '10:13:35', 'Lead', 'Product', 'Ozonators', '', 'Facebook', '2', 'North Zone', 'Prospect', '1', 'CLNT/N3', '0612281420');

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_businesspartner_BPLID`
--

CREATE TABLE `BusinessPartner_businesspartner_BPLID` (
  `id` bigint NOT NULL,
  `businesspartner_id` bigint NOT NULL,
  `branch_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_businesspartner_BPLID`
--

INSERT INTO `BusinessPartner_businesspartner_BPLID` (`id`, `businesspartner_id`, `branch_id`) VALUES
(4, 4, 1),
(5, 5, 1),
(12, 12, 1),
(13, 13, 1),
(14, 14, 1),
(15, 15, 1),
(16, 16, 1),
(17, 17, 1),
(18, 18, 1),
(19, 19, 1),
(20, 20, 1),
(21, 21, 1),
(22, 22, 1),
(23, 23, 1),
(24, 24, 1),
(25, 25, 1),
(26, 26, 1),
(27, 27, 1),
(28, 28, 1),
(29, 29, 1),
(30, 30, 1),
(31, 31, 1),
(32, 32, 1),
(33, 33, 1),
(34, 34, 1),
(35, 35, 1),
(36, 36, 1),
(37, 37, 1),
(38, 38, 1),
(39, 39, 1),
(40, 40, 1),
(41, 41, 1),
(43, 43, 1),
(44, 44, 1),
(45, 45, 1),
(46, 46, 1),
(47, 47, 1),
(48, 48, 1),
(49, 49, 1),
(50, 50, 1),
(51, 51, 1),
(52, 52, 1),
(53, 53, 1),
(54, 54, 1),
(55, 55, 1),
(56, 56, 1),
(57, 57, 1),
(58, 58, 1);

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_customercode`
--

CREATE TABLE `BusinessPartner_customercode` (
  `id` bigint NOT NULL,
  `cc_prefix` varchar(100) NOT NULL,
  `counter` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_customercode`
--

INSERT INTO `BusinessPartner_customercode` (`id`, `cc_prefix`, `counter`) VALUES
(1, 'CLNT/E1', 4),
(2, 'CLNT/W2', 4),
(3, 'CLNT/N3', 10),
(4, 'CLNT/S4', 1),
(5, 'CNTR/E1', 3),
(6, 'CNTR/W2', 0),
(7, 'CNTR/N3', 2),
(8, 'CNTR/S4', 0),
(9, 'KTCL/E1', 0),
(10, 'KTCL/W2', 0),
(11, 'KTCL/N3', 0),
(12, 'KTCL/S4', 0),
(13, 'MEPC/E1', 0),
(14, 'MEPC/W2', 0),
(15, 'MEPC/N3', 0),
(16, 'MEPC/S4', 0),
(17, 'PRMC/E1', 0),
(18, 'PRMC/W2', 0),
(19, 'PRMC/N3', 1),
(20, 'PRMC/S4', 0),
(21, 'ARCH/E1', 3),
(22, 'ARCH/W2', 1),
(23, 'ARCH/N3', 1),
(24, 'ARCH/S4', 0),
(25, 'FMNC/E1', 0),
(26, 'FMNC/W2', 0),
(27, 'FMNC/N3', 1),
(28, 'FMNC/S4', 0),
(29, 'OTHR/E1', 0),
(30, 'OTHR/W2', 0),
(31, 'OTHR/N3', 0),
(32, 'OTHR/S4', 0),
(33, 'CLNT/N3', 11),
(34, 'CLNT/N3', 12),
(35, 'ARCH/E1', 4),
(36, 'CLNT/N3', 15),
(37, 'CNTR/E1', 4),
(38, 'CNTR/E1', 5),
(39, 'KTCL/E1', 1),
(40, 'FMNC/E1', 1),
(41, 'ARCH/W2', 2);

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_customergroup`
--

CREATE TABLE `BusinessPartner_customergroup` (
  `id` bigint NOT NULL,
  `CustomerGroup` varchar(100) NOT NULL,
  `Code` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_customergroup`
--

INSERT INTO `BusinessPartner_customergroup` (`id`, `CustomerGroup`, `Code`) VALUES
(1, 'CLIENT', 'CLNT'),
(2, 'CONTRACTOR', 'CNTR'),
(3, 'KITCHEN CONSULTANT', 'KTCL'),
(4, 'MEP CONSULTANT', 'MEPC'),
(5, 'PROJECT MANAGEMENT CONSULTANT', 'PRMC'),
(6, 'ARCHITECT', 'ARCH'),
(7, 'FACILITY MANAGEMENT', 'FMNC'),
(8, 'OTHERS', 'OTHR');

-- --------------------------------------------------------

--
-- Table structure for table `BusinessPartner_customerzone`
--

CREATE TABLE `BusinessPartner_customerzone` (
  `id` bigint NOT NULL,
  `CustomerZone` varchar(100) NOT NULL,
  `Code` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `BusinessPartner_customerzone`
--

INSERT INTO `BusinessPartner_customerzone` (`id`, `CustomerZone`, `Code`) VALUES
(1, 'East', 'E'),
(2, 'West', 'W'),
(3, 'North', 'N'),
(4, 'South', 'S');

-- --------------------------------------------------------

--
-- Table structure for table `Campaign_campaign`
--

CREATE TABLE `Campaign_campaign` (
  `id` bigint NOT NULL,
  `CampaignName` varchar(100) NOT NULL,
  `StartDate` varchar(100) NOT NULL,
  `EndDate` varchar(100) NOT NULL,
  `Type` varchar(255) NOT NULL,
  `Frequency` varchar(255) NOT NULL,
  `WeekDay` varchar(255) NOT NULL,
  `MonthlyDate` longtext NOT NULL,
  `Message` longtext NOT NULL,
  `QualityResponse` varchar(255) NOT NULL,
  `Sent` int NOT NULL,
  `Delivered` int NOT NULL,
  `Opened` int NOT NULL,
  `Responded` int NOT NULL,
  `Status` int NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `RunTime` varchar(15) NOT NULL,
  `Attachments` longtext NOT NULL,
  `CampaignOwner_id` varchar(20) NOT NULL,
  `CampaignSetId_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Campaign_campaignset`
--

CREATE TABLE `Campaign_campaignset` (
  `id` bigint NOT NULL,
  `CampaignSetName` varchar(100) NOT NULL,
  `CampSetType` varchar(255) NOT NULL,
  `CampaignAccess` varchar(250) NOT NULL,
  `Description` varchar(250) NOT NULL,
  `LeadSource` varchar(1000) NOT NULL,
  `LeadPriority` varchar(250) NOT NULL,
  `LeadStatus` varchar(250) NOT NULL,
  `LeadFromDate` varchar(100) NOT NULL,
  `LeadToDate` varchar(100) NOT NULL,
  `LeadZone` longtext NOT NULL,
  `LeadGroupType` longtext NOT NULL,
  `LeadCategory` longtext NOT NULL,
  `OppType` varchar(250) NOT NULL,
  `OppSalePerson` varchar(250) NOT NULL,
  `OppStage` varchar(250) NOT NULL,
  `OppFromDate` varchar(100) NOT NULL,
  `OppToDate` varchar(100) NOT NULL,
  `OppZone` longtext NOT NULL,
  `OppGroupType` longtext NOT NULL,
  `OppCategory` longtext NOT NULL,
  `BPType` varchar(250) NOT NULL,
  `BPSalePerson` varchar(250) NOT NULL,
  `BPCountry` varchar(250) NOT NULL,
  `BPCountryCode` varchar(1000) NOT NULL,
  `BPState` varchar(1000) NOT NULL,
  `BPStateCode` varchar(1000) NOT NULL,
  `BPIndustry` longtext NOT NULL,
  `BPFromDate` varchar(100) NOT NULL,
  `BPToDate` varchar(100) NOT NULL,
  `BPZone` longtext NOT NULL,
  `BPGroupType` longtext NOT NULL,
  `BPCategory` longtext NOT NULL,
  `category` varchar(250) NOT NULL,
  `intProdCat` varchar(250) NOT NULL,
  `intProjCat` varchar(250) NOT NULL,
  `MemberList` varchar(250) NOT NULL,
  `Status` int NOT NULL,
  `CreateDate` varchar(100) NOT NULL,
  `CreateTime` varchar(100) NOT NULL,
  `AllLead` int NOT NULL,
  `AllOpp` int NOT NULL,
  `AllBP` int NOT NULL,
  `CampaignSetOwner_id` varchar(20) NOT NULL,
  `CreateBy_id` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Campaign_campaignset`
--

INSERT INTO `Campaign_campaignset` (`id`, `CampaignSetName`, `CampSetType`, `CampaignAccess`, `Description`, `LeadSource`, `LeadPriority`, `LeadStatus`, `LeadFromDate`, `LeadToDate`, `LeadZone`, `LeadGroupType`, `LeadCategory`, `OppType`, `OppSalePerson`, `OppStage`, `OppFromDate`, `OppToDate`, `OppZone`, `OppGroupType`, `OppCategory`, `BPType`, `BPSalePerson`, `BPCountry`, `BPCountryCode`, `BPState`, `BPStateCode`, `BPIndustry`, `BPFromDate`, `BPToDate`, `BPZone`, `BPGroupType`, `BPCategory`, `category`, `intProdCat`, `intProjCat`, `MemberList`, `Status`, `CreateDate`, `CreateTime`, `AllLead`, `AllOpp`, `AllBP`, `CampaignSetOwner_id`, `CreateBy_id`) VALUES
(1, 'Diwali Special Offer', 'Emailer', '', '', 'Instagram', '', 'Qualified', '2022-10-07', '2022-10-16', 'North Zone', 'Kitchen Consultant', 'Drinking Water Stations', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Water Softner', '', 1, '2022-10-07', '', 0, 0, 0, '98', '98'),
(2, 'Big Grand Offer', 'WhatsApp', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1, '2022-10-11', '', 0, 0, 1, '1', '1'),
(4, 'Cinntra Test Camp', 'Emailer', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1, '2022-10-11', '', 0, 0, 1, '1', '1'),
(5, 'Abhi Test Campaign', 'Emailer', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1, '2022-10-11', '', 0, 0, 1, '1', '1'),
(6, 'Dell Infra Logistics', 'Emailer', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1, '2022-10-12', '', 1, 1, 1, '1', '1');

-- --------------------------------------------------------

--
-- Table structure for table `Campaign_campaignsetmembers`
--

CREATE TABLE `Campaign_campaignsetmembers` (
  `id` bigint NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `CampSetId_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Campaign_campaignsetmembers`
--

INSERT INTO `Campaign_campaignsetmembers` (`id`, `Name`, `Phone`, `Email`, `CampSetId_id`) VALUES
(77, 'Rahul', '9560763295', 'rahul@gmail.com', 2),
(78, 'Arif', '9711767677', '', 2),
(79, 'Abishek', '1234512345', 'rahul@gmail.com', 2),
(80, 'Ankit Verma', '9879868968', 'ankitverma@gmail.com', 2),
(81, 'Abhinav Tyagi', '9797979766', 'abhinavtyagi@gmail.com', 2),
(82, 'Laksay Tyagi', '98765678998', 'lakshaytyagi@gmail.com', 2),
(83, 'Ashok', '9876898076', 'ashokch@gmail.com', 2),
(84, 'Nitin Tyagi', '9879868687', 'nitintyagi@gmail.com', 2),
(85, 'Chandan Singh', '8979879797', 'chandansingh@gmail.com', 2),
(86, 'Rahul Akarniya', '7987987979', 'rahul.akarniya@cinntra.co.in', 2),
(87, 'Bhoopi', '9798798780', '', 2),
(88, 'Santanu Sahu', '1231231212', '', 2),
(89, 'Ankit Sharma', '8018762164', 'ankit.sharma@gmail.com', 2),
(142, 'Rahul', '9560763295', 'rahul@gmail.com', 4),
(143, 'Arif', '9711767677', '', 4),
(144, 'Abishek', '1234512345', 'rahul@gmail.com', 4),
(145, 'Ankit Verma', '9879868968', 'ankitverma@gmail.com', 4),
(146, 'Abhinav Tyagi', '9797979766', 'abhinavtyagi@gmail.com', 4),
(147, 'Laksay Tyagi', '98765678998', 'lakshaytyagi@gmail.com', 4),
(148, 'Ashok', '9876898076', 'ashokch@gmail.com', 4),
(149, 'Nitin Tyagi', '9879868687', 'nitintyagi@gmail.com', 4),
(150, 'Chandan Singh', '8979879797', 'chandansingh@gmail.com', 4),
(151, 'Rahul Akarniya', '7987987979', 'rahul.akarniya@cinntra.co.in', 4),
(152, 'Bhoopi', '9798798780', '', 4),
(153, 'Santanu Sahu', '1231231212', '', 4),
(154, 'Ankit Sharma', '8018762164', 'ankit.sharma@gmail.com', 4),
(155, 'Rahul', '9560763295', 'rahul@gmail.com', 5),
(156, 'Abishek', '1234512345', 'rahul@gmail.com', 5),
(157, 'Arif', '9711767677', '', 5),
(158, 'Ankit Verma', '9879868968', 'ankitverma@gmail.com', 5),
(159, 'Abhinav Tyagi', '9797979766', 'abhinavtyagi@gmail.com', 5),
(160, 'Laksay Tyagi', '98765678998', 'lakshaytyagi@gmail.com', 5),
(161, 'Ashok', '9876898076', 'ashokch@gmail.com', 5),
(162, 'Nitin Tyagi', '9879868687', 'nitintyagi@gmail.com', 5),
(163, 'Chandan Singh', '8979879797', 'chandansingh@gmail.com', 5),
(164, 'Rahul Akarniya', '7987987979', 'rahul.akarniya@cinntra.co.in', 5),
(165, 'Bhoopi', '9798798780', '', 5),
(166, 'Santanu Sahu', '1231231212', '', 5),
(167, 'Ankit Sharma', '8018762164', 'ankit.sharma@gmail.com', 5),
(168, 'Abhi Tyagi', '8285067282', 'abhi.tyagi@gmail.com', 5),
(169, 'qdfqfasdasdcsadf', '9090909000', '', 5),
(170, 'rtyuio', '3456456566', '', 5),
(215, 'Rahulaa', '1231231122', 'abcd@gmail.co', 6),
(216, 'Rahul', '9711767677', 'rahul@gmail.com', 6),
(217, 'Rahul', '9711767671', 'abcd@gmail.c', 6),
(218, 'Rahul', '1233212211', 'abcd@gmail.com', 6),
(219, 'Rahul', '9711767634', 'abcd@gmail.comm', 6),
(220, 'Rahul', '8800380688', 'rahul@gmail.con', 6),
(221, 'Anil Tyagi', '9876898765', 'aniltyagi@gmail.com', 6),
(222, 'asdf', '9711767622', 'vaibhavtyagi@gmail.com', 6),
(223, 'ADSads', '9711767673', 'SDASD@gmail.com', 6),
(224, 'Rahul', '8800380680', 'rahul.akarniya@cinntra.com', 6),
(225, 'Abhinav Tyagi', '9797979766', 'abhinavtyagi@gmail.com', 6),
(226, 'Ashok', '9876898076', 'ashokch@gmail.com', 6),
(227, 'Chotu', '9678968965', 'chotu@gmail.com', 6),
(228, 'Nitin Tyagi', '9879868687', 'nitintyagi@gmail.com', 6),
(229, 'Chandan Singh', '8979879797', 'chandansingh@gmail.com', 6),
(230, 'Rahul Akarniya', '7987987979', 'rahul.akarniya@cinntra.co.in', 6),
(231, 'Rakesh Jain', '8686876876', 'ankur.tyagi@cinntra.com', 6),
(232, 'Abhi Tyagi', '9080987987', 'abhi.tyagi@gmail.com', 6),
(233, 'Rahul', '9560763295', 'rahul@gmail.com', 6),
(234, 'Abishek', '1234512345', 'rahul@gmail.com', 6),
(235, 'Ankit Verma', '9879868968', 'ankitverma@gmail.com', 6),
(236, 'Laksay Tyagi', '98765678998', 'lakshaytyagi@gmail.com', 6),
(237, 'Bhoopi', '9798798780', '', 6),
(238, 'Santanu Sahu', '1231231212', '', 6),
(239, 'Ankit Sharma', '8018762164', 'ankit.sharma@gmail.com', 6),
(240, 'Abhi Tyagi', '7678858755', 'abhi.tyagi@gmail.com', 6),
(241, 'qdfqfasdasdcsadf', '9090909000', '', 6),
(242, 'rtyuio', '3456456566', '', 6),
(243, 'Ankur Tyagi Ji', '8285067282', 'ankur.tyagi@cinntra.com', 6);

-- --------------------------------------------------------

--
-- Table structure for table `Category_category`
--

CREATE TABLE `Category_category` (
  `id` bigint NOT NULL,
  `Number` int NOT NULL,
  `GroupName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Category_category`
--

INSERT INTO `Category_category` (`id`, `Number`, `GroupName`) VALUES
(1, 100, 'F.G Items'),
(2, 101, 'Component Item\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `ClientBankDetails_clientbankdetails`
--

CREATE TABLE `ClientBankDetails_clientbankdetails` (
  `id` bigint NOT NULL,
  `clientName` varchar(100) NOT NULL,
  `clientEmail` varchar(70) NOT NULL,
  `clientMobile` varchar(20) NOT NULL,
  `clientAddress` longtext NOT NULL,
  `clientGST` varchar(30) NOT NULL,
  `bankName` varchar(40) NOT NULL,
  `bankIFSC` varchar(40) NOT NULL,
  `bankAccountNo` varchar(100) NOT NULL,
  `AccountHolderName` varchar(100) NOT NULL,
  `TermsConditions` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ClientBankDetails_clientbankdetails`
--

INSERT INTO `ClientBankDetails_clientbankdetails` (`id`, `clientName`, `clientEmail`, `clientMobile`, `clientAddress`, `clientGST`, `bankName`, `bankIFSC`, `bankAccountNo`, `AccountHolderName`, `TermsConditions`) VALUES
(1, 'Wae Inhouse', 'wae@info.com', '9876543219', 'New Addres', 'GSTIN202020', 'Bank of Baroda', 'BOB1098765', '4321765890', 'HAKS OWNER', 'A Constitution Bench of the Supreme Court on Monday ruled that a judgment delivered by a larger bench will prevail irrespective of the number of judge');

-- --------------------------------------------------------

--
-- Table structure for table `Company_branch`
--

CREATE TABLE `Company_branch` (
  `id` bigint NOT NULL,
  `BPLId` varchar(5) NOT NULL,
  `BPLName` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `MainBPL` varchar(5) NOT NULL,
  `Disabled` varchar(5) NOT NULL,
  `UserSign2` varchar(5) NOT NULL,
  `UpdateDate` varchar(50) NOT NULL,
  `DflWhs` varchar(50) NOT NULL,
  `TaxIdNum` varchar(100) NOT NULL,
  `StreetNo` varchar(100) NOT NULL,
  `Building` varchar(100) NOT NULL,
  `ZipCode` varchar(100) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `Country` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Company_branch`
--

INSERT INTO `Company_branch` (`id`, `BPLId`, `BPLName`, `Address`, `MainBPL`, `Disabled`, `UserSign2`, `UpdateDate`, `DflWhs`, `TaxIdNum`, `StreetNo`, `Building`, `ZipCode`, `City`, `State`, `Country`) VALUES
(1, '1', 'WAE_Live', 'H-18, Sector 63', 'Y', 'N', 'NULL', '2022-04-14 00:00:00', '01', '07AABCV9939R1Z9', 'None', 'None', 'None', 'None', 'None', 'IN');

-- --------------------------------------------------------

--
-- Table structure for table `Company_company`
--

CREATE TABLE `Company_company` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` varchar(250) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(35) NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `natureOfIndustry` varchar(100) NOT NULL,
  `ERP` varchar(100) NOT NULL,
  `serverIP` varchar(100) NOT NULL,
  `port` int NOT NULL,
  `user` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `license_limit` int NOT NULL,
  `active` int NOT NULL,
  `timestamp` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Countries_countries`
--

CREATE TABLE `Countries_countries` (
  `id` bigint NOT NULL,
  `Code` varchar(5) NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Countries_countries`
--

INSERT INTO `Countries_countries` (`id`, `Code`, `Name`) VALUES
(1, 'AD', 'Andorra'),
(2, 'AE', 'United Arab Emir.'),
(3, 'AF', 'Afghanistan'),
(4, 'AG', 'Antigua/Barbuda'),
(5, 'AI', 'Anguilla'),
(6, 'AL', 'Albania'),
(7, 'AM', 'Armenia'),
(8, 'AN', 'Dutch Antilles'),
(9, 'AO', 'Angola'),
(10, 'AQ', 'Antarctica'),
(11, 'AR', 'Argentina'),
(12, 'AS', 'Samoa, American'),
(13, 'AT', 'Austria'),
(14, 'AU', 'Australia'),
(15, 'AW', 'Aruba'),
(16, 'AZ', 'Azerbaijan'),
(17, 'BA', 'Bosnia-Herzegovina'),
(18, 'BB', 'Barbados'),
(19, 'BD', 'Bangladesh'),
(20, 'BE', 'Belgium'),
(21, 'BF', 'Burkina-Faso'),
(22, 'BG', 'Bulgaria'),
(23, 'BH', 'Bahrain'),
(24, 'BI', 'Burundi'),
(25, 'BJ', 'Benin'),
(26, 'BM', 'Bermuda'),
(27, 'BN', 'Brunei Dar-es-S'),
(28, 'BO', 'Bolivia'),
(29, 'BQ', 'Bonaire, Sint Eustatius en Saba'),
(30, 'BR', 'Brazil'),
(31, 'BS', 'Bahamas'),
(32, 'BT', 'Bhutan'),
(33, 'BV', 'Bouvet Island'),
(34, 'BW', 'Botswana'),
(35, 'BY', 'Belarus'),
(36, 'BZ', 'Belize'),
(37, 'CA', 'Canada'),
(38, 'CC', 'Coconut Islands'),
(39, 'CD', 'Congo'),
(40, 'CF', 'Central African Rep'),
(41, 'CG', 'Congo'),
(42, 'CH', 'Schweiz'),
(43, 'CI', 'Ivory Coast'),
(44, 'CK', 'Cook Islands'),
(45, 'CL', 'Chile'),
(46, 'CM', 'Cameroon'),
(47, 'CN', 'China'),
(48, 'CO', 'Colombia'),
(49, 'CR', 'Costa Rica'),
(50, 'CU', 'Cuba'),
(51, 'CV', 'Cape Verde'),
(52, 'CW', 'Curaçao'),
(53, 'CX', 'Christmas Island'),
(54, 'CY', 'Cyprus'),
(55, 'CZ', 'Czech Republic'),
(56, 'DE', 'Germany'),
(57, 'DJ', 'Djibouti'),
(58, 'DK', 'Denmark'),
(59, 'DM', 'Dominica'),
(60, 'DO', 'Dominican Republic'),
(61, 'DZ', 'Algeria'),
(62, 'EC', 'Ecuador'),
(63, 'EE', 'Estonia'),
(64, 'EG', 'Egypt'),
(65, 'EH', 'West Sahara'),
(66, 'EL', 'Greece'),
(67, 'ER', 'Eritrea'),
(68, 'ES', 'Spain'),
(69, 'ET', 'Ethiopia'),
(70, 'FI', 'Finland'),
(71, 'FJ', 'Fiji'),
(72, 'FK', 'Falkland Islands'),
(73, 'FM', 'Micronesia'),
(74, 'FO', 'Faroe Islands'),
(75, 'FR', 'France'),
(76, 'GA', 'Gabon'),
(77, 'GB', 'United Kingdom'),
(78, 'GD', 'Grenada'),
(79, 'GE', 'Georgia'),
(80, 'GF', 'French Guayana'),
(81, 'GH', 'Ghana'),
(82, 'GI', 'Gibraltar'),
(83, 'GL', 'Greenland'),
(84, 'GM', 'Gambia'),
(85, 'GN', 'Guinea'),
(86, 'GP', 'Guadeloupe'),
(87, 'GQ', 'Equatorial Guinea'),
(88, 'GS', 'S. Sandwich Ins'),
(89, 'GT', 'Guatemala'),
(90, 'GU', 'Guam'),
(91, 'GW', 'Guinea-Bissau'),
(92, 'GY', 'Guyana'),
(93, 'HK', 'Hong Kong'),
(94, 'HM', 'Heard/McDnld Islnds'),
(95, 'HN', 'Honduras'),
(96, 'HR', 'Croatia'),
(97, 'HT', 'Haiti'),
(98, 'HU', 'Hungary'),
(99, 'ID', 'Indonesia'),
(100, 'IE', 'Ireland'),
(101, 'IL', 'Israel'),
(102, 'IN', 'India'),
(103, 'IO', 'Brit.Ind.Oc.Ter'),
(104, 'IQ', 'Iraq'),
(105, 'IR', 'Iran'),
(106, 'IS', 'Iceland'),
(107, 'IT', 'Italy'),
(108, 'JM', 'Jamaica'),
(109, 'JO', 'Jordan'),
(110, 'JP', 'Japan'),
(111, 'KE', 'Kenya'),
(112, 'KG', 'Kyrgyzstan'),
(113, 'KH', 'Cambodia'),
(114, 'KI', 'Kiribati'),
(115, 'KM', 'Comoros'),
(116, 'KN', 'St Kitts & Nevis'),
(117, 'KP', 'North Korea'),
(118, 'KR', 'South Korea'),
(119, 'KW', 'Kuwait'),
(120, 'KY', 'Cayman Islands'),
(121, 'KZ', 'Kazakhstan'),
(122, 'LA', 'Laos'),
(123, 'LB', 'Lebanon'),
(124, 'LC', 'St. Lucia'),
(125, 'LI', 'Liechtenstein'),
(126, 'LK', 'Sri Lanka'),
(127, 'LR', 'Liberia'),
(128, 'LS', 'Lesotho'),
(129, 'LT', 'Lithuania'),
(130, 'LU', 'Luxembourg'),
(131, 'LV', 'Latvia'),
(132, 'LY', 'Libya'),
(133, 'MA', 'Morocco'),
(134, 'MC', 'Monaco'),
(135, 'MD', 'Moldavia'),
(136, 'MG', 'Madagascar'),
(137, 'MH', 'Marshall Islands'),
(138, 'MK', 'Macedonia'),
(139, 'ML', 'Mali'),
(140, 'MM', 'Myanmar'),
(141, 'MN', 'Mongolia'),
(142, 'MO', 'Macao'),
(143, 'MP', 'N.Mariana Island'),
(144, 'MQ', 'Martinique'),
(145, 'MR', 'Mauretania'),
(146, 'MS', 'Montserrat'),
(147, 'MT', 'Malta'),
(148, 'MU', 'Mauritius'),
(149, 'MV', 'Maldives'),
(150, 'MW', 'Malawi'),
(151, 'MX', 'Mexico'),
(152, 'MY', 'Malaysia'),
(153, 'MZ', 'Mozambique'),
(154, 'NA', 'Namibia'),
(155, 'NC', 'New Caledonia'),
(156, 'NE', 'Niger'),
(157, 'NF', 'Norfolk Island'),
(158, 'NG', 'Nigeria'),
(159, 'NI', 'Nicaragua'),
(160, 'NL', 'Netherlands'),
(161, 'NO', 'Norway'),
(162, 'NP', 'Nepal'),
(163, 'NR', 'Nauru'),
(164, 'NU', 'Niue Islands'),
(165, 'NZ', 'New Zealand'),
(166, 'OM', 'Oman'),
(167, 'PA', 'Panama'),
(168, 'PE', 'Peru'),
(169, 'PF', 'French Polynesia'),
(170, 'PG', 'Papua New Guinea'),
(171, 'PH', 'Philippines'),
(172, 'PK', 'Pakistan'),
(173, 'PL', 'Poland'),
(174, 'PM', 'St.Pier,Miquel.'),
(175, 'PN', 'Pitcairn Islands'),
(176, 'PR', 'Puerto Rico'),
(177, 'PT', 'Portugal'),
(178, 'PW', 'Palau'),
(179, 'PY', 'Paraguay'),
(180, 'QA', 'Qatar'),
(181, 'RE', 'Reunion'),
(182, 'RO', 'Romania'),
(183, 'RU', 'Russian Fed.'),
(184, 'RW', 'Ruanda'),
(185, 'SA', 'Saudi Arabia'),
(186, 'SB', 'Solomon Islands'),
(187, 'SC', 'Seychelles'),
(188, 'SD', 'Sudan'),
(189, 'SE', 'Sweden'),
(190, 'SG', 'Singapore'),
(191, 'SH', 'St. Helena'),
(192, 'SI', 'Slovenia'),
(193, 'SJ', 'Svalbard'),
(194, 'SK', 'Slovakia'),
(195, 'SL', 'Sierra Leone'),
(196, 'SM', 'San Marino'),
(197, 'SN', 'Senegal'),
(198, 'SO', 'Somalia'),
(199, 'SR', 'Suriname'),
(200, 'ST', 'S.Tome,Principe'),
(201, 'SV', 'El Salvador'),
(202, 'SX', 'Sint Maarten'),
(203, 'SY', 'Syria'),
(204, 'SZ', 'Swaziland'),
(205, 'TC', 'Turksh Caicosin'),
(206, 'TD', 'Chad'),
(207, 'TF', 'French S.Territ'),
(208, 'TG', 'Togo'),
(209, 'TH', 'Thailand'),
(210, 'TJ', 'Tajikstan'),
(211, 'TK', 'Tokelau Islands'),
(212, 'TM', 'Turkmenistan'),
(213, 'TN', 'Tunisia'),
(214, 'TO', 'Tonga'),
(215, 'TP', 'East Timor'),
(216, 'TR', 'Turkey'),
(217, 'TT', 'Trinidad,Tobago'),
(218, 'TV', 'Tuvalu'),
(219, 'TW', 'Taiwan'),
(220, 'TZ', 'Tanzania'),
(221, 'UA', 'Ukraine'),
(222, 'UG', 'Uganda'),
(223, 'UM', 'Minor Outl.Ins.'),
(224, 'US', 'USA'),
(225, 'UY', 'Uruguay'),
(226, 'UZ', 'Uzbekistan'),
(227, 'VA', 'Vatican City'),
(228, 'VC', 'St. Vincent'),
(229, 'VE', 'Venezuela'),
(230, 'VG', 'British Virg. Islnd'),
(231, 'VI', 'American Virg.Islnd'),
(232, 'VN', 'Vietnam'),
(233, 'VU', 'Vanuatu'),
(234, 'WF', 'Wallis,Futuna'),
(235, 'WS', 'Western Samoa'),
(236, 'XX', '-No Country-'),
(237, 'YE', 'Yemen'),
(238, 'YT', 'Mayotte'),
(239, 'YU', 'Yugoslavia'),
(240, 'ZA', 'South Africa'),
(241, 'ZM', 'Zambia'),
(242, 'ZW', 'Zimbabwe');

-- --------------------------------------------------------

--
-- Table structure for table `Countries_states`
--

CREATE TABLE `Countries_states` (
  `id` bigint NOT NULL,
  `Code` varchar(5) NOT NULL,
  `Country` varchar(4) NOT NULL,
  `Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Countries_states`
--

INSERT INTO `Countries_states` (`id`, `Code`, `Country`, `Name`) VALUES
(1, 'BDS', 'AF', 'Badakhshān'),
(2, 'BGL', 'AF', 'Baghlān'),
(3, 'BAL', 'AF', 'Balkh'),
(4, 'BDG', 'AF', 'Bādghīs'),
(5, 'BAM', 'AF', 'Bāmyān'),
(6, 'DAY', 'AF', 'Dāykundī'),
(7, 'FRA', 'AF', 'Farāh'),
(8, 'FYB', 'AF', 'Fāryāb'),
(9, 'GHA', 'AF', 'Ghaznī'),
(10, 'GHO', 'AF', 'Ghōr'),
(11, 'HEL', 'AF', 'Helmand'),
(12, 'HER', 'AF', 'Herāt'),
(13, 'JOW', 'AF', 'Jowzjān'),
(14, 'KAN', 'AF', 'Kandahār'),
(15, 'KHO', 'AF', 'Khōst'),
(16, 'KNR', 'AF', 'Kunar'),
(17, 'KDZ', 'AF', 'Kunduz'),
(18, 'KAB', 'AF', 'Kābul'),
(19, 'KAP', 'AF', 'Kāpīsā'),
(20, 'LAG', 'AF', 'Laghmān'),
(21, 'LOG', 'AF', 'Lōgar'),
(22, 'NAN', 'AF', 'Nangarhār'),
(23, 'NIM', 'AF', 'Nīmrōz'),
(24, 'NUR', 'AF', 'Nūristān'),
(25, 'PIA', 'AF', 'Paktiyā'),
(26, 'PKA', 'AF', 'Paktīkā'),
(27, 'PAN', 'AF', 'Panjshayr'),
(28, 'PAR', 'AF', 'Parwān'),
(29, 'SAM', 'AF', 'Samangān'),
(30, 'SAR', 'AF', 'Sar-e Pul'),
(31, 'TAK', 'AF', 'Takhār'),
(32, 'URU', 'AF', 'Uruzgān'),
(33, 'WAR', 'AF', 'Wardak'),
(34, 'ZAB', 'AF', 'Zābul'),
(35, '01', 'AL', 'Berat'),
(36, '09', 'AL', 'Dibër'),
(37, '02', 'AL', 'Durrës'),
(38, '03', 'AL', 'Elbasan'),
(39, '04', 'AL', 'Fier'),
(40, '05', 'AL', 'Gjirokastër'),
(41, '06', 'AL', 'Korçë'),
(42, '07', 'AL', 'Kukës'),
(43, '08', 'AL', 'Lezhë'),
(44, '10', 'AL', 'Shkodër'),
(45, '11', 'AL', 'Tiranë'),
(46, '12', 'AL', 'Vlorë'),
(47, '01', 'DZ', 'Adrar'),
(48, '16', 'DZ', 'Alger'),
(49, '23', 'DZ', 'Annaba'),
(50, '44', 'DZ', 'Aïn Defla'),
(51, '46', 'DZ', 'Aïn Témouchent'),
(52, '05', 'DZ', 'Batna'),
(53, '07', 'DZ', 'Biskra'),
(54, '09', 'DZ', 'Blida'),
(55, '34', 'DZ', 'Bordj Bou Arréridj'),
(56, '10', 'DZ', 'Bouira'),
(57, '35', 'DZ', 'Boumerdès'),
(58, '08', 'DZ', 'Béchar'),
(59, '06', 'DZ', 'Béjaïa'),
(60, '02', 'DZ', 'Chlef'),
(61, '25', 'DZ', 'Constantine'),
(62, '17', 'DZ', 'Djelfa'),
(63, '32', 'DZ', 'El Bayadh'),
(64, '39', 'DZ', 'El Oued'),
(65, '36', 'DZ', 'El Tarf'),
(66, '47', 'DZ', 'Ghardaïa'),
(67, '24', 'DZ', 'Guelma'),
(68, '33', 'DZ', 'Illizi'),
(69, '18', 'DZ', 'Jijel'),
(70, '40', 'DZ', 'Khenchela'),
(71, '03', 'DZ', 'Laghouat'),
(72, '29', 'DZ', 'Mascara'),
(73, '43', 'DZ', 'Mila'),
(74, '27', 'DZ', 'Mostaganem'),
(75, '28', 'DZ', 'Msila'),
(76, '26', 'DZ', 'Médéa'),
(77, '45', 'DZ', 'Naama'),
(78, '31', 'DZ', 'Oran'),
(79, '30', 'DZ', 'Ouargla'),
(80, '04', 'DZ', 'Oum el Bouaghi'),
(81, '48', 'DZ', 'Relizane'),
(82, '20', 'DZ', 'Saïda'),
(83, '22', 'DZ', 'Sidi Bel Abbès'),
(84, '21', 'DZ', 'Skikda'),
(85, '41', 'DZ', 'Souk Ahras'),
(86, '19', 'DZ', 'Sétif'),
(87, '11', 'DZ', 'Tamanghasset'),
(88, '14', 'DZ', 'Tiaret'),
(89, '37', 'DZ', 'Tindouf'),
(90, '42', 'DZ', 'Tipaza'),
(91, '38', 'DZ', 'Tissemsilt'),
(92, '15', 'DZ', 'Tizi Ouzou'),
(93, '13', 'DZ', 'Tlemcen'),
(94, '12', 'DZ', 'Tébessa'),
(95, '07', 'AD', 'Andorra la Vella'),
(96, '02', 'AD', 'Canillo'),
(97, '03', 'AD', 'Encamp'),
(98, '08', 'AD', 'Escaldes-Engordany'),
(99, '04', 'AD', 'La Massana'),
(100, '05', 'AD', 'Ordino'),
(101, '06', 'AD', 'Sant Julià de Lòria'),
(102, 'BGO', 'AO', 'Bengo'),
(103, 'BGU', 'AO', 'Benguela'),
(104, 'BIE', 'AO', 'Bié'),
(105, 'CAB', 'AO', 'Cabinda'),
(106, 'CNN', 'AO', 'Cunene'),
(107, 'HUA', 'AO', 'Huambo'),
(108, 'HUI', 'AO', 'Huíla'),
(109, 'CCU', 'AO', 'Kuando Kubango'),
(110, 'CNO', 'AO', 'Kwanza Norte'),
(111, 'CUS', 'AO', 'Kwanza Sul'),
(112, 'LUA', 'AO', 'Luanda'),
(113, 'LNO', 'AO', 'Lunda Norte'),
(114, 'LSU', 'AO', 'Lunda Sul'),
(115, 'MAL', 'AO', 'Malange'),
(116, 'MOX', 'AO', 'Moxico'),
(117, 'NAM', 'AO', 'Namibe'),
(118, 'UIG', 'AO', 'Uíge'),
(119, 'ZAI', 'AO', 'Zaire'),
(120, '10', 'AG', 'Barbuda'),
(121, '11', 'AG', 'Redonda'),
(122, '03', 'AG', 'Saint George'),
(123, '04', 'AG', 'Saint John'),
(124, '05', 'AG', 'Saint Mary'),
(125, '06', 'AG', 'Saint Paul'),
(126, '07', 'AG', 'Saint Peter'),
(127, '08', 'AG', 'Saint Philip'),
(128, 'B', 'AR', 'Buenos Aires'),
(129, 'K', 'AR', 'Catamarca'),
(130, 'H', 'AR', 'Chaco'),
(131, 'U', 'AR', 'Chubut'),
(132, 'C', 'AR', 'Ciudad Autónoma de Buenos Aires'),
(133, 'W', 'AR', 'Corrientes'),
(134, 'X', 'AR', 'Córdoba'),
(135, 'E', 'AR', 'Entre Ríos'),
(136, 'P', 'AR', 'Formosa'),
(137, 'Y', 'AR', 'Jujuy'),
(138, 'L', 'AR', 'La Pampa'),
(139, 'F', 'AR', 'La Rioja'),
(140, 'M', 'AR', 'Mendoza'),
(141, 'N', 'AR', 'Misiones'),
(142, 'Q', 'AR', 'Neuquén'),
(143, 'R', 'AR', 'Río Negro'),
(144, 'A', 'AR', 'Salta'),
(145, 'J', 'AR', 'San Juan'),
(146, 'D', 'AR', 'San Luis'),
(147, 'Z', 'AR', 'Santa Cruz'),
(148, 'S', 'AR', 'Santa Fe'),
(149, 'G', 'AR', 'Santiago del Estero'),
(150, 'V', 'AR', 'Tierra del Fuego'),
(151, 'T', 'AR', 'Tucumán'),
(152, 'AG', 'AM', 'Aragac̣otn'),
(153, 'AR', 'AM', 'Ararat'),
(154, 'AV', 'AM', 'Armavir'),
(155, 'ER', 'AM', 'Erevan'),
(156, 'GR', 'AM', 'Geġark\'unik\''),
(157, 'KT', 'AM', 'Kotayk\''),
(158, 'LO', 'AM', 'Loṙi'),
(159, 'SU', 'AM', 'Syunik\''),
(160, 'TV', 'AM', 'Tavuš'),
(161, 'VD', 'AM', 'Vayoć Jor'),
(162, 'SH', 'AM', 'Širak'),
(163, 'ACT', 'AU', 'Australian Capital Territory'),
(164, 'NSW', 'AU', 'New South Wales'),
(165, 'NT', 'AU', 'Northern Territory'),
(166, 'QLD', 'AU', 'Queensland'),
(167, 'SA', 'AU', 'South Australia'),
(168, 'TAS', 'AU', 'Tasmania'),
(169, 'VIC', 'AU', 'Victoria'),
(170, 'WA', 'AU', 'Western Australia'),
(171, 'B', 'AT', 'Burgenland'),
(172, 'K', 'AT', 'Kärnten'),
(173, 'NÖ', 'AT', 'Niederösterreich'),
(174, 'OÖ', 'AT', 'Oberösterreich'),
(175, 'S', 'AT', 'Salzburg'),
(176, 'ST', 'AT', 'Steiermark'),
(177, 'T', 'AT', 'Tirol'),
(178, 'V', 'AT', 'Vorarlberg'),
(179, 'W', 'AT', 'Wien'),
(180, 'NX', 'AZ', 'Naxçıvan'),
(181, 'AK', 'BS', 'Acklins'),
(182, 'BY', 'BS', 'Berry Islands'),
(183, 'BI', 'BS', 'Bimini'),
(184, 'BP', 'BS', 'Black Point'),
(185, 'CI', 'BS', 'Cat Island'),
(186, 'CO', 'BS', 'Central Abaco'),
(187, 'CS', 'BS', 'Central Andros'),
(188, 'CE', 'BS', 'Central Eleuthera'),
(189, 'FP', 'BS', 'City of Freeport'),
(190, 'CK', 'BS', 'Crooked Island and Long Cay'),
(191, 'EG', 'BS', 'East Grand Bahama'),
(192, 'EX', 'BS', 'Exuma'),
(193, 'GC', 'BS', 'Grand Cay'),
(194, 'HI', 'BS', 'Harbour Island'),
(195, 'HT', 'BS', 'Hope Town'),
(196, 'IN', 'BS', 'Inagua'),
(197, 'LI', 'BS', 'Long Island'),
(198, 'MC', 'BS', 'Mangrove Cay'),
(199, 'MG', 'BS', 'Mayaguana'),
(200, 'MI', 'BS', 'Moores Island'),
(201, 'NO', 'BS', 'North Abaco'),
(202, 'NS', 'BS', 'North Andros'),
(203, 'NE', 'BS', 'North Eleuthera'),
(204, 'RI', 'BS', 'Ragged Island'),
(205, 'RC', 'BS', 'Rum Cay'),
(206, 'SS', 'BS', 'San Salvador'),
(207, 'SO', 'BS', 'South Abaco'),
(208, 'SA', 'BS', 'South Andros'),
(209, 'SE', 'BS', 'South Eleuthera'),
(210, 'SW', 'BS', 'Spanish Wells'),
(211, 'WG', 'BS', 'West Grand Bahama'),
(212, '14', 'BH', 'Al Janūbīyah'),
(213, '13', 'BH', 'Al Manāmah'),
(214, '15', 'BH', 'Al Muḩarraq'),
(215, '16', 'BH', 'Al Wusţá'),
(216, '17', 'BH', 'Ash Shamālīyah'),
(217, 'A', 'BD', 'Barisal'),
(218, 'B', 'BD', 'Chittagong'),
(219, 'C', 'BD', 'Dhaka'),
(220, 'D', 'BD', 'Khulna'),
(221, 'E', 'BD', 'Rajshahi'),
(222, 'F', 'BD', 'Rangpur'),
(223, 'G', 'BD', 'Sylhet'),
(224, '01', 'BB', 'Christ Church'),
(225, '02', 'BB', 'Saint Andrew'),
(226, '03', 'BB', 'Saint George'),
(227, '04', 'BB', 'Saint James'),
(228, '05', 'BB', 'Saint John'),
(229, '06', 'BB', 'Saint Joseph'),
(230, '07', 'BB', 'Saint Lucy'),
(231, '08', 'BB', 'Saint Michael'),
(232, '09', 'BB', 'Saint Peter'),
(233, '10', 'BB', 'Saint Philip'),
(234, '11', 'BB', 'Saint Thomas'),
(235, 'BR', 'BY', 'Brestskaya voblasts\''),
(236, 'HO', 'BY', 'Homyel\'skaya voblasts\''),
(237, 'HM', 'BY', 'Horad Minsk'),
(238, 'HR', 'BY', 'Hrodzenskaya voblasts\''),
(239, 'MA', 'BY', 'Mahilyowskaya voblasts\''),
(240, 'MI', 'BY', 'Minskaya voblasts\''),
(241, 'VI', 'BY', 'Vitsyebskaya voblasts\''),
(242, 'BRU', 'BE', 'Brussels Hoofdstedelijk Gewest'),
(243, 'WAL', 'BE', 'Région Wallonne'),
(244, 'VLG', 'BE', 'Vlaams Gewest'),
(245, 'BZ', 'BZ', 'Belize'),
(246, 'CY', 'BZ', 'Cayo'),
(247, 'CZL', 'BZ', 'Corozal'),
(248, 'OW', 'BZ', 'Orange Walk'),
(249, 'SC', 'BZ', 'Stann Creek'),
(250, 'TOL', 'BZ', 'Toledo'),
(251, 'AL', 'BJ', 'Alibori'),
(252, 'AK', 'BJ', 'Atakora'),
(253, 'AQ', 'BJ', 'Atlantique'),
(254, 'BO', 'BJ', 'Borgou'),
(255, 'CO', 'BJ', 'Collines'),
(256, 'DO', 'BJ', 'Donga'),
(257, 'KO', 'BJ', 'Kouffo'),
(258, 'LI', 'BJ', 'Littoral'),
(259, 'MO', 'BJ', 'Mono'),
(260, 'OU', 'BJ', 'Ouémé'),
(261, 'PL', 'BJ', 'Plateau'),
(262, 'ZO', 'BJ', 'Zou'),
(263, '33', 'BT', 'Bumthang'),
(264, '12', 'BT', 'Chhukha'),
(265, '22', 'BT', 'Dagana'),
(266, 'GA', 'BT', 'Gasa'),
(267, '13', 'BT', 'Ha'),
(268, '44', 'BT', 'Lhuentse'),
(269, '42', 'BT', 'Monggar'),
(270, '11', 'BT', 'Paro'),
(271, '43', 'BT', 'Pemagatshel'),
(272, '23', 'BT', 'Punakha'),
(273, '45', 'BT', 'Samdrup Jongkha'),
(274, '14', 'BT', 'Samtse'),
(275, '31', 'BT', 'Sarpang'),
(276, '15', 'BT', 'Thimphu'),
(277, 'TY', 'BT', 'Trashi Yangtse'),
(278, '41', 'BT', 'Trashigang'),
(279, '32', 'BT', 'Trongsa'),
(280, '21', 'BT', 'Tsirang'),
(281, '24', 'BT', 'Wangdue Phodrang'),
(282, '34', 'BT', 'Zhemgang'),
(283, 'H', 'BO', 'Chuquisaca'),
(284, 'C', 'BO', 'Cochabamba'),
(285, 'B', 'BO', 'El Beni'),
(286, 'L', 'BO', 'La Paz'),
(287, 'O', 'BO', 'Oruro'),
(288, 'N', 'BO', 'Pando'),
(289, 'P', 'BO', 'Potosí'),
(290, 'S', 'BO', 'Santa Cruz'),
(291, 'T', 'BO', 'Tarija'),
(292, 'BRC', 'BA', 'Brčko distrikt'),
(293, 'BIH', 'BA', 'Federacija Bosna i Hercegovina'),
(294, 'SRP', 'BA', 'Republika Srpska'),
(295, 'CE', 'BW', 'Central'),
(296, 'CH', 'BW', 'Chobe'),
(297, 'FR', 'BW', 'Francistown'),
(298, 'GA', 'BW', 'Gaborone'),
(299, 'GH', 'BW', 'Ghanzi'),
(300, 'JW', 'BW', 'Jwaneng'),
(301, 'KG', 'BW', 'Kgalagadi'),
(302, 'KL', 'BW', 'Kgatleng'),
(303, 'KW', 'BW', 'Kweneng'),
(304, 'LO', 'BW', 'Lobatse'),
(305, 'NE', 'BW', 'North-East'),
(306, 'NW', 'BW', 'North-West'),
(307, 'SP', 'BW', 'Selibe Phikwe'),
(308, 'SE', 'BW', 'South-East'),
(309, 'SO', 'BW', 'Southern'),
(310, 'ST', 'BW', 'Sowa Town'),
(311, 'AC', 'BR', 'Acre'),
(312, 'AL', 'BR', 'Alagoas'),
(313, 'AP', 'BR', 'Amapá'),
(314, 'AM', 'BR', 'Amazonas'),
(315, 'BA', 'BR', 'Bahia'),
(316, 'CE', 'BR', 'Ceará'),
(317, 'DF', 'BR', 'Distrito Federal'),
(318, 'ES', 'BR', 'Espírito Santo'),
(319, 'GO', 'BR', 'Goiás'),
(320, 'MA', 'BR', 'Maranhão'),
(321, 'MT', 'BR', 'Mato Grosso'),
(322, 'MS', 'BR', 'Mato Grosso do Sul'),
(323, 'MG', 'BR', 'Minas Gerais'),
(324, 'PR', 'BR', 'Paraná'),
(325, 'PB', 'BR', 'Paraíba'),
(326, 'PA', 'BR', 'Pará'),
(327, 'PE', 'BR', 'Pernambuco'),
(328, 'PI', 'BR', 'Piauí'),
(329, 'RN', 'BR', 'Rio Grande do Norte'),
(330, 'RS', 'BR', 'Rio Grande do Sul'),
(331, 'RJ', 'BR', 'Rio de Janeiro'),
(332, 'RO', 'BR', 'Rondônia'),
(333, 'RR', 'BR', 'Roraima'),
(334, 'SC', 'BR', 'Santa Catarina'),
(335, 'SE', 'BR', 'Sergipe'),
(336, 'SP', 'BR', 'São Paulo'),
(337, 'TO', 'BR', 'Tocantins'),
(338, '81', 'UM', 'Baker Island'),
(339, '84', 'UM', 'Howland Island'),
(340, '86', 'UM', 'Jarvis Island'),
(341, '67', 'UM', 'Johnston Atoll'),
(342, '89', 'UM', 'Kingman Reef'),
(343, '71', 'UM', 'Midway Islands'),
(344, '76', 'UM', 'Navassa Island'),
(345, '95', 'UM', 'Palmyra Atoll'),
(346, '79', 'UM', 'Wake Island'),
(347, 'BE', 'BN', 'Belait'),
(348, 'BM', 'BN', 'Brunei-Muara'),
(349, 'TE', 'BN', 'Temburong'),
(350, 'TU', 'BN', 'Tutong'),
(351, '01', 'BG', 'Blagoevgrad'),
(352, '02', 'BG', 'Burgas'),
(353, '08', 'BG', 'Dobrich'),
(354, '07', 'BG', 'Gabrovo'),
(355, '26', 'BG', 'Haskovo'),
(356, '09', 'BG', 'Kardzhali'),
(357, '10', 'BG', 'Kyustendil'),
(358, '11', 'BG', 'Lovech'),
(359, '12', 'BG', 'Montana'),
(360, '13', 'BG', 'Pazardzhik'),
(361, '14', 'BG', 'Pernik'),
(362, '15', 'BG', 'Pleven'),
(363, '16', 'BG', 'Plovdiv'),
(364, '17', 'BG', 'Razgrad'),
(365, '18', 'BG', 'Ruse'),
(366, '27', 'BG', 'Shumen'),
(367, '19', 'BG', 'Silistra'),
(368, '20', 'BG', 'Sliven'),
(369, '21', 'BG', 'Smolyan'),
(370, '23', 'BG', 'Sofia'),
(371, '22', 'BG', 'Sofia-Grad'),
(372, '24', 'BG', 'Stara Zagora'),
(373, '25', 'BG', 'Targovishte'),
(374, '03', 'BG', 'Varna'),
(375, '04', 'BG', 'Veliko Tarnovo'),
(376, '05', 'BG', 'Vidin'),
(377, '06', 'BG', 'Vratsa'),
(378, '28', 'BG', 'Yambol'),
(379, '01', 'BF', 'Boucle du Mouhoun'),
(380, '02', 'BF', 'Cascades'),
(381, '03', 'BF', 'Centre'),
(382, '04', 'BF', 'Centre-Est'),
(383, '05', 'BF', 'Centre-Nord'),
(384, '06', 'BF', 'Centre-Ouest'),
(385, '07', 'BF', 'Centre-Sud'),
(386, '08', 'BF', 'Est'),
(387, '09', 'BF', 'Hauts-Bassins'),
(388, '10', 'BF', 'Nord'),
(389, '11', 'BF', 'Plateau-Central'),
(390, '12', 'BF', 'Sahel'),
(391, '13', 'BF', 'Sud-Ouest'),
(392, 'BB', 'BI', 'Bubanza'),
(393, 'BM', 'BI', 'Bujumbura Mairie'),
(394, 'BL', 'BI', 'Bujumbura Rural'),
(395, 'BR', 'BI', 'Bururi'),
(396, 'CA', 'BI', 'Cankuzo'),
(397, 'CI', 'BI', 'Cibitoke'),
(398, 'GI', 'BI', 'Gitega'),
(399, 'KR', 'BI', 'Karuzi'),
(400, 'KY', 'BI', 'Kayanza'),
(401, 'KI', 'BI', 'Kirundo'),
(402, 'MA', 'BI', 'Makamba'),
(403, 'MU', 'BI', 'Muramvya'),
(404, 'MY', 'BI', 'Muyinga'),
(405, 'MW', 'BI', 'Mwaro'),
(406, 'NG', 'BI', 'Ngozi'),
(407, 'RT', 'BI', 'Rutana'),
(408, 'RY', 'BI', 'Ruyigi'),
(409, '2', 'KH', 'Baat Dambang'),
(410, '1', 'KH', 'Banteay Mean Chey'),
(411, '3', 'KH', 'Kampong Chaam'),
(412, '4', 'KH', 'Kampong Chhnang'),
(413, '5', 'KH', 'Kampong Spueu'),
(414, '6', 'KH', 'Kampong Thum'),
(415, '7', 'KH', 'Kampot'),
(416, '8', 'KH', 'Kandaal'),
(417, '9', 'KH', 'Kaoh Kong'),
(418, '10', 'KH', 'Kracheh'),
(419, '23', 'KH', 'Krong Kaeb'),
(420, '24', 'KH', 'Krong Pailin'),
(421, '18', 'KH', 'Krong Preah Sihanouk'),
(422, '11', 'KH', 'Mondol Kiri'),
(423, '22', 'KH', 'Otdar Mean Chey'),
(424, '12', 'KH', 'Phnom Penh'),
(425, '15', 'KH', 'Pousaat'),
(426, '13', 'KH', 'Preah Vihear'),
(427, '14', 'KH', 'Prey Veaeng'),
(428, '16', 'KH', 'Rotanak Kiri'),
(429, '17', 'KH', 'Siem Reab'),
(430, '19', 'KH', 'Stueng Traeng'),
(431, '20', 'KH', 'Svaay Rieng'),
(432, '21', 'KH', 'Taakaev'),
(433, 'AD', 'CM', 'Adamaoua'),
(434, 'CE', 'CM', 'Centre'),
(435, 'ES', 'CM', 'East'),
(436, 'EN', 'CM', 'Far North'),
(437, 'LT', 'CM', 'Littoral'),
(438, 'NO', 'CM', 'North'),
(439, 'NW', 'CM', 'North-West'),
(440, 'SU', 'CM', 'South'),
(441, 'SW', 'CM', 'South-West'),
(442, 'OU', 'CM', 'West'),
(443, 'AB', 'CA', 'Alberta'),
(444, 'BC', 'CA', 'British Columbia'),
(445, 'MB', 'CA', 'Manitoba'),
(446, 'NB', 'CA', 'New Brunswick'),
(447, 'NL', 'CA', 'Newfoundland and Labrador'),
(448, 'NS', 'CA', 'Nova Scotia'),
(449, 'ON', 'CA', 'Ontario'),
(450, 'PE', 'CA', 'Prince Edward Island'),
(451, 'QC', 'CA', 'Quebec'),
(452, 'SK', 'CA', 'Saskatchewan'),
(453, 'NT', 'CA', 'Northwest Territories'),
(454, 'NU', 'CA', 'Nunavut'),
(455, 'YT', 'CA', 'Yukon'),
(456, 'B', 'CV', 'Ilhas de Barlavento'),
(457, 'S', 'CV', 'Ilhas de Sotavento'),
(458, 'BB', 'CF', 'Bamingui-Bangoran'),
(459, 'BGF', 'CF', 'Bangui'),
(460, 'BK', 'CF', 'Basse-Kotto'),
(461, 'KB', 'CF', 'Gribingui'),
(462, 'HM', 'CF', 'Haut-Mbomou'),
(463, 'HK', 'CF', 'Haute-Kotto'),
(464, 'HS', 'CF', 'Haute-Sangha / Mambéré-Kadéï'),
(465, 'KG', 'CF', 'Kémo-Gribingui'),
(466, 'LB', 'CF', 'Lobaye'),
(467, 'MB', 'CF', 'Mbomou'),
(468, 'NM', 'CF', 'Nana-Mambéré'),
(469, 'MP', 'CF', 'Ombella-Mpoko'),
(470, 'UK', 'CF', 'Ouaka'),
(471, 'AC', 'CF', 'Ouham'),
(472, 'OP', 'CF', 'Ouham-Pendé'),
(473, 'SE', 'CF', 'Sangha'),
(474, 'VK', 'CF', 'Vakaga'),
(475, 'BA', 'TD', 'Al Baṭḩah'),
(476, 'LC', 'TD', 'Al Buḩayrah'),
(477, 'BG', 'TD', 'Baḩr al Ghazāl'),
(478, 'BO', 'TD', 'Būrkū'),
(479, 'EN', 'TD', 'Innīdī'),
(480, 'KA', 'TD', 'Kānim'),
(481, 'LO', 'TD', 'Lūqūn al Gharbī'),
(482, 'LR', 'TD', 'Lūqūn ash Sharqī'),
(483, 'ND', 'TD', 'Madīnat Injamīnā'),
(484, 'MA', 'TD', 'Māndūl'),
(485, 'MO', 'TD', 'Māyū Kībbī al Gharbī'),
(486, 'ME', 'TD', 'Māyū Kībbī ash Sharqī'),
(487, 'GR', 'TD', 'Qīrā'),
(488, 'SA', 'TD', 'Salāmāt'),
(489, 'CB', 'TD', 'Shārī Bāqirmī'),
(490, 'MC', 'TD', 'Shārī al Awsaṭ'),
(491, 'SI', 'TD', 'Sīlā'),
(492, 'TI', 'TD', 'Tibastī'),
(493, 'TA', 'TD', 'Tānjilī'),
(494, 'OD', 'TD', 'Waddāy'),
(495, 'WF', 'TD', 'Wādī Fīrā'),
(496, 'HL', 'TD', 'Ḥajjar Lamīs'),
(497, 'AI', 'CL', 'Aisén del General Carlos Ibañez del Campo'),
(498, 'AN', 'CL', 'Antofagasta'),
(499, 'AR', 'CL', 'Araucanía'),
(500, 'AP', 'CL', 'Arica y Parinacota'),
(501, 'AT', 'CL', 'Atacama'),
(502, 'BI', 'CL', 'Bío-Bío'),
(503, 'CO', 'CL', 'Coquimbo'),
(504, 'LI', 'CL', 'Libertador General Bernardo O\'Higgins'),
(505, 'LL', 'CL', 'Los Lagos'),
(506, 'LR', 'CL', 'Los Ríos'),
(507, 'MA', 'CL', 'Magallanes'),
(508, 'ML', 'CL', 'Maule'),
(509, 'RM', 'CL', 'Región Metropolitana de Santiago'),
(510, 'TA', 'CL', 'Tarapacá'),
(511, 'VS', 'CL', 'Valparaíso'),
(512, '45', 'CN', 'Guangxi'),
(513, '15', 'CN', 'Nei Mongol'),
(514, '64', 'CN', 'Ningxia'),
(515, '65', 'CN', 'Xinjiang'),
(516, '54', 'CN', 'Xizang'),
(517, '11', 'CN', 'Beijing'),
(518, '50', 'CN', 'Chongqing'),
(519, '31', 'CN', 'Shanghai'),
(520, '12', 'CN', 'Tianjin'),
(521, '34', 'CN', 'Anhui'),
(522, '35', 'CN', 'Fujian'),
(523, '62', 'CN', 'Gansu'),
(524, '44', 'CN', 'Guangdong'),
(525, '52', 'CN', 'Guizhou'),
(526, '46', 'CN', 'Hainan'),
(527, '13', 'CN', 'Hebei'),
(528, '23', 'CN', 'Heilongjiang'),
(529, '41', 'CN', 'Henan'),
(530, '42', 'CN', 'Hubei'),
(531, '43', 'CN', 'Hunan'),
(532, '32', 'CN', 'Jiangsu'),
(533, '36', 'CN', 'Jiangxi'),
(534, '22', 'CN', 'Jilin'),
(535, '21', 'CN', 'Liaoning'),
(536, '63', 'CN', 'Qinghai'),
(537, '61', 'CN', 'Shaanxi'),
(538, '37', 'CN', 'Shandong'),
(539, '14', 'CN', 'Shanxi'),
(540, '51', 'CN', 'Sichuan'),
(541, '71', 'CN', 'Taiwan'),
(542, '53', 'CN', 'Yunnan'),
(543, '33', 'CN', 'Zhejiang'),
(544, '91', 'CN', 'Hong Kong'),
(545, '92', 'CN', 'Macao'),
(546, '', 'CN', 'Hong Kong Island'),
(547, 'KOWLO', 'CN', 'Kowloon'),
(548, 'NEW T', 'CN', 'New Territories'),
(549, 'AMA', 'CO', 'Amazonas'),
(550, 'ANT', 'CO', 'Antioquia'),
(551, 'ARA', 'CO', 'Arauca'),
(552, 'ATL', 'CO', 'Atlántico'),
(553, 'BOL', 'CO', 'Bolívar'),
(554, 'BOY', 'CO', 'Boyacá'),
(555, 'CAL', 'CO', 'Caldas'),
(556, 'CAQ', 'CO', 'Caquetá'),
(557, 'CAS', 'CO', 'Casanare'),
(558, 'CAU', 'CO', 'Cauca'),
(559, 'CES', 'CO', 'Cesar'),
(560, 'CHO', 'CO', 'Chocó'),
(561, 'CUN', 'CO', 'Cundinamarca'),
(562, 'COR', 'CO', 'Córdoba'),
(563, 'DC', 'CO', 'Distrito Capital de Bogotá'),
(564, 'GUA', 'CO', 'Guainía'),
(565, 'GUV', 'CO', 'Guaviare'),
(566, 'HUI', 'CO', 'Huila'),
(567, 'LAG', 'CO', 'La Guajira'),
(568, 'MAG', 'CO', 'Magdalena'),
(569, 'MET', 'CO', 'Meta'),
(570, 'NAR', 'CO', 'Nariño'),
(571, 'NSA', 'CO', 'Norte de Santander'),
(572, 'PUT', 'CO', 'Putumayo'),
(573, 'QUI', 'CO', 'Quindío'),
(574, 'RIS', 'CO', 'Risaralda'),
(575, 'SAP', 'CO', 'San Andrés, Providencia y Santa Catalina'),
(576, 'SAN', 'CO', 'Santander'),
(577, 'SUC', 'CO', 'Sucre'),
(578, 'TOL', 'CO', 'Tolima'),
(579, 'VAC', 'CO', 'Valle del Cauca'),
(580, 'VAU', 'CO', 'Vaupés'),
(581, 'VID', 'CO', 'Vichada'),
(582, 'A', 'KM', 'Anjouan'),
(583, 'G', 'KM', 'Grande Comore'),
(584, 'M', 'KM', 'Mohéli'),
(585, '11', 'CG', 'Bouenza'),
(586, 'BZV', 'CG', 'Brazzaville'),
(587, '8', 'CG', 'Cuvette'),
(588, '15', 'CG', 'Cuvette-Ouest'),
(589, '5', 'CG', 'Kouilou'),
(590, '7', 'CG', 'Likouala'),
(591, '2', 'CG', 'Lékoumou'),
(592, '9', 'CG', 'Niari'),
(593, '14', 'CG', 'Plateaux'),
(594, '16', 'CG', 'Pointe-Noire'),
(595, '12', 'CG', 'Pool'),
(596, '13', 'CG', 'Sangha'),
(597, 'BN', 'CD', 'Bandundu'),
(598, 'BC', 'CD', 'Bas-Congo'),
(599, 'KW', 'CD', 'Kasai-Occidental'),
(600, 'KE', 'CD', 'Kasai-Oriental'),
(601, 'KA', 'CD', 'Katanga'),
(602, 'KN', 'CD', 'Kinshasa'),
(603, 'MA', 'CD', 'Maniema'),
(604, 'NK', 'CD', 'Nord-Kivu'),
(605, 'OR', 'CD', 'Orientale'),
(606, 'SK', 'CD', 'Sud-Kivu'),
(607, 'EQ', 'CD', 'Équateur'),
(608, 'A', 'CR', 'Alajuela'),
(609, 'C', 'CR', 'Cartago'),
(610, 'G', 'CR', 'Guanacaste'),
(611, 'H', 'CR', 'Heredia'),
(612, 'L', 'CR', 'Limón'),
(613, 'P', 'CR', 'Puntarenas'),
(614, 'SJ', 'CR', 'San José'),
(615, '07', 'HR', 'Bjelovarsko-bilogorska županija'),
(616, '12', 'HR', 'Brodsko-posavska županija'),
(617, '19', 'HR', 'Dubrovačko-neretvanska županija'),
(618, '21', 'HR', 'Grad Zagreb'),
(619, '18', 'HR', 'Istarska županija'),
(620, '04', 'HR', 'Karlovačka županija'),
(621, '06', 'HR', 'Koprivničko-križevačka županija'),
(622, '02', 'HR', 'Krapinsko-zagorska županija'),
(623, '09', 'HR', 'Ličko-senjska županija'),
(624, '20', 'HR', 'Međimurska županija'),
(625, '14', 'HR', 'Osječko-baranjska županija'),
(626, '11', 'HR', 'Požeško-slavonska županija'),
(627, '08', 'HR', 'Primorsko-goranska županija'),
(628, '03', 'HR', 'Sisačko-moslavačka županija'),
(629, '17', 'HR', 'Splitsko-dalmatinska županija'),
(630, '05', 'HR', 'Varaždinska županija'),
(631, '10', 'HR', 'Virovitičko-podravska županija'),
(632, '16', 'HR', 'Vukovarsko-srijemska županija'),
(633, '13', 'HR', 'Zadarska županija'),
(634, '01', 'HR', 'Zagrebačka županija'),
(635, '15', 'HR', 'Šibensko-kninska županija'),
(636, '15', 'CU', 'Artemisa'),
(637, '09', 'CU', 'Camagüey'),
(638, '08', 'CU', 'Ciego de Ávila'),
(639, '06', 'CU', 'Cienfuegos'),
(640, '12', 'CU', 'Granma'),
(641, '14', 'CU', 'Guantánamo'),
(642, '11', 'CU', 'Holguín'),
(643, '99', 'CU', 'Isla de la Juventud'),
(644, '03', 'CU', 'La Habana'),
(645, '10', 'CU', 'Las Tunas'),
(646, '04', 'CU', 'Matanzas'),
(647, '16', 'CU', 'Mayabeque'),
(648, '01', 'CU', 'Pinar del Río'),
(649, '07', 'CU', 'Sancti Spíritus'),
(650, '13', 'CU', 'Santiago de Cuba'),
(651, '05', 'CU', 'Villa Clara'),
(652, '04', 'CY', 'Ammochostos'),
(653, '06', 'CY', 'Keryneia'),
(654, '03', 'CY', 'Larnaka'),
(655, '01', 'CY', 'Lefkosia'),
(656, '02', 'CY', 'Lemesos'),
(657, '05', 'CY', 'Pafos'),
(658, 'JM', 'CZ', 'Jihomoravský kraj'),
(659, 'JC', 'CZ', 'Jihočeský kraj'),
(660, 'KA', 'CZ', 'Karlovarský kraj'),
(661, 'KR', 'CZ', 'Královéhradecký kraj'),
(662, 'LI', 'CZ', 'Liberecký kraj'),
(663, 'MO', 'CZ', 'Moravskoslezský kraj'),
(664, 'OL', 'CZ', 'Olomoucký kraj'),
(665, 'PA', 'CZ', 'Pardubický kraj'),
(666, 'PL', 'CZ', 'Plzeňský kraj'),
(667, 'PR', 'CZ', 'Praha, hlavní město'),
(668, 'ST', 'CZ', 'Středočeský kraj'),
(669, 'VY', 'CZ', 'Vysočina'),
(670, 'ZL', 'CZ', 'Zlínský kraj'),
(671, 'US', 'CZ', 'Ústecký kraj'),
(672, '84', 'DK', 'Hovedstaden'),
(673, '82', 'DK', 'Midtjylland'),
(674, '81', 'DK', 'Nordjylland'),
(675, '85', 'DK', 'Sjælland'),
(676, '83', 'DK', 'Syddanmark'),
(677, 'AS', 'DJ', 'Ali Sabieh'),
(678, 'AR', 'DJ', 'Arta'),
(679, 'DI', 'DJ', 'Dikhil'),
(680, 'DJ', 'DJ', 'Djibouti'),
(681, 'OB', 'DJ', 'Obock'),
(682, 'TA', 'DJ', 'Tadjourah'),
(683, '02', 'DM', 'Saint Andrew'),
(684, '03', 'DM', 'Saint David'),
(685, '04', 'DM', 'Saint George'),
(686, '05', 'DM', 'Saint John'),
(687, '06', 'DM', 'Saint Joseph'),
(688, '07', 'DM', 'Saint Luke'),
(689, '08', 'DM', 'Saint Mark'),
(690, '09', 'DM', 'Saint Patrick'),
(691, '10', 'DM', 'Saint Paul'),
(692, '11', 'DM', 'Saint Peter'),
(693, '33', 'DO', 'Cibao Nordeste'),
(694, '34', 'DO', 'Cibao Noroeste'),
(695, '35', 'DO', 'Cibao Norte'),
(696, '36', 'DO', 'Cibao Sur'),
(697, '37', 'DO', 'El Valle'),
(698, '38', 'DO', 'Enriquillo'),
(699, '39', 'DO', 'Higuamo'),
(700, '40', 'DO', 'Ozama'),
(701, '41', 'DO', 'Valdesia'),
(702, '42', 'DO', 'Yuma'),
(703, 'A', 'EC', 'Azuay'),
(704, 'B', 'EC', 'Bolívar'),
(705, 'C', 'EC', 'Carchi'),
(706, 'F', 'EC', 'Cañar'),
(707, 'H', 'EC', 'Chimborazo'),
(708, 'X', 'EC', 'Cotopaxi'),
(709, 'O', 'EC', 'El Oro'),
(710, 'E', 'EC', 'Esmeraldas'),
(711, 'W', 'EC', 'Galápagos'),
(712, 'G', 'EC', 'Guayas'),
(713, 'I', 'EC', 'Imbabura'),
(714, 'L', 'EC', 'Loja'),
(715, 'R', 'EC', 'Los Ríos'),
(716, 'M', 'EC', 'Manabí'),
(717, 'S', 'EC', 'Morona-Santiago'),
(718, 'N', 'EC', 'Napo'),
(719, 'D', 'EC', 'Orellana'),
(720, 'Y', 'EC', 'Pastaza'),
(721, 'P', 'EC', 'Pichincha'),
(722, 'SE', 'EC', 'Santa Elena'),
(723, 'SD', 'EC', 'Santo Domingo de los Tsáchilas'),
(724, 'U', 'EC', 'Sucumbíos'),
(725, 'T', 'EC', 'Tungurahua'),
(726, 'Z', 'EC', 'Zamora-Chinchipe'),
(727, 'DK', 'EG', 'Ad Daqahlīyah'),
(728, 'BA', 'EG', 'Al Baḩr al Aḩmar'),
(729, 'BH', 'EG', 'Al Buḩayrah'),
(730, 'FYM', 'EG', 'Al Fayyūm'),
(731, 'GH', 'EG', 'Al Gharbīyah'),
(732, 'ALX', 'EG', 'Al Iskandarīyah'),
(733, 'IS', 'EG', 'Al Ismāٰīlīyah'),
(734, 'GZ', 'EG', 'Al Jīzah'),
(735, 'MN', 'EG', 'Al Minyā'),
(736, 'MNF', 'EG', 'Al Minūfīyah'),
(737, 'KB', 'EG', 'Al Qalyūbīyah'),
(738, 'C', 'EG', 'Al Qāhirah'),
(739, 'LX', 'EG', 'Al Uqşur'),
(740, 'WAD', 'EG', 'Al Wādī al Jadīd'),
(741, 'SUZ', 'EG', 'As Suways'),
(742, 'SU', 'EG', 'As Sādis min Uktūbar'),
(743, 'SHR', 'EG', 'Ash Sharqīyah'),
(744, 'ASN', 'EG', 'Aswān'),
(745, 'AST', 'EG', 'Asyūţ'),
(746, 'BNS', 'EG', 'Banī Suwayf'),
(747, 'PTS', 'EG', 'Būr Saٰīd'),
(748, 'DT', 'EG', 'Dumyāţ'),
(749, 'JS', 'EG', 'Janūb Sīnā\''),
(750, 'KFS', 'EG', 'Kafr ash Shaykh'),
(751, 'MT', 'EG', 'Maţrūḩ'),
(752, 'KN', 'EG', 'Qinā'),
(753, 'SIN', 'EG', 'Shamāl Sīnā\''),
(754, 'SHG', 'EG', 'Sūhāj'),
(755, 'HU', 'EG', 'Ḩulwān'),
(756, 'AH', 'SV', 'Ahuachapán'),
(757, 'CA', 'SV', 'Cabañas'),
(758, 'CH', 'SV', 'Chalatenango'),
(759, 'CU', 'SV', 'Cuscatlán'),
(760, 'LI', 'SV', 'La Libertad'),
(761, 'PA', 'SV', 'La Paz'),
(762, 'UN', 'SV', 'La Unión'),
(763, 'MO', 'SV', 'Morazán'),
(764, 'SM', 'SV', 'San Miguel'),
(765, 'SS', 'SV', 'San Salvador'),
(766, 'SV', 'SV', 'San Vicente'),
(767, 'SA', 'SV', 'Santa Ana'),
(768, 'SO', 'SV', 'Sonsonate'),
(769, 'US', 'SV', 'Usulután'),
(770, 'C', 'GQ', 'Región Continental'),
(771, 'I', 'GQ', 'Región Insular'),
(772, 'MA', 'ER', 'Al Awsaţ'),
(773, 'DU', 'ER', 'Al Janūbĩ'),
(774, 'AN', 'ER', 'Ansabā'),
(775, 'DK', 'ER', 'Janūbī al Baḩrī al Aḩmar'),
(776, 'GB', 'ER', 'Qāsh-Barkah'),
(777, 'SK', 'ER', 'Shimālī al Baḩrī al Aḩmar'),
(778, '37', 'EE', 'Harjumaa'),
(779, '39', 'EE', 'Hiiumaa'),
(780, '44', 'EE', 'Ida-Virumaa'),
(781, '51', 'EE', 'Järvamaa'),
(782, '49', 'EE', 'Jõgevamaa'),
(783, '59', 'EE', 'Lääne-Virumaa'),
(784, '57', 'EE', 'Läänemaa'),
(785, '67', 'EE', 'Pärnumaa'),
(786, '65', 'EE', 'Põlvamaa'),
(787, '70', 'EE', 'Raplamaa'),
(788, '74', 'EE', 'Saaremaa'),
(789, '78', 'EE', 'Tartumaa'),
(790, '82', 'EE', 'Valgamaa'),
(791, '84', 'EE', 'Viljandimaa'),
(792, '86', 'EE', 'Võrumaa'),
(793, 'BE', 'ET', 'Bīnshangul Gumuz'),
(794, 'DD', 'ET', 'Dirē Dawa'),
(795, 'GA', 'ET', 'Gambēla Hizboch'),
(796, 'HA', 'ET', 'Hārerī Hizb'),
(797, 'OR', 'ET', 'Oromīya'),
(798, 'SO', 'ET', 'Sumalē'),
(799, 'TI', 'ET', 'Tigray'),
(800, 'SN', 'ET', 'YeDebub Bihēroch Bihēreseboch na Hizboch'),
(801, 'AA', 'ET', 'Ādīs Ābeba'),
(802, 'AF', 'ET', 'Āfar'),
(803, 'AM', 'ET', 'Āmara'),
(804, 'C', 'FJ', 'Central'),
(805, 'E', 'FJ', 'Eastern'),
(806, 'N', 'FJ', 'Northern'),
(807, 'R', 'FJ', 'Rotuma'),
(808, 'W', 'FJ', 'Western'),
(809, '01', 'FI', 'Ahvenanmaan maakunta'),
(810, '02', 'FI', 'Etelä-Karjala'),
(811, '03', 'FI', 'Etelä-Pohjanmaa'),
(812, '04', 'FI', 'Etelä-Savo'),
(813, '05', 'FI', 'Kainuu'),
(814, '06', 'FI', 'Kanta-Häme'),
(815, '07', 'FI', 'Keski-Pohjanmaa'),
(816, '08', 'FI', 'Keski-Suomi'),
(817, '09', 'FI', 'Kymenlaakso'),
(818, '10', 'FI', 'Lappi'),
(819, '11', 'FI', 'Pirkanmaa'),
(820, '12', 'FI', 'Pohjanmaa'),
(821, '13', 'FI', 'Pohjois-Karjala'),
(822, '14', 'FI', 'Pohjois-Pohjanmaa'),
(823, '15', 'FI', 'Pohjois-Savo'),
(824, '16', 'FI', 'Päijät-Häme'),
(825, '17', 'FI', 'Satakunta'),
(826, '18', 'FI', 'Uusimaa'),
(827, '19', 'FI', 'Varsinais-Suomi'),
(828, 'A', 'FR', 'Alsace'),
(829, 'B', 'FR', 'Aquitaine'),
(830, 'C', 'FR', 'Auvergne'),
(831, 'E', 'FR', 'Brittany'),
(832, 'D', 'FR', 'Burgundy'),
(833, 'F', 'FR', 'Centre-Val de Loire'),
(834, 'G', 'FR', 'Champagne-Ardenne'),
(835, 'H', 'FR', 'Corsica'),
(836, 'I', 'FR', 'Franche-Comté'),
(837, 'K', 'FR', 'Languedoc-Roussillon'),
(838, 'L', 'FR', 'Limousin'),
(839, 'M', 'FR', 'Lorraine'),
(840, 'P', 'FR', 'Lower Normandy'),
(841, 'N', 'FR', 'Midi-Pyrénées'),
(842, 'O', 'FR', 'Nord-Pas-de-Calais'),
(843, 'R', 'FR', 'Pays de la Loire'),
(844, 'S', 'FR', 'Picardy'),
(845, 'T', 'FR', 'Poitou-Charentes'),
(846, 'U', 'FR', 'Provence-Alpes-Côte d\'Azur'),
(847, 'V', 'FR', 'Rhône-Alpes'),
(848, 'Q', 'FR', 'Upper Normandy'),
(849, 'J', 'FR', 'Île-de-France'),
(850, '1', 'GA', 'Estuaire'),
(851, '2', 'GA', 'Haut-Ogooué'),
(852, '3', 'GA', 'Moyen-Ogooué'),
(853, '4', 'GA', 'Ngounié'),
(854, '5', 'GA', 'Nyanga'),
(855, '6', 'GA', 'Ogooué-Ivindo'),
(856, '7', 'GA', 'Ogooué-Lolo'),
(857, '8', 'GA', 'Ogooué-Maritime'),
(858, '9', 'GA', 'Woleu-Ntem'),
(859, 'B', 'GM', 'Banjul'),
(860, 'M', 'GM', 'Central River'),
(861, 'L', 'GM', 'Lower River'),
(862, 'N', 'GM', 'North Bank'),
(863, 'U', 'GM', 'Upper River'),
(864, 'W', 'GM', 'Western'),
(865, 'AB', 'GE', 'Abkhazia'),
(866, 'AJ', 'GE', 'Ajaria'),
(867, 'GU', 'GE', 'Guria'),
(868, 'IM', 'GE', 'Imereti'),
(869, 'KA', 'GE', 'K\'akheti'),
(870, 'KK', 'GE', 'Kvemo Kartli'),
(871, 'MM', 'GE', 'Mtskheta-Mtianeti'),
(872, 'RL', 'GE', 'Rach\'a-Lechkhumi-Kvemo Svaneti'),
(873, 'SZ', 'GE', 'Samegrelo-Zemo Svaneti'),
(874, 'SJ', 'GE', 'Samtskhe-Javakheti'),
(875, 'SK', 'GE', 'Shida Kartli'),
(876, 'TB', 'GE', 'Tbilisi'),
(877, 'BW', 'DE', 'Baden-Württemberg'),
(878, 'BY', 'DE', 'Bayern'),
(879, 'BE', 'DE', 'Berlin'),
(880, 'BB', 'DE', 'Brandenburg'),
(881, 'HB', 'DE', 'Bremen'),
(882, 'HH', 'DE', 'Hamburg'),
(883, 'HE', 'DE', 'Hessen'),
(884, 'MV', 'DE', 'Mecklenburg-Vorpommern'),
(885, 'NI', 'DE', 'Niedersachsen'),
(886, 'NW', 'DE', 'Nordrhein-Westfalen'),
(887, 'RP', 'DE', 'Rheinland-Pfalz'),
(888, 'SL', 'DE', 'Saarland'),
(889, 'SN', 'DE', 'Sachsen'),
(890, 'ST', 'DE', 'Sachsen-Anhalt'),
(891, 'SH', 'DE', 'Schleswig-Holstein'),
(892, 'TH', 'DE', 'Thüringen'),
(893, 'AH', 'GH', 'Ashanti'),
(894, 'BA', 'GH', 'Brong-Ahafo'),
(895, 'CP', 'GH', 'Central'),
(896, 'EP', 'GH', 'Eastern'),
(897, 'AA', 'GH', 'Greater Accra'),
(898, 'NP', 'GH', 'Northern'),
(899, 'UE', 'GH', 'Upper East'),
(900, 'UW', 'GH', 'Upper West'),
(901, 'TV', 'GH', 'Volta'),
(902, 'WP', 'GH', 'Western'),
(903, 'A', 'GR', 'Anatoliki Makedonia kai Thraki'),
(904, 'I', 'GR', 'Attiki'),
(905, 'G', 'GR', 'Dytiki Ellada'),
(906, 'C', 'GR', 'Dytiki Makedonia'),
(907, 'F', 'GR', 'Ionia Nisia'),
(908, 'D', 'GR', 'Ipeiros'),
(909, 'B', 'GR', 'Kentriki Makedonia'),
(910, 'M', 'GR', 'Kriti'),
(911, 'L', 'GR', 'Notio Aigaio'),
(912, 'J', 'GR', 'Peloponnisos'),
(913, 'H', 'GR', 'Sterea Ellada'),
(914, 'E', 'GR', 'Thessalia'),
(915, 'K', 'GR', 'Voreio Aigaio'),
(916, 'KU', 'GL', 'Kommune Kujalleq'),
(917, 'SM', 'GL', 'Kommuneqarfik Sermersooq'),
(918, 'QA', 'GL', 'Qaasuitsup Kommunia'),
(919, 'QE', 'GL', 'Qeqqata Kommunia'),
(920, '01', 'GD', 'Saint Andrew'),
(921, '02', 'GD', 'Saint David'),
(922, '03', 'GD', 'Saint George'),
(923, '04', 'GD', 'Saint John'),
(924, '05', 'GD', 'Saint Mark'),
(925, '06', 'GD', 'Saint Patrick'),
(926, '10', 'GD', 'Southern Grenadine Islands'),
(927, 'AV', 'GT', 'Alta Verapaz'),
(928, 'BV', 'GT', 'Baja Verapaz'),
(929, 'CM', 'GT', 'Chimaltenango'),
(930, 'CQ', 'GT', 'Chiquimula'),
(931, 'PR', 'GT', 'El Progreso'),
(932, 'ES', 'GT', 'Escuintla'),
(933, 'GU', 'GT', 'Guatemala'),
(934, 'HU', 'GT', 'Huehuetenango'),
(935, 'IZ', 'GT', 'Izabal'),
(936, 'JA', 'GT', 'Jalapa'),
(937, 'JU', 'GT', 'Jutiapa'),
(938, 'PE', 'GT', 'Petén'),
(939, 'QZ', 'GT', 'Quetzaltenango'),
(940, 'QC', 'GT', 'Quiché'),
(941, 'RE', 'GT', 'Retalhuleu'),
(942, 'SA', 'GT', 'Sacatepéquez'),
(943, 'SM', 'GT', 'San Marcos'),
(944, 'SR', 'GT', 'Santa Rosa'),
(945, 'SO', 'GT', 'Sololá'),
(946, 'SU', 'GT', 'Suchitepéquez'),
(947, 'TO', 'GT', 'Totonicapán'),
(948, 'ZA', 'GT', 'Zacapa'),
(949, 'B', 'GN', 'Boké'),
(950, 'C', 'GN', 'Conakry'),
(951, 'F', 'GN', 'Faranah'),
(952, 'K', 'GN', 'Kankan'),
(953, 'D', 'GN', 'Kindia'),
(954, 'L', 'GN', 'Labé'),
(955, 'M', 'GN', 'Mamou'),
(956, 'N', 'GN', 'Nzérékoré'),
(957, 'L', 'GW', 'Leste'),
(958, 'N', 'GW', 'Norte'),
(959, 'S', 'GW', 'Sul'),
(960, 'BA', 'GY', 'Barima-Waini'),
(961, 'CU', 'GY', 'Cuyuni-Mazaruni'),
(962, 'DE', 'GY', 'Demerara-Mahaica'),
(963, 'EB', 'GY', 'East Berbice-Corentyne'),
(964, 'ES', 'GY', 'Essequibo Islands-West Demerara'),
(965, 'MA', 'GY', 'Mahaica-Berbice'),
(966, 'PM', 'GY', 'Pomeroon-Supenaam'),
(967, 'PT', 'GY', 'Potaro-Siparuni'),
(968, 'UD', 'GY', 'Upper Demerara-Berbice'),
(969, 'UT', 'GY', 'Upper Takutu-Upper Essequibo'),
(970, 'AR', 'HT', 'Artibonite'),
(971, 'CE', 'HT', 'Centre'),
(972, 'GA', 'HT', 'Grande-Anse'),
(973, 'NI', 'HT', 'Nippes'),
(974, 'ND', 'HT', 'Nord'),
(975, 'NE', 'HT', 'Nord-Est'),
(976, 'NO', 'HT', 'Nord-Ouest'),
(977, 'OU', 'HT', 'Ouest'),
(978, 'SD', 'HT', 'Sud'),
(979, 'SE', 'HT', 'Sud-Est'),
(980, 'AT', 'HN', 'Atlántida'),
(981, 'CH', 'HN', 'Choluteca'),
(982, 'CL', 'HN', 'Colón'),
(983, 'CM', 'HN', 'Comayagua'),
(984, 'CP', 'HN', 'Copán'),
(985, 'CR', 'HN', 'Cortés'),
(986, 'EP', 'HN', 'El Paraíso'),
(987, 'FM', 'HN', 'Francisco Morazán'),
(988, 'GD', 'HN', 'Gracias a Dios'),
(989, 'IN', 'HN', 'Intibucá'),
(990, 'IB', 'HN', 'Islas de la Bahía'),
(991, 'LP', 'HN', 'La Paz'),
(992, 'LE', 'HN', 'Lempira'),
(993, 'OC', 'HN', 'Ocotepeque'),
(994, 'OL', 'HN', 'Olancho'),
(995, 'SB', 'HN', 'Santa Bárbara'),
(996, 'VA', 'HN', 'Valle'),
(997, 'YO', 'HN', 'Yoro'),
(998, 'BA', 'HU', 'Baranya'),
(999, 'BZ', 'HU', 'Borsod-Abaúj-Zemplén'),
(1000, 'BU', 'HU', 'Budapest'),
(1001, 'BK', 'HU', 'Bács-Kiskun'),
(1002, 'BE', 'HU', 'Békés'),
(1003, 'BC', 'HU', 'Békéscsaba'),
(1004, 'CS', 'HU', 'Csongrád'),
(1005, 'DE', 'HU', 'Debrecen'),
(1006, 'DU', 'HU', 'Dunaújváros'),
(1007, 'EG', 'HU', 'Eger'),
(1008, 'FE', 'HU', 'Fejér'),
(1009, 'GY', 'HU', 'Győr'),
(1010, 'GS', 'HU', 'Győr-Moson-Sopron'),
(1011, 'HB', 'HU', 'Hajdú-Bihar'),
(1012, 'HE', 'HU', 'Heves'),
(1013, 'HV', 'HU', 'Hódmezővásárhely'),
(1014, 'JN', 'HU', 'Jász-Nagykun-Szolnok'),
(1015, 'KV', 'HU', 'Kaposvár'),
(1016, 'KM', 'HU', 'Kecskemét'),
(1017, 'KE', 'HU', 'Komárom-Esztergom'),
(1018, 'MI', 'HU', 'Miskolc'),
(1019, 'NK', 'HU', 'Nagykanizsa'),
(1020, 'NY', 'HU', 'Nyíregyháza'),
(1021, 'NO', 'HU', 'Nógrád'),
(1022, 'PE', 'HU', 'Pest'),
(1023, 'PS', 'HU', 'Pécs'),
(1024, 'ST', 'HU', 'Salgótarján'),
(1025, 'SO', 'HU', 'Somogy'),
(1026, 'SN', 'HU', 'Sopron'),
(1027, 'SZ', 'HU', 'Szabolcs-Szatmár-Bereg'),
(1028, 'SD', 'HU', 'Szeged'),
(1029, 'SS', 'HU', 'Szekszárd'),
(1030, 'SK', 'HU', 'Szolnok'),
(1031, 'SH', 'HU', 'Szombathely'),
(1032, 'SF', 'HU', 'Székesfehérvár'),
(1033, 'TB', 'HU', 'Tatabánya'),
(1034, 'TO', 'HU', 'Tolna'),
(1035, 'VA', 'HU', 'Vas'),
(1036, 'VE', 'HU', 'Veszprém'),
(1037, 'VM', 'HU', 'Veszprém'),
(1038, 'ZA', 'HU', 'Zala'),
(1039, 'ZE', 'HU', 'Zalaegerszeg'),
(1040, 'ER', 'HU', 'Érd'),
(1041, '7', 'IS', 'Austurland'),
(1042, '1', 'IS', 'Höfuðborgarsvæði utan Reykjavíkur'),
(1043, '6', 'IS', 'Norðurland eystra'),
(1044, '5', 'IS', 'Norðurland vestra'),
(1045, '0', 'IS', 'Reykjavík'),
(1046, '8', 'IS', 'Suðurland'),
(1047, '2', 'IS', 'Suðurnes'),
(1048, '4', 'IS', 'Vestfirðir'),
(1049, '3', 'IS', 'Vesturland'),
(1050, 'AN', 'IN', 'Andaman and Nicobar Islands'),
(1051, 'CH', 'IN', 'Chandigarh'),
(1052, 'DN', 'IN', 'Dadra and Nagar Haveli'),
(1053, 'DD', 'IN', 'Daman and Diu'),
(1054, 'DL', 'IN', 'Delhi'),
(1055, 'LD', 'IN', 'Lakshadweep'),
(1056, 'PY', 'IN', 'Puducherry'),
(1057, 'AP', 'IN', 'Andhra Pradesh'),
(1058, 'AR', 'IN', 'Arunachal Pradesh'),
(1059, 'AS', 'IN', 'Assam'),
(1060, 'BR', 'IN', 'Bihar'),
(1061, 'CT', 'IN', 'Chhattisgarh'),
(1062, 'GA', 'IN', 'Goa'),
(1063, 'GJ', 'IN', 'Gujarat'),
(1064, 'HR', 'IN', 'Haryana'),
(1065, 'HP', 'IN', 'Himachal Pradesh'),
(1066, 'JK', 'IN', 'Jammu and Kashmir'),
(1067, 'JH', 'IN', 'Jharkhand'),
(1068, 'KA', 'IN', 'Karnataka'),
(1069, 'KL', 'IN', 'Kerala'),
(1070, 'MP', 'IN', 'Madhya Pradesh'),
(1071, 'MH', 'IN', 'Maharashtra'),
(1072, 'MN', 'IN', 'Manipur'),
(1073, 'ML', 'IN', 'Meghalaya'),
(1074, 'MZ', 'IN', 'Mizoram'),
(1075, 'NL', 'IN', 'Nagaland'),
(1076, 'OR', 'IN', 'Odisha'),
(1077, 'PB', 'IN', 'Punjab'),
(1078, 'RJ', 'IN', 'Rajasthan'),
(1079, 'SK', 'IN', 'Sikkim'),
(1080, 'TN', 'IN', 'Tamil Nadu'),
(1081, 'TG', 'IN', 'Telangana'),
(1082, 'TR', 'IN', 'Tripura'),
(1083, 'UP', 'IN', 'Uttar Pradesh'),
(1084, 'UT', 'IN', 'Uttarakhand'),
(1085, 'WB', 'IN', 'West Bengal'),
(1086, 'JW', 'ID', 'Jawa'),
(1087, 'KA', 'ID', 'Kalimantan'),
(1088, 'ML', 'ID', 'Maluku'),
(1089, 'NU', 'ID', 'Nusa Tenggara'),
(1090, 'PP', 'ID', 'Papua'),
(1091, 'SL', 'ID', 'Sulawesi'),
(1092, 'SM', 'ID', 'Sumatera'),
(1093, '06', 'CI', '18 Montagnes'),
(1094, '16', 'CI', 'Agnébi'),
(1095, '17', 'CI', 'Bafing'),
(1096, '09', 'CI', 'Bas-Sassandra'),
(1097, '10', 'CI', 'Denguélé'),
(1098, '18', 'CI', 'Fromager'),
(1099, '02', 'CI', 'Haut-Sassandra'),
(1100, '07', 'CI', 'Lacs'),
(1101, '01', 'CI', 'Lagunes'),
(1102, '12', 'CI', 'Marahoué'),
(1103, '19', 'CI', 'Moyen-Cavally'),
(1104, '05', 'CI', 'Moyen-Comoé'),
(1105, '11', 'CI', 'Nzi-Comoé'),
(1106, '03', 'CI', 'Savanes'),
(1107, '15', 'CI', 'Sud-Bandama'),
(1108, '13', 'CI', 'Sud-Comoé'),
(1109, '04', 'CI', 'Vallée du Bandama'),
(1110, '14', 'CI', 'Worodougou'),
(1111, '08', 'CI', 'Zanzan'),
(1112, '32', 'IR', 'Alborz'),
(1113, '03', 'IR', 'Ardabīl'),
(1114, '06', 'IR', 'Būshehr'),
(1115, '08', 'IR', 'Chahār Maḩāll va Bakhtīārī'),
(1116, '04', 'IR', 'Eşfahān'),
(1117, '14', 'IR', 'Fārs'),
(1118, '27', 'IR', 'Golestān'),
(1119, '19', 'IR', 'Gīlān'),
(1120, '24', 'IR', 'Hamadān'),
(1121, '23', 'IR', 'Hormozgān'),
(1122, '15', 'IR', 'Kermān'),
(1123, '17', 'IR', 'Kermānshāh'),
(1124, '29', 'IR', 'Khorāsān-e Janūbī'),
(1125, '30', 'IR', 'Khorāsān-e Razavī'),
(1126, '31', 'IR', 'Khorāsān-e Shemālī'),
(1127, '10', 'IR', 'Khūzestān'),
(1128, '18', 'IR', 'Kohgīlūyeh va Būyer Aḩmad'),
(1129, '16', 'IR', 'Kordestān'),
(1130, '20', 'IR', 'Lorestān'),
(1131, '22', 'IR', 'Markazī'),
(1132, '21', 'IR', 'Māzandarān'),
(1133, '28', 'IR', 'Qazvīn'),
(1134, '26', 'IR', 'Qom'),
(1135, '12', 'IR', 'Semnān'),
(1136, '13', 'IR', 'Sīstān va Balūchestān'),
(1137, '07', 'IR', 'Tehrān'),
(1138, '25', 'IR', 'Yazd'),
(1139, '11', 'IR', 'Zanjān'),
(1140, '02', 'IR', 'Āz̄arbāyjān-e Gharbī'),
(1141, '01', 'IR', 'Āz̄arbāyjān-e Sharqī'),
(1142, '05', 'IR', 'Īlām'),
(1143, 'AN', 'IQ', 'Al Anbār'),
(1144, 'BA', 'IQ', 'Al Başrah'),
(1145, 'MU', 'IQ', 'Al Muthanná'),
(1146, 'QA', 'IQ', 'Al Qādisīyah'),
(1147, 'NA', 'IQ', 'An Najaf'),
(1148, 'AR', 'IQ', 'Arbīl'),
(1149, 'SU', 'IQ', 'As Sulaymānīyah'),
(1150, 'TS', 'IQ', 'At Ta\'mīm'),
(1151, 'BG', 'IQ', 'Baghdād'),
(1152, 'BB', 'IQ', 'Bābil'),
(1153, 'DA', 'IQ', 'Dahūk'),
(1154, 'DQ', 'IQ', 'Dhī Qār'),
(1155, 'DI', 'IQ', 'Diyālá'),
(1156, 'KA', 'IQ', 'Karbalā\''),
(1157, 'MA', 'IQ', 'Maysān'),
(1158, 'NI', 'IQ', 'Nīnawá'),
(1159, 'WA', 'IQ', 'Wāsiţ'),
(1160, 'SD', 'IQ', 'Şalāḩ ad Dīn'),
(1161, 'C', 'IE', 'Connaught'),
(1162, 'L', 'IE', 'Leinster'),
(1163, 'M', 'IE', 'Munster'),
(1164, 'U', 'IE', 'Ulster'),
(1165, 'D', 'IL', 'HaDarom'),
(1166, 'M', 'IL', 'HaMerkaz'),
(1167, 'Z', 'IL', 'HaTsafon'),
(1168, 'HA', 'IL', 'H̱efa'),
(1169, 'TA', 'IL', 'Tel-Aviv'),
(1170, 'JM', 'IL', 'Yerushalayim'),
(1171, '65', 'IT', 'Abruzzo'),
(1172, '77', 'IT', 'Basilicata'),
(1173, '78', 'IT', 'Calabria'),
(1174, '72', 'IT', 'Campania'),
(1175, '45', 'IT', 'Emilia-Romagna'),
(1176, '36', 'IT', 'Friuli-Venezia Giulia'),
(1177, '62', 'IT', 'Lazio'),
(1178, '42', 'IT', 'Liguria'),
(1179, '25', 'IT', 'Lombardia'),
(1180, '57', 'IT', 'Marche'),
(1181, '67', 'IT', 'Molise'),
(1182, '21', 'IT', 'Piemonte'),
(1183, '75', 'IT', 'Puglia'),
(1184, '88', 'IT', 'Sardegna'),
(1185, '82', 'IT', 'Sicilia'),
(1186, '52', 'IT', 'Toscana'),
(1187, '32', 'IT', 'Trentino-Alto Adige'),
(1188, '55', 'IT', 'Umbria'),
(1189, '23', 'IT', 'Valle d\'Aosta'),
(1190, '34', 'IT', 'Veneto'),
(1191, '13', 'JM', 'Clarendon'),
(1192, '09', 'JM', 'Hanover'),
(1193, '01', 'JM', 'Kingston'),
(1194, '12', 'JM', 'Manchester'),
(1195, '04', 'JM', 'Portland'),
(1196, '02', 'JM', 'Saint Andrew'),
(1197, '06', 'JM', 'Saint Ann'),
(1198, '14', 'JM', 'Saint Catherine'),
(1199, '11', 'JM', 'Saint Elizabeth'),
(1200, '08', 'JM', 'Saint James'),
(1201, '05', 'JM', 'Saint Mary'),
(1202, '03', 'JM', 'Saint Thomas'),
(1203, '07', 'JM', 'Trelawny'),
(1204, '10', 'JM', 'Westmoreland'),
(1205, '23', 'JP', 'Aiti'),
(1206, '05', 'JP', 'Akita'),
(1207, '02', 'JP', 'Aomori'),
(1208, '38', 'JP', 'Ehime'),
(1209, '21', 'JP', 'Gihu'),
(1210, '10', 'JP', 'Gunma'),
(1211, '34', 'JP', 'Hirosima'),
(1212, '01', 'JP', 'Hokkaidô'),
(1213, '18', 'JP', 'Hukui'),
(1214, '40', 'JP', 'Hukuoka'),
(1215, '07', 'JP', 'Hukusima'),
(1216, '28', 'JP', 'Hyôgo'),
(1217, '08', 'JP', 'Ibaraki'),
(1218, '17', 'JP', 'Isikawa'),
(1219, '03', 'JP', 'Iwate'),
(1220, '37', 'JP', 'Kagawa'),
(1221, '46', 'JP', 'Kagosima'),
(1222, '14', 'JP', 'Kanagawa'),
(1223, '43', 'JP', 'Kumamoto'),
(1224, '26', 'JP', 'Kyôto'),
(1225, '39', 'JP', 'Kôti'),
(1226, '24', 'JP', 'Mie'),
(1227, '04', 'JP', 'Miyagi'),
(1228, '45', 'JP', 'Miyazaki'),
(1229, '20', 'JP', 'Nagano'),
(1230, '42', 'JP', 'Nagasaki'),
(1231, '29', 'JP', 'Nara'),
(1232, '15', 'JP', 'Niigata'),
(1233, '33', 'JP', 'Okayama'),
(1234, '47', 'JP', 'Okinawa'),
(1235, '41', 'JP', 'Saga'),
(1236, '11', 'JP', 'Saitama'),
(1237, '25', 'JP', 'Siga'),
(1238, '32', 'JP', 'Simane'),
(1239, '22', 'JP', 'Sizuoka'),
(1240, '12', 'JP', 'Tiba'),
(1241, '36', 'JP', 'Tokusima'),
(1242, '09', 'JP', 'Totigi'),
(1243, '31', 'JP', 'Tottori'),
(1244, '16', 'JP', 'Toyama'),
(1245, '13', 'JP', 'Tôkyô'),
(1246, '30', 'JP', 'Wakayama'),
(1247, '06', 'JP', 'Yamagata'),
(1248, '35', 'JP', 'Yamaguti'),
(1249, '19', 'JP', 'Yamanasi'),
(1250, '44', 'JP', 'Ôita'),
(1251, '27', 'JP', 'Ôsaka'),
(1252, 'BA', 'JO', 'Al Balqā\''),
(1253, 'AQ', 'JO', 'Al ʽAqabah'),
(1254, 'AZ', 'JO', 'Az Zarqā\''),
(1255, 'AT', 'JO', 'Aţ Ţafīlah'),
(1256, 'IR', 'JO', 'Irbid'),
(1257, 'JA', 'JO', 'Jerash'),
(1258, 'KA', 'JO', 'Karak'),
(1259, 'MN', 'JO', 'Ma\'ān'),
(1260, 'MA', 'JO', 'Mafraq'),
(1261, 'MD', 'JO', 'Mādabā'),
(1262, 'AJ', 'JO', 'ʽAjlūn'),
(1263, 'AM', 'JO', '‘Ammān'),
(1264, 'ALA', 'KZ', 'Almaty'),
(1265, 'ALM', 'KZ', 'Almaty oblysy'),
(1266, 'AKM', 'KZ', 'Aqmola oblysy'),
(1267, 'AKT', 'KZ', 'Aqtöbe oblysy'),
(1268, 'AST', 'KZ', 'Astana'),
(1269, 'ATY', 'KZ', 'Atyraū oblysy'),
(1270, 'ZAP', 'KZ', 'Batys Qazaqstan oblysy'),
(1271, 'MAN', 'KZ', 'Mangghystaū oblysy'),
(1272, 'YUZ', 'KZ', 'Ongtüstik Qazaqstan oblysy'),
(1273, 'PAV', 'KZ', 'Pavlodar oblysy'),
(1274, 'KAR', 'KZ', 'Qaraghandy oblysy'),
(1275, 'KUS', 'KZ', 'Qostanay oblysy'),
(1276, 'KZY', 'KZ', 'Qyzylorda oblysy'),
(1277, 'VOS', 'KZ', 'Shyghys Qazaqstan oblysy'),
(1278, 'SEV', 'KZ', 'Soltüstik Qazaqstan oblysy'),
(1279, 'ZHA', 'KZ', 'Zhambyl oblysy'),
(1280, '200', 'KE', 'Central'),
(1281, '300', 'KE', 'Coast'),
(1282, '400', 'KE', 'Eastern'),
(1283, '110', 'KE', 'Nairobi'),
(1284, '500', 'KE', 'North-Eastern'),
(1285, '600', 'KE', 'Nyanza'),
(1286, '700', 'KE', 'Rift Valley'),
(1287, '800', 'KE', 'Western'),
(1288, 'G', 'KI', 'Gilbert Islands'),
(1289, 'L', 'KI', 'Line Islands'),
(1290, 'P', 'KI', 'Phoenix Islands'),
(1291, 'AH', 'KW', 'Al Aḩmadi'),
(1292, 'FA', 'KW', 'Al Farwānīyah'),
(1293, 'JA', 'KW', 'Al Jahrā’'),
(1294, 'KU', 'KW', 'Al Kuwayt'),
(1295, 'MU', 'KW', 'Mubārak al Kabīr'),
(1296, 'HA', 'KW', 'Ḩawallī'),
(1297, 'B', 'KG', 'Batken'),
(1298, 'GB', 'KG', 'Bishkek'),
(1299, 'C', 'KG', 'Chü'),
(1300, 'J', 'KG', 'Jalal-Abad'),
(1301, 'N', 'KG', 'Naryn'),
(1302, 'O', 'KG', 'Osh'),
(1303, 'T', 'KG', 'Talas'),
(1304, 'Y', 'KG', 'Ysyk-Köl'),
(1305, 'AT', 'LA', 'Attapu'),
(1306, 'BK', 'LA', 'Bokèo'),
(1307, 'BL', 'LA', 'Bolikhamxai'),
(1308, 'CH', 'LA', 'Champasak'),
(1309, 'HO', 'LA', 'Houaphan'),
(1310, 'KH', 'LA', 'Khammouan'),
(1311, 'LM', 'LA', 'Louang Namtha'),
(1312, 'LP', 'LA', 'Louangphabang'),
(1313, 'OU', 'LA', 'Oudômxai'),
(1314, 'PH', 'LA', 'Phôngsali'),
(1315, 'SL', 'LA', 'Salavan'),
(1316, 'SV', 'LA', 'Savannakhét'),
(1317, 'VT', 'LA', 'Vientiane'),
(1318, 'VI', 'LA', 'Vientiane'),
(1319, 'XA', 'LA', 'Xaignabouli'),
(1320, 'XN', 'LA', 'Xaisômboun'),
(1321, 'XI', 'LA', 'Xiangkhoang'),
(1322, 'XE', 'LA', 'Xékong'),
(1323, '001', 'LV', 'Aglonas novads'),
(1324, '002', 'LV', 'Aizkraukles novads'),
(1325, '003', 'LV', 'Aizputes novads'),
(1326, '004', 'LV', 'Aknīstes novads'),
(1327, '005', 'LV', 'Alojas novads'),
(1328, '006', 'LV', 'Alsungas novads'),
(1329, '007', 'LV', 'Alūksnes novads'),
(1330, '008', 'LV', 'Amatas novads'),
(1331, '009', 'LV', 'Apes novads'),
(1332, '010', 'LV', 'Auces novads'),
(1333, '012', 'LV', 'Babītes novads'),
(1334, '013', 'LV', 'Baldones novads'),
(1335, '014', 'LV', 'Baltinavas novads'),
(1336, '015', 'LV', 'Balvu novads'),
(1337, '016', 'LV', 'Bauskas novads'),
(1338, '017', 'LV', 'Beverīnas novads'),
(1339, '018', 'LV', 'Brocēnu novads'),
(1340, '019', 'LV', 'Burtnieku novads'),
(1341, '020', 'LV', 'Carnikavas novads'),
(1342, '021', 'LV', 'Cesvaines novads'),
(1343, '023', 'LV', 'Ciblas novads'),
(1344, '022', 'LV', 'Cēsu novads'),
(1345, '024', 'LV', 'Dagdas novads'),
(1346, 'DGV', 'LV', 'Daugavpils'),
(1347, '025', 'LV', 'Daugavpils novads'),
(1348, '026', 'LV', 'Dobeles novads'),
(1349, '027', 'LV', 'Dundagas novads'),
(1350, '028', 'LV', 'Durbes novads'),
(1351, '029', 'LV', 'Engures novads'),
(1352, '031', 'LV', 'Garkalnes novads'),
(1353, '032', 'LV', 'Grobiņas novads'),
(1354, '033', 'LV', 'Gulbenes novads'),
(1355, '034', 'LV', 'Iecavas novads'),
(1356, '035', 'LV', 'Ikšķiles novads'),
(1357, '036', 'LV', 'Ilūkstes novads'),
(1358, '037', 'LV', 'Inčukalna novads'),
(1359, '038', 'LV', 'Jaunjelgavas novads'),
(1360, '039', 'LV', 'Jaunpiebalgas novads'),
(1361, '040', 'LV', 'Jaunpils novads'),
(1362, 'JEL', 'LV', 'Jelgava'),
(1363, '041', 'LV', 'Jelgavas novads'),
(1364, 'JKB', 'LV', 'Jēkabpils'),
(1365, '042', 'LV', 'Jēkabpils novads'),
(1366, 'JUR', 'LV', 'Jūrmala'),
(1367, '043', 'LV', 'Kandavas novads'),
(1368, '045', 'LV', 'Kocēnu novads'),
(1369, '046', 'LV', 'Kokneses novads'),
(1370, '048', 'LV', 'Krimuldas novads'),
(1371, '049', 'LV', 'Krustpils novads'),
(1372, '047', 'LV', 'Krāslavas novads'),
(1373, '050', 'LV', 'Kuldīgas novads'),
(1374, '044', 'LV', 'Kārsavas novads'),
(1375, '053', 'LV', 'Lielvārdes novads'),
(1376, 'LPX', 'LV', 'Liepāja'),
(1377, '054', 'LV', 'Limbažu novads'),
(1378, '057', 'LV', 'Lubānas novads'),
(1379, '058', 'LV', 'Ludzas novads'),
(1380, '055', 'LV', 'Līgatnes novads'),
(1381, '056', 'LV', 'Līvānu novads'),
(1382, '059', 'LV', 'Madonas novads'),
(1383, '060', 'LV', 'Mazsalacas novads'),
(1384, '061', 'LV', 'Mālpils novads'),
(1385, '062', 'LV', 'Mārupes novads'),
(1386, '063', 'LV', 'Mērsraga novads'),
(1387, '064', 'LV', 'Naukšēnu novads'),
(1388, '065', 'LV', 'Neretas novads'),
(1389, '066', 'LV', 'Nīcas novads'),
(1390, '067', 'LV', 'Ogres novads'),
(1391, '068', 'LV', 'Olaines novads'),
(1392, '069', 'LV', 'Ozolnieku novads'),
(1393, '073', 'LV', 'Preiļu novads'),
(1394, '074', 'LV', 'Priekules novads'),
(1395, '075', 'LV', 'Priekuļu novads'),
(1396, '070', 'LV', 'Pārgaujas novads'),
(1397, '071', 'LV', 'Pāvilostas novads'),
(1398, '072', 'LV', 'Pļaviņu novads'),
(1399, '076', 'LV', 'Raunas novads'),
(1400, '078', 'LV', 'Riebiņu novads'),
(1401, '079', 'LV', 'Rojas novads'),
(1402, '080', 'LV', 'Ropažu novads'),
(1403, '081', 'LV', 'Rucavas novads'),
(1404, '082', 'LV', 'Rugāju novads'),
(1405, '083', 'LV', 'Rundāles novads'),
(1406, 'REZ', 'LV', 'Rēzekne'),
(1407, '077', 'LV', 'Rēzeknes novads'),
(1408, 'RIX', 'LV', 'Rīga'),
(1409, '084', 'LV', 'Rūjienas novads'),
(1410, '086', 'LV', 'Salacgrīvas novads'),
(1411, '085', 'LV', 'Salas novads'),
(1412, '087', 'LV', 'Salaspils novads'),
(1413, '088', 'LV', 'Saldus novads'),
(1414, '089', 'LV', 'Saulkrastu novads'),
(1415, '091', 'LV', 'Siguldas novads'),
(1416, '093', 'LV', 'Skrundas novads'),
(1417, '092', 'LV', 'Skrīveru novads'),
(1418, '094', 'LV', 'Smiltenes novads'),
(1419, '095', 'LV', 'Stopiņu novads'),
(1420, '096', 'LV', 'Strenču novads'),
(1421, '090', 'LV', 'Sējas novads'),
(1422, '097', 'LV', 'Talsu novads'),
(1423, '099', 'LV', 'Tukuma novads'),
(1424, '098', 'LV', 'Tērvetes novads'),
(1425, '100', 'LV', 'Vaiņodes novads'),
(1426, '101', 'LV', 'Valkas novads'),
(1427, 'VMR', 'LV', 'Valmiera'),
(1428, '102', 'LV', 'Varakļānu novads'),
(1429, '104', 'LV', 'Vecpiebalgas novads'),
(1430, '105', 'LV', 'Vecumnieku novads'),
(1431, 'VEN', 'LV', 'Ventspils'),
(1432, '106', 'LV', 'Ventspils novads'),
(1433, '107', 'LV', 'Viesītes novads'),
(1434, '108', 'LV', 'Viļakas novads'),
(1435, '109', 'LV', 'Viļānu novads'),
(1436, '103', 'LV', 'Vārkavas novads'),
(1437, '110', 'LV', 'Zilupes novads'),
(1438, '011', 'LV', 'Ādažu novads'),
(1439, '030', 'LV', 'Ērgļu novads'),
(1440, '051', 'LV', 'Ķeguma novads'),
(1441, '052', 'LV', 'Ķekavas novads'),
(1442, 'AK', 'LB', 'Aakkâr'),
(1443, 'BH', 'LB', 'Baalbek-Hermel'),
(1444, 'BA', 'LB', 'Beyrouth'),
(1445, 'BI', 'LB', 'Béqaa'),
(1446, 'AS', 'LB', 'Liban-Nord'),
(1447, 'JA', 'LB', 'Liban-Sud'),
(1448, 'JL', 'LB', 'Mont-Liban'),
(1449, 'NA', 'LB', 'Nabatîyé'),
(1450, 'D', 'LS', 'Berea'),
(1451, 'B', 'LS', 'Butha-Buthe'),
(1452, 'C', 'LS', 'Leribe'),
(1453, 'E', 'LS', 'Mafeteng'),
(1454, 'A', 'LS', 'Maseru'),
(1455, 'F', 'LS', 'Mohale\'s Hoek'),
(1456, 'J', 'LS', 'Mokhotlong'),
(1457, 'H', 'LS', 'Qacha\'s Nek'),
(1458, 'G', 'LS', 'Quthing'),
(1459, 'K', 'LS', 'Thaba-Tseka'),
(1460, 'BM', 'LR', 'Bomi'),
(1461, 'BG', 'LR', 'Bong'),
(1462, 'GP', 'LR', 'Gbarpolu'),
(1463, 'GB', 'LR', 'Grand Bassa'),
(1464, 'CM', 'LR', 'Grand Cape Mount'),
(1465, 'GG', 'LR', 'Grand Gedeh'),
(1466, 'GK', 'LR', 'Grand Kru'),
(1467, 'LO', 'LR', 'Lofa'),
(1468, 'MG', 'LR', 'Margibi'),
(1469, 'MY', 'LR', 'Maryland'),
(1470, 'MO', 'LR', 'Montserrado'),
(1471, 'NI', 'LR', 'Nimba'),
(1472, 'RG', 'LR', 'River Gee'),
(1473, 'RI', 'LR', 'Rivercess'),
(1474, 'SI', 'LR', 'Sinoe'),
(1475, 'BU', 'LY', 'Al Buţnān'),
(1476, 'JA', 'LY', 'Al Jabal al Akhḑar'),
(1477, 'JG', 'LY', 'Al Jabal al Gharbī'),
(1478, 'JI', 'LY', 'Al Jifārah'),
(1479, 'JU', 'LY', 'Al Jufrah'),
(1480, 'KF', 'LY', 'Al Kufrah'),
(1481, 'MJ', 'LY', 'Al Marj'),
(1482, 'MB', 'LY', 'Al Marqab'),
(1483, 'WA', 'LY', 'Al Wāḩāt'),
(1484, 'NQ', 'LY', 'An Nuqaţ al Khams'),
(1485, 'ZA', 'LY', 'Az Zāwiyah'),
(1486, 'BA', 'LY', 'Banghāzī'),
(1487, 'DR', 'LY', 'Darnah'),
(1488, 'GT', 'LY', 'Ghāt'),
(1489, 'MI', 'LY', 'Mişrātah'),
(1490, 'MQ', 'LY', 'Murzuq'),
(1491, 'NL', 'LY', 'Nālūt'),
(1492, 'SB', 'LY', 'Sabhā'),
(1493, 'SR', 'LY', 'Surt'),
(1494, 'WD', 'LY', 'Wādī al Ḩayāt'),
(1495, 'WS', 'LY', 'Wādī ash Shāţiʾ'),
(1496, 'TB', 'LY', 'Ţarābulus'),
(1497, '01', 'LI', 'Balzers'),
(1498, '02', 'LI', 'Eschen'),
(1499, '03', 'LI', 'Gamprin'),
(1500, '04', 'LI', 'Mauren'),
(1501, '05', 'LI', 'Planken'),
(1502, '06', 'LI', 'Ruggell'),
(1503, '07', 'LI', 'Schaan'),
(1504, '08', 'LI', 'Schellenberg'),
(1505, '09', 'LI', 'Triesen'),
(1506, '10', 'LI', 'Triesenberg'),
(1507, '11', 'LI', 'Vaduz'),
(1508, 'AL', 'LT', 'Alytaus Apskritis'),
(1509, 'KU', 'LT', 'Kauno Apskritis'),
(1510, 'KL', 'LT', 'Klaipėdos Apskritis'),
(1511, 'MR', 'LT', 'Marijampolės Apskritis'),
(1512, 'PN', 'LT', 'Panevėžio Apskritis'),
(1513, 'TA', 'LT', 'Tauragės Apskritis'),
(1514, 'TE', 'LT', 'Telšių Apskritis'),
(1515, 'UT', 'LT', 'Utenos Apskritis'),
(1516, 'VL', 'LT', 'Vilniaus Apskritis'),
(1517, 'SA', 'LT', 'Šiaulių Apskritis'),
(1518, 'D', 'LU', 'Diekirch'),
(1519, 'G', 'LU', 'Grevenmacher'),
(1520, 'L', 'LU', 'Luxembourg'),
(1521, '01', 'MK', 'Aerodrom'),
(1522, '02', 'MK', 'Aračinovo'),
(1523, '03', 'MK', 'Berovo'),
(1524, '04', 'MK', 'Bitola'),
(1525, '05', 'MK', 'Bogdanci'),
(1526, '06', 'MK', 'Bogovinje'),
(1527, '07', 'MK', 'Bosilovo'),
(1528, '08', 'MK', 'Brvenica'),
(1529, '09', 'MK', 'Butel'),
(1530, '77', 'MK', 'Centar'),
(1531, '78', 'MK', 'Centar Župa'),
(1532, '21', 'MK', 'Debar'),
(1533, '22', 'MK', 'Debarca'),
(1534, '23', 'MK', 'Delčevo'),
(1535, '25', 'MK', 'Demir Hisar'),
(1536, '24', 'MK', 'Demir Kapija'),
(1537, '26', 'MK', 'Dojran'),
(1538, '27', 'MK', 'Dolneni'),
(1539, '28', 'MK', 'Drugovo'),
(1540, '17', 'MK', 'Gazi Baba'),
(1541, '18', 'MK', 'Gevgelija'),
(1542, '29', 'MK', 'Gjorče Petrov'),
(1543, '19', 'MK', 'Gostivar'),
(1544, '20', 'MK', 'Gradsko'),
(1545, '34', 'MK', 'Ilinden'),
(1546, '35', 'MK', 'Jegunovce'),
(1547, '37', 'MK', 'Karbinci'),
(1548, '38', 'MK', 'Karpoš'),
(1549, '36', 'MK', 'Kavadarci'),
(1550, '39', 'MK', 'Kisela Voda'),
(1551, '40', 'MK', 'Kičevo'),
(1552, '41', 'MK', 'Konče'),
(1553, '42', 'MK', 'Kočani'),
(1554, '43', 'MK', 'Kratovo'),
(1555, '44', 'MK', 'Kriva Palanka'),
(1556, '45', 'MK', 'Krivogaštani'),
(1557, '46', 'MK', 'Kruševo'),
(1558, '47', 'MK', 'Kumanovo'),
(1559, '48', 'MK', 'Lipkovo'),
(1560, '49', 'MK', 'Lozovo'),
(1561, '51', 'MK', 'Makedonska Kamenica'),
(1562, '52', 'MK', 'Makedonski Brod'),
(1563, '50', 'MK', 'Mavrovo i Rostuša'),
(1564, '53', 'MK', 'Mogila'),
(1565, '54', 'MK', 'Negotino'),
(1566, '55', 'MK', 'Novaci'),
(1567, '56', 'MK', 'Novo Selo'),
(1568, '58', 'MK', 'Ohrid'),
(1569, '57', 'MK', 'Oslomej'),
(1570, '60', 'MK', 'Pehčevo'),
(1571, '59', 'MK', 'Petrovec'),
(1572, '61', 'MK', 'Plasnica'),
(1573, '62', 'MK', 'Prilep'),
(1574, '63', 'MK', 'Probištip'),
(1575, '64', 'MK', 'Radoviš'),
(1576, '65', 'MK', 'Rankovce'),
(1577, '66', 'MK', 'Resen'),
(1578, '67', 'MK', 'Rosoman'),
(1579, '68', 'MK', 'Saraj'),
(1580, '70', 'MK', 'Sopište'),
(1581, '71', 'MK', 'Staro Nagoričane'),
(1582, '72', 'MK', 'Struga'),
(1583, '73', 'MK', 'Strumica'),
(1584, '74', 'MK', 'Studeničani'),
(1585, '69', 'MK', 'Sveti Nikole');
INSERT INTO `Countries_states` (`id`, `Code`, `Country`, `Name`) VALUES
(1586, '75', 'MK', 'Tearce'),
(1587, '76', 'MK', 'Tetovo'),
(1588, '10', 'MK', 'Valandovo'),
(1589, '11', 'MK', 'Vasilevo'),
(1590, '13', 'MK', 'Veles'),
(1591, '12', 'MK', 'Vevčani'),
(1592, '14', 'MK', 'Vinica'),
(1593, '15', 'MK', 'Vraneštica'),
(1594, '16', 'MK', 'Vrapčište'),
(1595, '31', 'MK', 'Zajas'),
(1596, '32', 'MK', 'Zelenikovo'),
(1597, '33', 'MK', 'Zrnovci'),
(1598, '79', 'MK', 'Čair'),
(1599, '80', 'MK', 'Čaška'),
(1600, '81', 'MK', 'Češinovo-Obleševo'),
(1601, '82', 'MK', 'Čučer Sandevo'),
(1602, '83', 'MK', 'Štip'),
(1603, '84', 'MK', 'Šuto Orizari'),
(1604, '30', 'MK', 'Želino'),
(1605, 'T', 'MG', 'Antananarivo'),
(1606, 'D', 'MG', 'Antsiranana'),
(1607, 'F', 'MG', 'Fianarantsoa'),
(1608, 'M', 'MG', 'Mahajanga'),
(1609, 'A', 'MG', 'Toamasina'),
(1610, 'U', 'MG', 'Toliara'),
(1611, 'C', 'MW', 'Central Region'),
(1612, 'N', 'MW', 'Northern Region'),
(1613, 'S', 'MW', 'Southern Region'),
(1614, '14', 'MY', 'Wilayah Persekutuan Kuala Lumpur'),
(1615, '15', 'MY', 'Wilayah Persekutuan Labuan'),
(1616, '16', 'MY', 'Wilayah Persekutuan Putrajaya'),
(1617, '01', 'MY', 'Johor'),
(1618, '02', 'MY', 'Kedah'),
(1619, '03', 'MY', 'Kelantan'),
(1620, '04', 'MY', 'Melaka'),
(1621, '05', 'MY', 'Negeri Sembilan'),
(1622, '06', 'MY', 'Pahang'),
(1623, '08', 'MY', 'Perak'),
(1624, '09', 'MY', 'Perlis'),
(1625, '07', 'MY', 'Pulau Pinang'),
(1626, '12', 'MY', 'Sabah'),
(1627, '13', 'MY', 'Sarawak'),
(1628, '10', 'MY', 'Selangor'),
(1629, '11', 'MY', 'Terengganu'),
(1630, 'CE', 'MV', 'Central'),
(1631, 'MLE', 'MV', 'Male'),
(1632, 'NO', 'MV', 'North'),
(1633, 'NC', 'MV', 'North Central'),
(1634, 'SU', 'MV', 'South'),
(1635, 'SC', 'MV', 'South Central'),
(1636, 'UN', 'MV', 'Upper North'),
(1637, 'US', 'MV', 'Upper South'),
(1638, 'BKO', 'ML', 'Bamako'),
(1639, '7', 'ML', 'Gao'),
(1640, '1', 'ML', 'Kayes'),
(1641, '8', 'ML', 'Kidal'),
(1642, '2', 'ML', 'Koulikoro'),
(1643, '5', 'ML', 'Mopti'),
(1644, '3', 'ML', 'Sikasso'),
(1645, '4', 'ML', 'Ségou'),
(1646, '6', 'ML', 'Tombouctou'),
(1647, '01', 'MT', 'Attard'),
(1648, '02', 'MT', 'Balzan'),
(1649, '03', 'MT', 'Birgu'),
(1650, '04', 'MT', 'Birkirkara'),
(1651, '05', 'MT', 'Birżebbuġa'),
(1652, '06', 'MT', 'Bormla'),
(1653, '07', 'MT', 'Dingli'),
(1654, '08', 'MT', 'Fgura'),
(1655, '09', 'MT', 'Floriana'),
(1656, '10', 'MT', 'Fontana'),
(1657, '11', 'MT', 'Gudja'),
(1658, '13', 'MT', 'Għajnsielem'),
(1659, '14', 'MT', 'Għarb'),
(1660, '15', 'MT', 'Għargħur'),
(1661, '16', 'MT', 'Għasri'),
(1662, '17', 'MT', 'Għaxaq'),
(1663, '12', 'MT', 'Gżira'),
(1664, '19', 'MT', 'Iklin'),
(1665, '20', 'MT', 'Isla'),
(1666, '21', 'MT', 'Kalkara'),
(1667, '22', 'MT', 'Kerċem'),
(1668, '23', 'MT', 'Kirkop'),
(1669, '24', 'MT', 'Lija'),
(1670, '25', 'MT', 'Luqa'),
(1671, '26', 'MT', 'Marsa'),
(1672, '27', 'MT', 'Marsaskala'),
(1673, '28', 'MT', 'Marsaxlokk'),
(1674, '29', 'MT', 'Mdina'),
(1675, '30', 'MT', 'Mellieħa'),
(1676, '32', 'MT', 'Mosta'),
(1677, '33', 'MT', 'Mqabba'),
(1678, '34', 'MT', 'Msida'),
(1679, '35', 'MT', 'Mtarfa'),
(1680, '36', 'MT', 'Munxar'),
(1681, '31', 'MT', 'Mġarr'),
(1682, '37', 'MT', 'Nadur'),
(1683, '38', 'MT', 'Naxxar'),
(1684, '39', 'MT', 'Paola'),
(1685, '40', 'MT', 'Pembroke'),
(1686, '41', 'MT', 'Pietà'),
(1687, '42', 'MT', 'Qala'),
(1688, '43', 'MT', 'Qormi'),
(1689, '44', 'MT', 'Qrendi'),
(1690, '45', 'MT', 'Rabat Għawdex'),
(1691, '46', 'MT', 'Rabat Malta'),
(1692, '47', 'MT', 'Safi'),
(1693, '50', 'MT', 'San Lawrenz'),
(1694, '51', 'MT', 'San Pawl il-Baħar'),
(1695, '48', 'MT', 'San Ġiljan'),
(1696, '49', 'MT', 'San Ġwann'),
(1697, '52', 'MT', 'Sannat'),
(1698, '53', 'MT', 'Santa Luċija'),
(1699, '54', 'MT', 'Santa Venera'),
(1700, '55', 'MT', 'Siġġiewi'),
(1701, '56', 'MT', 'Sliema'),
(1702, '57', 'MT', 'Swieqi'),
(1703, '58', 'MT', 'Ta\' Xbiex'),
(1704, '59', 'MT', 'Tarxien'),
(1705, '60', 'MT', 'Valletta'),
(1706, '61', 'MT', 'Xagħra'),
(1707, '62', 'MT', 'Xewkija'),
(1708, '63', 'MT', 'Xgħajra'),
(1709, '18', 'MT', 'Ħamrun'),
(1710, '64', 'MT', 'Żabbar'),
(1711, '65', 'MT', 'Żebbuġ Għawdex'),
(1712, '66', 'MT', 'Żebbuġ Malta'),
(1713, '67', 'MT', 'Żejtun'),
(1714, '68', 'MT', 'Żurrieq'),
(1715, 'L', 'MH', 'Ralik chain'),
(1716, 'T', 'MH', 'Ratak chain'),
(1717, '07', 'MR', 'Adrar'),
(1718, '03', 'MR', 'Assaba'),
(1719, '05', 'MR', 'Brakna'),
(1720, '08', 'MR', 'Dakhlet Nouâdhibou'),
(1721, '04', 'MR', 'Gorgol'),
(1722, '10', 'MR', 'Guidimaka'),
(1723, '01', 'MR', 'Hodh ech Chargui'),
(1724, '02', 'MR', 'Hodh el Gharbi'),
(1725, '12', 'MR', 'Inchiri'),
(1726, 'NKC', 'MR', 'Nouakchott'),
(1727, '09', 'MR', 'Tagant'),
(1728, '11', 'MR', 'Tiris Zemmour'),
(1729, '06', 'MR', 'Trarza'),
(1730, 'AG', 'MU', 'Agalega Islands'),
(1731, 'BR', 'MU', 'Beau Bassin-Rose Hill'),
(1732, 'BL', 'MU', 'Black River'),
(1733, 'CC', 'MU', 'Cargados Carajos Shoals'),
(1734, 'CU', 'MU', 'Curepipe'),
(1735, 'FL', 'MU', 'Flacq'),
(1736, 'GP', 'MU', 'Grand Port'),
(1737, 'MO', 'MU', 'Moka'),
(1738, 'PA', 'MU', 'Pamplemousses'),
(1739, 'PW', 'MU', 'Plaines Wilhems'),
(1740, 'PL', 'MU', 'Port Louis'),
(1741, 'PU', 'MU', 'Port Louis'),
(1742, 'QB', 'MU', 'Quatre Bornes'),
(1743, 'RR', 'MU', 'Rivière du Rempart'),
(1744, 'RO', 'MU', 'Rodrigues Island'),
(1745, 'SA', 'MU', 'Savanne'),
(1746, 'VP', 'MU', 'Vacoas-Phoenix'),
(1747, 'DIF', 'MX', 'Distrito Federal'),
(1748, 'AGU', 'MX', 'Aguascalientes'),
(1749, 'BCN', 'MX', 'Baja California'),
(1750, 'BCS', 'MX', 'Baja California Sur'),
(1751, 'CAM', 'MX', 'Campeche'),
(1752, 'CHP', 'MX', 'Chiapas'),
(1753, 'CHH', 'MX', 'Chihuahua'),
(1754, 'COA', 'MX', 'Coahuila'),
(1755, 'COL', 'MX', 'Colima'),
(1756, 'DUR', 'MX', 'Durango'),
(1757, 'GUA', 'MX', 'Guanajuato'),
(1758, 'GRO', 'MX', 'Guerrero'),
(1759, 'HID', 'MX', 'Hidalgo'),
(1760, 'JAL', 'MX', 'Jalisco'),
(1761, 'MIC', 'MX', 'Michoacán'),
(1762, 'MOR', 'MX', 'Morelos'),
(1763, 'MEX', 'MX', 'México'),
(1764, 'NAY', 'MX', 'Nayarit'),
(1765, 'NLE', 'MX', 'Nuevo León'),
(1766, 'OAX', 'MX', 'Oaxaca'),
(1767, 'PUE', 'MX', 'Puebla'),
(1768, 'QUE', 'MX', 'Querétaro'),
(1769, 'ROO', 'MX', 'Quintana Roo'),
(1770, 'SLP', 'MX', 'San Luis Potosí'),
(1771, 'SIN', 'MX', 'Sinaloa'),
(1772, 'SON', 'MX', 'Sonora'),
(1773, 'TAB', 'MX', 'Tabasco'),
(1774, 'TAM', 'MX', 'Tamaulipas'),
(1775, 'TLA', 'MX', 'Tlaxcala'),
(1776, 'VER', 'MX', 'Veracruz'),
(1777, 'YUC', 'MX', 'Yucatán'),
(1778, 'ZAC', 'MX', 'Zacatecas'),
(1779, 'TRK', 'FM', 'Chuuk'),
(1780, 'KSA', 'FM', 'Kosrae'),
(1781, 'PNI', 'FM', 'Pohnpei'),
(1782, 'YAP', 'FM', 'Yap'),
(1783, 'AN', 'MD', 'Anenii Noi'),
(1784, 'BS', 'MD', 'Basarabeasca'),
(1785, 'BR', 'MD', 'Briceni'),
(1786, 'BA', 'MD', 'Bălţi'),
(1787, 'CA', 'MD', 'Cahul'),
(1788, 'CT', 'MD', 'Cantemir'),
(1789, 'CU', 'MD', 'Chişinău'),
(1790, 'CM', 'MD', 'Cimişlia'),
(1791, 'CR', 'MD', 'Criuleni'),
(1792, 'CL', 'MD', 'Călăraşi'),
(1793, 'CS', 'MD', 'Căuşeni'),
(1794, 'DO', 'MD', 'Donduşeni'),
(1795, 'DR', 'MD', 'Drochia'),
(1796, 'DU', 'MD', 'Dubăsari'),
(1797, 'ED', 'MD', 'Edineţ'),
(1798, 'FL', 'MD', 'Floreşti'),
(1799, 'FA', 'MD', 'Făleşti'),
(1800, 'GL', 'MD', 'Glodeni'),
(1801, 'GA', 'MD', 'Găgăuzia, Unitatea teritorială autonomă'),
(1802, 'HI', 'MD', 'Hînceşti'),
(1803, 'IA', 'MD', 'Ialoveni'),
(1804, 'LE', 'MD', 'Leova'),
(1805, 'NI', 'MD', 'Nisporeni'),
(1806, 'OC', 'MD', 'Ocniţa'),
(1807, 'OR', 'MD', 'Orhei'),
(1808, 'RE', 'MD', 'Rezina'),
(1809, 'RI', 'MD', 'Rîşcani'),
(1810, 'SO', 'MD', 'Soroca'),
(1811, 'ST', 'MD', 'Străşeni'),
(1812, 'SN', 'MD', 'Stînga Nistrului, unitatea teritorială din'),
(1813, 'SI', 'MD', 'Sîngerei'),
(1814, 'TA', 'MD', 'Taraclia'),
(1815, 'TE', 'MD', 'Teleneşti'),
(1816, 'BD', 'MD', 'Tighina'),
(1817, 'UN', 'MD', 'Ungheni'),
(1818, 'SD', 'MD', 'Şoldăneşti'),
(1819, 'SV', 'MD', 'Ştefan Vodă'),
(1820, 'FO', 'MC', 'Fontvieille'),
(1821, 'JE', 'MC', 'Jardin Exotique'),
(1822, 'CL', 'MC', 'La Colle'),
(1823, 'CO', 'MC', 'La Condamine'),
(1824, 'GA', 'MC', 'La Gare'),
(1825, 'SO', 'MC', 'La Source'),
(1826, 'LA', 'MC', 'Larvotto'),
(1827, 'MA', 'MC', 'Malbousquet'),
(1828, 'MO', 'MC', 'Monaco-Ville'),
(1829, 'MG', 'MC', 'Moneghetti'),
(1830, 'MC', 'MC', 'Monte-Carlo'),
(1831, 'MU', 'MC', 'Moulins'),
(1832, 'PH', 'MC', 'Port-Hercule'),
(1833, 'SR', 'MC', 'Saint-Roman'),
(1834, 'SD', 'MC', 'Sainte-Dévote'),
(1835, 'SP', 'MC', 'Spélugues'),
(1836, 'VR', 'MC', 'Vallon de la Rousse'),
(1837, '073', 'MN', 'Arhangay'),
(1838, '071', 'MN', 'Bayan-Ölgiy'),
(1839, '069', 'MN', 'Bayanhongor'),
(1840, '067', 'MN', 'Bulgan'),
(1841, '037', 'MN', 'Darhan uul'),
(1842, '061', 'MN', 'Dornod'),
(1843, '063', 'MN', 'Dornogovĭ'),
(1844, '059', 'MN', 'Dundgovĭ'),
(1845, '057', 'MN', 'Dzavhan'),
(1846, '065', 'MN', 'Govĭ-Altay'),
(1847, '064', 'MN', 'Govĭ-Sümber'),
(1848, '039', 'MN', 'Hentiy'),
(1849, '043', 'MN', 'Hovd'),
(1850, '041', 'MN', 'Hövsgöl'),
(1851, '035', 'MN', 'Orhon'),
(1852, '049', 'MN', 'Selenge'),
(1853, '051', 'MN', 'Sühbaatar'),
(1854, '047', 'MN', 'Töv'),
(1855, '1', 'MN', 'Ulaanbaatar'),
(1856, '046', 'MN', 'Uvs'),
(1857, '053', 'MN', 'Ömnögovĭ'),
(1858, '055', 'MN', 'Övörhangay'),
(1859, '01', 'ME', 'Andrijevica'),
(1860, '02', 'ME', 'Bar'),
(1861, '03', 'ME', 'Berane'),
(1862, '04', 'ME', 'Bijelo Polje'),
(1863, '05', 'ME', 'Budva'),
(1864, '06', 'ME', 'Cetinje'),
(1865, '07', 'ME', 'Danilovgrad'),
(1866, '22', 'ME', 'Gusinje'),
(1867, '08', 'ME', 'Herceg-Novi'),
(1868, '09', 'ME', 'Kolašin'),
(1869, '10', 'ME', 'Kotor'),
(1870, '11', 'ME', 'Mojkovac'),
(1871, '12', 'ME', 'Nikšić'),
(1872, '23', 'ME', 'Petnjica'),
(1873, '13', 'ME', 'Plav'),
(1874, '14', 'ME', 'Pljevlja'),
(1875, '15', 'ME', 'Plužine'),
(1876, '16', 'ME', 'Podgorica'),
(1877, '17', 'ME', 'Rožaje'),
(1878, '19', 'ME', 'Tivat'),
(1879, '20', 'ME', 'Ulcinj'),
(1880, '18', 'ME', 'Šavnik'),
(1881, '21', 'ME', 'Žabljak'),
(1882, '09', 'MA', 'Chaouia-Ouardigha'),
(1883, '10', 'MA', 'Doukhala-Abda'),
(1884, '05', 'MA', 'Fès-Boulemane'),
(1885, '02', 'MA', 'Gharb-Chrarda-Beni Hssen'),
(1886, '08', 'MA', 'Grand Casablanca'),
(1887, '14', 'MA', 'Guelmim-Es Smara'),
(1888, '04', 'MA', 'L\'Oriental'),
(1889, '15', 'MA', 'Laâyoune-Boujdour-Sakia el Hamra'),
(1890, '11', 'MA', 'Marrakech-Tensift-Al Haouz'),
(1891, '06', 'MA', 'Meknès-Tafilalet'),
(1892, '16', 'MA', 'Oued ed Dahab-Lagouira'),
(1893, '07', 'MA', 'Rabat-Salé-Zemmour-Zaer'),
(1894, '13', 'MA', 'Souss-Massa-Drâa'),
(1895, '12', 'MA', 'Tadla-Azilal'),
(1896, '01', 'MA', 'Tanger-Tétouan'),
(1897, '03', 'MA', 'Taza-Al Hoceima-Taounate'),
(1898, 'P', 'MZ', 'Cabo Delgado'),
(1899, 'G', 'MZ', 'Gaza'),
(1900, 'I', 'MZ', 'Inhambane'),
(1901, 'B', 'MZ', 'Manica'),
(1902, 'MPM', 'MZ', 'Maputo'),
(1903, 'L', 'MZ', 'Maputo'),
(1904, 'N', 'MZ', 'Nampula'),
(1905, 'A', 'MZ', 'Niassa'),
(1906, 'S', 'MZ', 'Sofala'),
(1907, 'T', 'MZ', 'Tete'),
(1908, 'Q', 'MZ', 'Zambézia'),
(1909, '07', 'MM', 'Ayeyarwady'),
(1910, '02', 'MM', 'Bago'),
(1911, '14', 'MM', 'Chin'),
(1912, '11', 'MM', 'Kachin'),
(1913, '12', 'MM', 'Kayah'),
(1914, '13', 'MM', 'Kayin'),
(1915, '03', 'MM', 'Magway'),
(1916, '04', 'MM', 'Mandalay'),
(1917, '15', 'MM', 'Mon'),
(1918, '16', 'MM', 'Rakhine'),
(1919, '01', 'MM', 'Sagaing'),
(1920, '17', 'MM', 'Shan'),
(1921, '05', 'MM', 'Tanintharyi'),
(1922, '06', 'MM', 'Yangon'),
(1923, 'ER', 'NA', 'Erongo'),
(1924, 'HA', 'NA', 'Hardap'),
(1925, 'KA', 'NA', 'Karas'),
(1926, 'KE', 'NA', 'Kavango East'),
(1927, 'KW', 'NA', 'Kavango West'),
(1928, 'KH', 'NA', 'Khomas'),
(1929, 'KU', 'NA', 'Kunene'),
(1930, 'OW', 'NA', 'Ohangwena'),
(1931, 'OH', 'NA', 'Omaheke'),
(1932, 'OS', 'NA', 'Omusati'),
(1933, 'ON', 'NA', 'Oshana'),
(1934, 'OT', 'NA', 'Oshikoto'),
(1935, 'OD', 'NA', 'Otjozondjupa'),
(1936, 'CA', 'NA', 'Zambezi'),
(1937, '01', 'NR', 'Aiwo'),
(1938, '02', 'NR', 'Anabar'),
(1939, '03', 'NR', 'Anetan'),
(1940, '04', 'NR', 'Anibare'),
(1941, '05', 'NR', 'Baiti'),
(1942, '06', 'NR', 'Boe'),
(1943, '07', 'NR', 'Buada'),
(1944, '08', 'NR', 'Denigomodu'),
(1945, '09', 'NR', 'Ewa'),
(1946, '10', 'NR', 'Ijuw'),
(1947, '11', 'NR', 'Meneng'),
(1948, '12', 'NR', 'Nibok'),
(1949, '13', 'NR', 'Uaboe'),
(1950, '14', 'NR', 'Yaren'),
(1951, '2', 'NP', 'Madhya Pashchimanchal'),
(1952, '1', 'NP', 'Madhyamanchal'),
(1953, '3', 'NP', 'Pashchimanchal'),
(1954, '4', 'NP', 'Purwanchal'),
(1955, '5', 'NP', 'Sudur Pashchimanchal'),
(1956, 'DR', 'NL', 'Drenthe'),
(1957, 'FL', 'NL', 'Flevoland'),
(1958, 'FR', 'NL', 'Fryslân'),
(1959, 'GE', 'NL', 'Gelderland'),
(1960, 'GR', 'NL', 'Groningen'),
(1961, 'LI', 'NL', 'Limburg'),
(1962, 'NB', 'NL', 'Noord-Brabant'),
(1963, 'NH', 'NL', 'Noord-Holland'),
(1964, 'OV', 'NL', 'Overijssel'),
(1965, 'UT', 'NL', 'Utrecht'),
(1966, 'ZE', 'NL', 'Zeeland'),
(1967, 'ZH', 'NL', 'Zuid-Holland'),
(1968, 'AW', 'NL', 'Aruba'),
(1969, 'CW', 'NL', 'Curaçao'),
(1970, 'SX', 'NL', 'Sint Maarten'),
(1971, 'BQ1', 'NL', 'Bonaire'),
(1972, 'BQ2', 'NL', 'Saba'),
(1973, 'BQ3', 'NL', 'Sint Eustatius'),
(1974, 'N', 'NZ', 'North Island'),
(1975, 'S', 'NZ', 'South Island'),
(1976, 'AUK', 'NZ', 'Auckland'),
(1977, 'BOP', 'NZ', 'Bay of Plenty'),
(1978, 'CAN', 'NZ', 'Canterbury'),
(1979, 'HKB', 'NZ', 'Hawke\'s Bay'),
(1980, 'MWT', 'NZ', 'Manawatu-Wanganui'),
(1981, 'NTL', 'NZ', 'Northland'),
(1982, 'OTA', 'NZ', 'Otago'),
(1983, 'STL', 'NZ', 'Southland'),
(1984, 'TKI', 'NZ', 'Taranaki'),
(1985, 'WKO', 'NZ', 'Waikato'),
(1986, 'WGN', 'NZ', 'Wellington'),
(1987, 'WTC', 'NZ', 'West Coast'),
(1988, 'CIT', 'NZ', 'Chatham Islands Territory'),
(1989, 'GIS', 'NZ', 'Gisborne District'),
(1990, 'MBH', 'NZ', 'Marlborough District'),
(1991, 'NSN', 'NZ', 'Nelson City'),
(1992, 'TAS', 'NZ', 'Tasman District'),
(1993, 'AN', 'NI', 'Atlántico Norte'),
(1994, 'AS', 'NI', 'Atlántico Sur'),
(1995, 'BO', 'NI', 'Boaco'),
(1996, 'CA', 'NI', 'Carazo'),
(1997, 'CI', 'NI', 'Chinandega'),
(1998, 'CO', 'NI', 'Chontales'),
(1999, 'ES', 'NI', 'Estelí'),
(2000, 'GR', 'NI', 'Granada'),
(2001, 'JI', 'NI', 'Jinotega'),
(2002, 'LE', 'NI', 'León'),
(2003, 'MD', 'NI', 'Madriz'),
(2004, 'MN', 'NI', 'Managua'),
(2005, 'MS', 'NI', 'Masaya'),
(2006, 'MT', 'NI', 'Matagalpa'),
(2007, 'NS', 'NI', 'Nueva Segovia'),
(2008, 'RI', 'NI', 'Rivas'),
(2009, 'SJ', 'NI', 'Río San Juan'),
(2010, '1', 'NE', 'Agadez'),
(2011, '2', 'NE', 'Diffa'),
(2012, '3', 'NE', 'Dosso'),
(2013, '4', 'NE', 'Maradi'),
(2014, '8', 'NE', 'Niamey'),
(2015, '5', 'NE', 'Tahoua'),
(2016, '6', 'NE', 'Tillabéri'),
(2017, '7', 'NE', 'Zinder'),
(2018, 'AB', 'NG', 'Abia'),
(2019, 'FC', 'NG', 'Abuja Federal Capital Territory'),
(2020, 'AD', 'NG', 'Adamawa'),
(2021, 'AK', 'NG', 'Akwa Ibom'),
(2022, 'AN', 'NG', 'Anambra'),
(2023, 'BA', 'NG', 'Bauchi'),
(2024, 'BY', 'NG', 'Bayelsa'),
(2025, 'BE', 'NG', 'Benue'),
(2026, 'BO', 'NG', 'Borno'),
(2027, 'CR', 'NG', 'Cross River'),
(2028, 'DE', 'NG', 'Delta'),
(2029, 'EB', 'NG', 'Ebonyi'),
(2030, 'ED', 'NG', 'Edo'),
(2031, 'EK', 'NG', 'Ekiti'),
(2032, 'EN', 'NG', 'Enugu'),
(2033, 'GO', 'NG', 'Gombe'),
(2034, 'IM', 'NG', 'Imo'),
(2035, 'JI', 'NG', 'Jigawa'),
(2036, 'KD', 'NG', 'Kaduna'),
(2037, 'KN', 'NG', 'Kano'),
(2038, 'KT', 'NG', 'Katsina'),
(2039, 'KE', 'NG', 'Kebbi'),
(2040, 'KO', 'NG', 'Kogi'),
(2041, 'KW', 'NG', 'Kwara'),
(2042, 'LA', 'NG', 'Lagos'),
(2043, 'NA', 'NG', 'Nassarawa'),
(2044, 'NI', 'NG', 'Niger'),
(2045, 'OG', 'NG', 'Ogun'),
(2046, 'ON', 'NG', 'Ondo'),
(2047, 'OS', 'NG', 'Osun'),
(2048, 'OY', 'NG', 'Oyo'),
(2049, 'PL', 'NG', 'Plateau'),
(2050, 'RI', 'NG', 'Rivers'),
(2051, 'SO', 'NG', 'Sokoto'),
(2052, 'TA', 'NG', 'Taraba'),
(2053, 'YO', 'NG', 'Yobe'),
(2054, 'ZA', 'NG', 'Zamfara'),
(2055, '04', 'KP', 'Chagang'),
(2056, '07', 'KP', 'Kangwon'),
(2057, '09', 'KP', 'North Hamgyong'),
(2058, '06', 'KP', 'North Hwanghae'),
(2059, '03', 'KP', 'North Pyongan'),
(2060, '01', 'KP', 'Pyongyang'),
(2061, '13', 'KP', 'Rason'),
(2062, '10', 'KP', 'Ryanggang'),
(2063, '08', 'KP', 'South Hamgyong'),
(2064, '05', 'KP', 'South Hwanghae'),
(2065, '02', 'KP', 'South Pyongan'),
(2066, '02', 'NO', 'Akershus'),
(2067, '09', 'NO', 'Aust-Agder'),
(2068, '06', 'NO', 'Buskerud'),
(2069, '20', 'NO', 'Finnmark'),
(2070, '04', 'NO', 'Hedmark'),
(2071, '12', 'NO', 'Hordaland'),
(2072, '22', 'NO', 'Jan Mayen'),
(2073, '15', 'NO', 'Møre og Romsdal'),
(2074, '17', 'NO', 'Nord-Trøndelag'),
(2075, '18', 'NO', 'Nordland'),
(2076, '05', 'NO', 'Oppland'),
(2077, '03', 'NO', 'Oslo'),
(2078, '11', 'NO', 'Rogaland'),
(2079, '14', 'NO', 'Sogn og Fjordane'),
(2080, '21', 'NO', 'Svalbard'),
(2081, '16', 'NO', 'Sør-Trøndelag'),
(2082, '08', 'NO', 'Telemark'),
(2083, '19', 'NO', 'Troms'),
(2084, '10', 'NO', 'Vest-Agder'),
(2085, '07', 'NO', 'Vestfold'),
(2086, '01', 'NO', 'Østfold'),
(2087, 'DA', 'OM', 'Ad Dākhilīyah'),
(2088, 'BU', 'OM', 'Al Buraymī'),
(2089, 'BA', 'OM', 'Al Bāţinah'),
(2090, 'WU', 'OM', 'Al Wusţá'),
(2091, 'SH', 'OM', 'Ash Sharqīyah'),
(2092, 'ZA', 'OM', 'Az̧ Z̧āhirah'),
(2093, 'MA', 'OM', 'Masqaţ'),
(2094, 'MU', 'OM', 'Musandam'),
(2095, 'ZU', 'OM', 'Z̧ufār'),
(2096, 'JK', 'PK', 'Azad Kashmir'),
(2097, 'BA', 'PK', 'Balochistan'),
(2098, 'TA', 'PK', 'Federally Administered Tribal Areas'),
(2099, 'GB', 'PK', 'Gilgit-Baltistan'),
(2100, 'IS', 'PK', 'Islamabad'),
(2101, 'KP', 'PK', 'Khyber Pakhtunkhwa'),
(2102, 'PB', 'PK', 'Punjab'),
(2103, 'SD', 'PK', 'Sindh'),
(2104, '002', 'PW', 'Aimeliik'),
(2105, '004', 'PW', 'Airai'),
(2106, '010', 'PW', 'Angaur'),
(2107, '050', 'PW', 'Hatobohei'),
(2108, '100', 'PW', 'Kayangel'),
(2109, '150', 'PW', 'Koror'),
(2110, '212', 'PW', 'Melekeok'),
(2111, '214', 'PW', 'Ngaraard'),
(2112, '218', 'PW', 'Ngarchelong'),
(2113, '222', 'PW', 'Ngardmau'),
(2114, '224', 'PW', 'Ngatpang'),
(2115, '226', 'PW', 'Ngchesar'),
(2116, '227', 'PW', 'Ngeremlengui'),
(2117, '228', 'PW', 'Ngiwal'),
(2118, '350', 'PW', 'Peleliu'),
(2119, '370', 'PW', 'Sonsorol'),
(2120, 'BTH', 'PS', 'Bethlehem'),
(2121, 'DEB', 'PS', 'Deir El Balah'),
(2122, 'GZA', 'PS', 'Gaza'),
(2123, 'HBN', 'PS', 'Hebron'),
(2124, 'JEN', 'PS', 'Jenin'),
(2125, 'JRH', 'PS', 'Jericho – Al Aghwar'),
(2126, 'JEM', 'PS', 'Jerusalem'),
(2127, 'KYS', 'PS', 'Khan Yunis'),
(2128, 'NBS', 'PS', 'Nablus'),
(2129, 'NGZ', 'PS', 'North Gaza'),
(2130, 'QQA', 'PS', 'Qalqilya'),
(2131, 'RFH', 'PS', 'Rafah'),
(2132, 'RBH', 'PS', 'Ramallah'),
(2133, 'SLT', 'PS', 'Salfit'),
(2134, 'TBS', 'PS', 'Tubas'),
(2135, 'TKM', 'PS', 'Tulkarm'),
(2136, '1', 'PA', 'Bocas del Toro'),
(2137, '4', 'PA', 'Chiriquí'),
(2138, '2', 'PA', 'Coclé'),
(2139, '3', 'PA', 'Colón'),
(2140, '5', 'PA', 'Darién'),
(2141, 'EM', 'PA', 'Emberá'),
(2142, '6', 'PA', 'Herrera'),
(2143, 'KY', 'PA', 'Kuna Yala'),
(2144, '7', 'PA', 'Los Santos'),
(2145, 'NB', 'PA', 'Ngöbe-Buglé'),
(2146, '8', 'PA', 'Panamá'),
(2147, '10', 'PA', 'Panamá Oeste'),
(2148, '9', 'PA', 'Veraguas'),
(2149, 'NSB', 'PG', 'Bougainville'),
(2150, 'CPM', 'PG', 'Central'),
(2151, 'CPK', 'PG', 'Chimbu'),
(2152, 'EBR', 'PG', 'East New Britain'),
(2153, 'ESW', 'PG', 'East Sepik'),
(2154, 'EHG', 'PG', 'Eastern Highlands'),
(2155, 'EPW', 'PG', 'Enga'),
(2156, 'GPK', 'PG', 'Gulf'),
(2157, 'MPM', 'PG', 'Madang'),
(2158, 'MRL', 'PG', 'Manus'),
(2159, 'MBA', 'PG', 'Milne Bay'),
(2160, 'MPL', 'PG', 'Morobe'),
(2161, 'NCD', 'PG', 'National Capital District'),
(2162, 'NIK', 'PG', 'New Ireland'),
(2163, 'NPP', 'PG', 'Northern'),
(2164, 'SAN', 'PG', 'Sandaun'),
(2165, 'SHM', 'PG', 'Southern Highlands'),
(2166, 'WBK', 'PG', 'West New Britain'),
(2167, 'WPD', 'PG', 'Western'),
(2168, 'WHM', 'PG', 'Western Highlands'),
(2169, '16', 'PY', 'Alto Paraguay'),
(2170, '10', 'PY', 'Alto Paraná'),
(2171, '13', 'PY', 'Amambay'),
(2172, 'ASU', 'PY', 'Asunción'),
(2173, '19', 'PY', 'Boquerón'),
(2174, '5', 'PY', 'Caaguazú'),
(2175, '6', 'PY', 'Caazapá'),
(2176, '14', 'PY', 'Canindeyú'),
(2177, '11', 'PY', 'Central'),
(2178, '1', 'PY', 'Concepción'),
(2179, '3', 'PY', 'Cordillera'),
(2180, '4', 'PY', 'Guairá'),
(2181, '7', 'PY', 'Itapúa'),
(2182, '8', 'PY', 'Misiones'),
(2183, '9', 'PY', 'Paraguarí'),
(2184, '15', 'PY', 'Presidente Hayes'),
(2185, '2', 'PY', 'San Pedro'),
(2186, '12', 'PY', 'Ñeembucú'),
(2187, 'AMA', 'PE', 'Amazonas'),
(2188, 'ANC', 'PE', 'Ancash'),
(2189, 'APU', 'PE', 'Apurímac'),
(2190, 'ARE', 'PE', 'Arequipa'),
(2191, 'AYA', 'PE', 'Ayacucho'),
(2192, 'CAJ', 'PE', 'Cajamarca'),
(2193, 'CUS', 'PE', 'Cusco'),
(2194, 'CAL', 'PE', 'El Callao'),
(2195, 'HUV', 'PE', 'Huancavelica'),
(2196, 'HUC', 'PE', 'Huánuco'),
(2197, 'ICA', 'PE', 'Ica'),
(2198, 'JUN', 'PE', 'Junín'),
(2199, 'LAL', 'PE', 'La Libertad'),
(2200, 'LAM', 'PE', 'Lambayeque'),
(2201, 'LIM', 'PE', 'Lima'),
(2202, 'LOR', 'PE', 'Loreto'),
(2203, 'MDD', 'PE', 'Madre de Dios'),
(2204, 'MOQ', 'PE', 'Moquegua'),
(2205, 'LMA', 'PE', 'Municipalidad Metropolitana de Lima'),
(2206, 'PAS', 'PE', 'Pasco'),
(2207, 'PIU', 'PE', 'Piura'),
(2208, 'PUN', 'PE', 'Puno'),
(2209, 'SAM', 'PE', 'San Martín'),
(2210, 'TAC', 'PE', 'Tacna'),
(2211, 'TUM', 'PE', 'Tumbes'),
(2212, 'UCA', 'PE', 'Ucayali'),
(2213, '14', 'PH', 'Autonomous Region in Muslim Mindanao'),
(2214, '05', 'PH', 'Bicol'),
(2215, '02', 'PH', 'Cagayan Valley'),
(2216, '40', 'PH', 'Calabarzon'),
(2217, '13', 'PH', 'Caraga'),
(2218, '03', 'PH', 'Central Luzon'),
(2219, '07', 'PH', 'Central Visayas'),
(2220, '15', 'PH', 'Cordillera Administrative Region'),
(2221, '11', 'PH', 'Davao'),
(2222, '08', 'PH', 'Eastern Visayas'),
(2223, '01', 'PH', 'Ilocos'),
(2224, '41', 'PH', 'Mimaropa'),
(2225, '00', 'PH', 'National Capital Region'),
(2226, '10', 'PH', 'Northern Mindanao'),
(2227, '12', 'PH', 'Soccsksargen'),
(2228, '06', 'PH', 'Western Visayas'),
(2229, '09', 'PH', 'Zamboanga Peninsula'),
(2230, 'DS', 'PL', 'Dolnośląskie'),
(2231, 'KP', 'PL', 'Kujawsko-pomorskie'),
(2232, 'LU', 'PL', 'Lubelskie'),
(2233, 'LB', 'PL', 'Lubuskie'),
(2234, 'MZ', 'PL', 'Mazowieckie'),
(2235, 'MA', 'PL', 'Małopolskie'),
(2236, 'OP', 'PL', 'Opolskie'),
(2237, 'PK', 'PL', 'Podkarpackie'),
(2238, 'PD', 'PL', 'Podlaskie'),
(2239, 'PM', 'PL', 'Pomorskie'),
(2240, 'WN', 'PL', 'Warmińsko-mazurskie'),
(2241, 'WP', 'PL', 'Wielkopolskie'),
(2242, 'ZP', 'PL', 'Zachodniopomorskie'),
(2243, 'LD', 'PL', 'Łódzkie'),
(2244, 'SL', 'PL', 'Śląskie'),
(2245, 'SK', 'PL', 'Świętokrzyskie'),
(2246, '01', 'PT', 'Aveiro'),
(2247, '02', 'PT', 'Beja'),
(2248, '03', 'PT', 'Braga'),
(2249, '04', 'PT', 'Bragança'),
(2250, '05', 'PT', 'Castelo Branco'),
(2251, '06', 'PT', 'Coimbra'),
(2252, '08', 'PT', 'Faro'),
(2253, '09', 'PT', 'Guarda'),
(2254, '10', 'PT', 'Leiria'),
(2255, '11', 'PT', 'Lisboa'),
(2256, '12', 'PT', 'Portalegre'),
(2257, '13', 'PT', 'Porto'),
(2258, '30', 'PT', 'Região Autónoma da Madeira'),
(2259, '20', 'PT', 'Região Autónoma dos Açores'),
(2260, '14', 'PT', 'Santarém'),
(2261, '15', 'PT', 'Setúbal'),
(2262, '16', 'PT', 'Viana do Castelo'),
(2263, '17', 'PT', 'Vila Real'),
(2264, '18', 'PT', 'Viseu'),
(2265, '07', 'PT', 'Évora'),
(2266, 'DA', 'QA', 'Ad Dawḩah'),
(2267, 'KH', 'QA', 'Al Khawr wa adh Dhakhīrah'),
(2268, 'WA', 'QA', 'Al Wakrah'),
(2269, 'RA', 'QA', 'Ar Rayyān'),
(2270, 'MS', 'QA', 'Ash Shamāl'),
(2271, 'ZA', 'QA', 'Az̧ Za̧`āyin'),
(2272, 'US', 'QA', 'Umm Şalāl'),
(2273, 'AB', 'RO', 'Alba'),
(2274, 'AR', 'RO', 'Arad'),
(2275, 'AG', 'RO', 'Argeș'),
(2276, 'BC', 'RO', 'Bacău'),
(2277, 'BH', 'RO', 'Bihor'),
(2278, 'BN', 'RO', 'Bistrița-Năsăud'),
(2279, 'BT', 'RO', 'Botoșani'),
(2280, 'BV', 'RO', 'Brașov'),
(2281, 'BR', 'RO', 'Brăila'),
(2282, 'B', 'RO', 'București'),
(2283, 'BZ', 'RO', 'Buzău'),
(2284, 'CS', 'RO', 'Caraș-Severin'),
(2285, 'CJ', 'RO', 'Cluj'),
(2286, 'CT', 'RO', 'Constanța'),
(2287, 'CV', 'RO', 'Covasna'),
(2288, 'CL', 'RO', 'Călărași'),
(2289, 'DJ', 'RO', 'Dolj'),
(2290, 'DB', 'RO', 'Dâmbovița'),
(2291, 'GL', 'RO', 'Galați'),
(2292, 'GR', 'RO', 'Giurgiu'),
(2293, 'GJ', 'RO', 'Gorj'),
(2294, 'HR', 'RO', 'Harghita'),
(2295, 'HD', 'RO', 'Hunedoara'),
(2296, 'IL', 'RO', 'Ialomița'),
(2297, 'IS', 'RO', 'Iași'),
(2298, 'IF', 'RO', 'Ilfov'),
(2299, 'MM', 'RO', 'Maramureș'),
(2300, 'MH', 'RO', 'Mehedinți'),
(2301, 'MS', 'RO', 'Mureș'),
(2302, 'NT', 'RO', 'Neamț'),
(2303, 'OT', 'RO', 'Olt'),
(2304, 'PH', 'RO', 'Prahova'),
(2305, 'SM', 'RO', 'Satu Mare'),
(2306, 'SB', 'RO', 'Sibiu'),
(2307, 'SV', 'RO', 'Suceava'),
(2308, 'SJ', 'RO', 'Sălaj'),
(2309, 'TR', 'RO', 'Teleorman'),
(2310, 'TM', 'RO', 'Timiș'),
(2311, 'TL', 'RO', 'Tulcea'),
(2312, 'VS', 'RO', 'Vaslui'),
(2313, 'VN', 'RO', 'Vrancea'),
(2314, 'VL', 'RO', 'Vâlcea'),
(2315, 'AMU', 'RU', 'Amurskaya oblast\''),
(2316, 'ARK', 'RU', 'Arkhangel\'skaya oblast\''),
(2317, 'AST', 'RU', 'Astrakhanskaya oblast\''),
(2318, 'BEL', 'RU', 'Belgorodskaya oblast\''),
(2319, 'BRY', 'RU', 'Bryanskaya oblast\''),
(2320, 'CHE', 'RU', 'Chelyabinskaya oblast\''),
(2321, 'IRK', 'RU', 'Irkutskaya oblast\''),
(2322, 'IVA', 'RU', 'Ivanovskaya oblast\''),
(2323, 'KGD', 'RU', 'Kaliningradskaya oblast\''),
(2324, 'KLU', 'RU', 'Kaluzhskaya oblast\''),
(2325, 'KEM', 'RU', 'Kemerovskaya oblast\''),
(2326, 'KIR', 'RU', 'Kirovskaya oblast\''),
(2327, 'KOS', 'RU', 'Kostromskaya oblast\''),
(2328, 'KGN', 'RU', 'Kurganskaya oblast\''),
(2329, 'KRS', 'RU', 'Kurskaya oblast\''),
(2330, 'LEN', 'RU', 'Leningradskaya oblast\''),
(2331, 'LIP', 'RU', 'Lipetskaya oblast\''),
(2332, 'MAG', 'RU', 'Magadanskaya oblast\''),
(2333, 'MOS', 'RU', 'Moskovskaya oblast\''),
(2334, 'MUR', 'RU', 'Murmanskaya oblast\''),
(2335, 'NIZ', 'RU', 'Nizhegorodskaya oblast\''),
(2336, 'NGR', 'RU', 'Novgorodskaya oblast\''),
(2337, 'NVS', 'RU', 'Novosibirskaya oblast\''),
(2338, 'OMS', 'RU', 'Omskaya oblast\''),
(2339, 'ORE', 'RU', 'Orenburgskaya oblast\''),
(2340, 'ORL', 'RU', 'Orlovskaya oblast\''),
(2341, 'PNZ', 'RU', 'Penzenskaya oblast\''),
(2342, 'PSK', 'RU', 'Pskovskaya oblast\''),
(2343, 'ROS', 'RU', 'Rostovskaya oblast\''),
(2344, 'RYA', 'RU', 'Ryazanskaya oblast\''),
(2345, 'SAK', 'RU', 'Sakhalinskaya oblast\''),
(2346, 'SAM', 'RU', 'Samarskaya oblast\''),
(2347, 'SAR', 'RU', 'Saratovskaya oblast\''),
(2348, 'SMO', 'RU', 'Smolenskaya oblast\''),
(2349, 'SVE', 'RU', 'Sverdlovskaya oblast\''),
(2350, 'TAM', 'RU', 'Tambovskaya oblast\''),
(2351, 'TOM', 'RU', 'Tomskaya oblast\''),
(2352, 'TUL', 'RU', 'Tul\'skaya oblast\''),
(2353, 'TVE', 'RU', 'Tverskaya oblast\''),
(2354, 'TYU', 'RU', 'Tyumenskaya oblast\''),
(2355, 'ULY', 'RU', 'Ul\'yanovskaya oblast\''),
(2356, 'VLA', 'RU', 'Vladimirskaya oblast\''),
(2357, 'VGG', 'RU', 'Volgogradskaya oblast\''),
(2358, 'VLG', 'RU', 'Vologodskaya oblast\''),
(2359, 'VOR', 'RU', 'Voronezhskaya oblast\''),
(2360, 'YAR', 'RU', 'Yaroslavskaya oblast\''),
(2361, 'ALT', 'RU', 'Altayskiy kray'),
(2362, 'KAM', 'RU', 'Kamchatskiy kray'),
(2363, 'KHA', 'RU', 'Khabarovskiy kray'),
(2364, 'KDA', 'RU', 'Krasnodarskiy kray'),
(2365, 'KYA', 'RU', 'Krasnoyarskiy kray'),
(2366, 'PER', 'RU', 'Permskiy kray'),
(2367, 'PRI', 'RU', 'Primorskiy kray'),
(2368, 'STA', 'RU', 'Stavropol\'skiy kray'),
(2369, 'ZAB', 'RU', 'Zabaykal\'skiy kray'),
(2370, 'MOW', 'RU', 'Moskva'),
(2371, 'SPE', 'RU', 'Sankt-Peterburg'),
(2372, 'CHU', 'RU', 'Chukotskiy avtonomnyy okrug'),
(2373, 'KHM', 'RU', 'Khanty-Mansiyskiy avtonomnyy okrug-Yugra'),
(2374, 'NEN', 'RU', 'Nenetskiy avtonomnyy okrug'),
(2375, 'YAN', 'RU', 'Yamalo-Nenetskiy avtonomnyy okrug'),
(2376, 'YEV', 'RU', 'Yevreyskaya avtonomnaya oblast\''),
(2377, 'AD', 'RU', 'Adygeya, Respublika'),
(2378, 'AL', 'RU', 'Altay, Respublika'),
(2379, 'BA', 'RU', 'Bashkortostan, Respublika'),
(2380, 'BU', 'RU', 'Buryatiya, Respublika'),
(2381, 'CE', 'RU', 'Chechenskaya Respublika'),
(2382, 'CU', 'RU', 'Chuvashskaya Respublika'),
(2383, 'DA', 'RU', 'Dagestan, Respublika'),
(2384, 'IN', 'RU', 'Ingushetiya, Respublika'),
(2385, 'KB', 'RU', 'Kabardino-Balkarskaya Respublika'),
(2386, 'KL', 'RU', 'Kalmykiya, Respublika'),
(2387, 'KC', 'RU', 'Karachayevo-Cherkesskaya Respublika'),
(2388, 'KR', 'RU', 'Kareliya, Respublika'),
(2389, 'KK', 'RU', 'Khakasiya, Respublika'),
(2390, 'KO', 'RU', 'Komi, Respublika'),
(2391, 'ME', 'RU', 'Mariy El, Respublika'),
(2392, 'MO', 'RU', 'Mordoviya, Respublika'),
(2393, 'SA', 'RU', 'Sakha, Respublika'),
(2394, 'SE', 'RU', 'Severnaya Osetiya-Alaniya, Respublika'),
(2395, 'TA', 'RU', 'Tatarstan, Respublika'),
(2396, 'TY', 'RU', 'Tyva, Respublika'),
(2397, 'UD', 'RU', 'Udmurtskaya Respublika'),
(2398, '02', 'RW', 'Est'),
(2399, '03', 'RW', 'Nord'),
(2400, '04', 'RW', 'Ouest'),
(2401, '05', 'RW', 'Sud'),
(2402, '01', 'RW', 'Ville de Kigali'),
(2403, 'AC', 'SH', 'Ascension'),
(2404, 'HL', 'SH', 'Saint Helena'),
(2405, 'TA', 'SH', 'Tristan da Cunha'),
(2406, 'N', 'KN', 'Nevis'),
(2407, 'K', 'KN', 'Saint Kitts'),
(2408, '01', 'LC', 'Anse la Raye'),
(2409, '02', 'LC', 'Castries'),
(2410, '03', 'LC', 'Choiseul'),
(2411, '04', 'LC', 'Dauphin'),
(2412, '05', 'LC', 'Dennery'),
(2413, '06', 'LC', 'Gros Islet'),
(2414, '07', 'LC', 'Laborie'),
(2415, '08', 'LC', 'Micoud'),
(2416, '09', 'LC', 'Praslin'),
(2417, '10', 'LC', 'Soufrière'),
(2418, '11', 'LC', 'Vieux Fort'),
(2419, '01', 'VC', 'Charlotte'),
(2420, '06', 'VC', 'Grenadines'),
(2421, '02', 'VC', 'Saint Andrew'),
(2422, '03', 'VC', 'Saint David'),
(2423, '04', 'VC', 'Saint George'),
(2424, '05', 'VC', 'Saint Patrick'),
(2425, 'AA', 'WS', 'A\'ana'),
(2426, 'AL', 'WS', 'Aiga-i-le-Tai'),
(2427, 'AT', 'WS', 'Atua'),
(2428, 'FA', 'WS', 'Fa\'asaleleaga'),
(2429, 'GE', 'WS', 'Gaga\'emauga'),
(2430, 'GI', 'WS', 'Gagaifomauga'),
(2431, 'PA', 'WS', 'Palauli'),
(2432, 'SA', 'WS', 'Satupa\'itea'),
(2433, 'TU', 'WS', 'Tuamasaga'),
(2434, 'VF', 'WS', 'Va\'a-o-Fonoti'),
(2435, 'VS', 'WS', 'Vaisigano'),
(2436, '01', 'SM', 'Acquaviva'),
(2437, '06', 'SM', 'Borgo Maggiore'),
(2438, '02', 'SM', 'Chiesanuova'),
(2439, '03', 'SM', 'Domagnano'),
(2440, '04', 'SM', 'Faetano'),
(2441, '05', 'SM', 'Fiorentino'),
(2442, '08', 'SM', 'Montegiardino'),
(2443, '07', 'SM', 'San Marino'),
(2444, '09', 'SM', 'Serravalle'),
(2445, 'P', 'ST', 'Príncipe'),
(2446, 'S', 'ST', 'São Tomé'),
(2447, '11', 'SA', 'Al Bāḩah'),
(2448, '12', 'SA', 'Al Jawf'),
(2449, '03', 'SA', 'Al Madīnah'),
(2450, '05', 'SA', 'Al Qaşīm'),
(2451, '08', 'SA', 'Al Ḩudūd ash Shamālīyah'),
(2452, '01', 'SA', 'Ar Riyāḑ'),
(2453, '04', 'SA', 'Ash Sharqīyah'),
(2454, '09', 'SA', 'Jīzān'),
(2455, '02', 'SA', 'Makkah'),
(2456, '10', 'SA', 'Najrān'),
(2457, '07', 'SA', 'Tabūk'),
(2458, '14', 'SA', 'ٰĀsīr'),
(2459, '06', 'SA', 'Ḩā\'il'),
(2460, 'DK', 'SN', 'Dakar'),
(2461, 'DB', 'SN', 'Diourbel'),
(2462, 'FK', 'SN', 'Fatick'),
(2463, 'KA', 'SN', 'Kaffrine'),
(2464, 'KL', 'SN', 'Kaolack'),
(2465, 'KD', 'SN', 'Kolda'),
(2466, 'KE', 'SN', 'Kédougou'),
(2467, 'LG', 'SN', 'Louga'),
(2468, 'MT', 'SN', 'Matam'),
(2469, 'SL', 'SN', 'Saint-Louis'),
(2470, 'SE', 'SN', 'Sédhiou'),
(2471, 'TC', 'SN', 'Tambacounda'),
(2472, 'TH', 'SN', 'Thiès'),
(2473, 'ZG', 'SN', 'Ziguinchor'),
(2474, 'KM', 'RS', 'Kosovo-Metohija'),
(2475, 'VO', 'RS', 'Vojvodina'),
(2476, '02', 'SC', 'Anse Boileau'),
(2477, '03', 'SC', 'Anse Etoile'),
(2478, '05', 'SC', 'Anse Royale'),
(2479, '01', 'SC', 'Anse aux Pins'),
(2480, '04', 'SC', 'Au Cap'),
(2481, '06', 'SC', 'Baie Lazare'),
(2482, '07', 'SC', 'Baie Sainte Anne'),
(2483, '08', 'SC', 'Beau Vallon'),
(2484, '09', 'SC', 'Bel Air'),
(2485, '10', 'SC', 'Bel Ombre'),
(2486, '11', 'SC', 'Cascade'),
(2487, '16', 'SC', 'English River'),
(2488, '12', 'SC', 'Glacis'),
(2489, '13', 'SC', 'Grand Anse Mahe'),
(2490, '14', 'SC', 'Grand Anse Praslin'),
(2491, '15', 'SC', 'La Digue'),
(2492, '24', 'SC', 'Les Mamelles'),
(2493, '17', 'SC', 'Mont Buxton'),
(2494, '18', 'SC', 'Mont Fleuri'),
(2495, '19', 'SC', 'Plaisance'),
(2496, '20', 'SC', 'Pointe Larue'),
(2497, '21', 'SC', 'Port Glaud'),
(2498, '25', 'SC', 'Roche Caiman'),
(2499, '22', 'SC', 'Saint Louis'),
(2500, '23', 'SC', 'Takamaka'),
(2501, 'E', 'SL', 'Eastern'),
(2502, 'N', 'SL', 'Northern'),
(2503, 'S', 'SL', 'Southern'),
(2504, 'W', 'SL', 'Western Area'),
(2505, '01', 'SG', 'Central Singapore'),
(2506, '02', 'SG', 'North East'),
(2507, '03', 'SG', 'North West'),
(2508, '04', 'SG', 'South East'),
(2509, '05', 'SG', 'South West'),
(2510, 'BC', 'SK', 'Banskobystrický kraj'),
(2511, 'BL', 'SK', 'Bratislavský kraj'),
(2512, 'KI', 'SK', 'Košický kraj'),
(2513, 'NI', 'SK', 'Nitriansky kraj'),
(2514, 'PV', 'SK', 'Prešovský kraj'),
(2515, 'TC', 'SK', 'Trenčiansky kraj'),
(2516, 'TA', 'SK', 'Trnavský kraj'),
(2517, 'ZI', 'SK', 'Žilinský kraj'),
(2518, '001', 'SI', 'Ajdovščina'),
(2519, '195', 'SI', 'Apače'),
(2520, '002', 'SI', 'Beltinci'),
(2521, '148', 'SI', 'Benedikt'),
(2522, '149', 'SI', 'Bistrica ob Sotli'),
(2523, '003', 'SI', 'Bled'),
(2524, '150', 'SI', 'Bloke'),
(2525, '004', 'SI', 'Bohinj'),
(2526, '005', 'SI', 'Borovnica'),
(2527, '006', 'SI', 'Bovec'),
(2528, '151', 'SI', 'Braslovče'),
(2529, '007', 'SI', 'Brda'),
(2530, '008', 'SI', 'Brezovica'),
(2531, '009', 'SI', 'Brežice'),
(2532, '152', 'SI', 'Cankova'),
(2533, '011', 'SI', 'Celje'),
(2534, '012', 'SI', 'Cerklje na Gorenjskem'),
(2535, '013', 'SI', 'Cerknica'),
(2536, '014', 'SI', 'Cerkno'),
(2537, '153', 'SI', 'Cerkvenjak'),
(2538, '196', 'SI', 'Cirkulane'),
(2539, '018', 'SI', 'Destrnik'),
(2540, '019', 'SI', 'Divača'),
(2541, '154', 'SI', 'Dobje'),
(2542, '020', 'SI', 'Dobrepolje'),
(2543, '155', 'SI', 'Dobrna'),
(2544, '021', 'SI', 'Dobrova–Polhov Gradec'),
(2545, '156', 'SI', 'Dobrovnik'),
(2546, '022', 'SI', 'Dol pri Ljubljani'),
(2547, '157', 'SI', 'Dolenjske Toplice'),
(2548, '023', 'SI', 'Domžale'),
(2549, '024', 'SI', 'Dornava'),
(2550, '025', 'SI', 'Dravograd'),
(2551, '026', 'SI', 'Duplek'),
(2552, '027', 'SI', 'Gorenja vas–Poljane'),
(2553, '028', 'SI', 'Gorišnica'),
(2554, '207', 'SI', 'Gorje'),
(2555, '029', 'SI', 'Gornja Radgona'),
(2556, '030', 'SI', 'Gornji Grad'),
(2557, '031', 'SI', 'Gornji Petrovci'),
(2558, '158', 'SI', 'Grad'),
(2559, '032', 'SI', 'Grosuplje'),
(2560, '159', 'SI', 'Hajdina'),
(2561, '161', 'SI', 'Hodoš'),
(2562, '162', 'SI', 'Horjul'),
(2563, '160', 'SI', 'Hoče–Slivnica'),
(2564, '034', 'SI', 'Hrastnik'),
(2565, '035', 'SI', 'Hrpelje-Kozina'),
(2566, '036', 'SI', 'Idrija'),
(2567, '037', 'SI', 'Ig'),
(2568, '038', 'SI', 'Ilirska Bistrica'),
(2569, '039', 'SI', 'Ivančna Gorica'),
(2570, '040', 'SI', 'Izola'),
(2571, '041', 'SI', 'Jesenice'),
(2572, '163', 'SI', 'Jezersko'),
(2573, '042', 'SI', 'Juršinci'),
(2574, '043', 'SI', 'Kamnik'),
(2575, '044', 'SI', 'Kanal'),
(2576, '045', 'SI', 'Kidričevo'),
(2577, '046', 'SI', 'Kobarid'),
(2578, '047', 'SI', 'Kobilje'),
(2579, '049', 'SI', 'Komen'),
(2580, '164', 'SI', 'Komenda'),
(2581, '050', 'SI', 'Koper'),
(2582, '197', 'SI', 'Kosanjevica na Krki'),
(2583, '165', 'SI', 'Kostel'),
(2584, '051', 'SI', 'Kozje'),
(2585, '048', 'SI', 'Kočevje'),
(2586, '052', 'SI', 'Kranj'),
(2587, '053', 'SI', 'Kranjska Gora'),
(2588, '166', 'SI', 'Križevci'),
(2589, '054', 'SI', 'Krško'),
(2590, '055', 'SI', 'Kungota'),
(2591, '056', 'SI', 'Kuzma'),
(2592, '057', 'SI', 'Laško'),
(2593, '058', 'SI', 'Lenart'),
(2594, '059', 'SI', 'Lendava'),
(2595, '060', 'SI', 'Litija'),
(2596, '061', 'SI', 'Ljubljana'),
(2597, '062', 'SI', 'Ljubno'),
(2598, '063', 'SI', 'Ljutomer'),
(2599, '208', 'SI', 'Log-Dragomer'),
(2600, '064', 'SI', 'Logatec'),
(2601, '167', 'SI', 'Lovrenc na Pohorju'),
(2602, '065', 'SI', 'Loška Dolina'),
(2603, '066', 'SI', 'Loški Potok'),
(2604, '068', 'SI', 'Lukovica'),
(2605, '067', 'SI', 'Luče'),
(2606, '069', 'SI', 'Majšperk'),
(2607, '198', 'SI', 'Makole'),
(2608, '070', 'SI', 'Maribor'),
(2609, '168', 'SI', 'Markovci'),
(2610, '071', 'SI', 'Medvode'),
(2611, '072', 'SI', 'Mengeš'),
(2612, '073', 'SI', 'Metlika'),
(2613, '074', 'SI', 'Mežica'),
(2614, '169', 'SI', 'Miklavž na Dravskem Polju'),
(2615, '075', 'SI', 'Miren–Kostanjevica'),
(2616, '170', 'SI', 'Mirna Peč'),
(2617, '076', 'SI', 'Mislinja'),
(2618, '199', 'SI', 'Mokronog–Trebelno'),
(2619, '078', 'SI', 'Moravske Toplice'),
(2620, '077', 'SI', 'Moravče'),
(2621, '079', 'SI', 'Mozirje'),
(2622, '080', 'SI', 'Murska Sobota'),
(2623, '081', 'SI', 'Muta'),
(2624, '082', 'SI', 'Naklo'),
(2625, '083', 'SI', 'Nazarje'),
(2626, '084', 'SI', 'Nova Gorica'),
(2627, '085', 'SI', 'Novo Mesto'),
(2628, '086', 'SI', 'Odranci'),
(2629, '171', 'SI', 'Oplotnica'),
(2630, '087', 'SI', 'Ormož'),
(2631, '088', 'SI', 'Osilnica'),
(2632, '089', 'SI', 'Pesnica'),
(2633, '090', 'SI', 'Piran'),
(2634, '091', 'SI', 'Pivka'),
(2635, '172', 'SI', 'Podlehnik'),
(2636, '093', 'SI', 'Podvelka'),
(2637, '092', 'SI', 'Podčetrtek'),
(2638, '200', 'SI', 'Poljčane'),
(2639, '173', 'SI', 'Polzela'),
(2640, '094', 'SI', 'Postojna'),
(2641, '174', 'SI', 'Prebold'),
(2642, '095', 'SI', 'Preddvor'),
(2643, '175', 'SI', 'Prevalje'),
(2644, '096', 'SI', 'Ptuj'),
(2645, '097', 'SI', 'Puconci'),
(2646, '100', 'SI', 'Radenci'),
(2647, '099', 'SI', 'Radeče'),
(2648, '101', 'SI', 'Radlje ob Dravi'),
(2649, '102', 'SI', 'Radovljica'),
(2650, '103', 'SI', 'Ravne na Koroškem'),
(2651, '176', 'SI', 'Razkrižje'),
(2652, '098', 'SI', 'Rače–Fram'),
(2653, '201', 'SI', 'Renče-Vogrsko'),
(2654, '209', 'SI', 'Rečica ob Savinji'),
(2655, '104', 'SI', 'Ribnica'),
(2656, '177', 'SI', 'Ribnica na Pohorju'),
(2657, '107', 'SI', 'Rogatec'),
(2658, '106', 'SI', 'Rogaška Slatina'),
(2659, '105', 'SI', 'Rogašovci'),
(2660, '108', 'SI', 'Ruše'),
(2661, '178', 'SI', 'Selnica ob Dravi'),
(2662, '109', 'SI', 'Semič'),
(2663, '110', 'SI', 'Sevnica'),
(2664, '111', 'SI', 'Sežana'),
(2665, '112', 'SI', 'Slovenj Gradec'),
(2666, '113', 'SI', 'Slovenska Bistrica'),
(2667, '114', 'SI', 'Slovenske Konjice'),
(2668, '179', 'SI', 'Sodražica'),
(2669, '180', 'SI', 'Solčava'),
(2670, '202', 'SI', 'Središče ob Dravi'),
(2671, '115', 'SI', 'Starše'),
(2672, '203', 'SI', 'Straža'),
(2673, '181', 'SI', 'Sveta Ana'),
(2674, '204', 'SI', 'Sveta Trojica v Slovenskih Goricah'),
(2675, '182', 'SI', 'Sveti Andraž v Slovenskih Goricah'),
(2676, '116', 'SI', 'Sveti Jurij'),
(2677, '210', 'SI', 'Sveti Jurij v Slovenskih Goricah'),
(2678, '205', 'SI', 'Sveti Tomaž'),
(2679, '184', 'SI', 'Tabor'),
(2680, '010', 'SI', 'Tišina'),
(2681, '128', 'SI', 'Tolmin'),
(2682, '129', 'SI', 'Trbovlje'),
(2683, '130', 'SI', 'Trebnje'),
(2684, '185', 'SI', 'Trnovska Vas'),
(2685, '186', 'SI', 'Trzin'),
(2686, '131', 'SI', 'Tržič'),
(2687, '132', 'SI', 'Turnišče'),
(2688, '133', 'SI', 'Velenje'),
(2689, '187', 'SI', 'Velika Polana'),
(2690, '134', 'SI', 'Velike Lašče'),
(2691, '188', 'SI', 'Veržej'),
(2692, '135', 'SI', 'Videm'),
(2693, '136', 'SI', 'Vipava'),
(2694, '137', 'SI', 'Vitanje'),
(2695, '138', 'SI', 'Vodice'),
(2696, '139', 'SI', 'Vojnik'),
(2697, '189', 'SI', 'Vransko'),
(2698, '140', 'SI', 'Vrhnika'),
(2699, '141', 'SI', 'Vuzenica'),
(2700, '142', 'SI', 'Zagorje ob Savi'),
(2701, '143', 'SI', 'Zavrč'),
(2702, '144', 'SI', 'Zreče'),
(2703, '015', 'SI', 'Črenšovci'),
(2704, '016', 'SI', 'Črna na Koroškem'),
(2705, '017', 'SI', 'Črnomelj'),
(2706, '033', 'SI', 'Šalovci'),
(2707, '183', 'SI', 'Šempeter–Vrtojba'),
(2708, '118', 'SI', 'Šentilj'),
(2709, '119', 'SI', 'Šentjernej'),
(2710, '120', 'SI', 'Šentjur'),
(2711, '211', 'SI', 'Šentrupert'),
(2712, '117', 'SI', 'Šenčur'),
(2713, '121', 'SI', 'Škocjan'),
(2714, '122', 'SI', 'Škofja Loka'),
(2715, '123', 'SI', 'Škofljica'),
(2716, '124', 'SI', 'Šmarje pri Jelšah'),
(2717, '206', 'SI', 'Šmarješke Toplice'),
(2718, '125', 'SI', 'Šmartno ob Paki'),
(2719, '194', 'SI', 'Šmartno pri Litiji'),
(2720, '126', 'SI', 'Šoštanj'),
(2721, '127', 'SI', 'Štore'),
(2722, '190', 'SI', 'Žalec'),
(2723, '146', 'SI', 'Železniki'),
(2724, '191', 'SI', 'Žetale'),
(2725, '147', 'SI', 'Žiri'),
(2726, '192', 'SI', 'Žirovnica'),
(2727, '193', 'SI', 'Žužemberk'),
(2728, 'CT', 'SB', 'Capital Territory'),
(2729, 'CE', 'SB', 'Central'),
(2730, 'CH', 'SB', 'Choiseul'),
(2731, 'GU', 'SB', 'Guadalcanal'),
(2732, 'IS', 'SB', 'Isabel'),
(2733, 'MK', 'SB', 'Makira-Ulawa'),
(2734, 'ML', 'SB', 'Malaita'),
(2735, 'RB', 'SB', 'Rennell and Bellona'),
(2736, 'TE', 'SB', 'Temotu'),
(2737, 'WE', 'SB', 'Western'),
(2738, 'AW', 'SO', 'Awdal'),
(2739, 'BK', 'SO', 'Bakool'),
(2740, 'BN', 'SO', 'Banaadir'),
(2741, 'BR', 'SO', 'Bari'),
(2742, 'BY', 'SO', 'Bay'),
(2743, 'GA', 'SO', 'Galguduud'),
(2744, 'GE', 'SO', 'Gedo'),
(2745, 'HI', 'SO', 'Hiiraan'),
(2746, 'JD', 'SO', 'Jubbada Dhexe'),
(2747, 'JH', 'SO', 'Jubbada Hoose'),
(2748, 'MU', 'SO', 'Mudug'),
(2749, 'NU', 'SO', 'Nugaal'),
(2750, 'SA', 'SO', 'Sanaag'),
(2751, 'SD', 'SO', 'Shabeellaha Dhexe'),
(2752, 'SH', 'SO', 'Shabeellaha Hoose'),
(2753, 'SO', 'SO', 'Sool'),
(2754, 'TO', 'SO', 'Togdheer'),
(2755, 'WO', 'SO', 'Woqooyi Galbeed'),
(2756, 'EC', 'ZA', 'Eastern Cape'),
(2757, 'FS', 'ZA', 'Free State'),
(2758, 'GT', 'ZA', 'Gauteng'),
(2759, 'NL', 'ZA', 'KwaZulu-Natal'),
(2760, 'LP', 'ZA', 'Limpopo'),
(2761, 'MP', 'ZA', 'Mpumalanga'),
(2762, 'NW', 'ZA', 'North West'),
(2763, 'NC', 'ZA', 'Northern Cape'),
(2764, 'WC', 'ZA', 'Western Cape'),
(2765, '26', 'KR', 'Busan-gwangyeoksi'),
(2766, '43', 'KR', 'Chungcheongbuk-do'),
(2767, '44', 'KR', 'Chungcheongnam-do'),
(2768, '27', 'KR', 'Daegu-gwangyeoksi'),
(2769, '30', 'KR', 'Daejeon-gwangyeoksi'),
(2770, '42', 'KR', 'Gangwon-do'),
(2771, '29', 'KR', 'Gwangju-gwangyeoksi'),
(2772, '41', 'KR', 'Gyeonggi-do'),
(2773, '47', 'KR', 'Gyeongsangbuk-do'),
(2774, '48', 'KR', 'Gyeongsangnam-do'),
(2775, '28', 'KR', 'Incheon-gwangyeoksi'),
(2776, '49', 'KR', 'Jeju-teukbyeoljachido'),
(2777, '45', 'KR', 'Jeollabuk-do'),
(2778, '46', 'KR', 'Jeollanam-do'),
(2779, '50', 'KR', 'Sejong'),
(2780, '11', 'KR', 'Seoul-teukbyeolsi'),
(2781, '31', 'KR', 'Ulsan-gwangyeoksi'),
(2782, 'EC', 'SS', 'Central Equatoria'),
(2783, 'EE', 'SS', 'Eastern Equatoria'),
(2784, 'JG', 'SS', 'Jonglei'),
(2785, 'LK', 'SS', 'Lakes'),
(2786, 'BN', 'SS', 'Northern Bahr el Ghazal'),
(2787, 'UY', 'SS', 'Unity'),
(2788, 'NU', 'SS', 'Upper Nile'),
(2789, 'WR', 'SS', 'Warrap'),
(2790, 'BW', 'SS', 'Western Bahr el Ghazal'),
(2791, 'EW', 'SS', 'Western Equatoria'),
(2792, 'C', 'ES', 'A Coruña'),
(2793, 'AB', 'ES', 'Albacete'),
(2794, 'A', 'ES', 'Alicante'),
(2795, 'AL', 'ES', 'Almería'),
(2796, 'O', 'ES', 'Asturias'),
(2797, 'BA', 'ES', 'Badajoz'),
(2798, 'PM', 'ES', 'Balears'),
(2799, 'B', 'ES', 'Barcelona'),
(2800, 'BU', 'ES', 'Burgos'),
(2801, 'S', 'ES', 'Cantabria'),
(2802, 'CS', 'ES', 'Castellón'),
(2803, 'CR', 'ES', 'Ciudad Real'),
(2804, 'CU', 'ES', 'Cuenca'),
(2805, 'CC', 'ES', 'Cáceres'),
(2806, 'CA', 'ES', 'Cádiz'),
(2807, 'CO', 'ES', 'Córdoba'),
(2808, 'GI', 'ES', 'Girona'),
(2809, 'GR', 'ES', 'Granada'),
(2810, 'GU', 'ES', 'Guadalajara'),
(2811, 'SS', 'ES', 'Guipúzcoa'),
(2812, 'H', 'ES', 'Huelva'),
(2813, 'HU', 'ES', 'Huesca'),
(2814, 'J', 'ES', 'Jaén'),
(2815, 'LO', 'ES', 'La Rioja'),
(2816, 'GC', 'ES', 'Las Palmas'),
(2817, 'LE', 'ES', 'León'),
(2818, 'L', 'ES', 'Lleida'),
(2819, 'LU', 'ES', 'Lugo'),
(2820, 'M', 'ES', 'Madrid'),
(2821, 'MU', 'ES', 'Murcia'),
(2822, 'MA', 'ES', 'Málaga'),
(2823, 'NA', 'ES', 'Navarra'),
(2824, 'OR', 'ES', 'Ourense'),
(2825, 'P', 'ES', 'Palencia'),
(2826, 'PO', 'ES', 'Pontevedra'),
(2827, 'SA', 'ES', 'Salamanca'),
(2828, 'TF', 'ES', 'Santa Cruz de Tenerife'),
(2829, 'SG', 'ES', 'Segovia'),
(2830, 'SE', 'ES', 'Sevilla'),
(2831, 'SO', 'ES', 'Soria'),
(2832, 'T', 'ES', 'Tarragona'),
(2833, 'TE', 'ES', 'Teruel'),
(2834, 'TO', 'ES', 'Toledo'),
(2835, 'V', 'ES', 'Valencia'),
(2836, 'VA', 'ES', 'Valladolid'),
(2837, 'BI', 'ES', 'Vizcaya'),
(2838, 'ZA', 'ES', 'Zamora'),
(2839, 'Z', 'ES', 'Zaragoza'),
(2840, 'VI', 'ES', 'Álava'),
(2841, 'AV', 'ES', 'Ávila'),
(2842, 'CE', 'ES', 'Ceuta'),
(2843, 'ML', 'ES', 'Melilla'),
(2844, 'AN', 'ES', 'Andalucía'),
(2845, 'AR', 'ES', 'Aragón'),
(2846, 'AS', 'ES', 'Asturias, Principado de'),
(2847, 'CN', 'ES', 'Canarias'),
(2848, 'CB', 'ES', 'Cantabria'),
(2849, 'CL', 'ES', 'Castilla y León'),
(2850, 'CM', 'ES', 'Castilla-La Mancha'),
(2851, 'CT', 'ES', 'Catalunya'),
(2852, 'EX', 'ES', 'Extremadura'),
(2853, 'GA', 'ES', 'Galicia'),
(2854, 'IB', 'ES', 'Illes Balears'),
(2855, 'RI', 'ES', 'La Rioja'),
(2856, 'MD', 'ES', 'Madrid, Comunidad de'),
(2857, 'MC', 'ES', 'Murcia, Región de'),
(2858, 'NC', 'ES', 'Navarra, Comunidad Foral de'),
(2859, 'PV', 'ES', 'País Vasco'),
(2860, 'VC', 'ES', 'Valenciana, Comunidad'),
(2861, '2', 'LK', 'Central Province'),
(2862, '5', 'LK', 'Eastern Province'),
(2863, '7', 'LK', 'North Central Province'),
(2864, '6', 'LK', 'North Western Province'),
(2865, '4', 'LK', 'Northern Province'),
(2866, '9', 'LK', 'Sabaragamuwa Province'),
(2867, '3', 'LK', 'Southern Province'),
(2868, '8', 'LK', 'Uva Province'),
(2869, '1', 'LK', 'Western Province'),
(2870, 'RS', 'SD', 'Al Baḩr al Aḩmar'),
(2871, 'GZ', 'SD', 'Al Jazīrah'),
(2872, 'KH', 'SD', 'Al Kharţūm'),
(2873, 'GD', 'SD', 'Al Qaḑārif'),
(2874, 'NR', 'SD', 'An Nīl'),
(2875, 'NW', 'SD', 'An Nīl al Abyaḑ'),
(2876, 'NB', 'SD', 'An Nīl al Azraq'),
(2877, 'NO', 'SD', 'Ash Shamālīyah'),
(2878, 'DW', 'SD', 'Gharb Dārfūr'),
(2879, 'DS', 'SD', 'Janūb Dārfūr'),
(2880, 'KS', 'SD', 'Janūb Kurdufān'),
(2881, 'KA', 'SD', 'Kassalā'),
(2882, 'DN', 'SD', 'Shamāl Dārfūr'),
(2883, 'KN', 'SD', 'Shamāl Kurdufān'),
(2884, 'DE', 'SD', 'Sharq Dārfūr'),
(2885, 'SI', 'SD', 'Sinnār'),
(2886, 'DC', 'SD', 'Zalingei'),
(2887, 'BR', 'SR', 'Brokopondo'),
(2888, 'CM', 'SR', 'Commewijne'),
(2889, 'CR', 'SR', 'Coronie'),
(2890, 'MA', 'SR', 'Marowijne'),
(2891, 'NI', 'SR', 'Nickerie'),
(2892, 'PR', 'SR', 'Para'),
(2893, 'PM', 'SR', 'Paramaribo'),
(2894, 'SA', 'SR', 'Saramacca'),
(2895, 'SI', 'SR', 'Sipaliwini'),
(2896, 'WA', 'SR', 'Wanica'),
(2897, 'HH', 'SZ', 'Hhohho'),
(2898, 'LU', 'SZ', 'Lubombo'),
(2899, 'MA', 'SZ', 'Manzini'),
(2900, 'SH', 'SZ', 'Shiselweni'),
(2901, 'K', 'SE', 'Blekinge län'),
(2902, 'W', 'SE', 'Dalarnas län'),
(2903, 'I', 'SE', 'Gotlands län'),
(2904, 'X', 'SE', 'Gävleborgs län'),
(2905, 'N', 'SE', 'Hallands län'),
(2906, 'Z', 'SE', 'Jämtlands län'),
(2907, 'F', 'SE', 'Jönköpings län'),
(2908, 'H', 'SE', 'Kalmar län'),
(2909, 'G', 'SE', 'Kronobergs län'),
(2910, 'BD', 'SE', 'Norrbottens län'),
(2911, 'M', 'SE', 'Skåne län'),
(2912, 'AB', 'SE', 'Stockholms län'),
(2913, 'D', 'SE', 'Södermanlands län'),
(2914, 'C', 'SE', 'Uppsala län'),
(2915, 'S', 'SE', 'Värmlands län'),
(2916, 'AC', 'SE', 'Västerbottens län'),
(2917, 'Y', 'SE', 'Västernorrlands län'),
(2918, 'U', 'SE', 'Västmanlands län'),
(2919, 'O', 'SE', 'Västra Götalands län'),
(2920, 'T', 'SE', 'Örebro län'),
(2921, 'E', 'SE', 'Östergötlands län'),
(2922, 'AG', 'CH', 'Aargau'),
(2923, 'AR', 'CH', 'Appenzell Ausserrhoden'),
(2924, 'AI', 'CH', 'Appenzell Innerrhoden'),
(2925, 'BL', 'CH', 'Basel-Landschaft'),
(2926, 'BS', 'CH', 'Basel-Stadt'),
(2927, 'BE', 'CH', 'Bern'),
(2928, 'FR', 'CH', 'Fribourg'),
(2929, 'GE', 'CH', 'Genève'),
(2930, 'GL', 'CH', 'Glarus'),
(2931, 'GR', 'CH', 'Graubünden'),
(2932, 'JU', 'CH', 'Jura'),
(2933, 'LU', 'CH', 'Luzern'),
(2934, 'NE', 'CH', 'Neuchâtel'),
(2935, 'NW', 'CH', 'Nidwalden'),
(2936, 'OW', 'CH', 'Obwalden'),
(2937, 'SG', 'CH', 'Sankt Gallen'),
(2938, 'SH', 'CH', 'Schaffhausen'),
(2939, 'SZ', 'CH', 'Schwyz'),
(2940, 'SO', 'CH', 'Solothurn'),
(2941, 'TG', 'CH', 'Thurgau'),
(2942, 'TI', 'CH', 'Ticino'),
(2943, 'UR', 'CH', 'Uri'),
(2944, 'VS', 'CH', 'Valais'),
(2945, 'VD', 'CH', 'Vaud'),
(2946, 'ZG', 'CH', 'Zug'),
(2947, 'ZH', 'CH', 'Zürich'),
(2948, 'LA', 'SY', 'Al Lādhiqīyah'),
(2949, 'QU', 'SY', 'Al Qunayţirah'),
(2950, 'HA', 'SY', 'Al Ḩasakah'),
(2951, 'RA', 'SY', 'Ar Raqqah'),
(2952, 'SU', 'SY', 'As Suwaydā\''),
(2953, 'DR', 'SY', 'Darٰā'),
(2954, 'DY', 'SY', 'Dayr az Zawr'),
(2955, 'DI', 'SY', 'Dimashq'),
(2956, 'ID', 'SY', 'Idlib'),
(2957, 'RD', 'SY', 'Rīf Dimashq'),
(2958, 'TA', 'SY', 'Ţarţūs'),
(2959, 'HL', 'SY', 'Ḩalab'),
(2960, 'HM', 'SY', 'Ḩamāh'),
(2961, 'HI', 'SY', 'Ḩimş'),
(2962, 'CHA', 'TW', 'Changhua'),
(2963, 'CYQ', 'TW', 'Chiayi'),
(2964, 'CYI', 'TW', 'Chiayi'),
(2965, 'HSZ', 'TW', 'Hsinchu'),
(2966, 'HSQ', 'TW', 'Hsinchu'),
(2967, 'HUA', 'TW', 'Hualien'),
(2968, 'ILA', 'TW', 'Ilan'),
(2969, 'KHQ', 'TW', 'Kaohsiung'),
(2970, 'KHH', 'TW', 'Kaohsiung'),
(2971, 'KEE', 'TW', 'Keelung'),
(2972, 'MIA', 'TW', 'Miaoli'),
(2973, 'NAN', 'TW', 'Nantou'),
(2974, 'PEN', 'TW', 'Penghu'),
(2975, 'PIF', 'TW', 'Pingtung'),
(2976, 'TXG', 'TW', 'Taichung'),
(2977, 'TXQ', 'TW', 'Taichung'),
(2978, 'TNN', 'TW', 'Tainan'),
(2979, 'TNQ', 'TW', 'Tainan'),
(2980, 'TPE', 'TW', 'Taipei'),
(2981, 'TPQ', 'TW', 'Taipei'),
(2982, 'TTT', 'TW', 'Taitung'),
(2983, 'TAO', 'TW', 'Taoyuan'),
(2984, 'YUN', 'TW', 'Yunlin'),
(2985, 'DU', 'TJ', 'Dushanbe'),
(2986, 'KT', 'TJ', 'Khatlon'),
(2987, 'GB', 'TJ', 'Kŭhistoni Badakhshon'),
(2988, 'SU', 'TJ', 'Sughd'),
(2989, '01', 'TZ', 'Arusha'),
(2990, '02', 'TZ', 'Dar es Salaam'),
(2991, '03', 'TZ', 'Dodoma'),
(2992, '04', 'TZ', 'Iringa'),
(2993, '05', 'TZ', 'Kagera'),
(2994, '06', 'TZ', 'Kaskazini Pemba'),
(2995, '07', 'TZ', 'Kaskazini Unguja'),
(2996, '08', 'TZ', 'Kigoma'),
(2997, '09', 'TZ', 'Kilimanjaro'),
(2998, '10', 'TZ', 'Kusini Pemba'),
(2999, '11', 'TZ', 'Kusini Unguja'),
(3000, '12', 'TZ', 'Lindi'),
(3001, '26', 'TZ', 'Manyara'),
(3002, '13', 'TZ', 'Mara'),
(3003, '14', 'TZ', 'Mbeya'),
(3004, '15', 'TZ', 'Mjini Magharibi'),
(3005, '16', 'TZ', 'Morogoro'),
(3006, '17', 'TZ', 'Mtwara'),
(3007, '18', 'TZ', 'Mwanza'),
(3008, '19', 'TZ', 'Pwani'),
(3009, '20', 'TZ', 'Rukwa'),
(3010, '21', 'TZ', 'Ruvuma'),
(3011, '22', 'TZ', 'Shinyanga'),
(3012, '23', 'TZ', 'Singida'),
(3013, '24', 'TZ', 'Tabora'),
(3014, '25', 'TZ', 'Tanga'),
(3015, '37', 'TH', 'Amnat Charoen'),
(3016, '15', 'TH', 'Ang Thong'),
(3017, '38', 'TH', 'Bueng Kan'),
(3018, '31', 'TH', 'Buri Ram'),
(3019, '24', 'TH', 'Chachoengsao'),
(3020, '18', 'TH', 'Chai Nat'),
(3021, '36', 'TH', 'Chaiyaphum'),
(3022, '22', 'TH', 'Chanthaburi'),
(3023, '50', 'TH', 'Chiang Mai'),
(3024, '57', 'TH', 'Chiang Rai'),
(3025, '20', 'TH', 'Chon Buri'),
(3026, '86', 'TH', 'Chumphon'),
(3027, '46', 'TH', 'Kalasin'),
(3028, '62', 'TH', 'Kamphaeng Phet'),
(3029, '71', 'TH', 'Kanchanaburi'),
(3030, '40', 'TH', 'Khon Kaen'),
(3031, '81', 'TH', 'Krabi'),
(3032, '10', 'TH', 'Krung Thep Maha Nakhon'),
(3033, '52', 'TH', 'Lampang'),
(3034, '51', 'TH', 'Lamphun'),
(3035, '42', 'TH', 'Loei'),
(3036, '16', 'TH', 'Lop Buri'),
(3037, '58', 'TH', 'Mae Hong Son'),
(3038, '44', 'TH', 'Maha Sarakham'),
(3039, '49', 'TH', 'Mukdahan'),
(3040, '26', 'TH', 'Nakhon Nayok'),
(3041, '73', 'TH', 'Nakhon Pathom'),
(3042, '48', 'TH', 'Nakhon Phanom'),
(3043, '30', 'TH', 'Nakhon Ratchasima'),
(3044, '60', 'TH', 'Nakhon Sawan'),
(3045, '80', 'TH', 'Nakhon Si Thammarat'),
(3046, '55', 'TH', 'Nan'),
(3047, '96', 'TH', 'Narathiwat'),
(3048, '39', 'TH', 'Nong Bua Lam Phu'),
(3049, '43', 'TH', 'Nong Khai'),
(3050, '12', 'TH', 'Nonthaburi'),
(3051, '13', 'TH', 'Pathum Thani'),
(3052, '94', 'TH', 'Pattani'),
(3053, '82', 'TH', 'Phangnga'),
(3054, '93', 'TH', 'Phatthalung'),
(3055, 'S', 'TH', 'Phatthaya'),
(3056, '56', 'TH', 'Phayao'),
(3057, '67', 'TH', 'Phetchabun'),
(3058, '76', 'TH', 'Phetchaburi'),
(3059, '66', 'TH', 'Phichit'),
(3060, '65', 'TH', 'Phitsanulok'),
(3061, '14', 'TH', 'Phra Nakhon Si Ayutthaya'),
(3062, '54', 'TH', 'Phrae'),
(3063, '83', 'TH', 'Phuket'),
(3064, '25', 'TH', 'Prachin Buri'),
(3065, '77', 'TH', 'Prachuap Khiri Khan'),
(3066, '85', 'TH', 'Ranong'),
(3067, '70', 'TH', 'Ratchaburi'),
(3068, '21', 'TH', 'Rayong'),
(3069, '45', 'TH', 'Roi Et'),
(3070, '27', 'TH', 'Sa Kaeo'),
(3071, '47', 'TH', 'Sakon Nakhon'),
(3072, '11', 'TH', 'Samut Prakan'),
(3073, '74', 'TH', 'Samut Sakhon'),
(3074, '75', 'TH', 'Samut Songkhram'),
(3075, '19', 'TH', 'Saraburi'),
(3076, '91', 'TH', 'Satun'),
(3077, '33', 'TH', 'Si Sa Ket'),
(3078, '17', 'TH', 'Sing Buri'),
(3079, '90', 'TH', 'Songkhla'),
(3080, '64', 'TH', 'Sukhothai'),
(3081, '72', 'TH', 'Suphan Buri'),
(3082, '84', 'TH', 'Surat Thani'),
(3083, '32', 'TH', 'Surin'),
(3084, '63', 'TH', 'Tak'),
(3085, '92', 'TH', 'Trang'),
(3086, '23', 'TH', 'Trat'),
(3087, '34', 'TH', 'Ubon Ratchathani'),
(3088, '41', 'TH', 'Udon Thani'),
(3089, '61', 'TH', 'Uthai Thani'),
(3090, '53', 'TH', 'Uttaradit'),
(3091, '95', 'TH', 'Yala'),
(3092, '35', 'TH', 'Yasothon'),
(3093, 'AL', 'TL', 'Aileu'),
(3094, 'AN', 'TL', 'Ainaro'),
(3095, 'BA', 'TL', 'Baucau'),
(3096, 'BO', 'TL', 'Bobonaro'),
(3097, 'CO', 'TL', 'Cova Lima'),
(3098, 'DI', 'TL', 'Díli'),
(3099, 'ER', 'TL', 'Ermera'),
(3100, 'LA', 'TL', 'Lautem'),
(3101, 'LI', 'TL', 'Liquiça'),
(3102, 'MT', 'TL', 'Manatuto'),
(3103, 'MF', 'TL', 'Manufahi'),
(3104, 'OE', 'TL', 'Oecussi'),
(3105, 'VI', 'TL', 'Viqueque'),
(3106, 'C', 'TG', 'Centre'),
(3107, 'K', 'TG', 'Kara'),
(3108, 'M', 'TG', 'Maritime'),
(3109, 'P', 'TG', 'Plateaux'),
(3110, 'S', 'TG', 'Savannes'),
(3111, '01', 'TO', '\'Eua'),
(3112, '02', 'TO', 'Ha\'apai'),
(3113, '03', 'TO', 'Niuas'),
(3114, '04', 'TO', 'Tongatapu'),
(3115, '05', 'TO', 'Vava\'u'),
(3116, 'ARI', 'TT', 'Arima'),
(3117, 'CHA', 'TT', 'Chaguanas'),
(3118, 'CTT', 'TT', 'Couva-Tabaquite-Talparo'),
(3119, 'DMN', 'TT', 'Diego Martin'),
(3120, 'ETO', 'TT', 'Eastern Tobago'),
(3121, 'PED', 'TT', 'Penal-Debe'),
(3122, 'PTF', 'TT', 'Point Fortin'),
(3123, 'POS', 'TT', 'Port of Spain'),
(3124, 'PRT', 'TT', 'Princes Town'),
(3125, 'RCM', 'TT', 'Rio Claro-Mayaro'),
(3126, 'SFO', 'TT', 'San Fernando'),
(3127, 'SJL', 'TT', 'San Juan-Laventille'),
(3128, 'SGE', 'TT', 'Sangre Grande'),
(3129, 'SIP', 'TT', 'Siparia'),
(3130, 'TUP', 'TT', 'Tunapuna-Piarco'),
(3131, 'WTO', 'TT', 'Western Tobago'),
(3132, '12', 'TN', 'Ariana'),
(3133, '13', 'TN', 'Ben Arous'),
(3134, '23', 'TN', 'Bizerte'),
(3135, '31', 'TN', 'Béja'),
(3136, '81', 'TN', 'Gabès');
INSERT INTO `Countries_states` (`id`, `Code`, `Country`, `Name`) VALUES
(3137, '71', 'TN', 'Gafsa'),
(3138, '32', 'TN', 'Jendouba'),
(3139, '41', 'TN', 'Kairouan'),
(3140, '42', 'TN', 'Kasserine'),
(3141, '73', 'TN', 'Kebili'),
(3142, '14', 'TN', 'La Manouba'),
(3143, '33', 'TN', 'Le Kef'),
(3144, '53', 'TN', 'Mahdia'),
(3145, '82', 'TN', 'Medenine'),
(3146, '52', 'TN', 'Monastir'),
(3147, '21', 'TN', 'Nabeul'),
(3148, '61', 'TN', 'Sfax'),
(3149, '43', 'TN', 'Sidi Bouzid'),
(3150, '34', 'TN', 'Siliana'),
(3151, '51', 'TN', 'Sousse'),
(3152, '83', 'TN', 'Tataouine'),
(3153, '72', 'TN', 'Tozeur'),
(3154, '11', 'TN', 'Tunis'),
(3155, '22', 'TN', 'Zaghouan'),
(3156, '01', 'TR', 'Adana'),
(3157, '02', 'TR', 'Adıyaman'),
(3158, '03', 'TR', 'Afyonkarahisar'),
(3159, '68', 'TR', 'Aksaray'),
(3160, '05', 'TR', 'Amasya'),
(3161, '06', 'TR', 'Ankara'),
(3162, '07', 'TR', 'Antalya'),
(3163, '75', 'TR', 'Ardahan'),
(3164, '08', 'TR', 'Artvin'),
(3165, '09', 'TR', 'Aydın'),
(3166, '04', 'TR', 'Ağrı'),
(3167, '10', 'TR', 'Balıkesir'),
(3168, '74', 'TR', 'Bartın'),
(3169, '72', 'TR', 'Batman'),
(3170, '69', 'TR', 'Bayburt'),
(3171, '11', 'TR', 'Bilecik'),
(3172, '12', 'TR', 'Bingöl'),
(3173, '13', 'TR', 'Bitlis'),
(3174, '14', 'TR', 'Bolu'),
(3175, '15', 'TR', 'Burdur'),
(3176, '16', 'TR', 'Bursa'),
(3177, '20', 'TR', 'Denizli'),
(3178, '21', 'TR', 'Diyarbakır'),
(3179, '81', 'TR', 'Düzce'),
(3180, '22', 'TR', 'Edirne'),
(3181, '23', 'TR', 'Elazığ'),
(3182, '24', 'TR', 'Erzincan'),
(3183, '25', 'TR', 'Erzurum'),
(3184, '26', 'TR', 'Eskişehir'),
(3185, '27', 'TR', 'Gaziantep'),
(3186, '28', 'TR', 'Giresun'),
(3187, '29', 'TR', 'Gümüşhane'),
(3188, '30', 'TR', 'Hakkâri'),
(3189, '31', 'TR', 'Hatay'),
(3190, '32', 'TR', 'Isparta'),
(3191, '76', 'TR', 'Iğdır'),
(3192, '46', 'TR', 'Kahramanmaraş'),
(3193, '78', 'TR', 'Karabük'),
(3194, '70', 'TR', 'Karaman'),
(3195, '36', 'TR', 'Kars'),
(3196, '37', 'TR', 'Kastamonu'),
(3197, '38', 'TR', 'Kayseri'),
(3198, '79', 'TR', 'Kilis'),
(3199, '41', 'TR', 'Kocaeli'),
(3200, '42', 'TR', 'Konya'),
(3201, '43', 'TR', 'Kütahya'),
(3202, '39', 'TR', 'Kırklareli'),
(3203, '71', 'TR', 'Kırıkkale'),
(3204, '40', 'TR', 'Kırşehir'),
(3205, '44', 'TR', 'Malatya'),
(3206, '45', 'TR', 'Manisa'),
(3207, '47', 'TR', 'Mardin'),
(3208, '33', 'TR', 'Mersin'),
(3209, '48', 'TR', 'Muğla'),
(3210, '49', 'TR', 'Muş'),
(3211, '50', 'TR', 'Nevşehir'),
(3212, '51', 'TR', 'Niğde'),
(3213, '52', 'TR', 'Ordu'),
(3214, '80', 'TR', 'Osmaniye'),
(3215, '53', 'TR', 'Rize'),
(3216, '54', 'TR', 'Sakarya'),
(3217, '55', 'TR', 'Samsun'),
(3218, '56', 'TR', 'Siirt'),
(3219, '57', 'TR', 'Sinop'),
(3220, '58', 'TR', 'Sivas'),
(3221, '59', 'TR', 'Tekirdağ'),
(3222, '60', 'TR', 'Tokat'),
(3223, '61', 'TR', 'Trabzon'),
(3224, '62', 'TR', 'Tunceli'),
(3225, '64', 'TR', 'Uşak'),
(3226, '65', 'TR', 'Van'),
(3227, '77', 'TR', 'Yalova'),
(3228, '66', 'TR', 'Yozgat'),
(3229, '67', 'TR', 'Zonguldak'),
(3230, '17', 'TR', 'Çanakkale'),
(3231, '18', 'TR', 'Çankırı'),
(3232, '19', 'TR', 'Çorum'),
(3233, '34', 'TR', 'İstanbul'),
(3234, '35', 'TR', 'İzmir'),
(3235, '63', 'TR', 'Şanlıurfa'),
(3236, '73', 'TR', 'Şırnak'),
(3237, 'A', 'TM', 'Ahal'),
(3238, 'S', 'TM', 'Aşgabat'),
(3239, 'B', 'TM', 'Balkan'),
(3240, 'D', 'TM', 'Daşoguz'),
(3241, 'L', 'TM', 'Lebap'),
(3242, 'M', 'TM', 'Mary'),
(3243, 'FUN', 'TV', 'Funafuti'),
(3244, 'NMG', 'TV', 'Nanumanga'),
(3245, 'NMA', 'TV', 'Nanumea'),
(3246, 'NIT', 'TV', 'Niutao'),
(3247, 'NUI', 'TV', 'Nui'),
(3248, 'NKF', 'TV', 'Nukufetau'),
(3249, 'NKL', 'TV', 'Nukulaelae'),
(3250, 'VAI', 'TV', 'Vaitupu'),
(3251, 'C', 'UG', 'Central'),
(3252, 'E', 'UG', 'Eastern'),
(3253, 'N', 'UG', 'Northern'),
(3254, 'W', 'UG', 'Western'),
(3255, '43', 'UA', 'Avtonomna Respublika Krym'),
(3256, '71', 'UA', 'Cherkas\'ka Oblast\''),
(3257, '74', 'UA', 'Chernihivs\'ka Oblast\''),
(3258, '77', 'UA', 'Chernivets\'ka Oblast\''),
(3259, '12', 'UA', 'Dnipropetrovs\'ka Oblast\''),
(3260, '14', 'UA', 'Donets\'ka Oblast\''),
(3261, '26', 'UA', 'Ivano-Frankivs\'ka Oblast\''),
(3262, '63', 'UA', 'Kharkivs\'ka Oblast\''),
(3263, '65', 'UA', 'Khersons\'ka Oblast\''),
(3264, '68', 'UA', 'Khmel\'nyts\'ka Oblast\''),
(3265, '35', 'UA', 'Kirovohrads\'ka Oblast\''),
(3266, '30', 'UA', 'Kyïv'),
(3267, '32', 'UA', 'Kyïvs\'ka Oblast\''),
(3268, '46', 'UA', 'L\'vivs\'ka Oblast\''),
(3269, '09', 'UA', 'Luhans\'ka Oblast\''),
(3270, '48', 'UA', 'Mykolaïvs\'ka Oblast\''),
(3271, '51', 'UA', 'Odes\'ka Oblast\''),
(3272, '53', 'UA', 'Poltavs\'ka Oblast\''),
(3273, '56', 'UA', 'Rivnens\'ka Oblast\''),
(3274, '40', 'UA', 'Sevastopol\''),
(3275, '59', 'UA', 'Sums\'ka Oblast\''),
(3276, '61', 'UA', 'Ternopil\'s\'ka Oblast\''),
(3277, '05', 'UA', 'Vinnyts\'ka Oblast\''),
(3278, '07', 'UA', 'Volyns\'ka Oblast\''),
(3279, '21', 'UA', 'Zakarpats\'ka Oblast\''),
(3280, '23', 'UA', 'Zaporiz\'ka Oblast\''),
(3281, '18', 'UA', 'Zhytomyrs\'ka Oblast\''),
(3282, 'AJ', 'AE', '\'Ajmān'),
(3283, 'AZ', 'AE', 'Abū Z̧aby'),
(3284, 'FU', 'AE', 'Al Fujayrah'),
(3285, 'SH', 'AE', 'Ash Shāriqah'),
(3286, 'DU', 'AE', 'Dubayy'),
(3287, 'RK', 'AE', 'Ra\'s al Khaymah'),
(3288, 'UQ', 'AE', 'Umm al Qaywayn'),
(3289, 'BDG', 'GB', 'Barking and Dagenham'),
(3290, 'BNE', 'GB', 'Barnet'),
(3291, 'BEX', 'GB', 'Bexley'),
(3292, 'BEN', 'GB', 'Brent'),
(3293, 'BRY', 'GB', 'Bromley'),
(3294, 'CMD', 'GB', 'Camden'),
(3295, 'CRY', 'GB', 'Croydon'),
(3296, 'EAL', 'GB', 'Ealing'),
(3297, 'ENF', 'GB', 'Enfield'),
(3298, 'GRE', 'GB', 'Greenwich'),
(3299, 'HCK', 'GB', 'Hackney'),
(3300, 'HMF', 'GB', 'Hammersmith and Fulham'),
(3301, 'HRY', 'GB', 'Haringey'),
(3302, 'HRW', 'GB', 'Harrow'),
(3303, 'HAV', 'GB', 'Havering'),
(3304, 'HIL', 'GB', 'Hillingdon'),
(3305, 'HNS', 'GB', 'Hounslow'),
(3306, 'ISL', 'GB', 'Islington'),
(3307, 'KEC', 'GB', 'Kensington and Chelsea'),
(3308, 'KTT', 'GB', 'Kingston upon Thames'),
(3309, 'LBH', 'GB', 'Lambeth'),
(3310, 'LEW', 'GB', 'Lewisham'),
(3311, 'MRT', 'GB', 'Merton'),
(3312, 'NWM', 'GB', 'Newham'),
(3313, 'RDB', 'GB', 'Redbridge'),
(3314, 'RIC', 'GB', 'Richmond upon Thames'),
(3315, 'SWK', 'GB', 'Southwark'),
(3316, 'STN', 'GB', 'Sutton'),
(3317, 'TWH', 'GB', 'Tower Hamlets'),
(3318, 'WFT', 'GB', 'Waltham Forest'),
(3319, 'WND', 'GB', 'Wandsworth'),
(3320, 'WSM', 'GB', 'Westminster'),
(3321, 'EAW', 'GB', 'England and Wales'),
(3322, 'GBN', 'GB', 'Great Britain'),
(3323, 'UKM', 'GB', 'United Kingdom'),
(3324, 'LND', 'GB', 'London, City of'),
(3325, 'ABE', 'GB', 'Aberdeen City'),
(3326, 'ABD', 'GB', 'Aberdeenshire'),
(3327, 'ANS', 'GB', 'Angus'),
(3328, 'AGB', 'GB', 'Argyll and Bute'),
(3329, 'CLK', 'GB', 'Clackmannanshire'),
(3330, 'DGY', 'GB', 'Dumfries and Galloway'),
(3331, 'DND', 'GB', 'Dundee City'),
(3332, 'EAY', 'GB', 'East Ayrshire'),
(3333, 'EDU', 'GB', 'East Dunbartonshire'),
(3334, 'ELN', 'GB', 'East Lothian'),
(3335, 'ERW', 'GB', 'East Renfrewshire'),
(3336, 'EDH', 'GB', 'Edinburgh, City of'),
(3337, 'ELS', 'GB', 'Eilean Siar'),
(3338, 'FAL', 'GB', 'Falkirk'),
(3339, 'FIF', 'GB', 'Fife'),
(3340, 'GLG', 'GB', 'Glasgow City'),
(3341, 'HLD', 'GB', 'Highland'),
(3342, 'IVC', 'GB', 'Inverclyde'),
(3343, 'MLN', 'GB', 'Midlothian'),
(3344, 'MRY', 'GB', 'Moray'),
(3345, 'NAY', 'GB', 'North Ayrshire'),
(3346, 'NLK', 'GB', 'North Lanarkshire'),
(3347, 'ORK', 'GB', 'Orkney Islands'),
(3348, 'PKN', 'GB', 'Perth and Kinross'),
(3349, 'RFW', 'GB', 'Renfrewshire'),
(3350, 'SCB', 'GB', 'Scottish Borders, The'),
(3351, 'ZET', 'GB', 'Shetland Islands'),
(3352, 'SAY', 'GB', 'South Ayrshire'),
(3353, 'SLK', 'GB', 'South Lanarkshire'),
(3354, 'STG', 'GB', 'Stirling'),
(3355, 'WDU', 'GB', 'West Dunbartonshire'),
(3356, 'WLN', 'GB', 'West Lothian'),
(3357, 'ENG', 'GB', 'England'),
(3358, 'SCT', 'GB', 'Scotland'),
(3359, 'WLS', 'GB', 'Wales'),
(3360, 'ANT', 'GB', 'Antrim'),
(3361, 'ARD', 'GB', 'Ards'),
(3362, 'ARM', 'GB', 'Armagh'),
(3363, 'BLA', 'GB', 'Ballymena'),
(3364, 'BLY', 'GB', 'Ballymoney'),
(3365, 'BNB', 'GB', 'Banbridge'),
(3366, 'BFS', 'GB', 'Belfast'),
(3367, 'CKF', 'GB', 'Carrickfergus'),
(3368, 'CSR', 'GB', 'Castlereagh'),
(3369, 'CLR', 'GB', 'Coleraine'),
(3370, 'CKT', 'GB', 'Cookstown'),
(3371, 'CGV', 'GB', 'Craigavon'),
(3372, 'DRY', 'GB', 'Derry'),
(3373, 'DOW', 'GB', 'Down'),
(3374, 'DGN', 'GB', 'Dungannon and South Tyrone'),
(3375, 'FER', 'GB', 'Fermanagh'),
(3376, 'LRN', 'GB', 'Larne'),
(3377, 'LMV', 'GB', 'Limavady'),
(3378, 'LSB', 'GB', 'Lisburn'),
(3379, 'MFT', 'GB', 'Magherafelt'),
(3380, 'MYL', 'GB', 'Moyle'),
(3381, 'NYM', 'GB', 'Newry and Mourne District'),
(3382, 'NTA', 'GB', 'Newtownabbey'),
(3383, 'NDN', 'GB', 'North Down'),
(3384, 'OMH', 'GB', 'Omagh'),
(3385, 'STB', 'GB', 'Strabane'),
(3386, 'BNS', 'GB', 'Barnsley'),
(3387, 'BIR', 'GB', 'Birmingham'),
(3388, 'BOL', 'GB', 'Bolton'),
(3389, 'BRD', 'GB', 'Bradford'),
(3390, 'BUR', 'GB', 'Bury'),
(3391, 'CLD', 'GB', 'Calderdale'),
(3392, 'COV', 'GB', 'Coventry'),
(3393, 'DNC', 'GB', 'Doncaster'),
(3394, 'DUD', 'GB', 'Dudley'),
(3395, 'GAT', 'GB', 'Gateshead'),
(3396, 'KIR', 'GB', 'Kirklees'),
(3397, 'KWL', 'GB', 'Knowsley'),
(3398, 'LDS', 'GB', 'Leeds'),
(3399, 'LIV', 'GB', 'Liverpool'),
(3400, 'MAN', 'GB', 'Manchester'),
(3401, 'NET', 'GB', 'Newcastle upon Tyne'),
(3402, 'NTY', 'GB', 'North Tyneside'),
(3403, 'OLD', 'GB', 'Oldham'),
(3404, 'RCH', 'GB', 'Rochdale'),
(3405, 'ROT', 'GB', 'Rotherham'),
(3406, 'SLF', 'GB', 'Salford'),
(3407, 'SAW', 'GB', 'Sandwell'),
(3408, 'SFT', 'GB', 'Sefton'),
(3409, 'SHF', 'GB', 'Sheffield'),
(3410, 'SOL', 'GB', 'Solihull'),
(3411, 'STY', 'GB', 'South Tyneside'),
(3412, 'SHN', 'GB', 'St. Helens'),
(3413, 'SKP', 'GB', 'Stockport'),
(3414, 'SND', 'GB', 'Sunderland'),
(3415, 'TAM', 'GB', 'Tameside'),
(3416, 'TRF', 'GB', 'Trafford'),
(3417, 'WKF', 'GB', 'Wakefield'),
(3418, 'WLL', 'GB', 'Walsall'),
(3419, 'WGN', 'GB', 'Wigan'),
(3420, 'WRL', 'GB', 'Wirral'),
(3421, 'WLV', 'GB', 'Wolverhampton'),
(3422, 'NIR', 'GB', 'Northern Ireland'),
(3423, 'BKM', 'GB', 'Buckinghamshire'),
(3424, 'CAM', 'GB', 'Cambridgeshire'),
(3425, 'CMA', 'GB', 'Cumbria'),
(3426, 'DBY', 'GB', 'Derbyshire'),
(3427, 'DEV', 'GB', 'Devon'),
(3428, 'DOR', 'GB', 'Dorset'),
(3429, 'ESX', 'GB', 'East Sussex'),
(3430, 'ESS', 'GB', 'Essex'),
(3431, 'GLS', 'GB', 'Gloucestershire'),
(3432, 'HAM', 'GB', 'Hampshire'),
(3433, 'HRT', 'GB', 'Hertfordshire'),
(3434, 'KEN', 'GB', 'Kent'),
(3435, 'LAN', 'GB', 'Lancashire'),
(3436, 'LEC', 'GB', 'Leicestershire'),
(3437, 'LIN', 'GB', 'Lincolnshire'),
(3438, 'NFK', 'GB', 'Norfolk'),
(3439, 'NYK', 'GB', 'North Yorkshire'),
(3440, 'NTH', 'GB', 'Northamptonshire'),
(3441, 'NTT', 'GB', 'Nottinghamshire'),
(3442, 'OXF', 'GB', 'Oxfordshire'),
(3443, 'SOM', 'GB', 'Somerset'),
(3444, 'STS', 'GB', 'Staffordshire'),
(3445, 'SFK', 'GB', 'Suffolk'),
(3446, 'SRY', 'GB', 'Surrey'),
(3447, 'WAR', 'GB', 'Warwickshire'),
(3448, 'WSX', 'GB', 'West Sussex'),
(3449, 'WOR', 'GB', 'Worcestershire'),
(3450, 'BAS', 'GB', 'Bath and North East Somerset'),
(3451, 'BDF', 'GB', 'Bedford'),
(3452, 'BBD', 'GB', 'Blackburn with Darwen'),
(3453, 'BPL', 'GB', 'Blackpool'),
(3454, 'BGW', 'GB', 'Blaenau Gwent'),
(3455, 'BMH', 'GB', 'Bournemouth'),
(3456, 'BRC', 'GB', 'Bracknell Forest'),
(3457, 'BGE', 'GB', 'Bridgend'),
(3458, 'BNH', 'GB', 'Brighton and Hove'),
(3459, 'BST', 'GB', 'Bristol, City of'),
(3460, 'CAY', 'GB', 'Caerphilly'),
(3461, 'CRF', 'GB', 'Cardiff'),
(3462, 'CMN', 'GB', 'Carmarthenshire'),
(3463, 'CBF', 'GB', 'Central Bedfordshire'),
(3464, 'CGN', 'GB', 'Ceredigion'),
(3465, 'CHE', 'GB', 'Cheshire East'),
(3466, 'CHW', 'GB', 'Cheshire West and Chester'),
(3467, 'CWY', 'GB', 'Conwy'),
(3468, 'CON', 'GB', 'Cornwall'),
(3469, 'DAL', 'GB', 'Darlington'),
(3470, 'DEN', 'GB', 'Denbighshire'),
(3471, 'DER', 'GB', 'Derby'),
(3472, 'DUR', 'GB', 'Durham, County'),
(3473, 'ERY', 'GB', 'East Riding of Yorkshire'),
(3474, 'FLN', 'GB', 'Flintshire'),
(3475, 'GWN', 'GB', 'Gwynedd'),
(3476, 'HAL', 'GB', 'Halton'),
(3477, 'HPL', 'GB', 'Hartlepool'),
(3478, 'HEF', 'GB', 'Herefordshire'),
(3479, 'AGY', 'GB', 'Isle of Anglesey'),
(3480, 'IOW', 'GB', 'Isle of Wight'),
(3481, 'IOS', 'GB', 'Isles of Scilly'),
(3482, 'KHL', 'GB', 'Kingston upon Hull'),
(3483, 'LCE', 'GB', 'Leicester'),
(3484, 'LUT', 'GB', 'Luton'),
(3485, 'MDW', 'GB', 'Medway'),
(3486, 'MTY', 'GB', 'Merthyr Tydfil'),
(3487, 'MDB', 'GB', 'Middlesbrough'),
(3488, 'MIK', 'GB', 'Milton Keynes'),
(3489, 'MON', 'GB', 'Monmouthshire'),
(3490, 'NTL', 'GB', 'Neath Port Talbot'),
(3491, 'NWP', 'GB', 'Newport'),
(3492, 'NEL', 'GB', 'North East Lincolnshire'),
(3493, 'NLN', 'GB', 'North Lincolnshire'),
(3494, 'NSM', 'GB', 'North Somerset'),
(3495, 'NBL', 'GB', 'Northumberland'),
(3496, 'NGM', 'GB', 'Nottingham'),
(3497, 'PEM', 'GB', 'Pembrokeshire'),
(3498, 'PTE', 'GB', 'Peterborough'),
(3499, 'PLY', 'GB', 'Plymouth'),
(3500, 'POL', 'GB', 'Poole'),
(3501, 'POR', 'GB', 'Portsmouth'),
(3502, 'POW', 'GB', 'Powys'),
(3503, 'RDG', 'GB', 'Reading'),
(3504, 'RCC', 'GB', 'Redcar and Cleveland'),
(3505, 'RCT', 'GB', 'Rhondda, Cynon, Taff'),
(3506, 'RUT', 'GB', 'Rutland'),
(3507, 'SHR', 'GB', 'Shropshire'),
(3508, 'SLG', 'GB', 'Slough'),
(3509, 'SGC', 'GB', 'South Gloucestershire'),
(3510, 'STH', 'GB', 'Southampton'),
(3511, 'SOS', 'GB', 'Southend-on-Sea'),
(3512, 'STT', 'GB', 'Stockton-on-Tees'),
(3513, 'STE', 'GB', 'Stoke-on-Trent'),
(3514, 'SWA', 'GB', 'Swansea'),
(3515, 'SWD', 'GB', 'Swindon'),
(3516, 'TFW', 'GB', 'Telford and Wrekin'),
(3517, 'THR', 'GB', 'Thurrock'),
(3518, 'TOB', 'GB', 'Torbay'),
(3519, 'TOF', 'GB', 'Torfaen'),
(3520, 'VGL', 'GB', 'Vale of Glamorgan, The'),
(3521, 'WRT', 'GB', 'Warrington'),
(3522, 'WBK', 'GB', 'West Berkshire'),
(3523, 'WIL', 'GB', 'Wiltshire'),
(3524, 'WNM', 'GB', 'Windsor and Maidenhead'),
(3525, 'WOK', 'GB', 'Wokingham'),
(3526, 'WRX', 'GB', 'Wrexham'),
(3527, 'YOR', 'GB', 'York'),
(3528, 'DC', 'US', 'District of Columbia'),
(3529, 'AS', 'US', 'American Samoa'),
(3530, 'GU', 'US', 'Guam'),
(3531, 'MP', 'US', 'Northern Mariana Islands'),
(3532, 'PR', 'US', 'Puerto Rico'),
(3533, 'UM', 'US', 'United States Minor Outlying Islands'),
(3534, 'VI', 'US', 'Virgin Islands, U.S.'),
(3535, 'AL', 'US', 'Alabama'),
(3536, 'AK', 'US', 'Alaska'),
(3537, 'AZ', 'US', 'Arizona'),
(3538, 'AR', 'US', 'Arkansas'),
(3539, 'CA', 'US', 'California'),
(3540, 'CO', 'US', 'Colorado'),
(3541, 'CT', 'US', 'Connecticut'),
(3542, 'DE', 'US', 'Delaware'),
(3543, 'FL', 'US', 'Florida'),
(3544, 'GA', 'US', 'Georgia'),
(3545, 'HI', 'US', 'Hawaii'),
(3546, 'ID', 'US', 'Idaho'),
(3547, 'IL', 'US', 'Illinois'),
(3548, 'IN', 'US', 'Indiana'),
(3549, 'IA', 'US', 'Iowa'),
(3550, 'KS', 'US', 'Kansas'),
(3551, 'KY', 'US', 'Kentucky'),
(3552, 'LA', 'US', 'Louisiana'),
(3553, 'ME', 'US', 'Maine'),
(3554, 'MD', 'US', 'Maryland'),
(3555, 'MA', 'US', 'Massachusetts'),
(3556, 'MI', 'US', 'Michigan'),
(3557, 'MN', 'US', 'Minnesota'),
(3558, 'MS', 'US', 'Mississippi'),
(3559, 'MO', 'US', 'Missouri'),
(3560, 'MT', 'US', 'Montana'),
(3561, 'NE', 'US', 'Nebraska'),
(3562, 'NV', 'US', 'Nevada'),
(3563, 'NH', 'US', 'New Hampshire'),
(3564, 'NJ', 'US', 'New Jersey'),
(3565, 'NM', 'US', 'New Mexico'),
(3566, 'NY', 'US', 'New York'),
(3567, 'NC', 'US', 'North Carolina'),
(3568, 'ND', 'US', 'North Dakota'),
(3569, 'OH', 'US', 'Ohio'),
(3570, 'OK', 'US', 'Oklahoma'),
(3571, 'OR', 'US', 'Oregon'),
(3572, 'PA', 'US', 'Pennsylvania'),
(3573, 'RI', 'US', 'Rhode Island'),
(3574, 'SC', 'US', 'South Carolina'),
(3575, 'SD', 'US', 'South Dakota'),
(3576, 'TN', 'US', 'Tennessee'),
(3577, 'TX', 'US', 'Texas'),
(3578, 'UT', 'US', 'Utah'),
(3579, 'VT', 'US', 'Vermont'),
(3580, 'VA', 'US', 'Virginia'),
(3581, 'WA', 'US', 'Washington'),
(3582, 'WV', 'US', 'West Virginia'),
(3583, 'WI', 'US', 'Wisconsin'),
(3584, 'WY', 'US', 'Wyoming'),
(3585, 'AR', 'UY', 'Artigas'),
(3586, 'CA', 'UY', 'Canelones'),
(3587, 'CL', 'UY', 'Cerro Largo'),
(3588, 'CO', 'UY', 'Colonia'),
(3589, 'DU', 'UY', 'Durazno'),
(3590, 'FS', 'UY', 'Flores'),
(3591, 'FD', 'UY', 'Florida'),
(3592, 'LA', 'UY', 'Lavalleja'),
(3593, 'MA', 'UY', 'Maldonado'),
(3594, 'MO', 'UY', 'Montevideo'),
(3595, 'PA', 'UY', 'Paysandú'),
(3596, 'RV', 'UY', 'Rivera'),
(3597, 'RO', 'UY', 'Rocha'),
(3598, 'RN', 'UY', 'Río Negro'),
(3599, 'SA', 'UY', 'Salto'),
(3600, 'SJ', 'UY', 'San José'),
(3601, 'SO', 'UY', 'Soriano'),
(3602, 'TA', 'UY', 'Tacuarembó'),
(3603, 'TT', 'UY', 'Treinta y Tres'),
(3604, 'AN', 'UZ', 'Andijon'),
(3605, 'BU', 'UZ', 'Buxoro'),
(3606, 'FA', 'UZ', 'Farg‘ona'),
(3607, 'JI', 'UZ', 'Jizzax'),
(3608, 'NG', 'UZ', 'Namangan'),
(3609, 'NW', 'UZ', 'Navoiy'),
(3610, 'QA', 'UZ', 'Qashqadaryo'),
(3611, 'QR', 'UZ', 'Qoraqalpog‘iston Respublikasi'),
(3612, 'SA', 'UZ', 'Samarqand'),
(3613, 'SI', 'UZ', 'Sirdaryo'),
(3614, 'SU', 'UZ', 'Surxondaryo'),
(3615, 'TO', 'UZ', 'Toshkent'),
(3616, 'TK', 'UZ', 'Toshkent'),
(3617, 'XO', 'UZ', 'Xorazm'),
(3618, 'MAP', 'VU', 'Malampa'),
(3619, 'PAM', 'VU', 'Pénama'),
(3620, 'SAM', 'VU', 'Sanma'),
(3621, 'SEE', 'VU', 'Shéfa'),
(3622, 'TAE', 'VU', 'Taféa'),
(3623, 'TOB', 'VU', 'Torba'),
(3624, 'Z', 'VE', 'Amazonas'),
(3625, 'B', 'VE', 'Anzoátegui'),
(3626, 'C', 'VE', 'Apure'),
(3627, 'D', 'VE', 'Aragua'),
(3628, 'E', 'VE', 'Barinas'),
(3629, 'F', 'VE', 'Bolívar'),
(3630, 'G', 'VE', 'Carabobo'),
(3631, 'H', 'VE', 'Cojedes'),
(3632, 'Y', 'VE', 'Delta Amacuro'),
(3633, 'W', 'VE', 'Dependencias Federales'),
(3634, 'A', 'VE', 'Distrito Capital'),
(3635, 'I', 'VE', 'Falcón'),
(3636, 'J', 'VE', 'Guárico'),
(3637, 'K', 'VE', 'Lara'),
(3638, 'M', 'VE', 'Miranda'),
(3639, 'N', 'VE', 'Monagas'),
(3640, 'L', 'VE', 'Mérida'),
(3641, 'O', 'VE', 'Nueva Esparta'),
(3642, 'P', 'VE', 'Portuguesa'),
(3643, 'R', 'VE', 'Sucre'),
(3644, 'T', 'VE', 'Trujillo'),
(3645, 'S', 'VE', 'Táchira'),
(3646, 'X', 'VE', 'Vargas'),
(3647, 'U', 'VE', 'Yaracuy'),
(3648, 'V', 'VE', 'Zulia'),
(3649, '44', 'VN', 'An Giang'),
(3650, '43', 'VN', 'Bà Rịa–Vũng Tàu'),
(3651, '57', 'VN', 'Bình Dương'),
(3652, '58', 'VN', 'Bình Phước'),
(3653, '40', 'VN', 'Bình Thuận'),
(3654, '31', 'VN', 'Bình Định'),
(3655, '55', 'VN', 'Bạc Liêu'),
(3656, '54', 'VN', 'Bắc Giang'),
(3657, '53', 'VN', 'Bắc Kạn'),
(3658, '56', 'VN', 'Bắc Ninh'),
(3659, '50', 'VN', 'Bến Tre'),
(3660, '04', 'VN', 'Cao Bằng'),
(3661, '59', 'VN', 'Cà Mau'),
(3662, 'CT', 'VN', 'Cần Thơ'),
(3663, '30', 'VN', 'Gia Lai'),
(3664, '03', 'VN', 'Hà Giang'),
(3665, '63', 'VN', 'Hà Nam'),
(3666, 'HN', 'VN', 'Hà Nội'),
(3667, '15', 'VN', 'Hà Tây'),
(3668, '23', 'VN', 'Hà Tĩnh'),
(3669, '14', 'VN', 'Hòa Bình'),
(3670, '66', 'VN', 'Hưng Yên'),
(3671, '61', 'VN', 'Hải Dương'),
(3672, 'HP', 'VN', 'Hải Phòng'),
(3673, '73', 'VN', 'Hậu Giang'),
(3674, 'SG', 'VN', 'Hồ Chí Minh'),
(3675, '34', 'VN', 'Khánh Hòa'),
(3676, '47', 'VN', 'Kiên Giang'),
(3677, '28', 'VN', 'Kon Tum'),
(3678, '01', 'VN', 'Lai Châu'),
(3679, '41', 'VN', 'Long An'),
(3680, '02', 'VN', 'Lào Cai'),
(3681, '35', 'VN', 'Lâm Đồng'),
(3682, '09', 'VN', 'Lạng Sơn'),
(3683, '67', 'VN', 'Nam Định'),
(3684, '22', 'VN', 'Nghệ An'),
(3685, '18', 'VN', 'Ninh Bình'),
(3686, '36', 'VN', 'Ninh Thuận'),
(3687, '68', 'VN', 'Phú Thọ'),
(3688, '32', 'VN', 'Phú Yên'),
(3689, '24', 'VN', 'Quảng Bình'),
(3690, '27', 'VN', 'Quảng Nam'),
(3691, '29', 'VN', 'Quảng Ngãi'),
(3692, '13', 'VN', 'Quảng Ninh'),
(3693, '25', 'VN', 'Quảng Trị'),
(3694, '52', 'VN', 'Sóc Trăng'),
(3695, '05', 'VN', 'Sơn La'),
(3696, '21', 'VN', 'Thanh Hóa'),
(3697, '20', 'VN', 'Thái Bình'),
(3698, '69', 'VN', 'Thái Nguyên'),
(3699, '26', 'VN', 'Thừa Thiên–Huế'),
(3700, '46', 'VN', 'Tiền Giang'),
(3701, '51', 'VN', 'Trà Vinh'),
(3702, '07', 'VN', 'Tuyên Quang'),
(3703, '37', 'VN', 'Tây Ninh'),
(3704, '49', 'VN', 'Vĩnh Long'),
(3705, '70', 'VN', 'Vĩnh Phúc'),
(3706, '06', 'VN', 'Yên Bái'),
(3707, '71', 'VN', 'Điện Biên'),
(3708, 'DN', 'VN', 'Đà Nẵng'),
(3709, '33', 'VN', 'Đắk Lắk'),
(3710, '72', 'VN', 'Đắk Nông'),
(3711, '39', 'VN', 'Đồng Nai'),
(3712, '45', 'VN', 'Đồng Tháp'),
(3713, 'AD', 'YE', '\'Adan'),
(3714, 'AM', 'YE', '\'Amrān'),
(3715, 'AB', 'YE', 'Abyān'),
(3716, 'BA', 'YE', 'Al Bayḑā\''),
(3717, 'JA', 'YE', 'Al Jawf'),
(3718, 'MR', 'YE', 'Al Mahrah'),
(3719, 'MW', 'YE', 'Al Maḩwīt'),
(3720, 'HU', 'YE', 'Al Ḩudaydah'),
(3721, 'DA', 'YE', 'Aḑ Ḑāli\''),
(3722, 'DH', 'YE', 'Dhamār'),
(3723, 'IB', 'YE', 'Ibb'),
(3724, 'LA', 'YE', 'Laḩij'),
(3725, 'MA', 'YE', 'Ma\'rib'),
(3726, 'RA', 'YE', 'Raymah'),
(3727, 'SH', 'YE', 'Shabwah'),
(3728, 'TA', 'YE', 'Tā‘izz'),
(3729, 'SA', 'YE', 'Şan‘ā\''),
(3730, 'SN', 'YE', 'Şan‘ā\''),
(3731, 'SD', 'YE', 'Şā‘dah'),
(3732, 'HJ', 'YE', 'Ḩajjah'),
(3733, 'HD', 'YE', 'Ḩaḑramawt'),
(3734, '02', 'ZM', 'Central'),
(3735, '08', 'ZM', 'Copperbelt'),
(3736, '03', 'ZM', 'Eastern'),
(3737, '04', 'ZM', 'Luapula'),
(3738, '09', 'ZM', 'Lusaka'),
(3739, '06', 'ZM', 'North-Western'),
(3740, '05', 'ZM', 'Northern'),
(3741, '07', 'ZM', 'Southern'),
(3742, '01', 'ZM', 'Western'),
(3743, 'BU', 'ZW', 'Bulawayo'),
(3744, 'HA', 'ZW', 'Harare'),
(3745, 'MA', 'ZW', 'Manicaland'),
(3746, 'MC', 'ZW', 'Mashonaland Central'),
(3747, 'ME', 'ZW', 'Mashonaland East'),
(3748, 'MW', 'ZW', 'Mashonaland West'),
(3749, 'MV', 'ZW', 'Masvingo'),
(3750, 'MN', 'ZW', 'Matabeleland North'),
(3751, 'MS', 'ZW', 'Matabeleland South'),
(3752, 'MI', 'ZW', 'Midlands'),
(3753, 'in32', 'IN', 'up');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(31, 'Activity', 'activity'),
(32, 'Activity', 'chatter'),
(33, 'Activity', 'maps'),
(1, 'admin', 'logentry'),
(70, 'Attachment', 'attachment'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(18, 'Branch', 'branch'),
(24, 'BusinessPartner', 'bpaddresses'),
(25, 'BusinessPartner', 'bpbranch'),
(26, 'BusinessPartner', 'bpcurrency'),
(27, 'BusinessPartner', 'bpdepartment'),
(28, 'BusinessPartner', 'bpemployee'),
(29, 'BusinessPartner', 'bpposition'),
(30, 'BusinessPartner', 'businesspartner'),
(72, 'BusinessPartner', 'customercode'),
(73, 'BusinessPartner', 'customergroup'),
(74, 'BusinessPartner', 'customerzone'),
(67, 'Campaign', 'campaign'),
(65, 'Campaign', 'campaignset'),
(66, 'Campaign', 'campaignsetmembers'),
(48, 'Category', 'category'),
(71, 'ClientBankDetails', 'clientbankdetails'),
(16, 'Company', 'branch'),
(17, 'Company', 'company'),
(5, 'contenttypes', 'contenttype'),
(34, 'Countries', 'countries'),
(35, 'Countries', 'states'),
(12, 'Employee', 'employee'),
(15, 'Employee', 'target'),
(14, 'Employee', 'targetqty'),
(13, 'Employee', 'targetyr'),
(36, 'Industries', 'industries'),
(62, 'Invoice', 'addressextension'),
(63, 'Invoice', 'documentlines'),
(64, 'Invoice', 'invoice'),
(45, 'Item', 'department'),
(47, 'Item', 'item'),
(46, 'Item', 'tax'),
(7, 'Lead', 'chatter'),
(11, 'Lead', 'lead'),
(8, 'Lead', 'leaditem'),
(9, 'Lead', 'source'),
(10, 'Lead', 'type'),
(49, 'Notification', 'notification'),
(19, 'Opportunity', 'line'),
(20, 'Opportunity', 'oppitem'),
(21, 'Opportunity', 'opportunity'),
(22, 'Opportunity', 'stage'),
(23, 'Opportunity', 'staticstage'),
(69, 'Order', 'addendumrequest'),
(42, 'Order', 'addressextension'),
(75, 'Order', 'custcode'),
(43, 'Order', 'documentlines'),
(44, 'Order', 'order'),
(37, 'PaymentTermsTypes', 'paymenttermstypes'),
(68, 'Project', 'project'),
(38, 'Quotation', 'addressextension'),
(39, 'Quotation', 'appslave'),
(40, 'Quotation', 'documentlines'),
(41, 'Quotation', 'quotation'),
(6, 'sessions', 'session'),
(50, 'Tender', 'corrigendumlist'),
(51, 'Tender', 'coverdetail'),
(52, 'Tender', 'critcaldates'),
(53, 'Tender', 'documents'),
(54, 'Tender', 'lowestone'),
(55, 'Tender', 'paymentinstrument'),
(56, 'Tender', 'technicalopening'),
(57, 'Tender', 'tender'),
(58, 'Tender', 'tenderopening'),
(59, 'Tender', 'tendersubmission'),
(60, 'Tender', 'tenitem'),
(61, 'Tender', 'workoritemdetails');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Activity', '0001_initial', '2022-09-05 12:38:39.357922'),
(2, 'Branch', '0001_initial', '2022-09-05 12:38:39.386245'),
(3, 'Company', '0001_initial', '2022-09-05 12:38:39.440188'),
(4, 'BusinessPartner', '0001_initial', '2022-09-05 12:38:39.709260'),
(5, 'Employee', '0001_initial', '2022-09-05 12:38:39.955655'),
(6, 'Campaign', '0001_initial', '2022-09-05 12:38:40.242872'),
(7, 'Category', '0001_initial', '2022-09-05 12:38:40.262195'),
(8, 'Countries', '0001_initial', '2022-09-05 12:38:40.291805'),
(9, 'Industries', '0001_initial', '2022-09-05 12:38:40.308140'),
(10, 'Invoice', '0001_initial', '2022-09-05 12:38:40.448552'),
(11, 'Item', '0001_initial', '2022-09-05 12:38:40.520111'),
(12, 'Lead', '0001_initial', '2022-09-05 12:38:40.713727'),
(13, 'Notification', '0001_initial', '2022-09-05 12:38:40.740150'),
(14, 'Opportunity', '0001_initial', '2022-09-05 12:38:40.907854'),
(15, 'Order', '0001_initial', '2022-09-05 12:38:41.014998'),
(16, 'PaymentTermsTypes', '0001_initial', '2022-09-05 12:38:41.028819'),
(17, 'Project', '0001_initial', '2022-09-05 12:38:41.074697'),
(18, 'Quotation', '0001_initial', '2022-09-05 12:38:41.384610'),
(19, 'Tender', '0001_initial', '2022-09-05 12:38:41.663674'),
(20, 'contenttypes', '0001_initial', '2022-09-05 12:38:41.700761'),
(21, 'auth', '0001_initial', '2022-09-05 12:38:41.982677'),
(22, 'admin', '0001_initial', '2022-09-05 12:38:42.058646'),
(23, 'admin', '0002_logentry_remove_auto_add', '2022-09-05 12:38:42.073478'),
(24, 'admin', '0003_logentry_add_action_flag_choices', '2022-09-05 12:38:42.086474'),
(25, 'contenttypes', '0002_remove_content_type_name', '2022-09-05 12:38:42.217846'),
(26, 'auth', '0002_alter_permission_name_max_length', '2022-09-05 12:38:42.250362'),
(27, 'auth', '0003_alter_user_email_max_length', '2022-09-05 12:38:42.277422'),
(28, 'auth', '0004_alter_user_username_opts', '2022-09-05 12:38:42.290728'),
(29, 'auth', '0005_alter_user_last_login_null', '2022-09-05 12:38:42.321651'),
(30, 'auth', '0006_require_contenttypes_0002', '2022-09-05 12:38:42.324161'),
(31, 'auth', '0007_alter_validators_add_error_messages', '2022-09-05 12:38:42.337920'),
(32, 'auth', '0008_alter_user_username_max_length', '2022-09-05 12:38:42.375759'),
(33, 'auth', '0009_alter_user_last_name_max_length', '2022-09-05 12:38:42.409007'),
(34, 'auth', '0010_alter_group_name_max_length', '2022-09-05 12:38:42.435466'),
(35, 'auth', '0011_update_proxy_permissions', '2022-09-05 12:38:42.514730'),
(36, 'auth', '0012_alter_user_first_name_max_length', '2022-09-05 12:38:42.548920'),
(37, 'sessions', '0001_initial', '2022-09-05 12:38:42.568932'),
(38, 'BusinessPartner', '0002_auto_20220905_1338', '2022-09-05 13:38:36.561742'),
(39, 'Quotation', '0002_auto_20220906_0559', '2022-09-06 05:59:18.314791'),
(40, 'Order', '0002_addendumrequest', '2022-09-06 07:44:59.813688'),
(41, 'Order', '0003_auto_20220906_1107', '2022-09-06 11:07:33.100357'),
(42, 'Quotation', '0003_quotation_qtno', '2022-09-06 12:11:58.608252'),
(43, 'Order', '0004_auto_20220906_1233', '2022-09-06 12:33:53.210680'),
(44, 'Opportunity', '0002_staticstage_utype', '2022-09-07 10:49:58.175119'),
(45, 'Opportunity', '0003_remove_staticstage_utype', '2022-09-07 10:56:19.314737'),
(46, 'Opportunity', '0004_staticstage_utype', '2022-09-07 10:56:33.286091'),
(47, 'Attachment', '0001_initial', '2022-09-13 05:51:21.854595'),
(48, 'Lead', '0002_lead_code', '2022-09-14 06:05:32.437444'),
(49, 'Attachment', '0002_attachment_caption', '2022-09-19 10:07:34.896158'),
(50, 'ClientBankDetails', '0001_initial', '2022-09-19 12:49:56.790213'),
(51, 'BusinessPartner', '0003_auto_20220927_1134', '2022-09-27 11:35:05.526293'),
(52, 'BusinessPartner', '0004_auto_20220928_0939', '2022-09-28 09:39:46.087434'),
(53, 'Opportunity', '0005_auto_20220928_1118', '2022-09-28 11:18:45.840403'),
(54, 'Quotation', '0004_auto_20220929_0759', '2022-09-29 07:59:50.449251'),
(55, 'Project', '0002_auto_20220929_0912', '2022-09-29 09:12:30.664302'),
(56, 'BusinessPartner', '0005_auto_20220929_0926', '2022-09-29 09:27:04.322932'),
(57, 'Project', '0003_auto_20220929_0943', '2022-09-29 09:43:27.225693'),
(58, 'Project', '0004_auto_20220930_1005', '2022-09-30 10:05:54.252510'),
(59, 'BusinessPartner', '0006_businesspartner_customerstatus', '2022-10-06 10:10:23.908126'),
(60, 'Order', '0005_auto_20221007_0719', '2022-10-07 07:19:52.468724'),
(61, 'Project', '0005_project_grouptype', '2022-10-10 06:24:02.452953'),
(62, 'BusinessPartner', '0007_auto_20221010_0725', '2022-10-10 07:25:48.085964'),
(63, 'Quotation', '0005_auto_20221010_0851', '2022-10-10 08:51:53.454916'),
(64, 'Item', '0002_item_uomno', '2022-10-10 10:02:27.981224'),
(65, 'BusinessPartner', '0008_auto_20221010_1322', '2022-10-10 13:22:27.300633'),
(66, 'BusinessPartner', '0009_auto_20221011_0640', '2022-10-11 06:40:30.934539'),
(67, 'Order', '0006_auto_20221011_0925', '2022-10-11 09:26:10.879805'),
(68, 'Project', '0006_auto_20221011_1037', '2022-10-11 10:37:32.962939'),
(69, 'Attachment', '0003_attachment_filename', '2022-10-17 10:20:42.415971'),
(70, 'Order', '0007_auto_20221101_0919', '2022-11-01 09:19:44.111017'),
(71, 'Order', '0008_auto_20221102_0743', '2022-11-02 07:44:02.952773'),
(72, 'Order', '0009_alter_documentlines_uomno', '2022-11-02 07:48:11.544385'),
(73, 'Opportunity', '0006_auto_20221103_0909', '2022-11-03 09:10:05.500983'),
(74, 'Order', '0010_auto_20221104_0601', '2022-11-04 06:02:12.599027'),
(75, 'Order', '0011_custcode', '2022-11-04 12:03:28.204352'),
(76, 'Order', '0012_order_urn_no', '2022-11-07 11:36:58.996194'),
(77, 'Order', '0013_rename_urn_no_order_urn', '2022-11-08 08:59:33.314125'),
(78, 'Project', '0007_rename_cardcode_project_cardcode', '2022-11-11 09:39:09.740174'),
(79, 'BusinessPartner', '0010_businesspartner_u_landline', '2022-11-11 11:38:11.718915'),
(80, 'Quotation', '0006_quotation_bpemail', '2022-11-14 08:54:51.310392'),
(81, 'Order', '0014_order_nettotal', '2022-11-21 13:25:55.624466');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Employee_employee`
--

CREATE TABLE `Employee_employee` (
  `id` bigint NOT NULL,
  `companyID` varchar(50) NOT NULL,
  `SalesEmployeeCode` varchar(20) NOT NULL,
  `SalesEmployeeName` varchar(50) NOT NULL,
  `EmployeeID` varchar(30) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `middleName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Mobile` varchar(15) NOT NULL,
  `role` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `branch` varchar(20) NOT NULL,
  `Active` varchar(20) NOT NULL,
  `salesUnit` varchar(50) NOT NULL,
  `passwordUpdatedOn` varchar(30) NOT NULL,
  `lastLoginOn` varchar(30) NOT NULL,
  `logedIn` varchar(20) NOT NULL,
  `reportingTo` varchar(20) NOT NULL,
  `FCM` varchar(250) NOT NULL,
  `div` varchar(250) NOT NULL,
  `timestamp` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee_employee`
--

INSERT INTO `Employee_employee` (`id`, `companyID`, `SalesEmployeeCode`, `SalesEmployeeName`, `EmployeeID`, `userName`, `password`, `firstName`, `middleName`, `lastName`, `Email`, `Mobile`, `role`, `position`, `branch`, `Active`, `salesUnit`, `passwordUpdatedOn`, `lastLoginOn`, `logedIn`, `reportingTo`, `FCM`, `div`, `timestamp`) VALUES
(1, '1', '1', 'sriram', '', 'sriram', 'wae@12345', 'sriram', '', '', '', '', 'admin', 'Director', '', 'tYES', 'Consumable', '', '', '', '0', 'dV_IcUjJ3UpMhD8KjSctrM:APA91bG1wAdv8XW5NBmw4MQYsEdazViW4Wf1ysRsxlbK8tkmBSXG9d4-CDa5XegZyPUKp8xHzX1uwUgXQyYSRXhA6rGNiXxGwCfBPbvTvUrF1vrS1AQN2D4Q7kFuKnkv3O0y2PFRJOiR', '100', '27-07-2022 11:15:03 AM'),
(88, '1', '88', 'Ziauddin', '', 'zdn1@gmail.com', '12345', 'Ziauddin', '', 'Shaikh', 'zdn1@gmail.com', '9506144733', 'marketing', 'Developer', '1', 'tNO', '', '', '', '', '1', '', '100', '01-09-2022 12:16:47 PM'),
(89, '1', '89', 'Rahul', '', 'rahul@gmail.com', '1234', 'Rahul', '', 'akarniya', 'rahul@gmail.com', '9560763295', 'manager', 'Developer', '1', 'tYES', '', '', '', '', '103', '', '100', '05-09-2022 4:28:58 PM'),
(90, '1', '90', 'Arif', '', 'rahul.akarniya@cinntra.com', '1234', 'Arif', '', 'Ansari', 'rahul.akarniya@cinntra.com', '9560763297', 'marketing', 'Developer', '1', 'tYES', '', '', '', '', '1', '', '100', '05-09-2022 5:26:30 PM'),
(91, '1', '91', 'Bhupendra', '', 'bhupi@gmail.com', '123', 'Bhupendra', '', 'Pal', 'bhupi@gmail.com', '1234123121', 'salesman', 'Developer', '1', 'tYES', '', '', '', '', '89', '', '100', '05-09-2022 6:34:02 PM'),
(92, '1', '92', 'Santanu', '', 'santanu.kumar@cinntra.com', '123123', 'Santanu', '', 'Sahu', 'santanu.kumar@cinntra.com', '8018762164', 'salesman', 'Analyst', '1', 'tYES', '', '', '', '', '102', '', '100', '06-09-2022 5:32:12 PM'),
(93, '1', '93', 'Mamta', '', 'Mamta@waecorp.com', '123123', 'Mamta', '', 'saxena', 'Mamta@waecorp.com', '8801876321', 'salesman', 'Sales Mngr', '1', 'tYES', '', '', '', '', '102', '', '100', '07-09-2022 11:33:21 AM'),
(94, '1', '94', 'Sarthak', '9876578', 'sarthaktyagi@gmail.com', '123', 'Sarthak', '', 'Tyagi', 'sarthaktyagi@gmail.com', '9798796796', 'manager', 'Departmental Manager', '1', 'tYES', '', '', '', '', '103', '', '100', '03-10-2022 11:03:01 AM'),
(95, '1', '95', 'Anuj', '97865687', 'anujmavi@gmail.com', '1234', 'Anuj', '', 'Mavi', 'anujmavi@gmail.com', '9079789798', 'salesman', 'Sales & Marketing Executive', '1', 'tYES', '', '', '', '', '94', '', '100', '03-10-2022 11:04:46 AM'),
(96, '1', '96', 'Lakshay', '6796798', 'lakshay.tyagi@cinntra.com', '123', 'Lakshay', '', 'Tyagi', 'lakshay.tyagi@cinntra.com', '9879868968', 'manager', 'Sales Managing Director', '1', 'tYES', '', '', '', '', '103', '', '100', '06-10-2022 2:33:04 PM'),
(97, '1', '97', 'Laxman', '98657898', 'laxman.singh@cinntra.com', '1234', 'Laxman', '', 'Singh', 'laxman.singh@cinntra.com', '6896867857', 'salesman', 'Sales Executive', '1', 'tYES', '', '', '', '', '96', '', '100', '06-10-2022 2:34:33 PM'),
(98, '1', '98', 'Samay', '98790', 'samaysingh@gmail.com', '123', 'Samay', '', 'Singh', 'samaysingh@gmail.com', '9876578908', 'manager', 'Sales Manager', '1', 'tYES', '', '', '', '', '103', '', '100', '06-10-2022 3:37:07 PM'),
(99, '1', '99', 'Madan', '8686676', 'madanpal@gmail.com', '1234', 'Madan', '', 'Pal', 'madanpal@gmail.com', '7897886866', 'salesman', 'Sales Executive', '1', 'tYES', '', '', '', '', '98', '', '100', '07-10-2022 6:06:30 PM'),
(100, '1', '100', 'Lucky', '979866', 'lucky.tyagi@gmail.com', '123', 'Lucky', '', 'Tyagi', 'lucky.tyagi@gmail.com', '8285067282', 'manager', 'Sales Manager', '1', 'tYES', '', '', '', '', '103', '', '100', '10-10-2022 4:51:06 PM'),
(101, '1', '101', 'Santanu', '786896', 'santanu.kumar@gmail.com', '123123', 'Santanu', '', 'Kumar', 'santanu.kumar@gmail.com', '9990989704', 'salesman', 'Sales Executive', '1', 'tYES', '', '', '', '', '100', '', '100', '10-10-2022 5:06:03 PM'),
(102, '1', '102', 'Rahul', '786766', 'rahul.tyagi@gmail.com', '1234', 'Rahul', '', 'Tyagi', 'rahul.tyagi@gmail.com', '9760918439', 'salesman', 'Sales Executive', '1', 'tYES', '', '', '', '', '100', '', '100', '10-10-2022 5:07:32 PM'),
(103, '1', '103', 'Akku', '8686768', 'akku.tyagi@gmail.com', '123', 'Akku', '', 'Tyagi', 'akku.tyagi@gmail.com', '8798798798', 'manager', 'Sales Manager', '1', 'tYES', '', '', '', '', '1', '', '100', '12-10-2022 1:22:10 PM'),
(104, '1', '104', 'Taslim', '876757', 'taslim.ahmed@gmail.com', '123', 'Taslim', '', 'Ahmed', 'taslim.ahmed@gmail.com', '8687897987', 'manager', 'Zonal Manager', '1', 'tNO', '', '', '', '', '1', '', '100', '03-11-2022 10:32:26 AM'),
(105, '1', '105', 'Avinash', '878576', 'avinash.kumar@gmail.com', '123', 'Avinash', '', 'Kumar', 'avinash.kumar@gmail.com', '7987654678', 'manager', 'Manager', '1', 'tYES', '', '', '', '', '1', '', '100', '03-11-2022 10:33:51 AM'),
(106, '1', '106', 'Devansh', '89756', 'devansh.singh@gmail.com', '1234', 'Devansh', '', 'Singh', 'devansh.singh@gmail.com', '8756890768', 'salesman', 'Sales Executive', '1', 'tYES', '', '', '', '', '105', '', '100', '03-11-2022 10:38:59 AM'),
(107, '1', '107', 'Farooq', '1233', 'farooq@cinntra.com', '12345', 'Farooq', '', 'Abdul', 'farooq@cinntra.com', '1231231230', 'salesman', 'Business Analyst', '1', 'tYES', '', '', '', '', '105', '', '100', '03-11-2022 12:28:58 PM');

-- --------------------------------------------------------

--
-- Table structure for table `Employee_target`
--

CREATE TABLE `Employee_target` (
  `id` bigint NOT NULL,
  `amount` double NOT NULL,
  `monthYear` varchar(50) NOT NULL,
  `qtr` int NOT NULL,
  `sale` double NOT NULL,
  `sale_diff` double NOT NULL,
  `CreatedDate` varchar(20) NOT NULL,
  `UpdatedDate` varchar(20) NOT NULL,
  `SalesPersonCode_id` varchar(20) DEFAULT NULL,
  `YearTarget_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee_target`
--

INSERT INTO `Employee_target` (`id`, `amount`, `monthYear`, `qtr`, `sale`, `sale_diff`, `CreatedDate`, `UpdatedDate`, `SalesPersonCode_id`, `YearTarget_id`) VALUES
(25, 10000, '2022-04', 1, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(26, 100000, '2022-05', 1, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(27, 100000, '2022-06', 1, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(28, 90000, '2022-07', 2, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(29, 100000, '2022-08', 2, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(30, 100000, '2022-09', 2, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(31, 50000, '2022-10', 3, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(32, 100000, '2022-11', 3, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(33, 100000, '2022-12', 3, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(34, 50000, '2023-01', 4, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(35, 100000, '2023-02', 4, 0, 0, '2022-11-04', '2022-11-04', '1', 9),
(36, 100000, '2023-03', 4, 0, 0, '2022-11-04', '2022-11-04', '1', 9);

-- --------------------------------------------------------

--
-- Table structure for table `Employee_targetqty`
--

CREATE TABLE `Employee_targetqty` (
  `id` bigint NOT NULL,
  `q1` bigint NOT NULL,
  `q2` bigint NOT NULL,
  `q3` bigint NOT NULL,
  `q4` bigint NOT NULL,
  `status` int NOT NULL,
  `CreatedDate` varchar(20) NOT NULL,
  `UpdatedDate` varchar(20) NOT NULL,
  `SalesPersonCode_id` varchar(20) DEFAULT NULL,
  `YearTarget_id` bigint NOT NULL,
  `reportingTo_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee_targetqty`
--

INSERT INTO `Employee_targetqty` (`id`, `q1`, `q2`, `q3`, `q4`, `status`, `CreatedDate`, `UpdatedDate`, `SalesPersonCode_id`, `YearTarget_id`, `reportingTo_id`) VALUES
(3, 210000, 290000, 250000, 250000, 0, '2022-11-04', '2022-11-04', '1', 9, NULL),
(4, 12500000, 10000000, 12500000, 15000000, 0, '2022-11-04', '2022-11-04', '1', 17, NULL),
(5, 60000, 60000, 60000, 70000, 0, '2022-11-15', '2022-11-15', '107', 16, '105');

-- --------------------------------------------------------

--
-- Table structure for table `Employee_targetyr`
--

CREATE TABLE `Employee_targetyr` (
  `id` bigint NOT NULL,
  `Department` varchar(50) NOT NULL,
  `StartYear` int NOT NULL,
  `EndYear` int NOT NULL,
  `YearTarget` bigint NOT NULL,
  `status` int NOT NULL,
  `CreatedDate` varchar(20) NOT NULL,
  `UpdatedDate` varchar(20) NOT NULL,
  `SalesPersonCode_id` varchar(20) DEFAULT NULL,
  `reportingTo_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Employee_targetyr`
--

INSERT INTO `Employee_targetyr` (`id`, `Department`, `StartYear`, `EndYear`, `YearTarget`, `status`, `CreatedDate`, `UpdatedDate`, `SalesPersonCode_id`, `reportingTo_id`) VALUES
(9, 'Product', 2022, 2023, 1000000, 0, '2022-11-04', '2022-11-04', '1', NULL),
(10, 'Product', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '88', '1'),
(11, 'Product', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '90', '1'),
(12, 'Product', 2022, 2023, 500000, 0, '2022-11-04', '2022-11-04', '103', '1'),
(13, 'Product', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '104', '1'),
(14, 'Product', 2022, 2023, 500000, 0, '2022-11-04', '2022-11-04', '105', '1'),
(15, 'Product', 2022, 2023, 250000, 0, '2022-11-04', '2022-11-04', '106', '105'),
(16, 'Product', 2022, 2023, 250000, 0, '2022-11-04', '2022-11-04', '107', '105'),
(17, 'Project', 2022, 2023, 50000000, 0, '2022-11-04', '2022-11-04', '1', NULL),
(18, 'Project', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '88', '1'),
(19, 'Project', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '90', '1'),
(20, 'Project', 2022, 2023, 25000000, 0, '2022-11-04', '2022-11-04', '103', '1'),
(21, 'Project', 2022, 2023, 0, 0, '2022-11-04', '2022-11-04', '104', '1'),
(22, 'Project', 2022, 2023, 25000000, 0, '2022-11-04', '2022-11-04', '105', '1'),
(23, 'Sales', 2022, 2023, 100000, 0, '2022-11-09', '2022-11-09', '1', NULL),
(24, 'Marketing', 2022, 2023, 100000, 0, '2022-11-09', '2022-11-09', '1', NULL),
(25, 'F.Gnew', 2025, 2026, 1234000, 0, '2022-11-16', '2022-11-16', '1', NULL),
(26, 'testg dweasdf', 2025, 2026, 1000, 0, '2022-11-17', '2022-11-17', '1', NULL),
(27, 'testg dweasdf', 2026, 2027, 1000, 0, '2022-11-17', '2022-11-17', '1', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Industries_industries`
--

CREATE TABLE `Industries_industries` (
  `id` bigint NOT NULL,
  `IndustryDescription` varchar(200) NOT NULL,
  `IndustryName` varchar(100) NOT NULL,
  `IndustryCode` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Industries_industries`
--

INSERT INTO `Industries_industries` (`id`, `IndustryDescription`, `IndustryName`, `IndustryCode`) VALUES
(1, 'IT', 'IT', '1'),
(2, 'Banking & Finance', 'Banking & Finance', '2'),
(3, 'Healthcare', 'Healthcare', '3'),
(4, 'Education', 'Education', '4'),
(5, 'HoReCa', 'HoReCa', '5'),
(6, 'Consultancy', 'Consultancy', '6'),
(7, 'Contractor', 'Contractor', '7'),
(8, 'NA', 'FinTech', '8');

-- --------------------------------------------------------

--
-- Table structure for table `Invoice_addressextension`
--

CREATE TABLE `Invoice_addressextension` (
  `id` bigint NOT NULL,
  `InvoiceID` varchar(5) NOT NULL,
  `BillToBuilding` varchar(100) NOT NULL,
  `ShipToState` varchar(100) NOT NULL,
  `BillToCity` varchar(100) NOT NULL,
  `ShipToCountry` varchar(100) NOT NULL,
  `BillToZipCode` varchar(100) NOT NULL,
  `ShipToStreet` varchar(100) NOT NULL,
  `BillToState` varchar(100) NOT NULL,
  `ShipToZipCode` varchar(100) NOT NULL,
  `BillToStreet` varchar(100) NOT NULL,
  `ShipToBuilding` varchar(100) NOT NULL,
  `ShipToCity` varchar(100) NOT NULL,
  `BillToCountry` varchar(100) NOT NULL,
  `U_SCOUNTRY` varchar(100) NOT NULL,
  `U_SSTATE` varchar(100) NOT NULL,
  `U_SHPTYPB` varchar(100) NOT NULL,
  `U_BSTATE` varchar(100) NOT NULL,
  `U_BCOUNTRY` varchar(100) NOT NULL,
  `U_SHPTYPS` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Invoice_documentlines`
--

CREATE TABLE `Invoice_documentlines` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `InvoiceID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `TaxCode` varchar(10) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Invoice_invoice`
--

CREATE TABLE `Invoice_invoice` (
  `id` bigint NOT NULL,
  `TaxDate` varchar(30) NOT NULL,
  `DocDueDate` varchar(30) NOT NULL,
  `ContactPersonCode` varchar(5) NOT NULL,
  `DiscountPercent` double NOT NULL,
  `DocDate` varchar(30) NOT NULL,
  `CardCode` varchar(30) NOT NULL,
  `Comments` varchar(150) NOT NULL,
  `SalesPersonCode` varchar(5) NOT NULL,
  `DocumentStatus` varchar(50) NOT NULL,
  `DocCurrency` varchar(50) NOT NULL,
  `DocTotal` varchar(50) NOT NULL,
  `CardName` varchar(150) NOT NULL,
  `VatSum` varchar(50) NOT NULL,
  `CreationDate` varchar(50) NOT NULL,
  `DocEntry` varchar(5) NOT NULL,
  `PaymentGroupCode` varchar(5) NOT NULL,
  `U_Term_Condition` longtext NOT NULL,
  `BPLID` varchar(5) NOT NULL,
  `CreateDate` varchar(30) NOT NULL,
  `CreateTime` varchar(30) NOT NULL,
  `UpdateDate` varchar(30) NOT NULL,
  `UpdateTime` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Item_department`
--

CREATE TABLE `Item_department` (
  `id` bigint NOT NULL,
  `FactorCode` varchar(50) NOT NULL,
  `FactorDescription` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Item_item`
--

CREATE TABLE `Item_item` (
  `id` bigint NOT NULL,
  `UnitPrice` double NOT NULL,
  `Currency` varchar(50) NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemCode` varchar(50) NOT NULL,
  `ItemName` varchar(150) NOT NULL,
  `TaxCode` varchar(50) NOT NULL,
  `U_DIV` varchar(10) NOT NULL,
  `InStock` int NOT NULL,
  `ItemsGroupCode_id` int NOT NULL,
  `UomNo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Item_item`
--

INSERT INTO `Item_item` (`id`, `UnitPrice`, `Currency`, `DiscountPercent`, `ItemCode`, `ItemName`, `TaxCode`, `U_DIV`, `InStock`, `ItemsGroupCode_id`, `UomNo`) VALUES
(1, 150, 'INR', 0.1, 'IT0001', 'Test Item', '0.18', '100', 15, 100, 'NOS'),
(2, 160, 'INR', 0.1, 'IT0002', 'Test Item 2', '.15', '101', 20, 101, 'Package'),
(3, 150, 'INR', 0.1, 'IT0003', 'Test Item asdf', '.18', '100', 15, 100, 'Package'),
(5, 50000, 'INR', 0.1, '', 'Water Chillerdfgsdg', '.18', '100', 25, 100, '674567'),
(7, 233, 'INR', 0.1, 'IT0007', 'new time', '0.1', '100', 15, 100, '200'),
(10, 56767, 'INR', 0.1, 'IT0010', 'Water Ozonator', '0.18', '100', 25, 100, 'NOS'),
(11, 50000, 'INR', 0.1, 'IT0011', 'iPhone', '0.18', '100', 25, 100, 'SET');

-- --------------------------------------------------------

--
-- Table structure for table `Item_tax`
--

CREATE TABLE `Item_tax` (
  `id` bigint NOT NULL,
  `Rate` double NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Code` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Lead_chatter`
--

CREATE TABLE `Lead_chatter` (
  `id` bigint NOT NULL,
  `Message` varchar(250) NOT NULL,
  `Lead_Id` varchar(10) NOT NULL,
  `Emp_Id` varchar(10) NOT NULL,
  `Emp_Name` varchar(50) NOT NULL,
  `UpdateDate` varchar(100) NOT NULL,
  `UpdateTime` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Lead_lead`
--

CREATE TABLE `Lead_lead` (
  `id` bigint NOT NULL,
  `date` varchar(60) NOT NULL,
  `location` varchar(100) NOT NULL,
  `companyName` varchar(100) NOT NULL,
  `numOfEmployee` int NOT NULL,
  `turnover` varchar(100) NOT NULL,
  `source` varchar(100) NOT NULL,
  `source_id` varchar(10) NOT NULL,
  `contactPerson` varchar(100) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `phoneNumber` varchar(20) NOT NULL,
  `message` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `leadType` varchar(50) NOT NULL,
  `productInterest` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `tender` int NOT NULL,
  `category` varchar(250) NOT NULL,
  `groupType` varchar(250) NOT NULL,
  `intProdCat` varchar(250) NOT NULL,
  `intProjCat` varchar(250) NOT NULL,
  `country` varchar(250) NOT NULL,
  `country_code` varchar(250) NOT NULL,
  `state` varchar(250) NOT NULL,
  `state_code` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `DivCode` varchar(50) NOT NULL,
  `DivName` varchar(50) NOT NULL,
  `BPStatus` varchar(2) NOT NULL,
  `OPStatus` varchar(2) NOT NULL,
  `TDStatus` varchar(2) NOT NULL,
  `QTStatus` varchar(2) NOT NULL,
  `ODStatus` varchar(2) NOT NULL,
  `junk` int NOT NULL,
  `timestamp` varchar(60) NOT NULL,
  `assignedTo_id` bigint NOT NULL,
  `employeeId_id` bigint NOT NULL,
  `code` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Lead_lead`
--

INSERT INTO `Lead_lead` (`id`, `date`, `location`, `companyName`, `numOfEmployee`, `turnover`, `source`, `source_id`, `contactPerson`, `designation`, `phoneNumber`, `message`, `email`, `leadType`, `productInterest`, `status`, `tender`, `category`, `groupType`, `intProdCat`, `intProjCat`, `country`, `country_code`, `state`, `state_code`, `city`, `DivCode`, `DivName`, `BPStatus`, `OPStatus`, `TDStatus`, `QTStatus`, `ODStatus`, `junk`, `timestamp`, `assignedTo_id`, `employeeId_id`, `code`) VALUES
(13, '2022-09-14', 'North Zone', 'IBM', 0, '', 'Facebook', '2', 'Rahulaa', '', '1231231122', 'Testing', 'abcd@gmail.co', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Bottle Filling Stations', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '1', '', '1', '1', 0, '2022-09-14 11:36:49 AM', 1, 1, 'FCBK/L13'),
(14, '2022-09-20', 'North Zone', 'N/A', 0, '', 'Linkedin', '3', 'Rahul', '', '9711767677', 'Testing', 'rahul@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', ' Jharkhand', 'JH', 'Jhadkand', '', '', '', '', '', '', '', 0, '2022-09-20 10:33:17 AM', 1, 1, 'FCBK/L14'),
(22, '2022-09-22', 'North Zone', 'new rahul co', 0, '', 'Linkedin', '3', 'Rahul', '', '9711767671', 'Testing', 'abcd@gmail.c', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Bottle Filling Stations', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-09-22 2:04:21 PM', 1, 1, 'LIND/L22'),
(28, '2022-08-08', 'West Zone', 'Cinntra', 0, '', 'Facebook', '2', 'Rahul', 'Developer', '1233212211', 'Testing', 'abcd@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Bottle Filling Stations', 'Sewage Treatment Plant', '', '', ' ', '', '', '', '', '', '', '', '', '', 0, '2022-09-22 5:54:57 PM', 1, 1, 'FCBK/L28'),
(29, '2022-09-23', 'North Zone', 'New asdfasd', 0, '', 'Facebook', '2', 'Rahul', '', '9711767634', 'Testing', 'abcd@gmail.comm', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Client', '', '', 'India', 'IN', ' Andaman and Nicobar Islands', 'AN', 'Arif', '', '', '', '', '', '', '', 0, '2022-09-23 4:24:19 PM', 1, 1, 'FCBK/L29'),
(30, '2022-09-23', 'North Zone', 'asdfaf', 0, '', 'Facebook', '2', 'Rahul', '', '8800380688', 'Testing', 'rahul@gmail.con', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-09-23 4:32:14 PM', 1, 1, 'FCBK/L30'),
(31, '2022-09-26', 'North Zone', 'MI Electronics', 0, '', 'Emailer', '7', 'Anil Tyagi', 'Sales', '9876898765', 'NA', 'aniltyagi@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 0, '2022-09-26 10:55:53 AM', 1, 1, 'EMLR/L31'),
(32, '2022-09-26', 'East Zone', 'testi rahu', 0, '', 'Facebook', '2', 'asdf', '', '9711767622', 'Testing', 'vaibhavtyagi@gmail.com', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '1', '', '', '', 0, '2022-09-26 3:52:16 PM', 1, 1, 'FCBK/L32'),
(33, '2022-09-26', 'North Zone', 'ASDasd', 0, '', 'Facebook', '2', 'ADSads', '', '9711767673', '', 'SDASD@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '1', '', '', '', 0, '2022-09-26 4:12:22 PM', 1, 1, 'FCBK/L33'),
(34, '2022-09-27', 'North Zone', 'test asdf', 0, '', 'Facebook', '2', 'Rahul', '', '8800380680', 'Testing', 'rahul.akarniya@cinntra.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '1', '', '', '', 1, '2022-09-27 10:26:48 AM', 1, 1, 'FCBK/L34'),
(35, '2022-10-03', 'East Zone', 'Ajanara Enclave', 0, '', 'Facebook', '2', 'Abhinav Tyagi', 'Sales leading Manager', '9797979766', 'NA', 'abhinavtyagi@gmail.com', 'New', '', 'Qualified', 0, 'Project', 'Project Management Consultant', '', 'Water Treatment Plant', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 1, '2022-10-03 11:20:11 AM', 95, 94, 'FCBK/L35'),
(36, '2022-10-03', 'North Zone', 'Trends', 0, '', 'Emailer', '7', 'Ashok', 'Sales manager', '9876898076', '', 'ashokch@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Project Management Consultant', 'Drinking Water Fountains', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 1, '2022-10-03 4:59:57 PM', 95, 1, 'EMLR/L36'),
(37, '2022-10-03', 'East', 'Ananda', 0, '', 'LinkedIn', '3', 'Chotu', 'Market Leading Manager', '9678968965', 'NA', 'chotu@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'MEP Consultant', 'Drinking Water Taps', '', '', '', ' ', '', '', '', '', '', '', '', '', '', 1, '2022-10-03 5:02:53 PM', 95, 1, 'EXTR/L37'),
(38, '2022-10-06', 'North Zone', 'Haldiram & CO.', 0, '', 'Facebook', '2', 'Nitin Tyagi', 'Managing Director', '9879868687', 'NA', 'nitintyagi@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Water Coolers', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Hapur', '', '', '', '1', '', '', '', 0, '2022-10-06 2:45:54 PM', 96, 96, 'FCBK/L38'),
(39, '2022-10-07', 'North Zone', 'Groffers Stove', 0, '', 'Instagram', '4', 'Chandan Singh', 'Sales Managing Director', '8979879797', 'Not assigned', 'chandansingh@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Drinking Water Stations', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 0, '2022-10-07 6:12:43 PM', 98, 98, 'INST/L39'),
(40, '2022-10-10', 'South Zone', 'IBM COMP LTD', 0, '', 'Linkedin', '3', 'Rahul Akarniya', 'Business Analyst', '7987987979', 'NA', 'rahul.akarniya@cinntra.co.in', 'New', '', 'Qualified', 0, 'Product', 'Project Management Consultant', 'Water Chillers ', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 0, '2022-10-10 5:11:08 PM', 101, 1, 'LIND/L40'),
(41, '2022-10-11', 'North Zone', 'Bajaj Finserve', 0, '', 'Whatsapp', '6', 'Rakesh Jain', '', '8686876876', '', 'ankur.tyagi@cinntra.com', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Water Coolers', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 0, '2022-10-11 11:56:20 AM', 1, 1, 'WHAP/L41'),
(42, '2022-10-11', 'North Zone', 'Pest Control', 0, '', 'Emailer', '7', 'Abhi Tyagi', 'Sales manager', '9080987987', '', 'abhi.tyagi@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Noida', '', '', '', '1', '', '', '', 1, '2022-10-11 5:51:51 PM', 1, 1, 'EMLR/L42'),
(43, '2022-10-17', 'East Zone', 'ASDsd', 0, '', 'Facebook', '2', 'ASDasd', 'Developer', '9711767670', 'ASSDA', 'rahul@gmail.comm', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Sewage Treatment Plant', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-10-17 2:20:17 PM', 1, 1, 'FCBK/L43'),
(44, '2022-10-17', 'North Zone', 'asdfdasf', 0, '', 'Facebook', '2', 'asdfadsf', 'asdfadsf', '9711767672', 'asdf', 'vaibhavtyagi@gmail.com3', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-10-17 3:51:08 PM', 1, 1, 'FCBK/L44'),
(45, '2022-10-18', 'North Zone', 'New Company ', 0, '', 'Linkedin', '3', 'Ab Delive', 'CEO', '8809069134', 'new suer sas', 'aryansantosh64@gmail.com', 'Follow Up', '', 'Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', ' Dadra and Nagar Haveli', 'DN', 'Patna', '', '', '', '', '', '', '', 0, '2022-10-18 12:30:59', 1, 1, 'LIND/L45'),
(46, '2022-10-18', 'North Zone', 'androiddev', 0, '', 'Instagram', '4', 'Pankaj Sharma', 'Developer', '9354786706', 'test', 'ps9758541207@gmail.com', 'Follow Up', '', 'Qualified', 0, 'Product', 'Client', 'Water Dispenser', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Hathras', '', '', '', '', '', '', '', 0, '2022-10-18 2:28:32 PM', 91, 1, 'INST/L46'),
(47, '2022-10-18', 'East Zone', 'New Dataum', 0, '', 'Linkedin', '3', 'Ab Delive', 'CEO', '8809069135', 'new suer sas', 'ashutoshk160@gmail.com', 'Follow Up', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Bottle Filling Stations', '', ' India', 'IN', ' Daman and Diu', 'DD', 'Patna', '', '', '', '', '', '', '', 0, '2022-10-18 14:30:19', 1, 1, ''),
(48, '2022-10-18', 'East Zone', 'New Dataumm', 0, '', 'Linkedin', '3', 'Ab Delive', 'CEO', '8809069137', 'new suer sas', 'ashutoshk160@gmail.co', 'Follow Up', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Bottle Filling Stations', '', ' India', 'IN', ' Daman and Diu', 'DD', 'Patna', '', '', '', '', '', '', '', 0, '2022-10-18 14:30:19', 1, 1, ''),
(49, '2022-10-18', 'East Zone', 'nya comapny ', 0, '', 'Facebook', '2', 'Ab Delive', 'Software Developer', '8809069130', 'new suer sas', 'bhoopendra.pal@cinntra.co', 'Follow Up', '', 'Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'India', 'IN', ' Chandigarh', 'CH', 'Delhi', '', '', '', '', '', '', '', 0, '2022-10-18 15:19:27', 89, 1, 'FCBK/L49'),
(50, '18-10-2022', 'East Zone', 'wqrwerwsdsfdsf', 0, '', 'Event', '2', 'sdfsdf sdfsdf adds', 'sdfsfdsfsdfdsfsf', '42342342343', 'Ewerwerwerwerwerwe', 'sdfsdfsfsdf@ssfsd.sdfsf', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'United Arab Emir.', 'AE', 'Dubayy', 'DU', 'sdfsfsdfsdfs', '', '', '', '', '', '', '', 0, '', 1, 1, ''),
(51, '18-10-2022', 'East Zone', 'errererererereer', 0, '', 'Event', '2', 'sdfsdf sdfsdf adds', 'sdfsfdsfsdfdsfsf', '42342342455', 'Ewerwerwerwerwerwe', 'sdfsdfsfsdf@ssfsd.sdfs', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'United Arab Emir.', 'AE', 'Dubayy', 'DU', 'sdfsfsdfsdfs', '', '', '', '', '', '', '', 0, '', 1, 1, ''),
(52, '2022-10-18', 'North Zone', 'ashutosh', 0, '', 'Linkedin', '3', 'ashu', 'asdf', '9711767999', 'Testing', 'rahul.akarniya@cinntra.c', 'New', '', 'Not Qualified', 0, 'Project', 'Client', '', 'Sewage Treatment Plant', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-10-18 3:37:42 PM', 1, 1, 'LIND/L52'),
(53, '2022-10-18', 'East Zone', 'Ashutosh 2', 0, '', 'Facebook', '2', 'Rahul', 'Developer', '9883343333', 'Testing', 'ashu@gmail.com', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'India', 'IN', ' Jharkhand', 'JH', 'Arif', '', '', '', '', '', '', '', 0, '2022-10-18 3:40:36 PM', 1, 1, 'FCBK/L53'),
(54, '2022-10-18', 'Fahvs', 'xucif', 10, '', 'Instagram', '4', 'Gxhfydyfu', 'Zgdrhfxu', '8356553385', 'xagahc', 'xyxyuf@gmqil.con', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Taps', '', 'India', 'IN', 'Daman and Diu', 'DD', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 15:53:31', 1, 1, ''),
(55, '18-10-2022', 'North Zone', 'dsfsdfsdfsfs', 0, '', 'Whatsapp', '2', 'sfsdfsfsdfsdfd', 'sdfsfssfsdfsfsf', '77045345353', 'Erwrwevrewrvwrvwrwrwerwer', 'sdfssdfdsfsfsd@sadaa.can', 'Follow Up', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Drinking Water Fountains', '', 'Armenia', 'AM', 'Tavuš', 'TV', 'dfgdgdgdgd', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, ''),
(56, '2022-10-18', 'Noida', 'hsibsjs', 10, '', 'Facebook', '2', ' Zjht x', 'Vhv subjK', '9768497684', 'gehbai', 'gshjzh@gmailc.om', 'Follow up', '', 'Not Qualified', 0, 'Project', 'Client', '', 'Sewage Treatment Plant', 'India', 'IN', 'Delhi', 'DL', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:03:28', 1, 1, ''),
(57, '2022-10-18', 'Bsibx', 'testtfg', 10, '', 'Facebook', '2', 'Hjsjdbdh', 'Gajsvjxb', '9795438778', 'gaugsbjx', 'vshbsbz@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Water Chillers', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:06:00', 1, 1, ''),
(58, '2022-10-18', 'Ysysyhz', 'bJzbxb', 10, '', 'Facebook', '2', 'Bzbxhgsv', 'VHvsjjznna', '9768168768', 'gsgshsh', 'vzhzhz@gmajlc.js', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Water Treatment Plant', 'India', 'IN', 'Daman and Diu', 'DD', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:09:00', 1, 1, ''),
(59, '18-10-2022', 'East Zone', 'asdgasdhsdahgd', 0, '', 'Emailer', '2', 'sdjfsfskjfhsfsdhjfsfj', 'sfhsdfshfsjdfsj', '99343434344', 'Sdfsfsfsfsfsfs', 'qweertyui@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'MEP Consultant', 'Drinking Water Fountains', '', 'United Arab Emir.', 'AE', 'Umm al Qaywayn', 'UQ', 'sdfsdf sdfsdf', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EMLR/L59'),
(60, '18-10-2022', 'East Zone', 'asdgasdhsdahg', 0, '', 'Emailer', '2', 'sdjfsfskjfhsfsdhjfsfj', 'sfhsdfshfsjdfsj', '99343434311', 'Sdfsfsfsfsfsfs', 'qweertyui@gmail.co', 'New', '', 'Not Qualified', 0, 'Product', 'MEP Consultant', 'Drinking Water Fountains', '', 'United Arab Emir.', 'AE', 'Umm al Qaywayn', 'UQ', 'sdfsdf sdfsdf', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, ''),
(61, '2022-10-18', 'Zhuzbj', 'cyctv', 10, '', 'Facebook', '2', 'Hshjzhbs', 'Vaugaivsj', '2183406706', 'hzjsbjs', 'gssshjzh@gmailc.om', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'India', 'IN', 'Daman and Diu', 'DD', 'West Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:13:09', 1, 1, ''),
(62, '18-10-2022', 'North Zone', 'qwertyuiop', 0, '', 'Event', '2', 'ASDFGHJKL', 'zxcvbnm', '53554353454', 'Dfsfsdfdsfdsfdfsdfdsfsdfsdfsfs', 'asdhutte@gmail.com', 'Follow Up', '', 'Qualified', 0, 'Product', 'MEP Consultant', 'Bottle Filling Stations', '', 'Albania', 'AL', 'Korçë', '06', 'dffssdfsdfsdfdsf', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EVNT/L62'),
(63, '18-10-2022', 'North Zone', 'qwertyuiopr', 0, '', 'Event', '2', 'ASDFGHJKL', 'zxcvbnm', '53554353455', 'Dfsfsdfdsfdsfdfsdfdsfsdfsdfsfs', 'asdhutte@gmail.co', 'Follow Up', '', 'Qualified', 0, 'Product', 'MEP Consultant', 'Bottle Filling Stations', '', 'Albania', 'AL', 'Korçë', '06', 'dffssdfsdfsdfdsf', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EVNT/L63'),
(64, '18-10-2022', 'West Zone', 'zxcvbnm', 0, '', 'Emailer', '2', 'asdfghjkl', 'qwertyuiop', '88923232323', 'Dsadasdasdsadasdadasdadasdas', 'ashu1221@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Contractor', 'Water Dispenser', '', 'Antigua/Barbuda', 'AG', 'Saint Philip', '08', 'dfsfsdjhkfsdfsdfsdf', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EMLR/L64'),
(65, '2022-10-18', 'Haigsn', 'vshsbzjj', 10, '', 'Facebook', '2', 'Sgjsghaj', 'Vshcdjdvj', '6786786707', 'vajvsjjd', 'vshsghsh@gmail.con', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Arunachal Pradesh', 'AR', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:16:11', 1, 1, ''),
(66, '2022-10-18', 'Hjfc b', 'thmnvm', 10, '', 'Facebook', '2', 'Vjfgbtc', 'Ghftvczbh', '9385578689', 'ghjgfcvv', 'ghfghhg@gmaj.bj', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Delhi', 'DL', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 16:38:52', 1, 1, ''),
(67, '2022-10-18', 'North Zone', 'thvm', 10, '', 'Facebook', '2', 'Vjfgbtc', 'Ghftvczbh', '938557889', 'ghjgfcvv', 'ghhhg@gmaj.bj', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Delhi', 'DL', 'Hjfc b', '', '', '', '', '', '', '', 0, '2022-10-18 16:38:52', 1, 1, 'FCBK/L67'),
(68, '2022-10-18', 'Shhshsh', 'gshshs', 10, '', 'Facebook', '2', 'Bzhagyavjs', 'Bhabbdbd', '7664867867', 'aghahaha', 'gshshha@gshsh.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 17:20:58', 1, 1, 'FCBK/L68'),
(69, '18-10-2022', 'East Zone', 'New COmpanay hai', 0, '', 'Event', '2', 'New Person hai', 'Developers', '88095324322', 'Ajlshchljsjlsajkllasjlkdaslkjdas', 'ashurtrt@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Bottle Filling Stations', '', 'Armenia', 'AM', 'Syunik\'', 'SU', 'hdhjkfhjksdfjksdfs', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EVNT/L69'),
(70, '18-10-2022', 'East Zone', 'New COmpanay hai first', 0, '', 'Event', '2', 'New Person hai', 'Developers', '88095324321', 'Ajlshchljsjlsajkllasjlkdaslkjdas', 'ashurtrt@gmail.co', 'New', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Bottle Filling Stations', '', 'Armenia', 'AM', 'Syunik\'', 'SU', 'hdhjkfhjksdfjksdfs', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EVNT/L70'),
(71, '2022-10-18', 'Gdhfsggxdh', 'hfgx', 10, '', 'Facebook', '2', 'Dggdjghc', 'Gfuggdgd', '8665255458', 'xgdhfj', 'gdfhgdgdgd@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 17:24:55', 1, 1, 'FCBK/L71'),
(72, '2022-10-18', 'Zvzghz', 'gshah', 10, '', 'Facebook', '2', 'Hajagyzv', 'Gzgzgz', '9764864884', 'gzhzhzj', 'zvvzvv@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 17:31:03', 1, 1, 'FCBK/L72'),
(73, '18-10-2022', 'East Zone', 'new hai firs', 0, '', 'Emailer', '2', 'new person', 'Patan ahi', '88090534234', 'Dsfsdfsfsfs', 'newemail@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Bottle Filling Stations', '', 'Argentina', 'AR', 'Entre Ríos', 'E', 'adsasdasdas', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EMLR/L73'),
(74, '2022-10-18', 'Chfhhx', 'gdgfu', 10, '', 'Facebook', '2', 'Ydgdyf', 'Ggxgdydyf', '8553555225', 'hhfufu', 'hxhch@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-18 17:37:50', 1, 1, 'FCBK/L74'),
(75, '18-10-2022', 'North Zone', 'dsghuewghrwewey', 0, '', 'Whatsapp', '2', 'ifsifdshdfshdfkh', 'hidfjhkdfsjfdsjkhfdjhk', '34279879783', 'Dfsdfsfsfsdfsdfsdfsfsfs', 'hdfsjhkdjdhsjh@hhjks.can', 'New', '', 'Qualified', 0, 'Product', 'Contractor', 'Drinking Water Fountains', '', 'Afghanistan', 'AF', 'Fāryāb', 'FYB', 'dfddsfsdfsds', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'WHAP/L75'),
(76, '18-10-2022', 'North Zone', 'nkjwekghrwerwerkhj', 0, '', 'Event', '2', 'sdjkfshdjkfhjksjhk', 'hdssjfsjhkfshjkfhj', '23242424322', 'Dfsfsdfs', 'hjhdjhkkjhjkhjhj@jjasdas.can', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Ozonators', '', 'Afghanistan', 'AF', 'Ghōr', 'GHO', 'rwerwerwerw', '', '', '', '', '', '', '', 0, '18-10-2022', 1, 1, 'EVNT/L76'),
(77, '2022-10-19', 'Tcyv', 'yv', 10, '', 'Facebook', '2', 'Gc', 'Gg', '6868866868', 'ycgy', 'gcyv@gmnj.vi', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 10:25:05', 1, 1, 'FCBK/L77'),
(78, '19-10-2022', 'North Zone', 'Ashutosh Tech', 0, '', 'Instagram', '2', 'Ashutosh', 'CEO', '88090543211', 'New Post added for leads', 'ashutr12@gmail.com', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Contractor', 'Ozonators', '', 'Austria', 'AT', 'Burgenland', 'B', 'Parma', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'INST/L78'),
(79, '2022-10-19', 'Xghcgcg', 'hcchhchf', 10, '', 'Facebook', '2', 'Tddygjgcxg', 'Xfgcgchchf', '6865254285', ' vb bcbv', 'gcchgf@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 11:03:16', 1, 1, 'FCBK/L79'),
(80, '19-10-2022', 'East Zone', 'dadas dads was dads d', 0, '', 'Facebook', '2', 'sdfsdf sdf sdfsf', 'we we\'re we ', '54676879875', 'Fdgdgdfgdfgd', 'werwwer@ada.can', 'Follow Up', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'Andorra', 'AD', 'Andorra la Vella', '07', 'erterterterter', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'FCBK/L80'),
(81, '19-10-2022', 'East Zone', 'dadas dads was dads d c', 0, '', 'Facebook', '2', 'sdfsdf sdf sdfsf', 'we we\'re we ', '54676879871', 'Fdgdgdfgdfgd', 'werwwer@ada.ca', 'Follow Up', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'Andorra', 'AD', 'Andorra la Vella', '07', 'erterterterter', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'FCBK/L81'),
(82, '2022-10-19', 'Gcgvbhjb', 'fxgchv', 10, '', 'Facebook', '2', 'Cgcghvcg', 'Cggchv', '5868685886', 'chchv', 'ghkg@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 11:22:26', 1, 1, 'FCBK/L82'),
(83, '2022-10-19', 'extgtgyhuh', 'drftgthy', 10, '', 'Facebook', '2', 'Xgthujuju', 'Exgyyhhuhuuh', '2825363636', 'dryguhij', 'xdctgtgy@ghbj.bj', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 11:32:24', 1, 1, 'FCBK/L83'),
(84, '2022-10-19', 'Xgdhhfnc', 'gxxggx', 10, '', 'Facebook', '2', 'Dgdhdhfhfjg', 'Xhfuffiit', '6854343248', 'chhcjgjg', 'gxbchchf@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 11:36:14', 1, 1, 'FCBK/L84'),
(85, '19-10-2022', 'North Zone', 'Werner wet werwe we', 0, '', 'Event', '2', 'we\'re we\'re', 'werrwrwerww', '34234256645', 'Dgdfgdgdgdgg', 'erewrwerwer@asd.dad', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Drinking Water Fountains', '', 'Albania', 'AL', 'Kukës', '07', 'reterteter', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'EVNT/L85'),
(86, '2022-10-19', 'Cfvghbjn', 'dxftgyyh', 10, '', 'Facebook', '2', 'Fchghhuhuh', 'Dxvgbhijij', '5885965869', 'xdgvufrxyv', 'dxvfhbhn@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '', '', '', '', 0, '2022-10-19 11:39:24', 1, 1, 'FCBK/L86'),
(87, '19-10-2022', 'North Zone', 'wet werwerwe', 0, '', 'Emailer', '2', 'werwerewrewrwr', 'werewrwerewrwe', '23423424244', 'Dffsfsfsfsf', 'ewwerwerwrw@asdas.as', 'Follow Up', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Drinking Water Fountains', '', 'Afghanistan', 'AF', 'Farāh', 'FRA', 'sfsvfdfsfsfd', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'EMLR/L87'),
(88, '19-10-2022', 'North Zone', 'wet werwerw', 0, '', 'Emailer', '2', 'werwerewrewrwr', 'werewrwerewrwe', '23423424246', 'Dffsfsfsfsf', 'ewwerwerwrw@asdas.a', 'Follow Up', '', 'Qualified', 0, 'Product', 'Kitchen Consultant', 'Drinking Water Fountains', '', 'Afghanistan', 'AF', 'Farāh', 'FRA', 'sfsvfdfsfsfd', '', '', '', '', '', '', '', 0, '19-10-2022', 1, 1, 'EMLR/L88'),
(89, '2022-10-19', 'North Zone', 'trcyv', 0, '', 'Facebook', '2', 'xryctvu', 'jiyufty', '0987654367', 'khugy', 'rctvbnm@ghjk.bh', 'New', '', 'Qualified', 0, 'Project', 'Contractor', '', 'Sewage Treatment Plant', 'India', 'IN', '', '', 'tvybun', '', '', '', '', '', '', '', 0, '2022-10-19 1:06:15 PM', 101, 1, 'FCBK/L89'),
(90, '2022-10-19', 'Shsjhxbx', 'bsjskbxjx', 10, '', 'Facebook', '2', 'Aoosghx', 'Nskgxuvsj', '9464668797', 'zhhxhchc', 'shhsjs@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Andaman and Nicobar Islands', 'AN', 'North Zone', '', '', '', '1', '', '', '', 0, '2022-10-19 13:19:12', 1, 1, 'FCBK/L90'),
(91, '2022-11-02', 'North Zone', 'Humdard', 0, '', 'Facebook', '2', 'Suresh Tyagi', 'Sales & Marketing Manager', '7428498286', '', 'suresh.tyagi@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Facility Management', 'Water Coolers', '', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Ghaziabad', '', '', '', '1', '', '', '', 0, '2022-11-02 6:00:36 PM', 1, 1, 'FCBK/L91'),
(92, '2022-11-03', 'North Zone', 'ITC', 0, '', 'Instagram', '4', 'Sudhir Kumar', 'Sales & Marketing Manager', '9879878678', '', 'sudhir.kumar@gmail.com', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Ultra Filtration Plant', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Ghaziabad', '', '', '', '1', '', '', '', 0, '2022-11-03 10:46:39 AM', 106, 106, 'INST/L92'),
(93, '2022-11-04', 'West Zone', 'Shiv Lakhan Textiles', 0, '', 'Emailer', '7', 'Shiv', '', '9090909090', '', 'shiv@cinntra.com', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Water Treatment Plant', 'India', 'IN', ' Maharashtra', 'MH', 'Mumbai', '', '', '', '1', '', '', '', 0, '2022-11-04 12:51:44 PM', 107, 107, 'EMLR/L93'),
(94, '2022-11-04', 'North Zone', 'Tesing Lead', 0, '', 'Facebook', '2', 'Rahul', '', '9711762333', '', 'rahul.akarniya@cinntra.co', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', '', '', 'Delhi', '', '', '', '', '', '', '', 0, '2022-11-04 3:43:22 PM', 1, 1, 'FCBK/L94'),
(95, '2022-11-04', 'East Zone', 'qqwert', 0, '', 'Facebook', '2', 'werty', '', '9090909099', '', 'shiv@cinntra.con', 'Follow Up', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', '', '', 'Mumbai', '', '', '', '', '', '', '', 0, '2022-11-04 3:43:46 PM', 107, 107, 'FCBK/L95'),
(96, '2022-11-07', 'North Zone', 'Lucky Traders', 0, '', 'Whatsapp', '6', 'Lucky Singh', 'Sales & Marketing Manager', '9898798797', '', 'luckysingh@gmail.com', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Ultra Filtration Plant', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Muradnagar', '', '', '', '1', '', '', '', 0, '2022-11-07 3:12:55 PM', 106, 106, 'WHAP/L96'),
(97, '2022-11-09', 'Noida', 'testing ', 10, '', 'Facebook', '2', 'Pankaj', 'Developer ', '9325878665', 'test', 'rahul11akarniya@gmail.com', 'Follow up', '', 'Qualified', 0, 'Project', 'Client', '', 'Water Treatment Plant', 'India', 'IN', 'Delhi', 'DL', 'East Zone', '', '', '', '', '', '', '', 0, '2022-11-09 12:10:27', 1, 1, 'FCBK/L97'),
(98, '2022-11-09', 'Testsh', 'wgsh', 10, '', 'Linkedin', '3', 'Gsgs', 'Tsgsjs', '9375876846', 'shhshu', 'sggs@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Lakshadweep', 'LD', 'North Zone', '', '', '', '1', '', '', '', 0, '2022-11-09 16:12:54', 1, 1, 'LIND/L98'),
(99, '2022-11-14', 'North Zone', 'Lux Co.', 0, '', 'Facebook', '2', 'AT', 'TY', '6789876567', '', 'at@gmail.com', 'New', '', 'Qualified', 0, 'Project', 'Client', '', 'Water Treatment Plant', 'India', 'IN', ' Uttar Pradesh', 'UP', 'Muradnagar', '', '', '', '1', '', '', '', 0, '2022-11-14 6:37:22 PM', 1, 1, 'FCBK/L99'),
(100, '2022-11-15', 'East Zone', 'Ankur Santanu Bros & Co.', 0, '', 'Website', '5', 'Ankur Sahu', 'CEO', '9310010422', '', 'Ankur@cinntra.com', 'New', '', 'Qualified', 0, 'Product', 'Architect', 'Water Chillers ', '', 'India', 'IN', ' Odisha', 'OR', 'Bhubaneshwar', '', '', '', '1', '', '', '', 0, '2022-11-15 11:04:24 AM', 1, 1, 'WBST/L100'),
(101, '2022-11-17', 'North Zone', 'gxhxfh', 10, '', 'Facebook', '2', 'Xgjghffd', 'Xghchchc', '7655386686', 'chjcjvjv', 'ddgyt@gmail.com', 'New', '', 'Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Daman and Diu', 'DD', 'Gdgggh', '', '', '', '', '', '', '', 0, '2022-11-17 12:13:59', 1, 1, 'FCBK/L101'),
(102, '2022-11-17', 'North Zone', 'tedgfg', 10, '', 'Facebook', '2', 'Tedvgg', 'Gxgfgcgc', '2568868896', 'fxfxgc', 'fxfxgxcg@hotmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Dadra and Nagar Haveli', 'DN', 'Fxgxgc', '', '', '', '', '', '', '', 0, '2022-11-17 12:15:50', 1, 1, 'FCBK/L102'),
(103, '2022-11-17', 'North Zone', 'xgjvjvjvhf', 10, '', 'Facebook', '2', 'Tesgg', 'Hfhgjgjb', '5868688558', 'chhchc', 'xgbnghh@gmail.com', 'New', '', 'Not Qualified', 0, 'Product', 'Client', 'Bottle Filling Stations', '', 'India', 'IN', 'Lakshadweep', 'LD', 'Ghhb', '', '', '', '', '', '', '', 0, '2022-11-17 12:22:16', 1, 1, 'FCBK/L103');

-- --------------------------------------------------------

--
-- Table structure for table `Lead_leaditem`
--

CREATE TABLE `Lead_leaditem` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `LeadID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `TaxCode` varchar(10) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Lead_source`
--

CREATE TABLE `Lead_source` (
  `id` bigint NOT NULL,
  `Name` varchar(50) NOT NULL,
  `CreatedDate` varchar(50) NOT NULL,
  `CreatedTime` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Lead_source`
--

INSERT INTO `Lead_source` (`id`, `Name`, `CreatedDate`, `CreatedTime`) VALUES
(2, 'Facebook', '2022-08-08', '12:47:16'),
(3, 'Linkedin', '2022-08-08', '12:47:16'),
(4, 'Instagram', '2022-08-08', '12:47:16'),
(5, 'Website', '2022-08-08', '12:47:16'),
(6, 'Whatsapp', '2022-08-08', '12:47:16'),
(7, 'Emailer', '2022-08-21', '21:16:33'),
(8, 'Event', '2022-08-25', '18:23:04'),
(10, 'Personal Contact', '2022-11-15', '15:31:30');

-- --------------------------------------------------------

--
-- Table structure for table `Lead_type`
--

CREATE TABLE `Lead_type` (
  `id` bigint NOT NULL,
  `Name` varchar(50) NOT NULL,
  `CreatedDate` varchar(50) NOT NULL,
  `CreatedTime` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Notification_notification`
--

CREATE TABLE `Notification_notification` (
  `id` bigint NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Description` varchar(250) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `SourceType` varchar(100) NOT NULL,
  `SourceID` varchar(10) NOT NULL,
  `Emp` varchar(4) NOT NULL,
  `Read` varchar(1) NOT NULL,
  `Push` int NOT NULL,
  `SourceTime` varchar(10) NOT NULL,
  `CreatedDate` varchar(10) NOT NULL,
  `CreatedTime` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Opportunity_line`
--

CREATE TABLE `Opportunity_line` (
  `id` bigint NOT NULL,
  `LineNum` varchar(9) NOT NULL,
  `SalesPerson` varchar(9) NOT NULL,
  `StartDate` varchar(50) NOT NULL,
  `ClosingDate` varchar(50) NOT NULL,
  `StageKey` varchar(9) NOT NULL,
  `MaxLocalTotal` varchar(100) NOT NULL,
  `MaxSystemTotal` varchar(100) NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `Contact` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `ContactPerson` varchar(100) NOT NULL,
  `SequenceNo` varchar(9) NOT NULL,
  `Opp_Id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Opportunity_line`
--

INSERT INTO `Opportunity_line` (`id`, `LineNum`, `SalesPerson`, `StartDate`, `ClosingDate`, `StageKey`, `MaxLocalTotal`, `MaxSystemTotal`, `Remarks`, `Contact`, `Status`, `ContactPerson`, `SequenceNo`, `Opp_Id`) VALUES
(1, '0', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'so_Open', '5', '1', 1),
(2, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '5', '', 1),
(3, '0', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'so_Open', '4', '2', 2),
(4, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '4', '', 2),
(5, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '5', '', 1),
(6, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '5', '', 1),
(7, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '5', '', 1),
(8, '1', '89', '2022-09-28', '2022-09-28', '1', '5000', '60000', 'Testing', 'tNO', 'sos_Open', '4', '', 2),
(9, '0', '94', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'so_Open', '17', '3', 3),
(10, '1', '94', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'sos_Open', '17', '', 3),
(11, '0', '95', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'so_Open', '21', '4', 4),
(12, '1', '95', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'sos_Open', '21', '', 4),
(13, '1', '95', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'sos_Open', '21', '', 4),
(14, '1', '95', '2022-10-03', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'sos_Open', '21', '', 4),
(15, '0', '97', '2022-10-06', '2022-10-16', '1', '5000', '60000', '', 'tNO', 'so_Open', '22', '5', 5),
(16, '0', '99', '2022-10-07', '2022-10-16', '1', '5000', '60000', 'NA', 'tNO', 'so_Open', '23', '6', 6),
(17, '0', '101', '2022-10-10', '2022-10-21', '1', '5000', '60000', '', 'tNO', 'so_Open', '27', '7', 7),
(18, '1', '101', '2022-10-10', '2022-10-21', '1', '5000', '60000', '', 'tNO', 'sos_Open', '27', '', 7),
(19, '0', '101', '2022-10-10', '2022-10-21', '1', '5000', '60000', '', 'tNO', 'so_Open', '28', '8', 8),
(20, '0', '102', '2022-10-11', '2022-10-11', '1', '5000', '60000', 'Testing', 'tNO', 'so_Open', '33', '9', 9),
(21, '0', '1', '2022-10-11', '2022-10-21', '1', '5000', '60000', '', 'tNO', 'so_Open', '36', '10', 10),
(22, '0', '102', '2022-10-17', '2022-10-17', '1', '5000', '60000', 'Testing', 'tNO', 'so_Open', '38', '11', 11),
(23, '0', '102', '2022-10-31', '2022-10-31', '1', '5000', '60000', '', 'tNO', 'so_Open', '42', '12', 12),
(24, '0', '103', '2022-11-02', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'so_Open', '44', '13', 13),
(25, '1', '103', '2022-11-02', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '44', '', 13),
(26, '0', '106', '2022-11-03', '2022-11-18', '1', '5000', '60000', '', 'tNO', 'so_Open', '45', '14', 14),
(27, '0', '107', '2022-11-03', '2022-11-03', '1', '5000', '60000', '', 'tNO', 'so_Open', '47', '15', 15),
(28, '0', '107', '2022-11-03', '2022-11-04', '1', '5000', '60000', '', 'tNO', 'so_Open', '48', '16', 16),
(29, '0', '106', '2022-11-03', '2022-11-03', '1', '5000', '60000', '', 'tNO', 'so_Open', '48', '19', 19),
(30, '0', '107', '2022-11-03', '2022-11-03', '1', '5000', '60000', '', 'tNO', 'so_Open', '48', '20', 20),
(31, '0', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'so_Open', '52', '21', 21),
(32, '1', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'sos_Open', '52', '', 21),
(33, '1', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'sos_Open', '52', '', 21),
(34, '0', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'so_Open', '53', '22', 22),
(35, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '53', '', 22),
(36, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '53', '', 22),
(37, '0', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'so_Open', '52', '23', 23),
(38, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '53', '', 22),
(39, '1', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'sos_Open', '52', '', 21),
(40, '1', '107', '2022-11-04', '2022-11-05', '1', '5000', '60000', '', 'tNO', 'sos_Open', '52', '', 23),
(41, '0', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'so_Open', '51', '24', 24),
(42, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 24),
(43, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 24),
(44, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 24),
(45, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 24),
(46, '1', '107', '2022-11-04', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 24),
(47, '0', '107', '2022-11-04', '2022-11-29', '1', '5000', '60000', '', 'tNO', 'so_Open', '51', '25', 25),
(48, '1', '107', '2022-11-04', '2022-11-29', '1', '5000', '60000', '', 'tNO', 'sos_Open', '51', '', 25),
(49, '0', '106', '2022-11-07', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'so_Open', '56', '26', 26),
(50, '0', '106', '2022-11-07', '2022-11-25', '1', '5000', '60000', '', 'tNO', 'so_Open', '56', '27', 27),
(51, '0', '107', '2022-11-14', '2022-11-30', '1', '5000', '60000', '', 'tNO', 'so_Open', '62', '28', 28),
(52, '0', '107', '2022-11-15', '2022-11-30', '1', '5000', '60000', 'retyuiojgfh ygfhuilkjbvhjkl nhjklmn', 'tNO', 'so_Open', '63', '29', 29),
(54, '0', '106', '2022-11-16', '2022-11-17', '1', '5000', '60000', 'test', 'tNO', 'so_Open', '70', '31', 31),
(55, '0', '106', '2022-11-17', '2022-11-17', '1', '5000', '60000', 'Testing', 'tNO', 'so_Open', '70', '32', 32),
(56, '0', '107', '2022-11-17', '2022-11-17', '1', '5000', '60000', 'asdfaf', 'tNO', 'so_Open', '70', '33', 33),
(58, '1', '105', '2022-11-17', '2022-11-17', '1', '5000', '60000', 'asdfaf', 'tNO', 'sos_Open', '70', '', 33),
(59, '1', '105', '2022-11-17', '2022-11-17', '1', '0.7', '0.7', 'asdfafed', 'tNO', 'sos_Open', '70', '', 33),
(60, '0', '92', '2022-11-21', '2022-11-21', '1', '5000', '60000', 'nay adaksjdha dajkd ada', 'tNO', 'so_Open', '53', '36', 36),
(61, '1', '92', '2022-11-21', '2022-11-21', '1', '5000', '60000', 'nay adaksjdha dajkd ada', 'tNO', 'sos_Open', '53', '', 36);

-- --------------------------------------------------------

--
-- Table structure for table `Opportunity_oppitem`
--

CREATE TABLE `Opportunity_oppitem` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `OppID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `TaxCode` varchar(10) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL,
  `Tax` double NOT NULL,
  `UomNo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Opportunity_oppitem`
--

INSERT INTO `Opportunity_oppitem` (`id`, `LineNum`, `OppID`, `Quantity`, `UnitPrice`, `DiscountPercent`, `ItemCode`, `ItemDescription`, `TaxCode`, `U_FGITEM`, `CostingCode2`, `ProjectCode`, `FreeText`, `Tax`, `UomNo`) VALUES
(1, 0, '2', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(2, 1, '2', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, ''),
(3, 0, '3', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(5, 1, '4', 10, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(6, 2, '4', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, ''),
(7, 0, '5', 10, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(8, 0, '6', 10, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(11, 2, '7', 11, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(12, 3, '7', 15, 160, 2, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, ''),
(13, 0, '8', 4, 160, 3, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, ''),
(14, 0, '10', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(16, 1, '13', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(17, 0, '14', 5, 150, 10, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(18, 0, '15', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(19, 0, '16', 5, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, ''),
(20, 0, '19', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 1, 'Package'),
(21, 0, '20', 1, 150, 1, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 3, 'Package'),
(27, 1, '24', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, 'Package'),
(29, 1, '25', 3, 233, 0, 'IT0007', 'new time', 'IGST12', 'IT0007', 'DEPT001', '100', '', 0, '200'),
(30, 0, '26', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, 'Package'),
(31, 0, '27', 5, 50000, 2, '', 'Water Chillerdfgsdg', 'IGST12', '', 'DEPT001', '100', '', 0, '674567'),
(32, 0, '28', 1, 56767, 2, 'IT0010', 'Water Ozonator', 'IGST12', 'IT0010', 'DEPT001', '100', '', 18, 'NOS'),
(33, 0, '29', 5, 56767, 2, 'IT0010', 'Water Ozonator', 'IGST12', 'IT0010', 'DEPT001', '100', 'gh,mmjhgf', 18, 'NOS'),
(35, 0, '31', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', 'test', 0, 'Package'),
(36, 0, '32', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, 'NOS'),
(37, 0, '33', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', 0, 'NOS'),
(38, 1, '33', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, 'Package'),
(40, 0, '36', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', 0, 'Package');

-- --------------------------------------------------------

--
-- Table structure for table `Opportunity_opportunity`
--

CREATE TABLE `Opportunity_opportunity` (
  `id` bigint NOT NULL,
  `SequentialNo` varchar(9) NOT NULL,
  `CardCode` varchar(100) NOT NULL,
  `SalesPerson` varchar(9) NOT NULL,
  `SalesPersonName` varchar(50) NOT NULL,
  `ContactPerson` varchar(9) NOT NULL,
  `ContactPersonName` varchar(50) NOT NULL,
  `Source` varchar(100) NOT NULL,
  `StartDate` varchar(50) NOT NULL,
  `PredictedClosingDate` varchar(50) NOT NULL,
  `MaxLocalTotal` varchar(100) NOT NULL,
  `MaxSystemTotal` varchar(100) NOT NULL,
  `Remarks` varchar(200) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `ReasonForClosing` varchar(100) NOT NULL,
  `TotalAmountLocal` varchar(100) NOT NULL,
  `TotalAmounSystem` varchar(100) NOT NULL,
  `CurrentStageNo` varchar(3) NOT NULL,
  `CurrentStageNumber` varchar(3) NOT NULL,
  `CurrentStageName` varchar(50) NOT NULL,
  `OpportunityName` varchar(100) NOT NULL,
  `Industry` varchar(100) NOT NULL,
  `LinkedDocumentType` varchar(100) NOT NULL,
  `DataOwnershipfield` int NOT NULL,
  `DataOwnershipName` varchar(50) NOT NULL,
  `StatusRemarks` varchar(100) NOT NULL,
  `ProjectCode` varchar(100) NOT NULL,
  `CustomerName` varchar(100) NOT NULL,
  `ClosingDate` varchar(100) NOT NULL,
  `ClosingType` varchar(100) NOT NULL,
  `OpportunityType` varchar(100) NOT NULL,
  `UpdateDate` varchar(50) NOT NULL,
  `UpdateTime` varchar(50) NOT NULL,
  `U_LEADID` int NOT NULL,
  `U_LEADNM` varchar(150) NOT NULL,
  `U_TYPE` varchar(100) NOT NULL,
  `U_LSOURCE` varchar(100) NOT NULL,
  `U_FAV` varchar(100) NOT NULL,
  `U_PROBLTY` varchar(100) NOT NULL,
  `DivCode` varchar(50) NOT NULL,
  `DivName` varchar(50) NOT NULL,
  `OppType` varchar(20) NOT NULL,
  `BPStatus` varchar(2) NOT NULL,
  `QTStatus` varchar(2) NOT NULL,
  `TDStatus` varchar(2) NOT NULL,
  `ODStatus` varchar(2) NOT NULL,
  `OPStatus` varchar(100) NOT NULL,
  `SolutionType` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Opportunity_opportunity`
--

INSERT INTO `Opportunity_opportunity` (`id`, `SequentialNo`, `CardCode`, `SalesPerson`, `SalesPersonName`, `ContactPerson`, `ContactPersonName`, `Source`, `StartDate`, `PredictedClosingDate`, `MaxLocalTotal`, `MaxSystemTotal`, `Remarks`, `Status`, `ReasonForClosing`, `TotalAmountLocal`, `TotalAmounSystem`, `CurrentStageNo`, `CurrentStageNumber`, `CurrentStageName`, `OpportunityName`, `Industry`, `LinkedDocumentType`, `DataOwnershipfield`, `DataOwnershipName`, `StatusRemarks`, `ProjectCode`, `CustomerName`, `ClosingDate`, `ClosingType`, `OpportunityType`, `UpdateDate`, `UpdateTime`, `U_LEADID`, `U_LEADNM`, `U_TYPE`, `U_LSOURCE`, `U_FAV`, `U_PROBLTY`, `DivCode`, `DivName`, `OppType`, `BPStatus`, `QTStatus`, `TDStatus`, `ODStatus`, `OPStatus`, `SolutionType`) VALUES
(1, '1', 'CS00005', '89', 'Rahul', '5', 'Rahul', '', '2022-09-28', '2022-09-28', '', '0.7576', 'Testing', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Tester Opportunity', 'None', 'None', 89, 'Rahul', '', '', 'Wepro', '2022-09-28', 'sos_Days', 'boOpSales', '2022-09-30', '1:20:51 PM', 34, 'test asdf', 'Lead', 'Self', 'N', '', '', '', '', '1', '', '', '', 'Won', 'CAPEX'),
(2, '2', 'CS00004', '89', 'Rahul', '4', 'Rahul', '', '2022-09-28', '2022-09-28', '', '0.7576', 'Testing', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Tester Opportunity New', 'None', 'None', 89, 'Rahul', '', '', 'Cinntra', '2022-09-28', 'sos_Days', 'boOpSales', '2022-09-30', '1:21:03 PM', 0, '', 'Lead', 'Self', 'N', '', '', '', '', '1', '1', '', '', 'Won', 'OPEX'),
(3, '3', 'CS00016', '94', 'Sarthak', '17', 'Abhinav Tyagi', '', '2022-10-03', '2022-10-16', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Ajanara Enclave', 'None', 'None', 94, 'Sarthak', '', '17', 'Ajanara Enclave', '2022-10-16', 'sos_Days', 'boOpSales', '2022-10-03', '4:29:20 PM', 35, 'Ajanara Enclave', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Warm', 'CAPEX'),
(4, '4', 'CS00019', '95', 'Anuj', '21', 'Ashok', '', '2022-10-03', '2022-10-16', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Trends', 'None', 'None', 95, 'Anuj', '', '18', 'Trends', '2022-10-16', 'sos_Days', 'boOpSales', '2022-10-06', '12:56:14 PM', 36, 'Trends', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'AMC'),
(5, '5', 'CS00020', '97', 'Laxman', '22', 'Nitin Tyagi', '', '2022-10-06', '2022-10-16', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Haldiram & CO.', 'None', 'None', 97, 'Laxman', '', '20', 'Haldiram & CO.', '2022-10-16', 'sos_Days', 'boOpSales', '2022-10-06', '3:06:41 PM', 38, 'Haldiram & CO.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'CAPEX'),
(6, '6', 'CS00021', '99', 'Madan', '23', 'Chandan Singh', '', '2022-10-07', '2022-10-16', '', '0.7576', 'NA', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Groffers Stove', 'None', 'None', 99, 'Madan', '', '', 'Groffers Stove', '2022-10-16', 'sos_Days', 'boOpSales', '2022-10-07', '6:48:29 PM', 39, 'Groffers Stove', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'CAPEX'),
(7, '7', 'CS00024', '101', 'Santanu', '27', 'Rahul Akarniya', '', '2022-10-10', '2022-10-21', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'IBM COMP LTD', 'None', 'None', 101, 'Santanu', '', '22', 'IBM COMP LTD', '2022-10-21', 'sos_Days', 'boOpSales', '2022-10-10', '5:46:41 PM', 40, 'IBM COMP LTD', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'CAPEX'),
(8, '8', 'CS00025', '101', 'Santanu', '28', 'Bhoopi', '', '2022-10-10', '2022-10-21', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Wipro Consultant', 'None', 'None', 101, 'Santanu', '', '', 'Wipro Infotech', '2022-10-21', 'sos_Days', 'boOpSales', '2022-10-10', '6:47:28 PM', 0, '', 'Lead', 'Self', 'N', '', '', '', '', '1', '', '', '', 'Lost', 'OPEX'),
(9, '9', 'CS00030', '102', 'Rahul', '33', 'Rahul', '', '2022-10-11', '2022-10-11', '', '0.7576', 'Testing', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Tester Opportunity Sunil', 'None', 'None', 102, 'Rahul', '', '', 'NEw bp 2', '2022-10-11', 'sos_Days', 'boOpSales', '2022-10-11', '5:22:12 PM', 0, '', 'Lead', 'Self', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'CAPEX'),
(10, '10', 'CS00033', '1', 'sriram', '36', 'Abhi Tyagi', '', '2022-10-11', '2022-10-21', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Pest Control', 'None', 'None', 1, 'sriram', '', '', 'Jyoti Pest Control', '2022-10-21', 'sos_Days', 'boOpSales', '2022-10-11', '6:24:05 PM', 42, 'Pest Control', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Lost', 'CAPEX'),
(11, '11', 'CS00034', '102', 'Rahul', '38', 'qdfqfasdasdcsadf', '', '2022-10-17', '2022-10-17', '', '0.7576', 'Testing', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Bajaj Finserve', 'None', 'None', 102, 'Rahul', '', '', 'qwdqdqwd', '2022-10-17', 'sos_Days', 'boOpSales', '2022-10-17', '5:30:29 PM', 41, 'Bajaj Finserve', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Lost', 'OPEX'),
(12, '12', 'CS00035', '102', 'Rahul', '42', 'Ankur Tyagi Ji', '', '2022-10-31', '2022-10-31', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'bsjskbxjx', 'None', 'None', 102, 'Rahul', '', '26', 'Dell Logistics', '2022-10-31', 'sos_Days', 'boOpSales', '2022-10-31', '6:16:56 PM', 90, 'bsjskbxjx', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Warm', 'OPEX'),
(13, '13', 'CS00036', '103', 'Akku', '44', 'Suresh Tyagi', '', '2022-11-02', '2022-11-30', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Humdard', 'None', 'None', 103, 'Akku', '', '30', 'Humdard', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-02', '7:06:17 PM', 91, 'Humdard', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'AMC'),
(14, '14', 'CS00037', '106', 'Devansh', '45', 'Sudhir Kumar', '', '2022-11-03', '2022-11-18', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'ITC', 'None', 'None', 106, 'Devansh', '', '31', 'ITC', '2022-11-18', 'sos_Days', 'boOpSales', '2022-11-03', '11:27:39 AM', 92, 'ITC', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Hot', 'CAMC'),
(15, '15', 'CS00039', '107', 'Farooq', '47', 'Sudhir Kumar', '', '2022-11-03', '2022-11-03', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Tester Opportunity', 'None', 'None', 107, 'Farooq', '', '31', 'Apco Water Architecture', '2022-11-03', 'sos_Days', 'boOpSales', '2022-11-03', '12:43:23 PM', 0, '', 'Lead', 'Self', 'N', '', '', '', '', '1', '1', '', '', 'Warm', 'CAPEX'),
(16, '16', 'CS00040', '107', 'Farooq', '48', 'Santanu', '', '2022-11-03', '2022-11-04', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'AGON IT SOLUTION LTD', 'None', 'None', 107, 'Farooq', '', '32', 'AGON IT SOLUTION 1233', '2022-11-04', 'sos_Days', 'boOpSales', '2022-11-03', '1:19:43 PM', 0, '', 'Lead', 'Self', 'N', '', '', '', '', '1', '1', '', '1', 'Warm', 'AMC'),
(19, '19', 'CS00040', '106', 'Devansh', '48', 'Santanu', '', '2022-11-03', '2022-11-03', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'ASDasd2323safs', 'None', 'None', 106, 'Devansh', '', '32', 'AGON IT SOLUTION 1233', '2022-11-03', 'sos_Days', 'boOpSales', '2022-11-03', '2:46:42 PM', 0, '', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Cold', 'CAPEX'),
(20, '20', 'CS00040', '107', 'Farooq', '48', 'Santanu', '', '2022-11-03', '2022-11-03', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'adsfadsf', 'None', 'None', 107, 'Farooq', '', '32', 'AGON IT SOLUTION 1233', '2022-11-03', 'sos_Days', 'boOpSales', '2022-11-03', '2:48:57 PM', 0, '', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Won', 'CAPEX'),
(21, '21', 'CS00043', '107', 'Farooq', '52', 'Ankur', '', '2022-11-04', '2022-11-05', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Shiv Lakhan Textiles 1', 'None', 'None', 107, 'Farooq', '', '34', 'Shiv Lakhan Textiles', '2022-11-05', 'sos_Days', 'boOpSales', '2022-11-04', '2:38:33 PM', 93, 'Shiv Lakhan Textiles', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '', 'Hot', 'CAMC'),
(22, '22', 'CS00044', '107', 'Farooq', '53', 'Srimaan', '', '2022-11-04', '2022-11-30', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Shiv Lakhan Textiles 2', 'None', 'None', 107, 'Farooq', '', '35', 'Textile Contractor Pvt Ltd', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-04', '2:38:18 PM', 93, 'Shiv Lakhan Textiles', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '1', 'Won', 'OPEX'),
(23, '23', 'CS00043', '107', 'Farooq', '52', 'Ankur', '', '2022-11-04', '2022-11-05', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Shiv Lakhan Textiles', 'None', 'None', 107, 'Farooq', '', '34', 'Shiv Lakhan Textiles', '2022-11-05', 'sos_Days', 'boOpSales', '2022-11-04', '3:53:14 PM', 93, 'Shiv Lakhan Textiles', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Won', 'CAMC'),
(24, '24', 'CS00043', '107', 'Farooq', '51', 'Shiv', '', '2022-11-04', '2022-11-30', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Shiv Lakhan Textiles', 'None', 'None', 107, 'Farooq', '', '35', 'Shiv Lakhan Textiles', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-04', '5:46:56 PM', 93, 'Shiv Lakhan Textiles', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Cold', 'AMC'),
(25, '25', 'CS00043', '107', 'Farooq', '51', 'Shiv', '', '2022-11-04', '2022-11-29', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Shiv Lakhan Textiles', 'None', 'None', 107, 'Farooq', '', '34', 'Shiv Lakhan Textiles', '2022-11-29', 'sos_Days', 'boOpSales', '2022-11-04', '5:49:19 PM', 93, 'Shiv Lakhan Textiles', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Lost', 'CAPEX'),
(26, '26', 'CS00047', '106', 'Devansh', '56', 'Lucky Singh', '', '2022-11-07', '2022-11-30', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Lucky Traders', 'None', 'None', 106, 'Devansh', '', '36', 'Lucky Traders', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-07', '3:28:51 PM', 96, 'Lucky Traders', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Cold', 'AMC'),
(27, '27', 'CS00047', '106', 'Devansh', '56', 'Samarth Singh', '', '2022-11-07', '2022-11-25', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Lucky Traders', 'None', 'None', 106, 'Devansh', '', '36', 'Lucky Traders', '2022-11-25', 'sos_Days', 'boOpSales', '2022-11-07', '4:06:36 PM', 96, 'Lucky Traders', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Hot', 'CAPEX'),
(28, '28', 'CS00051', '107', 'Farooq', '62', 'AT', '', '2022-11-14', '2022-11-30', '', '0.7576', '', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Lux Co.', 'None', 'None', 107, 'Farooq', '', '', 'Lux Co.', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-14', '6:43:23 PM', 99, 'Lux Co.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Cold', 'CAPEX'),
(29, '29', 'CS00052', '107', 'Farooq', '63', 'Ankur Sahu', '', '2022-11-15', '2022-11-30', '', '0.7576', 'retyuiojgfh ygfhuilkjbvhjkl nhjklmn', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Ankur Santanu Bros & Co.', 'None', 'None', 107, 'Farooq', '', '48', 'Ankur Santanu Bros & Co.', '2022-11-30', 'sos_Days', 'boOpSales', '2022-11-15', '11:57:59 AM', 100, 'Ankur Santanu Bros & Co.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Cold', 'OPEX'),
(31, '31', 'CS00056', '106', 'Devansh', '70', 'Lucky Singh', '', '2022-11-16', '2022-11-17', '', '0.7576', 'test', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'wgsh', 'None', 'None', 106, 'Devansh', '', '', 'naya company', '2022-11-17', 'sos_Days', 'boOpSales', '2022-11-16', '4:25:48 PM', 98, 'wgsh', 'Lead', 'Lead', 'N', '', '', '', '', '1', '1', '', '1', 'Cold', 'CAPEX'),
(32, '32', 'CS00056', '106', 'Devansh', '70', 'Lucky Singh', '', '2022-11-17', '2022-11-17', '', '0.7576', 'Testing', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Ankur Santanu Bros & Co.', 'None', 'None', 106, 'Devansh', '', '', 'naya company', '2022-11-17', 'sos_Days', 'boOpSales', '2022-11-17', '10:20:50 AM', 100, 'Ankur Santanu Bros & Co.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Cold', 'OPEX'),
(33, '33', 'CS00056', '105', 'Avinash', '70', 'Lucky Singh', '', '2022-11-17', '2022-11-17', '', '', 'asdfafed', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Ankur Santanu Bros & Co.', 'None', 'None', 105, 'Avinash', 'None', '', 'naya company', '2022-11-17', 'sos_Days', 'boOpSales', '21-11-2022', '03:47 pm', 100, 'Ankur Santanu Bros & Co.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Cold', 'CAPEX'),
(36, '36', 'CS00043', '92', 'Santanu', '53', 'Srimaan', '', '2022-11-21', '2022-11-21', '', '0.7576', 'nay adaksjdha dajkd ada', 'sos_Open', 'None', '0.7', '0.0', '1', '1.0', 'Prospecting', 'Naya Oppurtuinty', 'None', 'None', 92, 'Santanu', '', '36', 'Shiv Lakhan Textiles', '2022-11-21', 'sos_Days', 'boOpSales', '2022-11-21', '18:06:10', 100, 'Ankur Santanu Bros & Co.', 'Lead', 'Lead', 'N', '', '', '', '', '1', '', '', '', 'Cold', 'CAPEX');

-- --------------------------------------------------------

--
-- Table structure for table `Opportunity_stage`
--

CREATE TABLE `Opportunity_stage` (
  `id` bigint NOT NULL,
  `SequenceNo` varchar(9) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Stageno` double NOT NULL,
  `ClosingPercentage` varchar(100) NOT NULL,
  `Cancelled` varchar(100) NOT NULL,
  `IsSales` varchar(100) NOT NULL,
  `IsPurchasing` varchar(100) NOT NULL,
  `Comment` varchar(500) NOT NULL,
  `File` varchar(200) NOT NULL,
  `CreateDate` varchar(60) NOT NULL,
  `UpdateDate` varchar(60) NOT NULL,
  `Status` int NOT NULL,
  `Opp_Id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Opportunity_stage`
--

INSERT INTO `Opportunity_stage` (`id`, `SequenceNo`, `Name`, `Stageno`, `ClosingPercentage`, `Cancelled`, `IsSales`, `IsPurchasing`, `Comment`, `File`, `CreateDate`, `UpdateDate`, `Status`, `Opp_Id`) VALUES
(1, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(2, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(3, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(4, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(5, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(6, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(7, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 1),
(8, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '', 0, 1),
(9, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 2),
(10, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 2),
(11, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 2),
(12, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '', 0, 2),
(13, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '2022-09-28', 1, 2),
(14, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '', 0, 2),
(15, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-09-28', '', 0, 2),
(16, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', 'Done', '', '2022-09-28', '2022-09-28', 1, 2),
(17, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 3),
(18, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 3),
(19, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 3),
(20, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-11', 1, 3),
(21, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '', 0, 3),
(22, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '', 0, 3),
(23, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '', 0, 3),
(24, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '', 0, 3),
(25, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(26, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(27, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(28, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(29, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(30, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-03', '2022-10-03', 1, 4),
(31, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', 'vhj', '', '2022-11-18', '2022-11-19', 1, 4),
(32, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-19', '', 0, 4),
(33, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '2022-10-06', 1, 5),
(34, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '2022-10-06', 1, 5),
(35, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '2022-10-06', 1, 5),
(36, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '2022-10-06', 1, 5),
(37, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '2022-10-06', 1, 5),
(38, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '', 0, 5),
(39, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '', 0, 5),
(40, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-06', '', 0, 5),
(41, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(42, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(43, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(44, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(45, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(46, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(47, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '2022-10-07', 1, 6),
(48, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-07', '', 0, 6),
(49, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 7),
(50, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 7),
(51, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 7),
(52, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 7),
(53, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 7),
(54, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '', 0, 7),
(55, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '', 0, 7),
(56, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '', 0, 7),
(57, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 8),
(58, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 8),
(59, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-11', 1, 8),
(60, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 8),
(61, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-10', 1, 8),
(62, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '2022-10-11', 1, 8),
(63, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-10', '', 0, 8),
(64, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', 'Lsot', '', '2022-10-10', '', 0, 8),
(65, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 9),
(66, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 9),
(67, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 9),
(68, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 9),
(69, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 9),
(70, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 9),
(71, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 9),
(72, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 9),
(73, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 10),
(74, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 10),
(75, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 10),
(76, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 10),
(77, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 10),
(78, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '2022-10-11', 1, 10),
(79, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 10),
(80, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-11', '', 0, 10),
(81, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-10-17', 1, 11),
(82, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-11-01', 1, 11),
(83, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-10-27', 1, 11),
(84, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '', 0, 11),
(85, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-10-27', 1, 11),
(86, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '', 0, 11),
(87, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-10-27', 1, 11),
(88, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-17', '2022-10-31', 1, 11),
(89, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '2022-10-31', 1, 12),
(90, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '2022-11-01', 1, 12),
(91, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '2022-11-01', 1, 12),
(92, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '', 0, 12),
(93, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '', 0, 12),
(94, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '', 0, 12),
(95, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '', 0, 12),
(96, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-10-31', '', 0, 12),
(97, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '2022-11-02', 1, 13),
(98, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', 'Completed', '', '2022-11-02', '2022-11-02', 1, 13),
(99, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', 'Stage has been completed', '', '2022-11-02', '2022-11-03', 1, 13),
(100, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '2022-11-03', 1, 13),
(101, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '2022-11-03', 1, 13),
(102, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '2022-11-03', 1, 13),
(103, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '2022-11-03', 1, 13),
(104, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-02', '', 0, 13),
(105, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(106, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(107, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(108, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(109, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(110, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(111, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 14),
(112, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 14),
(113, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 15),
(114, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(115, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(116, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(117, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(118, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(119, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(120, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 15),
(121, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 16),
(122, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', 'rtyhjk', '', '2022-11-03', '', 0, 16),
(123, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(124, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(125, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(126, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(127, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(128, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 16),
(129, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 19),
(130, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(131, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(132, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(133, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(134, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(135, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(136, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 19),
(137, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-03', 1, 20),
(138, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(139, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(140, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(141, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(142, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(143, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '', 0, 20),
(144, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-03', '2022-11-24', 1, 20),
(145, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 21),
(146, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 21),
(147, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 21),
(148, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 21),
(149, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 21),
(150, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 21),
(151, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 21),
(152, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 21),
(153, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 22),
(154, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 22),
(155, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 22),
(156, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 22),
(157, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 22),
(158, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 22),
(159, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-07', 1, 22),
(160, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-07', 1, 22),
(161, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 23),
(162, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(163, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(164, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(165, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(166, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(167, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 23),
(168, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-05', 1, 23),
(169, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 24),
(170, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(171, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(172, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(173, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(174, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(175, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(176, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 24),
(177, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-04', 1, 25),
(178, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '', 0, 25),
(179, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-04', '2022-11-08', 1, 25),
(180, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-08', '', 0, 25),
(181, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-08', '2022-11-08', 1, 25),
(182, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-08', '', 0, 25),
(183, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-08', '2022-11-08', 1, 25),
(184, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-08', '2022-11-08', 1, 25),
(185, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 26),
(186, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(187, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(188, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(189, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(190, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(191, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(192, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 26),
(193, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(194, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(195, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(196, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(197, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 27),
(198, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(199, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '2022-11-07', 1, 27),
(200, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-07', '', 0, 27),
(201, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '2022-11-14', 1, 28),
(202, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(203, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(204, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(205, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(206, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(207, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(208, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-14', '', 0, 28),
(209, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-15', '2022-11-21', 1, 29),
(210, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-21', '', 0, 29),
(211, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(212, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(213, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(214, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(215, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(216, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 29),
(217, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '2022-11-16', 1, 30),
(218, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(219, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(220, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(221, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(222, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(223, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(224, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '', 0, 30),
(225, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '2022-11-16', 1, 31),
(226, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-16', '2022-11-18', 1, 31),
(227, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', 'ewr', '', '2022-11-18', '', 0, 31),
(228, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', 'vhj', '', '', '2022-11-19', 1, 31),
(229, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', 'gjj', '', '', '2022-11-19', 1, 31),
(230, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', 'vbj', '', '', '2022-11-30', 1, 31),
(231, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 31),
(232, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 31),
(233, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '2022-11-17', 1, 32),
(234, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(235, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(236, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(237, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(238, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(239, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(240, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '', 0, 32),
(241, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-17', '2022-11-17', 1, 33),
(242, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', 'test', '', '2022-11-21', '2022-11-23', 1, 33),
(243, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(244, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(245, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(246, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(247, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(248, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-23', '', 0, 33),
(249, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', 't st', '', '17-11-2022', '2022-11-18', 1, 35),
(250, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-18', '18-11-2022', 1, 35),
(251, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-18', '2022-11-18', 1, 35),
(252, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', 'Done yes', '', '2022-11-18', '2022-11-22', 1, 35),
(253, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', 'Pendding', '', '2022-11-22', '2022-11-18', 1, 35),
(254, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '5465', '', '2022-11-18', '2022-11-24', 1, 35),
(255, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-24', '2022-11-18', 1, 35),
(256, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', 'test', '', '2022-11-24', '2022-11-19', 1, 35),
(257, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-21', '2022-11-21', 1, 36),
(258, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', '', '', '2022-11-21', '', 0, 36),
(259, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36),
(260, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36),
(261, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36),
(262, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36),
(263, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36),
(264, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', '', '', '', '', 0, 36);

-- --------------------------------------------------------

--
-- Table structure for table `Opportunity_staticstage`
--

CREATE TABLE `Opportunity_staticstage` (
  `id` bigint NOT NULL,
  `SequenceNo` varchar(9) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Stageno` double NOT NULL,
  `ClosingPercentage` varchar(100) NOT NULL,
  `Cancelled` varchar(100) NOT NULL,
  `IsSales` varchar(100) NOT NULL,
  `IsPurchasing` varchar(100) NOT NULL,
  `UTYPE` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Opportunity_staticstage`
--

INSERT INTO `Opportunity_staticstage` (`id`, `SequenceNo`, `Name`, `Stageno`, `ClosingPercentage`, `Cancelled`, `IsSales`, `IsPurchasing`, `UTYPE`) VALUES
(1, '1', 'Prospecting', 1, '10.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(2, '2', 'Qualifying', 2, '10.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(3, '3', 'Need Analysis', 3, '20.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(4, '4', 'Value Proposition', 4, '30.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(5, '5', 'Evaluating', 5, '50.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(6, '6', 'Quotation', 6, '70.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(7, '7', 'Negotiation', 7, '80.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(8, '8', 'Close', 8, '100.0', 'tNO', 'tYES', 'tYES', 'Lead'),
(9, '1', 'Project', 1, '0.0', 'tNO', 'tYES', 'tYES', 'Project'),
(10, '2', 'Site Survey', 2, '20.0', 'tNO', 'tYES', 'tYES', 'Project'),
(11, '3', 'Requirement Analysis', 3, '40.0', 'tNO', 'tYES', 'tYES', 'Project'),
(12, '4', 'Quotation', 4, '60.0', 'tNO', 'tYES', 'tYES', 'Project'),
(13, '5', 'Negotiation', 5, '80.0', 'tNO', 'tYES', 'tYES', 'Project'),
(14, '6', 'Order', 6, '100.0', 'tNO', 'tYES', 'tYES', 'Project'),
(15, '1', 'Opening', 1, '20.0', 'tNO', 'tYES', 'tYES', 'Tender'),
(16, '2', 'Submission', 2, '40.0', 'tNO', 'tYES', 'tYES', 'Tender'),
(17, '3', 'Technical Opening', 3, '60.0', 'tNO', 'tYES', 'tYES', 'Tender'),
(18, '4', 'Financial Opening', 4, '80.0', 'tNO', 'tYES', 'tYES', 'Tender'),
(19, '5', 'Tender Order', 5, '100.0', 'tNO', 'tYES', 'tYES', 'Tender');

-- --------------------------------------------------------

--
-- Table structure for table `Order_addendumrequest`
--

CREATE TABLE `Order_addendumrequest` (
  `id` bigint NOT NULL,
  `OrderID` varchar(5) NOT NULL,
  `Date` varchar(50) NOT NULL,
  `Time` varchar(50) NOT NULL,
  `Attachments` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Order_addressextension`
--

CREATE TABLE `Order_addressextension` (
  `id` bigint NOT NULL,
  `OrderID` varchar(5) NOT NULL,
  `BillToBuilding` varchar(100) NOT NULL,
  `ShipToState` varchar(100) NOT NULL,
  `BillToCity` varchar(100) NOT NULL,
  `ShipToCountry` varchar(100) NOT NULL,
  `BillToZipCode` varchar(100) NOT NULL,
  `ShipToStreet` varchar(100) NOT NULL,
  `BillToState` varchar(100) NOT NULL,
  `ShipToZipCode` varchar(100) NOT NULL,
  `BillToStreet` varchar(100) NOT NULL,
  `ShipToBuilding` varchar(100) NOT NULL,
  `ShipToCity` varchar(100) NOT NULL,
  `BillToCountry` varchar(100) NOT NULL,
  `U_SCOUNTRY` varchar(100) NOT NULL,
  `U_SSTATE` varchar(100) NOT NULL,
  `U_SHPTYPB` varchar(100) NOT NULL,
  `U_BSTATE` varchar(100) NOT NULL,
  `U_BCOUNTRY` varchar(100) NOT NULL,
  `U_SHPTYPS` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Order_addressextension`
--

INSERT INTO `Order_addressextension` (`id`, `OrderID`, `BillToBuilding`, `ShipToState`, `BillToCity`, `ShipToCountry`, `BillToZipCode`, `ShipToStreet`, `BillToState`, `ShipToZipCode`, `BillToStreet`, `ShipToBuilding`, `ShipToCity`, `BillToCountry`, `U_SCOUNTRY`, `U_SSTATE`, `U_SHPTYPB`, `U_BSTATE`, `U_BCOUNTRY`, `U_SHPTYPS`) VALUES
(1, '1', 'Cinntra', 'JH', 'City', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'City', 'IN', 'India', 'Jharkhand', 'UPS Ground', 'Jharkhand', 'India', 'UPS Ground'),
(2, '2', 'Haldiram & CO.', 'UP', 'Hapur', 'IN', '201301', 'C-119, Sec-59, Hapur', 'UP', '201301', 'C-119, Sec-59, Hapur', 'Haldiram & CO.', 'Hapur', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(3, '3', 'Haldiram & CO.', 'UP', 'Hapur', 'IN', '201301', 'C-119, Sec-59, Hapur', 'UP', '201301', 'C-119, Sec-59, Hapur', 'Haldiram & CO.', 'Hapur', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(4, '4', 'Haldiram & CO.', 'UP', 'Hapur', 'IN', '201301', 'C-119, Sec-59, Hapur', 'UP', '201301', 'C-119, Sec-59, Hapur', 'Haldiram & CO.', 'Hapur', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(5, '5', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(6, '6', 'IBM COMP LTD', 'UP', 'Muradnagar', 'IN', '201206', '192, Basant Pur Saintli, Muradnagar', 'UP', '201206', '192, Basant Pur Saintli, Muradnagar', 'IBM COMP LTD', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(7, '7', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(8, '10', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(9, '11', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(10, '12', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(11, '13', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(12, '14', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(13, '15', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(14, '16', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(15, '17', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(16, '18', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(17, '19', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(18, '20', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(19, '21', 'Humdard', 'UP', 'Ghaziabad', 'IN', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'UP', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'Humdard', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(20, '22', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', ''),
(21, '23', 'Humdard', 'UP', 'Ghaziabad', 'IN', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'UP', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'Humdard', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(22, '24', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', ''),
(23, '25', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(24, '26', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(25, '27', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(26, '28', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(27, '29', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ASDASDASD', 'MH', '110929', 'ASDASDASD', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(28, '30', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ASDASDASD', 'MH', '110929', 'ASDASDASD', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(29, '31', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ASDASDASD', 'MH', '110929', 'ASDASDASD', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(30, '32', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ASDASDASD', 'MH', '110929', 'ASDASDASD', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(31, '33', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ASDASDASD', 'MH', '110929', 'ASDASDASD', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(32, '34', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(33, '35', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(34, '36', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(35, '37', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(36, '38', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(37, '39', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(38, '40', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(39, '41', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(40, '42', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(41, '43', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(42, '44', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'asfasdf asfdasdf adsfasdf asdfasdf', 'MH', '110929', 'asfasdf asfdasdf adsfasdf asdfasdf', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(43, '45', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Rajnagar Extension', 'UP', '201006', 'Rajnagar Extension', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Courier', 'Uttar Pradesh', 'India', 'By Courier'),
(44, '46', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Rajnagar Extension', 'UP', '201006', 'Rajnagar Extension', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(45, '47', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road'),
(46, '48', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(47, '49', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road'),
(48, '50', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', ''),
(49, '51', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'UP', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(50, '52', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road'),
(51, '53', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', ''),
(52, '54', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road'),
(53, '55', 'Shiv Lakhan Office', 'KA', 'Bhubaneswar', 'IN', '265001', 'ewfdsa wqertyuio', 'KA', '265001', 'ewfdsa wqertyuio', 'Shiv Lakhan Office', 'Bhubaneswar', 'IN', 'India', 'Karnataka', '', 'Karnataka', 'India', ''),
(54, '56', 'Shiv Lakhan Office', 'KA', 'Bhubaneswar', 'IN', '265001', 'ewfdsa wqertyuio', 'KA', '265001', 'ewfdsa wqertyuio', 'Shiv Lakhan Office', 'Bhubaneswar', 'IN', 'India', 'Karnataka', '', 'Karnataka', 'India', ''),
(55, '57', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', ''),
(56, '58', 'Shiv Lakhan Office', 'KA', 'Bhubaneswar', 'IN', '265001', 'ewfdsa wqertyuio', 'KA', '265001', 'ewfdsa wqertyuio', 'Shiv Lakhan Office', 'Bhubaneswar', 'IN', 'India', 'Karnataka', '', 'Karnataka', 'India', ''),
(57, '59', 'Shiv Lakhan Office', 'KA', 'Bhubaneswar', 'IN', '265001', 'ewfdsa wqertyuio', 'KA', '265001', 'ewfdsa wqertyuio', 'Shiv Lakhan Office', 'Bhubaneswar', 'IN', 'India', 'Karnataka', '', 'Karnataka', 'India', ''),
(58, '60', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(59, '61', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(60, '62', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(61, '63', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(62, '64', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', ''),
(63, '65', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', ''),
(64, '66', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', ''),
(65, '67', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', ''),
(66, '68', 'ITC', 'UP', 'Ghaziabad', 'IN', '110001', 'test adress', 'UP', '110001', 'test adress', 'ITC', 'Ghaziabad', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', ''),
(67, '69', 'ITC', 'UP', 'Ghaziabad', 'IN', '110001', 'test adress', 'UP', '110001', 'test adress', 'ITC', 'Ghaziabad', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', ''),
(68, '70', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', ''),
(69, '71', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', ''),
(70, '72', 'Lux Co.', 'UP', 'Muradnagar', 'IN', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'UP', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'Lux Co.', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(71, '73', 'Ankur Santanu Bros & Co.', 'OR', 'Bhubaneshwar', 'IN', '201301', 'Shaheed Nagar', 'OR', '201301', 'Shaheed Nagar', 'Ankur Santanu Bros & Co.', 'Bhubaneshwar', 'IN', 'India', 'Odisha', 'By Courier', 'Odisha', 'India', 'By Courier'),
(72, '74', 'Lux Co.', 'UP', 'Muradnagar', 'IN', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'UP', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'Lux Co.', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(73, '75', 'Lux Co.', 'UP', 'Muradnagar', 'IN', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'UP', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'Lux Co.', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(74, '76', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '645654654555555555', 'new adas dasdasd asdas', 'UP', '645654654555555555', 'new adas dasdasd asdas', 'Lucky Traders', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road'),
(75, '77', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '645654654555555555', 'new adas dasdasd asdas', 'UP', '645654654555555555', 'new adas dasdasd asdas', 'Lucky Traders', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road');

-- --------------------------------------------------------

--
-- Table structure for table `Order_custcode`
--

CREATE TABLE `Order_custcode` (
  `id` bigint NOT NULL,
  `cc_prefix` varchar(100) NOT NULL,
  `counter` int NOT NULL,
  `OrderId` int NOT NULL,
  `CustCodeBp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Order_custcode`
--

INSERT INTO `Order_custcode` (`id`, `cc_prefix`, `counter`, `OrderId`, `CustCodeBp`) VALUES
(1, 'ARCH/N', 1, 46, 'CS00039'),
(2, 'ARCH/N', 1, 45, 'CS00039'),
(3, 'CLNT/W', 1, 44, 'CS00043'),
(4, 'CLNT/W', 1, 43, 'CS00043'),
(5, 'CLNT/W', 1, 42, 'CS00043'),
(6, 'CLNT/W', 1, 41, 'CS00043'),
(7, 'CLNT/W', 1, 40, 'CS00043'),
(8, 'CLNT/W', 1, 35, 'CS00043'),
(9, 'CLNT/W', 1, 25, 'CS00043'),
(10, 'CLNT/N', 1, 24, 'CS00040'),
(11, 'FMNC/N', 1, 23, 'CS00036'),
(12, 'FMNC/N', 1, 21, 'CS00036'),
(13, 'CLNT/N', 1, 20, 'CS00035'),
(14, 'CLNT/N', 1, 18, 'CS00035'),
(15, 'CLNT/N', 1, 17, 'CS00035'),
(16, 'CLNT/N', 1, 16, 'CS00035'),
(17, 'CLNT/N', 1, 12, 'CS00035'),
(18, 'CLNT/N', 1, 10, 'CS00033'),
(19, 'CLNT/N', 1, 9, 'CS00033'),
(20, 'CLNT/N', 1, 8, 'CS00033'),
(21, 'CLNT/N', 1, 7, 'CS00033'),
(22, '', 1, 6, 'CS00024'),
(23, '', 1, 5, 'CS00021'),
(24, '', 1, 4, 'CS00020'),
(25, '', 1, 3, 'CS00020'),
(26, '', 1, 2, 'CS00020'),
(27, '', 1, 1, 'CS00005'),
(28, 'CLNT/N', 1, 47, 'CS00047'),
(30, 'CLNT/N', 1, 49, 'CS00047'),
(31, 'CLNT/N', 1, 50, 'CS00047'),
(32, 'CLNT/N', 1, 51, 'CS00037'),
(33, 'CLNT/N', 1, 52, 'CS00047'),
(34, 'CLNT/N', 1, 53, 'CS00040'),
(35, 'CLNT/N', 1, 54, 'CS00047'),
(36, 'CLNT/N', 1, 55, 'CS00046'),
(37, 'CLNT/N', 0, 56, 'CS00046'),
(38, 'CLNT/N', 0, 57, 'CS00047'),
(39, 'CLNT/N', 8, 58, 'CS00046'),
(50, 'CLNT/N', 9, 59, 'CS00046'),
(63, 'CLNT/W', 2, 65, 'CS00043'),
(64, 'CLNT/N', 10, 64, 'CS00040'),
(68, 'CNTR/E', 1, 66, 'CS00044'),
(69, 'CNTR/E', 2, 63, 'CS00044'),
(70, 'CNTR/E', 3, 62, 'CS00044'),
(71, 'CNTR/E', 4, 48, 'CS00044'),
(72, 'CLNT/N', 11, 67, 'CS00047'),
(73, 'ARCH/W', 1, 68, 'CS00048'),
(74, 'ARCH/W', 2, 69, 'CS00048'),
(75, 'CLNT/N', 12, 70, 'CS00047'),
(76, 'CLNT/N', 13, 71, 'CS00050'),
(77, 'CLNT/N', 14, 72, 'CS00051'),
(78, 'ARCH/E', 1, 73, 'CS00052'),
(79, 'CLNT/N', 15, 74, 'CS00051'),
(80, 'CLNT/N', 16, 75, 'CS00051'),
(81, 'KTCL/E', 1, 76, 'CS00056'),
(82, 'KTCL/E', 2, 77, 'CS00056');

-- --------------------------------------------------------

--
-- Table structure for table `Order_documentlines`
--

CREATE TABLE `Order_documentlines` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `OrderID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `TaxCode` varchar(50) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL,
  `At_Capacity` varchar(50) NOT NULL,
  `Ct_Capacity` varchar(50) NOT NULL,
  `Ht_Capacity` varchar(50) NOT NULL,
  `Machine_Body_Material` varchar(500) NOT NULL,
  `Machine_Colour` varchar(100) NOT NULL,
  `Machine_Dimension` varchar(100) NOT NULL,
  `Pro_Capacity` varchar(50) NOT NULL,
  `Sales_Type` varchar(100) NOT NULL,
  `Special_Remark` varchar(500) NOT NULL,
  `Tap_Qty` varchar(50) NOT NULL,
  `Tap_Type` varchar(50) NOT NULL,
  `Type_of_Machine` varchar(100) NOT NULL,
  `UV_Germ` varchar(500) NOT NULL,
  `Tax` double NOT NULL,
  `UomNo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Order_documentlines`
--

INSERT INTO `Order_documentlines` (`id`, `LineNum`, `OrderID`, `Quantity`, `UnitPrice`, `DiscountPercent`, `ItemDescription`, `ItemCode`, `TaxCode`, `U_FGITEM`, `CostingCode2`, `ProjectCode`, `FreeText`, `At_Capacity`, `Ct_Capacity`, `Ht_Capacity`, `Machine_Body_Material`, `Machine_Colour`, `Machine_Dimension`, `Pro_Capacity`, `Sales_Type`, `Special_Remark`, `Tap_Qty`, `Tap_Type`, `Type_of_Machine`, `UV_Germ`, `Tax`, `UomNo`) VALUES
(1, 0, '1', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(2, 0, '2', 15, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(3, 0, '3', 15, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(4, 0, '4', 15, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(5, 0, '5', 10, 150, 5, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(6, 0, '6', 10, 150, 10, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(7, 0, '7', 10, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(8, 0, '10', 10, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(9, 0, '12', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', 'afdsfdsa', 'Capacity', 'Capacity', 'asdfsdf', 'asdfdf', 'dimensasd', 'Capacity', 'asdf', 'asdfadf', '2', '121', 'asdf', 'asdf', 0, '0'),
(10, 0, '16', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(11, 1, '16', 1, 160, 1, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(12, 0, '17', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(13, 1, '17', 1, 160, 1, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(14, 0, '18', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(15, 1, '18', 1, 160, 1, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '0'),
(16, 0, '20', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 2, 'Package'),
(17, 1, '20', 1, 160, 1, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1, 'Package'),
(18, 0, '21', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(19, 0, '23', 1, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(20, 0, '24', 5, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(21, 0, '25', 10, 150, 1, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(22, 0, '35', 10, 150, 1, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(23, 0, '40', 10, 150, 1, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(24, 0, '41', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '2', '', '', '', 0, 'Package'),
(25, 0, '42', 100, 150, 0, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', '', '100', '', '100 Meter cube', '500 Meter Cube', 'DEF', 'Ceramic', 'Stainless Chrome', '1000 Centimeter', '100 Meter Cube', 'GHJ', 'NOTHING', '10', 'ABC', 'XYZ', 'Yes', 10, 'Package'),
(26, 0, '43', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(27, 1, '43', 1, 50000, 2, 'Water Chiller', '', 'IGST12', '', '', '100', '', '1234', '1234', '23145', 'sdsafdsa', 'Blue', '213145', '21345', 'asdsadf', 'asdsad', '2345', '23456', 'dsafd', 'asdfsaf', 0, '674567'),
(28, 0, '44', 100, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(29, 0, '45', 20, 233, 0, 'new time', 'IT0007', 'IGST12', 'IT0007', '', '100', '', '100 Meter cube', '500 Meter Cube', 'DEF', 'Ceramic', 'Stainless Chrome', '1000 Centimeter', '100 Meter Cube', 'GHJ', 'NOTHING', '10', 'ABC', 'XYZ', 'Yes', 0, '200'),
(30, 0, '46', 30, 233, 0, 'new time', 'IT0007', 'IGST12', 'IT0007', '', '100', '', '100 Meter cube', '500 Meter Cube', 'DEF', 'Ceramic', 'Stainless Chrome', '1000 Centimeter', '100 Meter Cube', 'GHJ', 'NOTHING', '10', 'ABC', 'XYZ', 'Yes', 0, '200'),
(31, 0, '47', 5, 50000, 2, 'Water Chillerdfgsdg', '', 'IGST12', '', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '674567'),
(32, 0, '48', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(33, 0, '49', 5, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(34, 0, '50', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(35, 0, '51', 5, 150, 10, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(36, 0, '52', 5, 50000, 2, 'Water Chillerdfgsdg', '', 'IGST12', '', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '674567'),
(37, 1, '52', 5, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(38, 0, '53', 5, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(39, 0, '54', 4, 150, 0, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(40, 0, '55', 2, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(41, 1, '55', 2, 150, 0, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(42, 0, '56', 4, 160, 0, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(43, 0, '57', 100, 160, 0, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(44, 0, '58', 5, 233, 0, 'new time', 'IT0007', 'IGST12', 'IT0007', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 10, '200'),
(45, 0, '59', 4, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(46, 0, '60', 5, 160, 0, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(47, 0, '61', 10, 150, 10, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 10, 'Package'),
(48, 0, '62', 5, 233, 2, 'new time', 'IT0007', 'IGST12', 'IT0007', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 18, '200'),
(49, 0, '63', 5, 233, 2, 'new time', 'IT0007', 'IGST12', 'IT0007', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 10, '200'),
(50, 0, '64', 5, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, ''),
(51, 0, '65', 3, 233, 0, 'new time', 'IT0007', 'IGST12', 'IT0007', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, '200'),
(52, 0, '66', 6, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 3, 'Package'),
(53, 0, '67', 10, 150, 2, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 5, 'Package'),
(54, 0, '68', 7, 160, 3, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 5, 'Package'),
(55, 0, '69', 8, 150, 1, 'Test Item asdf', 'IT0003', 'IGST12', 'IT0003', '', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 4, 'Package'),
(56, 0, '70', 5, 150, 2, 'Test Item', 'IT0001', 'IGST12', 'IT0001', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(57, 0, '71', 1, 150, 0, 'Test Item', 'IT0001', 'IGST12', 'IT0001', '', '100', '', '', '', '', '', '', '', '', 'Lease', '', '', 'Manual', 'UV', '', 0, 'Package'),
(58, 0, '72', 1, 56767, 2, 'Water Ozonator', 'IT0010', 'IGST12', 'IT0010', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 18, 'NOS'),
(59, 0, '73', 6, 56767, 3, 'Water Ozonator', 'IT0010', 'IGST12', 'IT0010', 'DEPT001', '100', 'gh,mmjhgf', '1234', '1232', '1235', 'asfdgh', 'Yellow', '123423', '2354', 'fgh', 'dsgf', '12', '1236', '1234adsfs', 'gdfhg', 15, 'NOS'),
(60, 0, '74', 1, 56767, 2, 'Water Ozonator', 'IT0010', 'IGST12', 'IT0010', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 18, 'NOS'),
(61, 0, '75', 1, 56767, 2, 'Water Ozonator', 'IT0010', 'IGST12', 'IT0010', 'DEPT001', '100', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 18, 'NOS'),
(62, 0, '76', 1, 160, 0, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package'),
(63, 0, '77', 1, 160, 0, 'Test Item 2', 'IT0002', 'IGST12', 'IT0002', '', '101', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 'Package');

-- --------------------------------------------------------

--
-- Table structure for table `Order_order`
--

CREATE TABLE `Order_order` (
  `id` bigint NOT NULL,
  `TaxDate` varchar(30) NOT NULL,
  `DocDueDate` varchar(30) NOT NULL,
  `ContactPersonCode` varchar(5) NOT NULL,
  `DiscountPercent` double NOT NULL,
  `DocDate` varchar(30) NOT NULL,
  `CardCode` varchar(30) NOT NULL,
  `Comments` varchar(150) NOT NULL,
  `SalesPersonCode` varchar(5) NOT NULL,
  `DocumentStatus` varchar(50) NOT NULL,
  `CancelStatus` varchar(50) NOT NULL,
  `DocCurrency` varchar(50) NOT NULL,
  `DocTotal` varchar(50) NOT NULL,
  `CardName` varchar(150) NOT NULL,
  `VatSum` varchar(50) NOT NULL,
  `CreationDate` varchar(50) NOT NULL,
  `DocEntry` varchar(5) NOT NULL,
  `PaymentGroupCode` varchar(5) NOT NULL,
  `U_Term_Condition` longtext NOT NULL,
  `U_TermInterestRate` double NOT NULL,
  `U_TermPaymentTerm` varchar(100) NOT NULL,
  `U_TermDueDate` varchar(100) NOT NULL,
  `U_QUOTNM` varchar(100) NOT NULL,
  `U_QUOTID` int NOT NULL,
  `U_LEADID` int NOT NULL,
  `U_LEADNM` varchar(150) NOT NULL,
  `U_OPPID` varchar(5) NOT NULL,
  `U_OPPRNM` varchar(100) NOT NULL,
  `BPLID` varchar(5) NOT NULL,
  `DelStatus` varchar(50) NOT NULL,
  `CreateDate` varchar(30) NOT NULL,
  `CreateTime` varchar(30) NOT NULL,
  `UpdateDate` varchar(30) NOT NULL,
  `UpdateTime` varchar(30) NOT NULL,
  `Attach` varchar(250) NOT NULL,
  `DatePO` varchar(150) NOT NULL,
  `OrdNo` varchar(50) NOT NULL,
  `PoNo` varchar(50) NOT NULL,
  `Project` varchar(50) NOT NULL,
  `GSTNo` varchar(100) NOT NULL,
  `GroupType` varchar(100) NOT NULL,
  `OPSNumber` varchar(100) NOT NULL,
  `OtherInstruction` varchar(100) NOT NULL,
  `POAmount` varchar(100) NOT NULL,
  `ProjectLocation` varchar(100) NOT NULL,
  `UrlNo` varchar(100) NOT NULL,
  `CivWork` varchar(100) NOT NULL,
  `Intall` varchar(100) NOT NULL,
  `LOCharges` varchar(100) NOT NULL,
  `MICharges` varchar(100) NOT NULL,
  `PlumStatus` varchar(100) NOT NULL,
  `SSStatus` varchar(100) NOT NULL,
  `addendum` varchar(20) NOT NULL,
  `approved_drawing` varchar(20) NOT NULL,
  `special_instructions` varchar(20) NOT NULL,
  `technical_details` varchar(20) NOT NULL,
  `URN` varchar(20) NOT NULL,
  `NetTotal` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Order_order`
--

INSERT INTO `Order_order` (`id`, `TaxDate`, `DocDueDate`, `ContactPersonCode`, `DiscountPercent`, `DocDate`, `CardCode`, `Comments`, `SalesPersonCode`, `DocumentStatus`, `CancelStatus`, `DocCurrency`, `DocTotal`, `CardName`, `VatSum`, `CreationDate`, `DocEntry`, `PaymentGroupCode`, `U_Term_Condition`, `U_TermInterestRate`, `U_TermPaymentTerm`, `U_TermDueDate`, `U_QUOTNM`, `U_QUOTID`, `U_LEADID`, `U_LEADNM`, `U_OPPID`, `U_OPPRNM`, `BPLID`, `DelStatus`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `Attach`, `DatePO`, `OrdNo`, `PoNo`, `Project`, `GSTNo`, `GroupType`, `OPSNumber`, `OtherInstruction`, `POAmount`, `ProjectLocation`, `UrlNo`, `CivWork`, `Intall`, `LOCharges`, `MICharges`, `PlumStatus`, `SSStatus`, `addendum`, `approved_drawing`, `special_instructions`, `technical_details`, `URN`, `NetTotal`) VALUES
(74, '2022-11-21', '2022-11-21', '62', 10, '', 'CS00051', 'Testing', '107', 'bost_Open', 'csNo', '', '56767.0', 'Lux Co.', '', '', '74', '2', 'Terms', 0, '2', '', 'Lux Co.', 78, 0, '', '28', 'Lux Co.', '', '', '2022-11-21', '7:02:38 PM', '2022-11-21', '7:02:38 PM', '', '2022-11-21', 'ORD00074', '89898989', '', '37AADCS0472N1Z1', 'Client', '', 'Instruction', '0', 'Delhi', '', 'Done', '200', '300', '100', 'Done', 'Yes', 'No', 'No', 'No', 'No', 'CLNT/N/URN10015', '59681'),
(75, '2022-11-21', '2022-11-21', '62', 10, '', 'CS00051', 'Des', '107', 'bost_Open', 'csNo', '', '56767.0', 'Lux Co.', '', '', '75', '2', 'Terms', 0, '2', '', 'Lux Co.', 78, 0, '', '28', 'Lux Co.', '', '', '2022-11-21', '7:12:24 PM', '2022-11-21', '7:12:24 PM', '', '2022-11-21', 'ORD00075', '1000000000000', '', '37AADCS0472N1Z1', 'Client', '', 'Other', '0', 'Delhi', '', 'Done', '200', '300', '100', 'Done', 'Yes', 'No', 'No', 'No', 'No', 'CLNT/N/URN10016', '59681'),
(76, '2022-11-21', '2022-11-21', '70', 0, '', 'CS00056', 'fsdzs', '106', 'bost_Open', 'csNo', '', '160.0', 'naya company', '', '', '76', '4', 'asdf', 0, '4', '', 'naya company', 81, 0, '', '31', 'wgsh', '', '', '2022-11-21', '7:19:57 PM', '2022-11-21', '7:19:57 PM', '', '2022-11-21', 'ORD00076', '123', '', '32456', 'Kitchen Consultant', '', 'asdf', '0', 'Delhi', '', 'Done', '0', '0', '0', 'Done', 'Yes', 'No', 'No', 'No', 'No', 'KTCL/E/URN10001', '160'),
(77, '2022-11-22', '2022-11-22', '70', 0, '', 'CS00056', 'fsdzs', '106', 'bost_Open', 'csNo', '', '160.0', 'naya company', '', '', '77', '4', 'asdf', 0, '4', '', 'naya company', 82, 0, '', '', '', '', '', '2022-11-22', '10:53:49 AM', '2022-11-22', '10:53:49 AM', '', '2022-11-22', 'ORD00077', '12341', '', '37AADCS0472N1Z1', 'Kitchen Consultant', '', 'adf', '0', 'Delhi', '', 'Done', '0', '0', '0', 'Done', 'Yes', 'No', 'No', 'No', 'No', 'KTCL/E/URN10002', '160');

-- --------------------------------------------------------

--
-- Table structure for table `PaymentTermsTypes_paymenttermstypes`
--

CREATE TABLE `PaymentTermsTypes_paymenttermstypes` (
  `id` bigint NOT NULL,
  `GroupNumber` varchar(3) NOT NULL,
  `PaymentTermsGroupName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PaymentTermsTypes_paymenttermstypes`
--

INSERT INTO `PaymentTermsTypes_paymenttermstypes` (`id`, `GroupNumber`, `PaymentTermsGroupName`) VALUES
(1, '-1', '- Cash Basic -'),
(2, '1', 'Net-30'),
(3, '2', '45 Days After Invoice Submission'),
(4, '4', '50% Advance & 50% Post Delivery');

-- --------------------------------------------------------

--
-- Table structure for table `Project_project`
--

CREATE TABLE `Project_project` (
  `id` bigint NOT NULL,
  `name` varchar(250) NOT NULL,
  `contact_person` varchar(250) NOT NULL,
  `start_date` varchar(50) NOT NULL,
  `details` varchar(1000) NOT NULL,
  `CardCode` varchar(100) NOT NULL,
  `sector` varchar(250) NOT NULL,
  `type` varchar(50) NOT NULL,
  `location` varchar(250) NOT NULL,
  `project_owner` varchar(250) NOT NULL,
  `completion_date` varchar(50) NOT NULL,
  `target_date` varchar(50) NOT NULL,
  `project_cost` varchar(250) NOT NULL,
  `project_status` varchar(50) NOT NULL,
  `address` varchar(500) NOT NULL,
  `customer_group_type` varchar(250) NOT NULL,
  `kit_consultant_code` varchar(250) NOT NULL,
  `kit_consultant_name` varchar(250) NOT NULL,
  `mep_consultant_code` varchar(250) NOT NULL,
  `mep_consultant_name` varchar(250) NOT NULL,
  `pm_consultant_code` varchar(250) NOT NULL,
  `pm_consultant_name` varchar(250) NOT NULL,
  `CreatedDate` varchar(50) NOT NULL,
  `CreatedTime` varchar(50) NOT NULL,
  `kit_contact_person` varchar(250) NOT NULL,
  `mep_contact_person` varchar(250) NOT NULL,
  `pm_contact_person` varchar(250) NOT NULL,
  `GroupType` varchar(100) NOT NULL,
  `arch_consultant_code` varchar(250) NOT NULL,
  `arch_consultant_name` varchar(250) NOT NULL,
  `arch_contact_person` varchar(250) NOT NULL,
  `cli_consultant_code` varchar(250) NOT NULL,
  `cli_consultant_name` varchar(250) NOT NULL,
  `cli_contact_person` varchar(250) NOT NULL,
  `contr_consultant_code` varchar(250) NOT NULL,
  `contr_consultant_name` varchar(250) NOT NULL,
  `contr_contact_person` varchar(250) NOT NULL,
  `fcm_consultant_code` varchar(250) NOT NULL,
  `fcm_consultant_name` varchar(250) NOT NULL,
  `fcm_contact_person` varchar(250) NOT NULL,
  `oth_consultant_code` varchar(250) NOT NULL,
  `oth_consultant_name` varchar(250) NOT NULL,
  `oth_contact_person` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Project_project`
--

INSERT INTO `Project_project` (`id`, `name`, `contact_person`, `start_date`, `details`, `CardCode`, `sector`, `type`, `location`, `project_owner`, `completion_date`, `target_date`, `project_cost`, `project_status`, `address`, `customer_group_type`, `kit_consultant_code`, `kit_consultant_name`, `mep_consultant_code`, `mep_consultant_name`, `pm_consultant_code`, `pm_consultant_name`, `CreatedDate`, `CreatedTime`, `kit_contact_person`, `mep_contact_person`, `pm_contact_person`, `GroupType`, `arch_consultant_code`, `arch_consultant_name`, `arch_contact_person`, `cli_consultant_code`, `cli_consultant_name`, `cli_contact_person`, `contr_consultant_code`, `contr_consultant_name`, `contr_contact_person`, `fcm_consultant_code`, `fcm_consultant_name`, `fcm_contact_person`, `oth_consultant_code`, `oth_consultant_name`, `oth_contact_person`) VALUES
(12, 'New Project', '4', '2022-09-30', 'Detials', 'CS00004', 'PPP', 'Urban', 'Delhi', 'Rahul', '2022-09-30', '2022-09-30', '1223', 'Planing', 'Karol bagh Delhi', '', 'CS00012', 'Testing Bp', 'CS00005', 'Wepro', 'CS00013', 'IBM', '2022-09-30', '4:12:29 PM', '15', '5', '13', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(13, 'Bridge Project', '4', '2022-09-30', 'Details', 'CS00004', 'PPP', 'Transport', 'Delhi', 'Rahul', '2022-09-30', '2022-09-30', '10000', 'Under Construction', 'Karol bagh', '', 'CS00012', 'Testing Bp', 'CS00005', 'Wepro', 'CS00013', 'IBM', '2022-09-30', '6:18:50 PM', '15', '5', '13', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(14, 'Pedlar', '4', '2022-09-30', 'the quick brown fox jumps right over the lazy little dong', 'CS00004', 'Private', 'Urban', 'Delhi', 'Rahul', '2022-09-30', '2022-09-30', '10000', 'Under Construction', 'E-138, Noida sec - 63, U.P.', '', 'CS00014', 'Testing kithen', 'CS00005', 'Wepro', 'CS00013', 'IBM', '2022-09-30', '6:27:42 PM', '14', '5', '13', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(15, 'Water Planter', '16', '2022-10-01', 'Work needs to be complete before date.', 'CS00015', 'Private', 'Office Building', 'Noida', 'Bhoopi', '2022-10-15', '2022-10-10', '1000000', 'Under Construction', 'E-138, Sec-63, Noida.', '', '', '', '', '', 'CS00013', 'IBM', '2022-10-03', '2:47:55 PM', '', '', '13', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(16, 'Water Softner', '17', '2022-10-03', '', 'CS00016', 'Private', 'Office Building', 'Noida', 'Bhoopi', '2022-10-16', '2022-10-10', '100000', 'Designing', '', '', 'CS00016', 'Ajanara Enclave', '', '', '', '', '2022-10-03', '3:20:16 PM', '17', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(17, 'Water treatment', '17', '2022-10-04', '', 'CS00016', 'Government', 'Commercial Complex', 'Ghaziabad', 'Rahul', '2022-10-16', '2022-10-13', '10000000', 'Under Construction', '', '', 'CS00016', 'Ajanara Enclave', '', '', '', '', '2022-10-03', '3:52:11 PM', '17', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(18, 'Water Plant', '21', '2022-10-04', '', 'CS00019', 'Private', 'Public Place', 'Modinagar', 'Laxman', '2022-10-14', '2022-10-10', '', 'Under Construction', '', '', '', '', '', '', 'CS00019', 'Trends', '2022-10-03', '5:22:39 PM', '', '', '21', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 'Water Plant Softner', '21', '2022-10-05', '', 'CS00019', 'Private', 'Institutional', 'Modinagar', 'Hardik', '2022-10-16', '2022-10-12', '1000000', 'Designing', '', '', '', '', '', '', 'CS00019', 'Trends', '2022-10-03', '5:22:39 PM', '', '', '21', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 'Water treatment', '22', '2022-10-07', '', 'CS00020', 'Private', 'Office Building', 'Hapur', 'Ankur Tyagi', '2022-10-16', '2022-10-14', '100000', 'Under Construction', '', '', 'CS00020', 'Haldiram & CO.', '', '', '', '', '2022-10-06', '2:56:10 PM', '22', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 'New Project', '24', '2022-10-10', 'Details', 'CS00022', 'Government', 'Institutional', 'Delhi', 'Rahul', '2022-10-10', '2022-10-10', '1223', 'Designing', 'Testing Address', '', 'CS00021', 'Groffers Stove', 'CS00005', 'Wepro', 'CS00019', 'Trends', '2022-10-10', '12:12:01 PM', '23', '5', '21', 'Contractor', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(22, 'Ozonator', '27', '2022-10-11', '', 'CS00024', 'Private', 'Office Building', 'Noida', 'Bhoopi', '2022-10-21', '2022-10-18', '100000', 'Under Construction', '', '', '', '', '', '', 'CS00024', 'IBM COMP LTD', '2022-10-10', '5:31:36 PM', '', '', '', 'Project Management Consultant', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(23, 'Google Noida Office', '29', '2022-10-11', '', 'CS00026', '', 'Office Building', 'Noida', 'Santanu', '2022-11-30', '2022-10-31', '20,00000', 'Planing', '', '', 'CS00020', 'Haldiram & CO.', 'CS00025', 'Lagero Infotech', 'CS00019', 'Trends', '2022-10-11', '11:30:14 AM', '22', '28', '21', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(24, 'New Project 2', '24', '2022-10-11', 'Detials', 'CS00022', 'Government', 'Metro/Rail', 'Delhi', 'Rahul', '2022-10-11', '2022-10-11', '1223', 'Planing', 'Testing Address', '', 'CS00020', 'Haldiram & CO.', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-10-11', '4:24:02 PM', '22', '28', '27', 'Client', 'CS00029', 'New BP', '32', 'CS00026', 'Google Inc.', '29', 'CS00028', 'Dell', '31', 'CS00031', 'New bp 3', '34', '', '', ''),
(25, 'Head Ofiice', '36', '', 'NA', 'CS00033', 'Private', 'Office Building', 'Noida', 'Santanu', '2022-10-12', '2022-10-11', '20,00000', 'Under Construction', 'NA', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-10-11', '6:19:37 PM', '23', '28', '27', 'Client', 'CS00030', 'NEw bp 2', '33', '', '', '', 'CS00027', 'FIncorp. Arch', '30', 'CS00031', 'New bp 3', '34', 'CS00029', 'New BP', '32'),
(26, 'IT Office', '', '', '', 'CS00035', 'Private', '', 'Delhi', '', '', '', '', '', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-10-12', '10:52:19 AM', '23', '28', '27', 'Client', 'CS00030', 'NEw bp 2', '33', 'CS00035', '', '42', 'CS00027', 'Dell', '30', 'CS00031', 'New bp 3', '34', 'CS00029', 'New BP', '32'),
(27, 'New Project Now', '', '2022-11-01', 'Details', 'CS00035', 'Government', 'Institutional', 'Delhi', 'Rahul', '2022-11-01', '2022-11-01', '', 'Designing', 'Address', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00019', 'Trends', '2022-11-01', '7:31:17 PM', '23', '28', '21', 'Contractor', 'CS00030', 'NEw bp 2', '33', 'CS00033', 'Jyoti Pest Control', '41', 'CS00034', 'qwdqdqwd', '37', 'CS00031', 'New bp 3', '34', 'CS00029', 'New BP', '32'),
(28, 'New Project', '42', '2022-11-02', 'Detials', 'CS00035', 'Government', 'Institutional', 'Delhi', 'Rahul', '2022-11-02', '2022-11-02', '1223', 'Designing', 'New Delhi', '', 'CS00021', 'Groffers Stove', 'CS00005', 'Wepro', 'CS00024', 'IBM COMP LTD', '2022-11-02', '11:30:30 AM', '23', '5', '27', 'Client', 'CS00030', 'NEw bp 2', '33', 'CS00035', 'Dell Logistics', '42', 'CS00032', 'asdf', '35', 'CS00031', 'New bp 3', '34', 'CS00029', 'New BP', '32'),
(29, 'New Project 44554', '42', '', '', 'CS00035', 'Government', '', '', '', '', '', '', '', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00019', 'Trends', '2022-11-02', '11:33:07 AM', '23', '28', '21', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(30, 'Water Treatment Plant', '44', '2022-11-04', '', 'CS00036', 'Private', 'Office Building', 'Ghaziabad', 'Humdard', '2022-11-30', '2022-11-25', '100000', 'Planing', 'No.5, Rajnagar Extension, Near Guldhar Station Road, Ghaziabad, Uttar Pradesh', '', '', '', '', '', '', '', '2022-11-02', '6:48:25 PM', '', '', '', 'Facility Management', '', '', '', '', '', '', '', '', '', 'CS00036', 'Humdard', '44', '', '', ''),
(31, 'Water Plant Project', '45', '2022-11-04', '', 'CS00037', 'Private', 'Office Building', 'Ghaziabad', 'ITC', '2022-11-20', '2022-11-18', '100000', 'Under Construction', '', '', '', '', '', '', '', '', '2022-11-03', '11:16:09 AM', '', '', '', 'Client', 'CS00039', 'Apco Water Architecture', '47', '', 'ITC', '', 'CS00038', 'Loco Treatment', '46', 'CS00036', 'Humdard', '44', '', '', ''),
(32, 'Twin Tower TREATMENT CENTRE', '', '', '', 'CS00038', '', '', '', '', '', '', '', '', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-11-03', '12:49:33 PM', '23', '28', '27', 'Contractor', '', '', '', 'CS00040', 'AGON IT SOLUTION 1233', '48', '', '', '', '', '', '', '', '', ''),
(33, 'Callnew', '', '', '', 'CS00040', '', '', '', '', '', '', '', '', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00041', 'adgfg', '2022-11-03', '6:10:17 PM', '23', '28', '49', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(34, 'Handlooms Building', '52', '2022-11-04', 'NB Towers, Plot No-426/2260, Ground, Nilakantha Nagar, Nayapalli, Bhubaneswar, Odisha 751012', 'CS00043', 'Private', 'Office Building', 'Bhubaneswar', 'Shiv Lakhan Textiles', '2022-12-10', '2022-11-30', '15,000Cr', 'Under Construction', 'NB Towers, Plot No-426/2260, Ground, Nilakantha Nagar, Nayapalli, Bhubaneswar, Odisha 751012', '', 'CS00020', 'Haldiram & CO.', 'CS00025', 'Lagero Infotech', 'CS00013', 'IBM', '2022-11-04', '1:09:06 PM', '22', '28', '13', 'Client', 'CS00039', 'Apco Water Architecture', '47', 'CS00043', 'Shiv Lakhan Textiles', '52', 'CS00038', 'Loco Treatment', '46', 'CS00036', 'Humdard', '44', 'CS00029', 'New BP', '32'),
(35, 'Modern Textiles', '', '', '', 'CS00043', 'Private', '', '', 'Shiv Lakhan Textiles', '', '', '', '', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00013', 'IBM', '2022-11-04', '1:22:10 PM', '23', '28', '13', 'Client', '', '', '', 'CS00043', 'Shiv Lakhan Textiles', '52', 'CS00044', 'Textile Contractor Pvt Ltd', '53', '', '', '', '', '', ''),
(36, 'L. Traders', '56', '2022-11-11', '', 'CS00047', 'Private', 'Office Building', 'Muradnagar', 'Lucky Traders', '2022-11-30', '2022-11-14', '1000000', 'Planing', '', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-11-07', '3:24:52 PM', '23', '28', '27', 'Client', 'CS00039', 'Apco Water Architecture', '47', 'CS00047', 'Lucky Traders', '56', 'CS00044', 'Textile Contractor Pvt Ltd', '53', 'CS00036', 'Humdard', '44', 'CS00029', 'New BP', '32'),
(37, 'cinnntra testing', '59', '2022-11-11', 'testing', 'CS00048', 'Government', 'Metro/Rail', 'Delhi', 'Groffers Stove', '2022-11-11', '2022-11-11', '00', 'Designing', 'test', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00041', 'adgfg', '2022-11-11', '3:19:33 PM', '23', '28', '49', 'Client', 'CS00039', 'Apco Water Architecture', '47', 'CS00049', 'eqasdfdasf', '60', 'CS00038', 'Loco Treatment', '46', 'CS00036', 'Humdard', '44', 'CS00029', 'New BP', '32'),
(38, 'Testing Android', '61', '2022-11-14', 'Android testing', 'CS00050', 'Government', 'Institutional', 'Noida', 'NEw com', '2022-11-25', '2022-11-15', '', 'Completed', 'testing', '', 'CS00021', 'Groffers Stove', '', '', '', '', '2022-11-14', '12:19:30 PM', '23', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(39, 'sdsd', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2022-11-14', '12:25:44 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(40, 'hkugyjgfhdfsdgzf', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', 'huk', '', '', '', '', '', '', '', '2022-11-14', '2:32:52 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(41, 'ljkhlkgh', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2022-11-14', '2:33:25 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(42, 'gdfsd', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2022-11-14', '2:48:22 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(43, 'sadfdgf', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2022-11-14', '2:48:52 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(44, 'jhuiy', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '2022-11-14', '2:50:12 PM', '', '', '', 'Client', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(45, 'vsvs', '61', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', 'Client', '', '', '', '', '', '', '14-11-2022', '04:03 pm', '-1', '-1', '-1', 'Client', '', '', '-1', '', '', '-1', '', '', '-1', '', '', '-1', '', '', '-1'),
(46, 'Ashutosh', '53', '2022-11-14', 'sdfsdfsfsdfs', 'CS00044', 'Government', 'Institutional', 'Patna', 'Haldiram & CO.', '2022-11-16', '2022-11-15', '43', 'Planing', 'zdvsdfds', '', 'CS00020', 'Haldiram & CO.', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-11-14', '16:19:34', '22', '28', '27', 'Kitchen Consultant', 'CS00039', 'Apco Water Architecture', '47', 'CS00047', 'Lucky Traders', '56', 'CS00038', 'Loco Treatment', '46', 'CS00036', 'Humdard', '44', 'CS00029', 'New BP', '32'),
(47, '', '', '', '', 'CS00050', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''),
(48, 'Grand Factory', '63', '2022-11-16', '1. ASFSDFSDF\r\n2. WFSDSDFDFSGFG\r\n3. 253ZXCDFSDF\r\n4. SDSDFGFSDFSGF', 'CS00052', 'Private', 'Commercial Complex', 'Gudari', 'Ankur Santanu Bros & Co.', '2022-11-19', '2022-11-17', '', 'Designing', 'Patia Square', '', 'CS00021', 'Groffers Stove', 'CS00025', 'Lagero Infotech', 'CS00024', 'IBM COMP LTD', '2022-11-15', '11:25:30 AM', '23', '28', '27', 'Architect', 'CS00052', 'Ankur Santanu Bros & Co.', '64', 'CS00015', 'Ajanara Heights', '16', 'CS00027', 'FIncorp. Arch', '30', 'CS00036', 'Humdard', '44', 'CS00029', 'New BP', '32'),
(49, 'It Interesting ', '', '15-12-2022', '', 'CS00055', 'PSU', '', '', '', '15-11-2022', '15-11-2022', '', '', 'Testing for sure and then the ', '', '', 'Testing kithen', '', 'Wepro', '', 'IBM COMP LTD', '', '', '', 'Wepro', '', '', 'Apco Water Architecture', 'Apco Water Architecture', '', '', 'AGON IT SOLUTION 1233', '', 'Textile Contractor Pvt Ltd', 'Textile Contractor Pvt Ltd', '', '', 'New bp 3', '', 'New Era was the last ', 'New Era was the last ', '');

-- --------------------------------------------------------

--
-- Table structure for table `Quotation_addressextension`
--

CREATE TABLE `Quotation_addressextension` (
  `id` bigint NOT NULL,
  `QuotationID` varchar(5) NOT NULL,
  `BillToBuilding` varchar(100) NOT NULL,
  `ShipToState` varchar(100) NOT NULL,
  `BillToCity` varchar(100) NOT NULL,
  `ShipToCountry` varchar(100) NOT NULL,
  `BillToZipCode` varchar(100) NOT NULL,
  `ShipToStreet` varchar(100) NOT NULL,
  `BillToState` varchar(100) NOT NULL,
  `ShipToZipCode` varchar(100) NOT NULL,
  `BillToStreet` varchar(100) NOT NULL,
  `ShipToBuilding` varchar(100) NOT NULL,
  `ShipToCity` varchar(100) NOT NULL,
  `BillToCountry` varchar(100) NOT NULL,
  `U_SCOUNTRY` varchar(100) NOT NULL,
  `U_SSTATE` varchar(100) NOT NULL,
  `U_SHPTYPB` varchar(100) NOT NULL,
  `U_BSTATE` varchar(100) NOT NULL,
  `U_BCOUNTRY` varchar(100) NOT NULL,
  `U_SHPTYPS` varchar(100) NOT NULL,
  `BillToRemark` varchar(255) NOT NULL,
  `ShipToRemark` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Quotation_addressextension`
--

INSERT INTO `Quotation_addressextension` (`id`, `QuotationID`, `BillToBuilding`, `ShipToState`, `BillToCity`, `ShipToCountry`, `BillToZipCode`, `ShipToStreet`, `BillToState`, `ShipToZipCode`, `BillToStreet`, `ShipToBuilding`, `ShipToCity`, `BillToCountry`, `U_SCOUNTRY`, `U_SSTATE`, `U_SHPTYPB`, `U_BSTATE`, `U_BCOUNTRY`, `U_SHPTYPS`, `BillToRemark`, `ShipToRemark`) VALUES
(1, '1', 'Cinntra', 'JH', 'City', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'City', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(2, '2', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', 'Testing Remark', 'Testing Remark'),
(3, '3', 'Cinntra', 'JH', 'City', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'City', 'IN', 'India', 'Jharkhand', 'UPS Ground', 'Jharkhand', 'India', 'UPS Red', 'Remarks Test', 'Remarks Test'),
(4, '4', 'Ajanara Enclave', 'PB', 'Hoshiarpur', 'IN', '201301', 'Nana House, Ajanara Enclave, Hoshiarpur', 'PB', '201301', 'Nana House, Ajanara Enclave, Hoshiarpur', 'Ajanara Enclave', 'Hoshiarpur', 'IN', 'India', 'Punjab', 'By Courier', 'Punjab', 'India', 'By Courier', '', ''),
(5, '5', 'Trends', 'UP', 'Modinagar', 'IN', '201206', 'Patel Nagar, Modinagar', 'UP', '201206', 'Patel Nagar, Modinagar', 'Trends', 'Modinagar', 'IN', 'India', 'Uttar Pradesh', 'Motor Express', 'Uttar Pradesh', 'India', 'Motor Express', '', ''),
(6, '6', 'Trends', 'UP', 'Modinagar', 'IN', '201206', 'Patel Nagar, Modinagar', 'UP', '201206', 'Patel Nagar, Modinagar', 'Trends', 'Modinagar', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(7, '7', 'Haldiram & CO.', 'UP', 'Hapur', 'IN', '201301', 'C-119, Sec-59, Hapur', 'UP', '201301', 'C-119, Sec-59, Hapur', 'Haldiram & CO.', 'Hapur', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(8, '8', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(9, '9', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', 'Testing', 'Testing'),
(15, '15', 'IBM COMP LTD', 'UP', 'Muradnagar', 'IN', '201206', '192, Basant Pur Saintli, Muradnagar', 'UP', '201206', '192, Basant Pur Saintli, Muradnagar', 'IBM COMP LTD', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(16, '16', 'IBM COMP LTD', 'UP', 'Muradnagar', 'IN', '201206', '192, Basant Pur Saintli, Muradnagar', 'UP', '201206', '192, Basant Pur Saintli, Muradnagar', 'IBM COMP LTD', 'Muradnagar', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(17, '17', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(18, '18', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(19, '19', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(20, '20', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(21, '21', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(22, '22', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(23, '23', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(24, '24', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(25, '25', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(26, '26', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(27, '27', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(28, '28', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(29, '29', 'MASSAED India Pvt Ltd', 'TG', 'Santanu Sahu', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Santanu Sahu', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(30, '30', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(31, '31', 'Jyoti Pest Control', 'UP', 'Ghaziabad', 'IN', '201001', 'C-121, RDC, Ghaziabad', 'UP', '201001', 'C-121, RDC, Ghaziabad', 'Jyoti Pest Control', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road', '', ''),
(32, '32', 'MASSAED India Pvt Ltd', 'TG', 'Santanu Sahu', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Santanu Sahu', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(33, '33', 'MASSAED India Pvt Ltd', 'TG', 'Santanu Sahu', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Santanu Sahu', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(34, '34', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(35, '35', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(36, '36', 'Groffers Stove', 'UP', 'Noida', 'IN', '201301', 'E-138, Sec-63, Noida', 'UP', '201301', 'E-138, Sec-63, Noida', 'Groffers Stove', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(37, '37', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(38, '38', 'Dell Logistics', 'UP', 'Noida', 'IN', '201301', 'E-138, Dell Logistics', 'UP', '201301', 'E-138, Dell Logistics', 'Dell Logistics', 'Noida', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(39, '39', 'Humdard', 'UP', 'Ghaziabad', 'IN', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'UP', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'Humdard', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road', '', ''),
(40, '40', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'UP', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road', '', ''),
(41, '41', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'UP', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(42, '42', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'UP', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(43, '43', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'UP', '201006', 'Plot no. 125, Delhi Meerut Road, Near Guldhar.', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(44, '44', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(45, '45', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Rajnagar Extension', 'UP', '201006', 'Rajnagar Extension', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', '', 'Uttar Pradesh', 'India', '', '', ''),
(46, '55', 'Humdard', 'UP', 'Ghaziabad', 'IN', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'UP', '201003', 'No.5, Rajnagar Extention, Near Guldhar station road. Ghaziabad', 'Humdard', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Road', 'Uttar Pradesh', 'India', 'By Road', '', ''),
(47, '56', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(48, '57', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(49, '58', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(50, '59', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(53, '62', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(55, '64', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(56, '65', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(57, '66', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(58, '67', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'asdf asfdasf', 'MH', '110929', 'asdf adfasdf', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(59, '68', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', '', '', ''),
(60, '69', 'Textile Contractor Pvt Ltd', 'OR', 'Bhubaneswar', 'IN', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'OR', '265001', 'Textile Contractor Pvt Ltd Shaheed nagar, BBSR, Odisha, India', 'Textile Contractor Pvt Ltd', 'Bhubaneswar', 'IN', 'India', 'Odisha', '', 'Odisha', 'India', '', '', ''),
(61, '70', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'MH', '110929', '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', '', 'Maharashtra', 'India', '', '', ''),
(62, '71', 'ITC', 'UP', 'Ghaziabad', 'IN', '201006', 'Rajnagar Extension', 'UP', '201006', 'Rajnagar Extension', 'ITC', 'Ghaziabad', 'IN', 'India', 'Uttar Pradesh', 'By Courier', 'Uttar Pradesh', 'India', 'By Courier', '', ''),
(63, '72', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', '', ''),
(64, '73', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', '', ''),
(65, '74', 'MASSAED India Pvt Ltd', 'TG', 'Hyderabad', 'IN', '500001', 'Hyderabad', 'TG', '500001', 'Hyderabad', 'MASSAED India Pvt Ltd', 'Hyderabad', 'IN', 'India', 'Telangana', '', 'Telangana', 'India', '', '', ''),
(66, '75', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', '', ''),
(67, '76', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'UP', '201206', 'Hno. 192, Village- Basant Pur Saintli, Muradnagar, Ghaziabad. ', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', '', ' Uttar Pradesh', 'India', '', '', ''),
(68, '77', 'Cinntra', 'JH', 'Arif', 'IN', '110005', 'dafdsf', 'JH', '110005', 'dafdsf', 'Cinntra', 'Arif', 'IN', 'India', 'Jharkhand', '', 'Jharkhand', 'India', '', '', ''),
(69, '78', 'Lux Co.', 'UP', 'Muradnagar', 'IN', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'UP', '201206', 'HNo. 192, Basant Pur Saintli, Muradnagar', 'Lux Co.', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', '', ''),
(70, '79', 'Ankur Santanu Bros & Co.', 'OR', 'Bhubaneshwar', 'IN', '201301', 'Shaheed Nagar', 'OR', '201301', 'Shaheed Nagar', 'Ankur Santanu Bros & Co.', 'Bhubaneshwar', 'IN', 'India', ' Odisha', 'By Courier', ' Odisha', 'India', 'By Courier', '', ''),
(71, '80', 'Shiv Lakhan Textiles', 'MH', 'mumbai', 'IN', '110929', 'ser', 'MH', '110929', 'ser', 'Shiv Lakhan Textiles', 'mumbai', 'IN', 'India', 'Maharashtra', 'By Road', 'Maharashtra', 'India', 'By Road', 'tsts', 'tsts'),
(72, '81', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '645654654555555555', 'new adas dasdasd asdas', 'UP', '645654654555555555', 'new adas dasdasd asdas', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', 'zxc', 'zxc'),
(73, '82', 'Lucky Traders', 'UP', 'Muradnagar', 'IN', '645654654555555555', 'new adas dasdasd asdas', 'UP', '645654654555555555', 'new adas dasdasd asdas', 'Lucky Traders', 'Muradnagar', 'IN', 'India', ' Uttar Pradesh', 'By Road', ' Uttar Pradesh', 'India', 'By Road', 'zxc', 'zxc');

-- --------------------------------------------------------

--
-- Table structure for table `Quotation_appslave`
--

CREATE TABLE `Quotation_appslave` (
  `id` bigint NOT NULL,
  `Min` double NOT NULL,
  `Max` double NOT NULL,
  `Level` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Quotation_appslave`
--

INSERT INTO `Quotation_appslave` (`id`, `Min`, `Max`, `Level`) VALUES
(1, 0, 7, 4),
(2, 0, 7, 3),
(3, 7, 100, 2),
(4, 7, 100, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Quotation_documentlines`
--

CREATE TABLE `Quotation_documentlines` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `QuotationID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `TaxCode` varchar(10) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL,
  `Tax` varchar(100) NOT NULL,
  `UomNo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Quotation_documentlines`
--

INSERT INTO `Quotation_documentlines` (`id`, `LineNum`, `QuotationID`, `Quantity`, `UnitPrice`, `DiscountPercent`, `ItemCode`, `ItemDescription`, `TaxCode`, `U_FGITEM`, `CostingCode2`, `ProjectCode`, `FreeText`, `Tax`, `UomNo`) VALUES
(1, 0, '1', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '', ''),
(2, 0, '2', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '', ''),
(3, 0, '3', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '', ''),
(7, 2, '5', 12, 150, 5, 'IT0001', 'Test Item', 'IGST12', '', '', '', '', '', ''),
(8, 3, '5', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', '', '', '', '', '', ''),
(9, 1, '4', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', '', '', '', '', '', ''),
(10, 2, '4', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', '', '', '', '', '', ''),
(15, 4, '6', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '', ''),
(16, 5, '6', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '', '', '', ''),
(19, 2, '7', 15, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '', ''),
(21, 1, '8', 11, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '', ''),
(22, 2, '8', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '', '', '', ''),
(23, 0, '9', 1, 150, 3, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', 'Testing', '4', ''),
(24, 0, '15', 11, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(25, 1, '15', 15, 160, 2, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', 'DEPT001', '101', '', '0', ''),
(26, 0, '16', 10, 150, 10, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '10', 'Package'),
(28, 1, '17', 10, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '0', 'Package'),
(29, 0, '18', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(30, 0, '19', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(31, 0, '20', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(32, 0, '21', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(33, 0, '22', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(34, 0, '23', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(35, 0, '24', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(36, 0, '25', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(37, 0, '26', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(38, 0, '27', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(39, 0, '28', 1, 150, 99, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(40, 0, '29', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(41, 0, '30', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(42, 0, '31', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(43, 0, '32', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(44, 0, '33', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(45, 0, '34', 10, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(46, 0, '35', 10, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(47, 0, '36', 10, 150, 5, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(51, 3, '37', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '2', 'Package'),
(52, 4, '37', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '', '', '1', 'Package'),
(53, 0, '38', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '2', 'Package'),
(54, 1, '38', 1, 160, 1, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '101', '', '1', 'Package'),
(55, 0, '39', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(58, 2, '40', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '0', 'Package'),
(59, 0, '41', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(60, 0, '42', 5, 150, 10, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(61, 0, '43', 5, 150, 10, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(62, 0, '44', 5, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(63, 0, '45', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(64, 0, '55', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(65, 0, '56', 5, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(66, 0, '57', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '1', 'Package'),
(68, 1, '58', 1, 150, 4, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '0', 'Package'),
(69, 0, '59', 10, 150, 1, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', 'DEPT001', '100', '', '0', 'Package'),
(70, 0, '62', 10, 150, 1, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', 'DEPT001', '100', '', '0', 'Package'),
(71, 0, '64', 1, 150, 4, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', '', '0', 'Package'),
(72, 0, '65', 10, 150, 1, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', 'DEPT001', '100', '', '0', 'Package'),
(73, 0, '66', 1, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '1', 'Package'),
(74, 0, '67', 10, 150, 1, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', 'DEPT001', '100', '', '0', 'Package'),
(75, 0, '68', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(76, 0, '69', 10, 150, 0, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', '', '100', '', '0', 'Package'),
(77, 0, '70', 3, 233, 0, 'IT0007', 'new time', 'IGST12', 'IT0007', 'DEPT001', '100', '', '0', '200'),
(78, 0, '71', 40, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', '', '0', 'Package'),
(79, 0, '72', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', 'Package'),
(80, 0, '73', 5, 50000, 2, '', 'Water Chillerdfgsdg', 'IGST12', '', 'DEPT001', '100', '', '0', '674567'),
(81, 0, '74', 5, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', ''),
(82, 0, '75', 4, 150, 0, 'IT0003', 'Test Item asdf', 'IGST12', 'IT0003', '', '100', '', '0', 'Package'),
(83, 0, '76', 5, 150, 2, 'IT0001', 'Test Item', 'IGST12', 'IT0001', 'DEPT001', '100', '', '0', 'Package'),
(85, 1, '77', 1, 56767, 0, 'IT0010', 'Water Ozonator', 'IGST12', 'IT0010', '', '', '', '0', 'NOS'),
(86, 0, '78', 1, 56767, 2, 'IT0010', 'Water Ozonator', 'IGST12', 'IT0010', 'DEPT001', '100', '', '18', 'NOS'),
(94, 7, '79', 3, 56767, 2, 'IT0010', 'Water Ozonator', 'IGST12', 'IT0010', '', '', '', '18', 'NOS'),
(95, 8, '79', 1, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '', 'Testing', '0', 'NOS'),
(96, 0, '80', 3, 150, 0, 'IT0001', 'Test Item', 'IGST12', 'IT0001', '', '100', 'ers', '0', 'NOS'),
(97, 0, '81', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '101', '', '0', 'Package'),
(98, 0, '82', 1, 160, 0, 'IT0002', 'Test Item 2', 'IGST12', 'IT0002', '', '101', '', '0', 'Package');

-- --------------------------------------------------------

--
-- Table structure for table `Quotation_quotation`
--

CREATE TABLE `Quotation_quotation` (
  `id` bigint NOT NULL,
  `TaxDate` varchar(30) NOT NULL,
  `DocDueDate` varchar(30) NOT NULL,
  `ContactPersonCode` varchar(5) NOT NULL,
  `DiscountPercent` double NOT NULL,
  `DocDate` varchar(30) NOT NULL,
  `CardCode` varchar(30) NOT NULL,
  `Comments` varchar(150) NOT NULL,
  `SalesPersonCode` varchar(5) NOT NULL,
  `DocumentStatus` varchar(50) NOT NULL,
  `CancelStatus` varchar(50) NOT NULL,
  `DocCurrency` varchar(50) NOT NULL,
  `DocTotal` varchar(50) NOT NULL,
  `CardName` varchar(150) NOT NULL,
  `VatSum` varchar(50) NOT NULL,
  `CreationDate` varchar(50) NOT NULL,
  `DocEntry` varchar(5) NOT NULL,
  `PaymentGroupCode` varchar(5) NOT NULL,
  `U_QUOTNM` varchar(100) NOT NULL,
  `U_PREQUOTATION` varchar(100) NOT NULL,
  `U_PREQTNM` varchar(250) NOT NULL,
  `U_LEADID` int NOT NULL,
  `U_LEADNM` varchar(150) NOT NULL,
  `U_Term_Condition` longtext NOT NULL,
  `U_TermInterestRate` double NOT NULL,
  `U_TermPaymentTerm` varchar(100) NOT NULL,
  `U_TermDueDate` varchar(100) NOT NULL,
  `BPLID` varchar(5) NOT NULL,
  `U_OPPID` varchar(5) NOT NULL,
  `U_OPPRNM` varchar(100) NOT NULL,
  `U_FAV` varchar(10) NOT NULL,
  `U_APPROVENM` varchar(30) NOT NULL,
  `Level1Status` varchar(30) NOT NULL,
  `Level2Status` varchar(30) NOT NULL,
  `Level3Status` varchar(30) NOT NULL,
  `FinalStatus` varchar(30) NOT NULL,
  `CreateDate` varchar(30) NOT NULL,
  `CreateTime` varchar(30) NOT NULL,
  `UpdateDate` varchar(30) NOT NULL,
  `UpdateTime` varchar(30) NOT NULL,
  `APPROVEID_id` varchar(20) DEFAULT NULL,
  `Level1_id` varchar(20) DEFAULT NULL,
  `Level2_id` varchar(20) DEFAULT NULL,
  `Level3_id` varchar(20) DEFAULT NULL,
  `Attach` varchar(250) NOT NULL,
  `DelTerm` longtext NOT NULL,
  `Discount` double NOT NULL,
  `GST` varchar(250) NOT NULL,
  `Intall` double NOT NULL,
  `Project` varchar(100) NOT NULL,
  `QuotType` varchar(100) NOT NULL,
  `Subject` varchar(100) NOT NULL,
  `QTNO` varchar(50) NOT NULL,
  `ApprvReq` varchar(30) NOT NULL,
  `LOCharges` varchar(30) NOT NULL,
  `MICharges` varchar(30) NOT NULL,
  `OthInstruct` varchar(255) NOT NULL,
  `QuotStat` varchar(30) NOT NULL,
  `BPEmail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Quotation_quotation`
--

INSERT INTO `Quotation_quotation` (`id`, `TaxDate`, `DocDueDate`, `ContactPersonCode`, `DiscountPercent`, `DocDate`, `CardCode`, `Comments`, `SalesPersonCode`, `DocumentStatus`, `CancelStatus`, `DocCurrency`, `DocTotal`, `CardName`, `VatSum`, `CreationDate`, `DocEntry`, `PaymentGroupCode`, `U_QUOTNM`, `U_PREQUOTATION`, `U_PREQTNM`, `U_LEADID`, `U_LEADNM`, `U_Term_Condition`, `U_TermInterestRate`, `U_TermPaymentTerm`, `U_TermDueDate`, `BPLID`, `U_OPPID`, `U_OPPRNM`, `U_FAV`, `U_APPROVENM`, `Level1Status`, `Level2Status`, `Level3Status`, `FinalStatus`, `CreateDate`, `CreateTime`, `UpdateDate`, `UpdateTime`, `APPROVEID_id`, `Level1_id`, `Level2_id`, `Level3_id`, `Attach`, `DelTerm`, `Discount`, `GST`, `Intall`, `Project`, `QuotType`, `Subject`, `QTNO`, `ApprvReq`, `LOCharges`, `MICharges`, `OthInstruct`, `QuotStat`, `BPEmail`) VALUES
(1, '2022-09-29', '2022-09-29', '5', 10, '2022-09-29', 'CS00005', 'Testing', '89', 'bost_Open', 'csNo', '', '150.0', 'Wepro', '', '', '1', '1', 'Testing Quot 786', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', '', '', '2022-09-29', '12:41:02 PM', '2022-09-29', '12:41:02 PM', NULL, NULL, NULL, NULL, '', 'terms', 0, 'GST1000', 0, '', 'Sales Quotation', 'Testing', 'QOT00001', 'Not Approved', '', '', '', 'Open', ''),
(2, '2022-09-29', '2022-09-29', '4', 10, '2022-09-29', 'CS00004', 'Testing', '89', 'bost_Open', 'csNo', '', '150.0', 'Cinntra', '', '', '2', '1', 'Testing Quot Rahul', '', '', 0, '', '', 0, '1', '', '', '2', 'Tester Opportunity New', 'N', '', '', '', '', '', '2022-09-29', '2:37:41 PM', '2022-09-29', '2:37:41 PM', NULL, NULL, NULL, NULL, '', 'terms', 0, 'GST1000', 10, '1', 'Sales Quotation', 'Testing', 'QOT00002', 'Approved', '100', '10', 'new Data', 'Open', ''),
(3, '2022-09-29', '2022-09-29', '5', 10, '2022-09-29', 'CS00005', 'DEscription', '89', 'bost_Open', 'csNo', '', '150.0', 'Wepro', '', '', '3', '1', 'Testing Quot Sir', '', '', 0, '', 'Terms and Condition', 0, '1', '', '', '', '', 'N', '', '', '', '', '', '2022-09-29', '2:54:14 PM', '2022-09-29', '2:54:14 PM', NULL, NULL, NULL, NULL, '', 'terms', 0, 'GST1000', 15, '', 'Sales Quotation', 'Testing Sub', 'QOT00003', 'Approved', '20', '10', 'new Data', 'Open', ''),
(4, '2022-10-04', '2022-12-03', '17', 10, '2022-10-05', 'CS00016', '', '94', 'bost_Open', 'csNo', '', '750.0', 'Ajanara Enclave', '', '', '4', '1', 'Ajanara Road Map', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', '', '', '2022-10-03', '4:29:40 PM', '2022-10-03', '4:29:40 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '17', 'Sales Quotation', 'Water Fountain', 'QOT00004', 'Approved', '0', '0', '', 'Open', ''),
(5, '2022-10-03', '2022-12-02', '21', 10, '2022-10-06', 'CS00019', '', '95', 'bost_Open', 'csNo', '', '1500.0', 'Trends', '', '', '5', '2', 'Water Plant Quotation', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', '', '', '2022-10-03', '6:17:56 PM', '2022-10-03', '6:17:56 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '18', 'Sales Quotation', '', 'QOT00005', 'Approved', '0', '0', '', 'Open', ''),
(6, '2022-10-06', '2022-10-06', '21', 10, '2022-10-06', 'CS00019', 'Testing', '95', 'bost_Open', 'csNo', '', '1500.0', 'Trends', '', '', '6', '3', 'Test Rahul Quot', '', '', 0, '', '', 0, '3', '', '', '4', 'Trends', 'N', '', '', '', '', '', '2022-10-06', '12:59:10 PM', '2022-10-06', '12:59:10 PM', NULL, NULL, NULL, NULL, '', '', 0, 'GST1000', 0, '', 'Sales Quotation', '', 'QOT00006', 'Approved', '0', '0', '', 'Closed', ''),
(7, '2022-10-06', '2022-10-16', '22', 10, '2022-10-10', 'CS00020', '', '97', 'bost_Open', 'csNo', '', '1500.0', 'Haldiram & CO.', '', '', '7', '2', 'Haldiram Project Quote', '', '', 0, '', '', 0, '2', '', '', '5', 'Haldiram & CO.', 'N', '', '', '', '', '', '2022-10-06', '3:28:06 PM', '2022-10-06', '3:28:06 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', 'Water Treatment', 'QOT00007', 'Approved', '0', '0', '', 'Open', ''),
(8, '2022-10-07', '2022-10-16', '23', 100, '2022-10-10', 'CS00021', 'NA', '99', 'bost_Open', 'csNo', '', '1500.0', 'Groffers Stove', '', '', '8', '-1', 'Groffers PI', '', '', 0, '', 'NA', 0, '-1', '', '', '6', 'Groffers Stove', 'N', '', '', '', '', '', '2022-10-07', '7:02:33 PM', '2022-10-07', '7:02:33 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 100, '', 'Performa Invoice', 'Water Softner', 'QOT00008', 'Approved', '0', '200', '', 'Open', ''),
(9, '2022-10-10', '2022-10-10', '23', 10, '2022-10-10', 'CS00021', 'Testing', '99', 'bost_Open', 'csNo', '', '150.0', 'Groffers Stove', '', '', '9', '-1', 'Testing Quot 0765', '', '', 0, '', 'Terms ', 0, '-1', '', '', '6', 'Groffers Stove', 'N', '', '', '', '', '', '2022-10-10', '2:56:40 PM', '2022-10-10', '2:56:40 PM', NULL, NULL, NULL, NULL, '', 'Delevery', 0, '', 0, '', 'Sales Quotation', 'Testing', 'QOT00009', 'Approved', '0', '0', 'Others', 'Open', ''),
(15, '2022-10-10', '2022-10-22', '27', 10, '2022-10-11', 'CS00024', '', '101', 'bost_Open', 'csNo', '', '4050.0', 'IBM COMP LTD', '', '', '15', '2', 'Grand offer of the month', '', '', 0, '', 'No T&C applicable for this project.', 0, '2', '', '', '7', 'IBM COMP LTD', 'N', '', '', '', '', '', '2022-10-10', '6:15:00 PM', '2022-10-10', '6:15:00 PM', NULL, NULL, NULL, NULL, '', 'Delivery before date', 0, '', 500, '22', 'Sales Quotation', 'Ozonator Treatment', 'QOT00015', 'Approved', '100', '1000', 'No Instructions', 'Open', ''),
(16, '2022-10-10', '2022-10-21', '27', 10, '2022-10-11', 'CS00024', '', '1', 'bost_Open', 'csNo', '', '1500.0', 'IBM COMP LTD', '', '', '16', '2', 'Grand Finale', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', '', '', '2022-10-10', '6:28:38 PM', '2022-10-10', '6:28:38 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 500, '22', 'Sales Quotation', 'Water Fountain', 'QOT00016', 'Approved', '100', '1000', '', 'Open', ''),
(17, '2022-10-11', '2022-10-21', '36', 10, '2022-10-12', 'CS00033', '', '1', 'bost_Open', 'csNo', '', '750.0', 'Jyoti Pest Control', '', '', '17', '2', 'Pest Control Quote', '', '', 0, '', '', 0, '2', '', '', '10', 'Pest Control', 'N', '', '', '', '', '', '2022-10-11', '6:32:50 PM', '2022-10-11', '6:32:50 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 50, '25', 'Sales Quotation', '', 'QOT00017', 'Approved', '50', '100', '', 'Open', ''),
(18, '2022-10-12', '2022-10-12', '36', 10, '2022-10-12', 'CS00033', '', '1', 'bost_Open', 'csNo', '', '750.0', 'Jyoti Pest Control', '', '', '18', '2', 'Test sir quit', '', '', 0, '', '', 0, '2', '', '', '10', 'Pest Control', 'N', '', 'Approved', '', '', 'Approved', '2022-10-12', '3:11:33 PM', '2022-10-12', '3:11:33 PM', '1', '1', NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00018', 'Approved', '0', '0', '', 'Open', ''),
(19, '2022-10-12', '2022-10-12', '36', 5, '2022-10-12', 'CS00033', '', '1', 'bost_Open', 'csNo', '', '750.0', 'Jyoti Pest Control', '', '', '19', '2', 'testing quo rohit', '', '', 0, '', '', 0, '2', '', '', '10', 'Pest Control', 'N', '', 'Approved', '', '', 'Approved', '2022-10-12', '3:12:39 PM', '2022-10-12', '3:12:39 PM', '1', '1', NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00019', 'Approved', '0', '0', '', 'Open', ''),
(20, '2022-10-12', '2022-10-12', '33', 10, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '20', '2', 'five discount quot', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', '', '', '2022-10-12', '3:15:48 PM', '2022-10-12', '3:15:48 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00020', 'Approved', '0', '0', '', 'Open', ''),
(21, '2022-10-12', '2022-10-12', '33', 5, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '21', '2', 'ten discount quot', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', 'Approved', 'Approved', '2022-10-12', '3:16:33 PM', '2022-10-12', '3:16:33 PM', '102', NULL, NULL, '102', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00021', 'Approved', '0', '0', '', 'Open', ''),
(22, '2022-10-12', '2022-10-12', '33', 10, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '22', '2', 'ten discount quot2', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', '', '', '2022-10-12', '3:31:40 PM', '2022-10-12', '3:31:40 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00022', 'Approved', '0', '0', '', 'Closed', ''),
(23, '2022-10-12', '2022-10-12', '33', 5, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '23', '2', 'five discount quot2', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', 'Approved', 'Approved', '2022-10-12', '3:38:27 PM', '2022-10-12', '3:38:27 PM', '102', NULL, NULL, '102', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00023', 'Approved', '0', '0', '', 'Closed', ''),
(24, '2022-10-12', '2022-10-12', '33', 5, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '24', '2', 'five discount quot3', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', 'Approved', 'Approved', '2022-10-12', '3:47:12 PM', '2022-10-12', '3:47:12 PM', '102', NULL, NULL, '102', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00024', 'Approved', '0', '0', '', 'Open', ''),
(25, '2022-10-12', '2022-10-12', '33', 10, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '25', '2', 'ten discount quot3', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', '', '', '', '', '2022-10-12', '3:47:43 PM', '2022-10-12', '3:47:43 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Performa Invoice', '', 'QOT00025', 'Not Approved', '0', '0', '', 'Open', ''),
(26, '2022-10-12', '2022-10-12', '33', 10, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '26', '2', 'ten discount quot5', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', 'Rejected', '', '', 'Rejected', '2022-10-12', '3:51:53 PM', '2022-10-12', '3:51:53 PM', '1', '1', NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00026', 'Approved', '0', '0', '', 'Open', ''),
(27, '2022-10-12', '2022-10-12', '33', 10, '2022-10-12', 'CS00030', '', '102', 'bost_Open', 'csNo', '', '150.0', 'NEw bp 2', '', '', '27', '2', 'ten discount quot6', '', '', 0, '', '', 0, '2', '', '', '9', 'Tester Opportunity Sunil', 'N', '', 'Approved', 'Pending', 'Approved', 'Approved', '2022-10-12', '3:54:04 PM', '2022-10-12', '3:54:04 PM', '1', '1', '100', '102', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00027', 'Approved', '0', '0', '', 'Open', ''),
(28, '2022-10-12', '2022-10-13', '42', 10, '2022-10-13', 'CS00035', '', '92', 'bost_Open', 'csNo', '', '150.0', 'Dell Logistics', '', '', '28', '2', 'wefrwerf', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', 'Approved', '', 'Approved', '2022-10-12', '4:24:11 PM', '2022-10-12', '4:24:11 PM', '92', NULL, '92', NULL, '', '', 0, '', 0, '26', 'Sales Quotation', 'qwrafafwefr', 'QOT00028', '', '0', '0', '', 'Open', ''),
(29, '2022-10-12', '2022-10-12', '37', 10, '2022-10-12', 'CS00034', '', '92', 'bost_Open', 'csNo', '', '150.0', 'qwdqdqwd', '', '', '29', '2', 'asdfasdf', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', 'Approved', 'Approved', 'Approved', '2022-10-12', '4:33:18 PM', '2022-10-12', '4:33:18 PM', '100', NULL, '100', '92', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00029', '', '0', '0', '', 'Open', ''),
(30, '2022-10-12', '2022-10-12', '42', 10, '2022-10-12', 'CS00035', '', '92', 'bost_Open', 'csNo', '', '150.0', 'Dell Logistics', '', '', '30', '2', 'asdfadsf', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', 'Rejected', 'Approved', 'Rejected', '2022-10-12', '4:44:47 PM', '2022-10-12', '4:44:47 PM', '100', NULL, '100', '92', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00030', '', '0', '0', '', 'Open', ''),
(31, '2022-10-12', '2022-10-13', '36', 6, '2022-10-20', 'CS00033', '', '91', 'bost_Open', 'csNo', '', '150.0', 'Jyoti Pest Control', '', '', '31', '2', 'qwe', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', 'Pending', 'Pending', '2022-10-12', '5:28:01 PM', '2022-10-12', '5:28:01 PM', NULL, NULL, NULL, '89', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00031', '', '0', '0', '', 'Open', ''),
(32, '2022-10-12', '2022-10-12', '37', 10, '2022-10-12', 'CS00034', '', '92', 'bost_Open', 'csNo', '', '150.0', 'qwdqdqwd', '', '', '32', '2', 'Testing Quot 786', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', '', '', '2022-10-12', '5:52:06 PM', '2022-10-12', '5:52:06 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', 'Testing', 'QOT00032', '', '0', '0', '', 'Open', ''),
(33, '2022-10-12', '2022-10-12', '37', 10, '2022-10-12', 'CS00034', '', '92', 'bost_Open', 'csNo', '', '150.0', 'qwdqdqwd', '', '', '33', '2', 'Testing Quot 786', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', '', '', '2022-10-12', '5:52:06 PM', '2022-10-12', '5:52:06 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', 'Testing', 'QOT00033', '', '0', '0', '', 'Open', ''),
(34, '2022-10-12', '2022-10-12', '23', 10, '2022-10-12', 'CS00021', '', '99', 'bost_Open', 'csNo', '', '1500.0', 'Groffers Stove', '', '', '34', '-1', 'Testing Quot 786234', '', '', 0, '', '', 0, '-1', '', '', '6', 'Groffers Stove', 'N', '', '', '', '', 'Approved', '2022-10-12', '5:57:03 PM', '2022-10-12', '5:57:03 PM', '99', NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00034', '', '0', '0', '', 'Closed', ''),
(35, '2022-10-12', '2022-10-12', '23', 8, '2022-10-12', 'CS00021', '', '99', 'bost_Open', 'csNo', '', '1500.0', 'Groffers Stove', '', '', '35', '-1', 'Testing Quot 7862233', '', '', 0, '', '', 0, '-1', '', '', '6', 'Groffers Stove', 'N', '', '', '', '', 'Approved', '2022-10-12', '5:58:12 PM', '2022-10-12', '5:58:12 PM', '99', NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00035', '', '0', '0', '', 'Closed', ''),
(36, '2022-10-12', '2022-10-12', '23', 11, '2022-10-12', 'CS00021', '', '99', 'bost_Open', 'csNo', '', '1500.0', 'Groffers Stove', '', '', '36', '-1', 'asfdasdfasdf', '', '', 0, '', '', 0, '-1', '', '', '6', 'Groffers Stove', 'N', '', '', '', 'Pending', 'Pending', '2022-10-12', '5:58:35 PM', '2022-10-12', '5:58:35 PM', NULL, NULL, NULL, '98', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00036', '', '0', '0', '', 'Closed', ''),
(37, '2022-11-01', '2022-11-01', '42', 10, '2022-11-01', 'CS00035', 'Testing', '102', 'bost_Open', 'csNo', '', '150.0', 'Dell Logistics', '', '', '37', '2', 'Testing opppppp', '', '', 0, '', '', 0, '2', '', '', '12', 'bsjskbxjx', 'N', '', 'Approved', '', '', 'Approved', '2022-11-01', '11:49:43 AM', '2022-11-01', '11:49:43 AM', '1', '1', NULL, NULL, '', '', 0, 'GST1000', 0, '27', 'Sales Quotation', 'Testing', 'QOT00037', '', '0', '0', '', 'Open', ''),
(38, '2022-11-02', '2022-11-02', '42', 0, '2022-11-02', 'CS00035', '', '102', 'bost_Open', 'csNo', '', '310.0', 'Dell Logistics', '', '', '38', '2', 'Testing Quot 78612312123123', '', '', 0, '', '', 0, '2', '', '', '12', 'bsjskbxjx', 'N', '', 'Approved', '', '', 'Approved', '2022-11-02', '12:40:29 PM', '2022-11-02', '12:40:29 PM', '1', '1', NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00038', '', '0', '0', '', 'Open', ''),
(39, '2022-11-04', '2023-01-13', '44', 0, '2022-11-07', 'CS00036', '', '103', 'bost_Open', 'csNo', '', '150.0', 'Humdard', '', '', '39', '2', 'Humdard Water Treatment Plant', '', '', 0, '', '', 0, '2', '', '', '13', 'Humdard', 'N', '', 'Approved', '', '', 'Approved', '2022-11-03', '10:11:27 AM', '2022-11-03', '10:11:27 AM', '1', '1', NULL, NULL, '', '', 0, '', 0, '30', 'Sales Quotation', '', 'QOT00039', '', '0', '0', '', 'Open', ''),
(40, '2022-11-03', '2022-11-18', '45', 4, '2022-11-05', 'CS00037', '', '106', 'bost_Open', 'csNo', '', '750.0', 'ITC', '', '', '40', '2', 'ITC  Project Quote', '', '', 0, '', '', 0, '2', '', '', '14', 'ITC', 'N', '', '', '', '', '', '2022-11-03', '11:40:33 AM', '2022-11-03', '11:40:33 AM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '31', 'Sales Quotation', '', 'QOT00040', '', '0', '0', '', 'Open', ''),
(41, '2022-11-03', '2022-11-04', '45', 0, '2022-11-05', 'CS00037', '', '106', 'bost_Open', 'csNo', '', '150.0', 'ITC', '', '', '41', '2', 'Potential Lead', '', '', 0, '', '', 0, '2', '', '', '14', 'ITC', 'N', '', '', '', '', '', '2022-11-03', '11:53:38 AM', '2022-11-03', '11:53:38 AM', NULL, NULL, NULL, NULL, '', '', 0, 'GST11233', 0, '', 'Sales Quotation', '', 'QOT00041', '', '0', '0', '', 'Open', ''),
(42, '2022-11-03', '2022-11-05', '45', 10, '2022-11-06', 'CS00037', '', '106', 'bost_Open', 'csNo', '', '750.0', 'ITC', '', '', '42', '2', 'Potential Lead 123', '', '', 0, '', '', 0, '2', '', '', '14', 'ITC', 'N', '', '', 'Pending', 'Approved', 'Pending', '2022-11-03', '11:56:30 AM', '2022-11-03', '11:56:30 AM', NULL, NULL, '104', '105', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00042', '', '0', '0', '', 'Open', ''),
(43, '2022-11-03', '2022-11-03', '45', 0, '2022-11-03', 'CS00037', '', '106', 'bost_Open', 'csNo', '', '750.0', 'ITC', '', '', '43', '2', 'NEw Rahul Quotation', '', '', 0, '', '', 0, '2', '', '', '14', 'ITC', 'N', '', '', '', '', '', '2022-11-03', '12:18:01 PM', '2022-11-03', '12:18:01 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Performa Invoice', '', 'QOT00043', '', '0', '0', '', 'Open', ''),
(44, '2022-11-03', '2022-11-04', '48', 0, '2022-11-12', 'CS00040', '', '107', 'bost_Open', 'csNo', '', '750.0', 'AGON IT SOLUTION 1233', '', '', '44', '1', 'Santanu Sahu', '', '', 0, '', '', 0, '1', '', '', '16', 'AGON IT SOLUTION LTD', 'N', '', '', '', '', '', '2022-11-03', '5:23:24 PM', '2022-11-03', '5:23:24 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00044', '', '0', '0', '', 'Open', ''),
(45, '2022-11-03', '2022-11-05', '47', 0, '2022-11-04', 'CS00039', '', '107', 'bost_Open', 'csNo', '', '150.0', 'Apco Water Architecture', '', '', '45', '1', 'qsdfasdf', '', '', 0, '', '', 0, '1', '', '', '15', 'Tester Opportunity', 'N', '', '', '', '', '', '2022-11-03', '5:25:58 PM', '2022-11-03', '5:25:58 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00045', '', '0', '0', '', 'Open', ''),
(55, '2022-11-04', '2022-11-04', '44', 0, '2022-11-04', 'CS00036', '', '103', 'bost_Open', 'csNo', '', '150.0', 'Humdard', '', '', '55', '2', 'Humdard', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', '', '', '', '2022-11-04', '11:15:42 AM', '2022-11-04', '11:15:42 AM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '30', 'Sales Quotation', '', 'QOT00055', '', '0', '0', '', 'Closed', ''),
(56, '2022-11-04', '2022-11-04', '48', 2, '2022-11-04', 'CS00040', '', '1', 'bost_Open', 'csNo', '', '750.0', 'AGON IT SOLUTION 1233', '', '', '56', '1', 'Sunil Quotation', '', '', 0, '', '', 0, '1', '', '', '16', 'AGON IT SOLUTION LTD', 'N', '', '', '', '', '', '2022-11-04', '11:53:40 AM', '2022-11-04', '11:53:40 AM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '32', 'Sales Quotation', '', 'QOT00056', '', '0', '0', '', 'Closed', ''),
(57, '2022-11-04', '2022-11-04', '48', 0, '2022-11-04', 'CS00040', '', '106', 'bost_Open', 'csNo', '', '150.0', 'AGON IT SOLUTION 1233', '', '', '57', '1', 'Rahul Quotation', '', '', 0, '', '', 0, '1', '', '', '19', 'ASDasd2323safs', 'N', '', '', '', '', '', '2022-11-04', '1:27:07 PM', '2022-11-04', '1:27:07 PM', NULL, NULL, NULL, NULL, '', '', 0, '', 0, '33', 'Sales Quotation', '', 'QOT00057', '', '0', '0', '', 'Open', ''),
(58, '2022-11-04', '2022-11-04', '51', 2, '2022-11-04', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '300.0', 'Shiv Lakhan Textiles', '', '', '58', '1', 'Testing new quot', '', '', 0, '', '', 0, '1', '', '', '21', 'Shiv Lakhan Textiles', 'N', '', '', 'Approved', '', 'Approved', '2022-11-04', '2:28:45 PM', '2022-11-04', '2:28:45 PM', '105', NULL, '105', NULL, '', '', 0, '', 0, '', 'Performa Invoice', '', 'QOT00058', '', '0', '0', '', 'Closed', ''),
(59, '2022-11-04', '2022-11-05', '51', 4, '2022-11-30', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '1500.0', 'Shiv Lakhan Textiles', '', '', '59', '1', 'Shiv Lakhan Textiles BBSR Pvt Ltd', '', '', 0, '', '', 0, '1', '', '', '23', 'Shiv Lakhan Textiles', 'N', '', 'Approved', '', '', 'Approved', '2022-11-04', '2:38:42 PM', '2022-11-04', '2:38:42 PM', '1', '1', NULL, NULL, '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00059', '', '0', '0', '', 'Open', ''),
(62, '2022-11-04', '2022-11-04', '51', 0, '2022-11-04', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '1500.0', 'Shiv Lakhan Textiles', '', '', '62', '1', 'Testing qqwerwer', '', '', 0, '', '', 0, '1', '', '', '23', 'Shiv Lakhan Textiles', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '2:51:42 PM', '2022-11-04', '2:51:42 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00062', '', '0', '0', '', 'Open', ''),
(64, '2022-11-04', '2022-11-05', '51', 2, '2022-11-11', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '150.0', 'Shiv Lakhan Textiles', '', '', '64', '1', 'Shiv Lakhan Textiles', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '2:52:36 PM', '2022-11-04', '2:52:36 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Performa Invoice', '', 'QOT00064', '', '0', '0', '', 'Open', ''),
(65, '2022-11-04', '2022-11-05', '51', 0, '2022-11-05', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '1500.0', 'Shiv Lakhan Textiles', '', '', '65', '1', 'Shiv Lakhan Textiles', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '2:53:12 PM', '2022-11-04', '2:53:12 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00065', '', '0', '0', '', 'Open', ''),
(66, '2022-11-04', '2022-11-04', '48', 5, '2022-11-04', 'CS00040', '', '106', 'bost_Open', 'csNo', '', '150.0', 'AGON IT SOLUTION 1233', '', '', '66', '1', 'Testing asdf', '', '', 0, '', '', 0, '1', '', '', '19', 'ASDasd2323safs', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '2:53:36 PM', '2022-11-04', '2:53:36 PM', '106', NULL, NULL, '106', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00066', '', '0', '0', '', 'Closed', ''),
(67, '2022-11-04', '2022-11-04', '51', 4, '2022-11-30', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '1500.0', 'Shiv Lakhan Textiles', '', '', '67', '1', 'Shiv Lakhan Textiles BBSR Pvt Ltd LLP', '', '', 0, '', '', 0, '1', '', '', '23', 'Shiv Lakhan Textiles', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '3:30:12 PM', '2022-11-04', '3:30:12 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Sales Quotation', 'Headson', 'QOT00067', '', '0', '0', '', 'Open', ''),
(68, '2022-11-04', '2022-11-04', '53', 5.1, '2022-11-30', 'CS00044', '', '107', 'bost_Open', 'csNo', '', '150.0', 'Textile Contractor Pvt Ltd', '', '', '68', '1', 'Shiv Lakhan Textiles', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '3:31:23 PM', '2022-11-04', '3:31:23 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00068', '', '0', '0', '', 'Open', ''),
(69, '2022-11-04', '2022-11-30', '53', 7.1, '2022-11-30', 'CS00044', '', '107', 'bost_Open', 'csNo', '', '1500.0', 'Textile Contractor Pvt Ltd', '', '', '69', '1', 'uqweiuqweiuqwkej', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', 'Rejected', 'Pending', 'Approved', 'Rejected', '2022-11-04', '3:36:31 PM', '2022-11-04', '3:36:31 PM', '1', '1', '105', '107', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00069', '', '0', '0', '', 'Open', ''),
(70, '2022-11-04', '2022-11-29', '51', 0, '2022-11-19', 'CS00043', '', '107', 'bost_Open', 'csNo', '', '699.0', 'Shiv Lakhan Textiles', '', '', '70', '1', 'TTT', '', '', 0, '', '', 0, '1', '', '', '25', 'Shiv Lakhan Textiles', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '5:50:29 PM', '2022-11-04', '5:50:29 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '35', 'Sales Quotation', '', 'QOT00070', '', '0', '0', '', 'Open', ''),
(71, '2022-11-04', '2022-11-04', '47', 6.9, '2022-11-12', 'CS00039', '', '107', 'bost_Open', 'csNo', '', '6000.0', 'Apco Water Architecture', '', '', '71', '1', 'wedrtyhuytrew 123', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', '', '', 'Approved', 'Approved', '2022-11-04', '6:57:57 PM', '2022-11-04', '6:57:57 PM', '107', NULL, NULL, '107', '', '', 0, '', 0, '', 'Sales Quotation', 'qwert', 'QOT00071', '', '0', '0', '', 'Open', ''),
(72, '2022-11-07', '2022-11-30', '56', 7.1, '2022-11-14', 'CS00047', '', '106', 'bost_Open', 'csNo', '', '750.0', 'Lucky Traders', '', '', '72', '2', 'Lucky Trader Quote', '', '', 0, '', 'This is final quote no change will be process once get approved.', 0, '2', '', '', '26', 'Lucky Traders', 'N', '', 'Approved', 'Pending', 'Approved', 'Approved', '2022-11-07', '3:33:33 PM', '2022-11-07', '3:33:33 PM', '1', '1', '103', '105', '', 'Delivery before date', 0, '', 100, '36', 'Sales Quotation', '', 'QOT00072', '', '200', '100', 'No Instructions', 'Open', ''),
(73, '2022-11-07', '2022-11-25', '56', 8, '2022-11-21', 'CS00047', '', '106', 'bost_Open', 'csNo', '', '250000.0', 'Lucky Traders', '', '', '73', '2', 'Lucky Sales Quote', '', '', 0, '', '', 0, '2', '', '', '27', 'Lucky Traders', 'N', '', 'Approved', 'Pending', 'Approved', 'Approved', '2022-11-07', '4:07:44 PM', '2022-11-07', '4:07:44 PM', '1', '1', '103', '105', '', '', 0, '', 150, '36', 'Sales Quotation', '', 'QOT00073', '', '150', '200', '', 'Open', ''),
(74, '2022-11-08', '2022-11-30', '48', 8, '2022-11-30', 'CS00040', '', '107', 'bost_Open', 'csNo', '', '750.0', 'AGON IT SOLUTION 1233', '', '', '74', '1', '8% Discounted', '', '', 0, '', '', 0, '1', '', '', '16', 'AGON IT SOLUTION LTD', 'N', '', '', 'Approved', 'Approved', 'Approved', '2022-11-08', '10:52:57 AM', '2022-11-08', '10:52:57 AM', '105', NULL, '105', '107', '', '', 0, '', 100, '', 'Performa Invoice', '', 'QOT00074', '', '100', '100', '', 'Open', ''),
(75, '2022-11-08', '2022-11-08', '', 15, '2022-11-30', 'CS00047', '', '107', 'bost_Open', 'csNo', '', '600.0', 'Lucky Traders', '', '', '75', '2', '15% Discount de raha hun', '', '', 0, '', '', 0, '2', '', '', '', '', 'N', '', '', 'Approved', 'Approved', 'Approved', '2022-11-08', '11:20:29 AM', '2022-11-08', '11:20:29 AM', '105', NULL, '105', '107', '', '', 0, '', 50, '', 'Sales Quotation', '', 'QOT00075', '', '50', '100', '', 'Open', ''),
(76, '2022-11-10', '2022-11-10', '56', 0, '2022-11-10', 'CS00047', '', '106', 'bost_Open', 'csNo', '', '750.0', 'Lucky Traders', '', '', '76', '2', 'Arif Quotation1', '', '', 0, '', '', 0, '2', '', '', '26', 'Lucky Traders', 'N', '', '', '', 'Approved', 'Approved', '2022-11-10', '2:09:25 PM', '2022-11-10', '2:09:25 PM', '106', NULL, NULL, '106', '', '', 0, '', 0, '', 'Sales Quotation', 'WOW WOW', 'QOT00076', '', '0', '0', '', 'Closed', ''),
(77, '2022-11-14', '2022-11-14', '61', 10, '2022-11-14', 'CS00050', '', '89', 'bost_Open', 'csNo', '', '150.0', 'NEw com', '', '', '77', '1', 'Testing quot', '', '', 0, '', '', 0, '1', '', '', '', '', 'N', '', 'Approved', 'Pending', 'Approved', 'Approved', '2022-11-14', '12:53:56 PM', '2022-11-14', '12:53:56 PM', '1', '1', '103', '89', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00077', '', '0', '100', '', 'Open', ''),
(78, '2022-11-14', '2022-11-30', '62', 10, '2022-11-16', 'CS00051', '', '107', 'bost_Open', 'csNo', '', '56767.0', 'Lux Co.', '', '', '78', '2', 'Lux Sales Quote', '', '', 0, '', 'weryuilkjhgfdbnm\r\ndasflkj;jhgfgkhj', 0, '2', '', '', '28', 'Lux Co.', 'N', '', 'Approved', 'Pending', 'Approved', 'Approved', '2022-11-14', '6:45:17 PM', '2022-11-14', '6:45:17 PM', '1', '1', '105', '107', '', 'wrqetyu', 0, '', 200, '', 'Sales Quotation', '', 'QOT00078', '', '300', '100', 'ewqruty', 'Open', ''),
(79, '2022-11-15', '2022-11-30', '63', 10, '2022-11-17', 'CS00052', 'eqrwyjhtg safdhgds sagdfd', '107', 'bost_Open', 'csNo', '', '283835.0', 'Ankur Santanu Bros & Co.', '', '', '79', '2', 'Ankur Santanu Bros & Co. Quote', '', '', 0, '', 'artfhgdfsgfd wertgt', 0, '2', '', '', '29', 'Ankur Santanu Bros & Co.', 'N', '', '', 'Approved', 'Approved', 'Approved', '2022-11-15', '12:02:05 PM', '2022-11-15', '12:02:05 PM', '105', NULL, '105', '107', '', 'sfdghnbvc  adsfgf', 0, '37AADCS0472N1Z1', 200, '48', 'Performa Invoice', 'Water Related Work', 'QOT00079', '', '300', '100', 'ewrthtg sdafghf', 'Open', ''),
(80, '2022-11-21', '2022-11-23', '51', 2, '2022-11-24', 'CS00043', 'resrhs', '107', 'bost_Open', 'csNo', '', '450.0', 'Shiv Lakhan Textiles', '', '', '80', '1', 'panksj', '', '', 0, '', 'res', 0, '1', '', '', '21', 'Shiv Lakhan Textiles 1', 'N', '', '', '', 'Approved', 'Approved', '2022-11-21', '3:50:18 PM', '2022-11-21', '3:50:18 PM', '107', NULL, NULL, '107', '', 'dt', 0, '123454656', 0, '34', 'Sales Quotation', 'tests', 'QOT00080', '', '0', '0', 'rest', 'Open', ''),
(81, '2022-11-21', '2022-11-23', '70', 0, '2022-12-07', 'CS00056', 'fsdzs', '106', 'bost_Open', 'csNo', '', '160.0', 'naya company', '', '', '81', '4', 'azsxdcvxb ', '', '', 0, '', 'zxz', 0, '4', '', '', '31', 'wgsh', 'N', '', '', '', 'Approved', 'Approved', '2022-11-21', '3:55:08 PM', '2022-11-21', '3:55:08 PM', '106', NULL, NULL, '106', '', 'fsdz', 0, '32456', 0, '', 'Sales Quotation', 'zxcz', 'QOT00081', '', '0', '0', 'czzzc', 'Open', ''),
(82, '2022-11-22', '2022-11-22', '70', 0, '2022-11-22', 'CS00056', 'fsdzs', '106', 'bost_Open', 'csNo', '', '160.0', 'naya company', '', '', '82', '4', 'naya company', '', '', 0, '', '', 0, '4', '', '', '', '', 'N', '', '', '', 'Approved', 'Approved', '2022-11-22', '10:51:19 AM', '2022-11-22', '10:51:19 AM', '106', NULL, NULL, '106', '', '', 0, '', 0, '', 'Sales Quotation', '', 'QOT00082', '', '0', '0', '', 'Closed', '');

-- --------------------------------------------------------

--
-- Table structure for table `Tender_corrigendumlist`
--

CREATE TABLE `Tender_corrigendumlist` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `Type` varchar(200) NOT NULL,
  `Title` varchar(200) NOT NULL,
  `File` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_coverdetail`
--

CREATE TABLE `Tender_coverdetail` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `CoverTitle` varchar(100) NOT NULL,
  `CoverDocType` varchar(100) NOT NULL,
  `CoverDesc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_critcaldates`
--

CREATE TABLE `Tender_critcaldates` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `PublishDate` varchar(200) NOT NULL,
  `BidOpeningDate` varchar(200) NOT NULL,
  `SaleStartDate` varchar(200) NOT NULL,
  `SaleEndDate` varchar(200) NOT NULL,
  `ClarificationStartDate` varchar(200) NOT NULL,
  `ClarificationEndDate` varchar(200) NOT NULL,
  `BidSubStartDate` varchar(200) NOT NULL,
  `BidSubEndDate` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_documents`
--

CREATE TABLE `Tender_documents` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `Type` varchar(200) NOT NULL,
  `Title` varchar(200) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `File` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_lowestone`
--

CREATE TABLE `Tender_lowestone` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `CompanyName` varchar(200) NOT NULL,
  `QuotedModel` varchar(100) NOT NULL,
  `Price` int NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_paymentinstrument`
--

CREATE TABLE `Tender_paymentinstrument` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `PaymentType` varchar(50) NOT NULL,
  `InstrumentType` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_technicalopening`
--

CREATE TABLE `Tender_technicalopening` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `CompanyName` varchar(200) NOT NULL,
  `QuotedModel` varchar(100) NOT NULL,
  `Part` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_tender`
--

CREATE TABLE `Tender_tender` (
  `id` bigint NOT NULL,
  `SalesPersonCode` varchar(5) NOT NULL,
  `OrganisationChain` varchar(200) NOT NULL,
  `TReferenceNo` varchar(100) NOT NULL,
  `TID` varchar(100) NOT NULL,
  `TType` varchar(100) NOT NULL,
  `TCategoey` varchar(100) NOT NULL,
  `GeneralTechEveAll` varchar(50) NOT NULL,
  `PaymentMode` varchar(50) NOT NULL,
  `MultiCurrency` varchar(50) NOT NULL,
  `FormOfContact` varchar(50) NOT NULL,
  `NoOfCovers` varchar(50) NOT NULL,
  `ItemTechEveAll` varchar(50) NOT NULL,
  `MultiCurrencyForBoq` varchar(50) NOT NULL,
  `TwoStageBidding` varchar(50) NOT NULL,
  `TenderFee` varchar(100) NOT NULL,
  `PayableTo` varchar(100) NOT NULL,
  `FeeExemptionAllow` varchar(50) NOT NULL,
  `FeePayableAt` varchar(100) NOT NULL,
  `EMDAmount` varchar(100) NOT NULL,
  `EMDFeeType` varchar(50) NOT NULL,
  `EMDPayableTo` varchar(50) NOT NULL,
  `EMDPayableAt` varchar(50) NOT NULL,
  `EMDExemptionAllow` varchar(50) NOT NULL,
  `EMDPercentage` varchar(50) NOT NULL,
  `InvitingAuthorityName` varchar(100) NOT NULL,
  `InvitingAuthorityAddress` varchar(200) NOT NULL,
  `Status` varchar(50) NOT NULL,
  `Comments` varchar(200) NOT NULL,
  `TenderSubStatus` int NOT NULL,
  `TenderOpenStatus` int NOT NULL,
  `TechOpenStatus` int NOT NULL,
  `LowestOneStatus` int NOT NULL,
  `U_LEADID` int NOT NULL,
  `U_LEADNM` varchar(150) NOT NULL,
  `U_OPPID` varchar(5) NOT NULL,
  `U_OPPRNM` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_tenderopening`
--

CREATE TABLE `Tender_tenderopening` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `CompanyName` varchar(200) NOT NULL,
  `QuotedModel` varchar(100) NOT NULL,
  `Part` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_tendersubmission`
--

CREATE TABLE `Tender_tendersubmission` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `FeeStatus` varchar(100) NOT NULL,
  `PaymentRegNo` varchar(100) NOT NULL,
  `PaymentMode` varchar(100) NOT NULL,
  `FeeAmount` varchar(100) NOT NULL,
  `BankName` varchar(100) NOT NULL,
  `AccountNo` varchar(100) NOT NULL,
  `IFSCCode` varchar(100) NOT NULL,
  `EMDFeeStatus` varchar(100) NOT NULL,
  `EMDTerms` varchar(100) NOT NULL,
  `EMDPaymentMode` varchar(100) NOT NULL,
  `EMDFeeAmount` varchar(100) NOT NULL,
  `EMDBankName` varchar(100) NOT NULL,
  `EMDAccountNo` varchar(100) NOT NULL,
  `EMDIFSCCode` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_tenitem`
--

CREATE TABLE `Tender_tenitem` (
  `id` bigint NOT NULL,
  `LineNum` int NOT NULL,
  `TenID` varchar(5) NOT NULL,
  `Quantity` int NOT NULL,
  `UnitPrice` double NOT NULL,
  `DiscountPercent` double NOT NULL,
  `ItemCode` varchar(20) NOT NULL,
  `ItemDescription` varchar(150) NOT NULL,
  `TaxCode` varchar(10) NOT NULL,
  `U_FGITEM` varchar(20) NOT NULL,
  `CostingCode2` varchar(20) NOT NULL,
  `ProjectCode` varchar(20) NOT NULL,
  `FreeText` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Tender_workoritemdetails`
--

CREATE TABLE `Tender_workoritemdetails` (
  `id` bigint NOT NULL,
  `TenderId` int NOT NULL,
  `Title` varchar(200) NOT NULL,
  `Description` longtext NOT NULL,
  `PreQualficationDetails` varchar(200) NOT NULL,
  `Remarks` varchar(200) NOT NULL,
  `TenderValue` varchar(200) NOT NULL,
  `ProductCategory` varchar(200) NOT NULL,
  `ProductSubCategory` varchar(200) NOT NULL,
  `ContactType` varchar(200) NOT NULL,
  `BidValidity` varchar(200) NOT NULL,
  `PeriodOfWork` varchar(200) NOT NULL,
  `Location` varchar(200) NOT NULL,
  `Pincode` varchar(200) NOT NULL,
  `PreBidMeetingPlace` varchar(200) NOT NULL,
  `PreBidMeetingAddress` varchar(200) NOT NULL,
  `PreBidMeetingDate` varchar(200) NOT NULL,
  `BidOpeningPlace` varchar(200) NOT NULL,
  `NDATenderAllow` varchar(200) NOT NULL,
  `PreferentialBidderAllow` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Activity_activity`
--
ALTER TABLE `Activity_activity`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Activity_chatter`
--
ALTER TABLE `Activity_chatter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Activity_maps`
--
ALTER TABLE `Activity_maps`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Attachment_attachment`
--
ALTER TABLE `Attachment_attachment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `Branch_branch`
--
ALTER TABLE `Branch_branch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpaddresses`
--
ALTER TABLE `BusinessPartner_bpaddresses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpbranch`
--
ALTER TABLE `BusinessPartner_bpbranch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpcurrency`
--
ALTER TABLE `BusinessPartner_bpcurrency`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpdepartment`
--
ALTER TABLE `BusinessPartner_bpdepartment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpemployee`
--
ALTER TABLE `BusinessPartner_bpemployee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_bpposition`
--
ALTER TABLE `BusinessPartner_bpposition`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_businesspartner`
--
ALTER TABLE `BusinessPartner_businesspartner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_businesspartner_BPLID`
--
ALTER TABLE `BusinessPartner_businesspartner_BPLID`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `BusinessPartner_business_businesspartner_id_branc_4bdf57c9_uniq` (`businesspartner_id`,`branch_id`),
  ADD KEY `BusinessPartner_busi_branch_id_08b51085_fk_Company_b` (`branch_id`);

--
-- Indexes for table `BusinessPartner_customercode`
--
ALTER TABLE `BusinessPartner_customercode`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_customergroup`
--
ALTER TABLE `BusinessPartner_customergroup`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `BusinessPartner_customerzone`
--
ALTER TABLE `BusinessPartner_customerzone`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Campaign_campaign`
--
ALTER TABLE `Campaign_campaign`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Campaign_campaign_CampaignOwner_id_bd3c5d7e_fk_Employee_` (`CampaignOwner_id`),
  ADD KEY `Campaign_campaign_CampaignSetId_id_a4247c7b_fk_Campaign_` (`CampaignSetId_id`);

--
-- Indexes for table `Campaign_campaignset`
--
ALTER TABLE `Campaign_campaignset`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Campaign_campaignset_CampaignSetOwner_id_d7400ddd_fk_Employee_` (`CampaignSetOwner_id`),
  ADD KEY `Campaign_campaignset_CreateBy_id_b1ea51b5_fk_Employee_` (`CreateBy_id`);

--
-- Indexes for table `Campaign_campaignsetmembers`
--
ALTER TABLE `Campaign_campaignsetmembers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Campaign_campaignset_CampSetId_id_0a3a55b7_fk_Campaign_` (`CampSetId_id`);

--
-- Indexes for table `Category_category`
--
ALTER TABLE `Category_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Number` (`Number`);

--
-- Indexes for table `ClientBankDetails_clientbankdetails`
--
ALTER TABLE `ClientBankDetails_clientbankdetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Company_branch`
--
ALTER TABLE `Company_branch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Company_company`
--
ALTER TABLE `Company_company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Countries_countries`
--
ALTER TABLE `Countries_countries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Countries_states`
--
ALTER TABLE `Countries_states`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

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
-- Indexes for table `Employee_employee`
--
ALTER TABLE `Employee_employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `SalesEmployeeCode` (`SalesEmployeeCode`);

--
-- Indexes for table `Employee_target`
--
ALTER TABLE `Employee_target`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Employee_target_SalesPersonCode_id_551e269b_fk_Employee_` (`SalesPersonCode_id`),
  ADD KEY `Employee_target_YearTarget_id_a65a6415_fk_Employee_targetyr_id` (`YearTarget_id`);

--
-- Indexes for table `Employee_targetqty`
--
ALTER TABLE `Employee_targetqty`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Employee_targetqty_SalesPersonCode_id_ea703785_fk_Employee_` (`SalesPersonCode_id`),
  ADD KEY `Employee_targetqty_YearTarget_id_93ad28c8_fk_Employee_` (`YearTarget_id`),
  ADD KEY `Employee_targetqty_reportingTo_id_580c81c2_fk_Employee_` (`reportingTo_id`);

--
-- Indexes for table `Employee_targetyr`
--
ALTER TABLE `Employee_targetyr`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Employee_targetyr_SalesPersonCode_id_9df9640d_fk_Employee_` (`SalesPersonCode_id`),
  ADD KEY `Employee_targetyr_reportingTo_id_3573c9bf_fk_Employee_` (`reportingTo_id`);

--
-- Indexes for table `Industries_industries`
--
ALTER TABLE `Industries_industries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Invoice_addressextension`
--
ALTER TABLE `Invoice_addressextension`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Invoice_documentlines`
--
ALTER TABLE `Invoice_documentlines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Invoice_invoice`
--
ALTER TABLE `Invoice_invoice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Item_department`
--
ALTER TABLE `Item_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Item_item`
--
ALTER TABLE `Item_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Item_item_ItemsGroupCode_id_d16d1b0b_fk_Category_category_Number` (`ItemsGroupCode_id`);

--
-- Indexes for table `Item_tax`
--
ALTER TABLE `Item_tax`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Lead_chatter`
--
ALTER TABLE `Lead_chatter`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Lead_lead`
--
ALTER TABLE `Lead_lead`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Lead_lead_assignedTo_id_f68215e3_fk_Employee_employee_id` (`assignedTo_id`),
  ADD KEY `Lead_lead_employeeId_id_2da1ad6f_fk_Employee_employee_id` (`employeeId_id`);

--
-- Indexes for table `Lead_leaditem`
--
ALTER TABLE `Lead_leaditem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Lead_source`
--
ALTER TABLE `Lead_source`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Lead_type`
--
ALTER TABLE `Lead_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Notification_notification`
--
ALTER TABLE `Notification_notification`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Opportunity_line`
--
ALTER TABLE `Opportunity_line`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Opportunity_oppitem`
--
ALTER TABLE `Opportunity_oppitem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Opportunity_opportunity`
--
ALTER TABLE `Opportunity_opportunity`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Opportunity_stage`
--
ALTER TABLE `Opportunity_stage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Opportunity_staticstage`
--
ALTER TABLE `Opportunity_staticstage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order_addendumrequest`
--
ALTER TABLE `Order_addendumrequest`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order_addressextension`
--
ALTER TABLE `Order_addressextension`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order_custcode`
--
ALTER TABLE `Order_custcode`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order_documentlines`
--
ALTER TABLE `Order_documentlines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Order_order`
--
ALTER TABLE `Order_order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PaymentTermsTypes_paymenttermstypes`
--
ALTER TABLE `PaymentTermsTypes_paymenttermstypes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Project_project`
--
ALTER TABLE `Project_project`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Quotation_addressextension`
--
ALTER TABLE `Quotation_addressextension`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Quotation_appslave`
--
ALTER TABLE `Quotation_appslave`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Quotation_documentlines`
--
ALTER TABLE `Quotation_documentlines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Quotation_quotation`
--
ALTER TABLE `Quotation_quotation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Quotation_quotation_APPROVEID_id_9834a047_fk_Employee_` (`APPROVEID_id`),
  ADD KEY `Quotation_quotation_Level1_id_ef56b38c_fk_Employee_` (`Level1_id`),
  ADD KEY `Quotation_quotation_Level2_id_1efba32f_fk_Employee_` (`Level2_id`),
  ADD KEY `Quotation_quotation_Level3_id_6bd281ad_fk_Employee_` (`Level3_id`);

--
-- Indexes for table `Tender_corrigendumlist`
--
ALTER TABLE `Tender_corrigendumlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_coverdetail`
--
ALTER TABLE `Tender_coverdetail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_critcaldates`
--
ALTER TABLE `Tender_critcaldates`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_documents`
--
ALTER TABLE `Tender_documents`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_lowestone`
--
ALTER TABLE `Tender_lowestone`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_paymentinstrument`
--
ALTER TABLE `Tender_paymentinstrument`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_technicalopening`
--
ALTER TABLE `Tender_technicalopening`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_tender`
--
ALTER TABLE `Tender_tender`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_tenderopening`
--
ALTER TABLE `Tender_tenderopening`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_tendersubmission`
--
ALTER TABLE `Tender_tendersubmission`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_tenitem`
--
ALTER TABLE `Tender_tenitem`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Tender_workoritemdetails`
--
ALTER TABLE `Tender_workoritemdetails`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Activity_activity`
--
ALTER TABLE `Activity_activity`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `Activity_chatter`
--
ALTER TABLE `Activity_chatter`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Activity_maps`
--
ALTER TABLE `Activity_maps`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Attachment_attachment`
--
ALTER TABLE `Attachment_attachment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=187;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=301;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Branch_branch`
--
ALTER TABLE `Branch_branch`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpaddresses`
--
ALTER TABLE `BusinessPartner_bpaddresses`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpbranch`
--
ALTER TABLE `BusinessPartner_bpbranch`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpcurrency`
--
ALTER TABLE `BusinessPartner_bpcurrency`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpdepartment`
--
ALTER TABLE `BusinessPartner_bpdepartment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpemployee`
--
ALTER TABLE `BusinessPartner_bpemployee`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `BusinessPartner_bpposition`
--
ALTER TABLE `BusinessPartner_bpposition`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `BusinessPartner_businesspartner`
--
ALTER TABLE `BusinessPartner_businesspartner`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `BusinessPartner_businesspartner_BPLID`
--
ALTER TABLE `BusinessPartner_businesspartner_BPLID`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `BusinessPartner_customercode`
--
ALTER TABLE `BusinessPartner_customercode`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `BusinessPartner_customergroup`
--
ALTER TABLE `BusinessPartner_customergroup`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `BusinessPartner_customerzone`
--
ALTER TABLE `BusinessPartner_customerzone`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Campaign_campaign`
--
ALTER TABLE `Campaign_campaign`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Campaign_campaignset`
--
ALTER TABLE `Campaign_campaignset`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Campaign_campaignsetmembers`
--
ALTER TABLE `Campaign_campaignsetmembers`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=244;

--
-- AUTO_INCREMENT for table `Category_category`
--
ALTER TABLE `Category_category`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ClientBankDetails_clientbankdetails`
--
ALTER TABLE `ClientBankDetails_clientbankdetails`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Company_branch`
--
ALTER TABLE `Company_branch`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Company_company`
--
ALTER TABLE `Company_company`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Countries_countries`
--
ALTER TABLE `Countries_countries`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=243;

--
-- AUTO_INCREMENT for table `Countries_states`
--
ALTER TABLE `Countries_states`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3754;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `Employee_employee`
--
ALTER TABLE `Employee_employee`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=108;

--
-- AUTO_INCREMENT for table `Employee_target`
--
ALTER TABLE `Employee_target`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `Employee_targetqty`
--
ALTER TABLE `Employee_targetqty`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Employee_targetyr`
--
ALTER TABLE `Employee_targetyr`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `Industries_industries`
--
ALTER TABLE `Industries_industries`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `Invoice_addressextension`
--
ALTER TABLE `Invoice_addressextension`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Invoice_documentlines`
--
ALTER TABLE `Invoice_documentlines`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Invoice_invoice`
--
ALTER TABLE `Invoice_invoice`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Item_department`
--
ALTER TABLE `Item_department`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Item_item`
--
ALTER TABLE `Item_item`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `Item_tax`
--
ALTER TABLE `Item_tax`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Lead_chatter`
--
ALTER TABLE `Lead_chatter`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Lead_lead`
--
ALTER TABLE `Lead_lead`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT for table `Lead_leaditem`
--
ALTER TABLE `Lead_leaditem`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Lead_source`
--
ALTER TABLE `Lead_source`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `Lead_type`
--
ALTER TABLE `Lead_type`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Notification_notification`
--
ALTER TABLE `Notification_notification`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Opportunity_line`
--
ALTER TABLE `Opportunity_line`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `Opportunity_oppitem`
--
ALTER TABLE `Opportunity_oppitem`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `Opportunity_opportunity`
--
ALTER TABLE `Opportunity_opportunity`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `Opportunity_stage`
--
ALTER TABLE `Opportunity_stage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=265;

--
-- AUTO_INCREMENT for table `Opportunity_staticstage`
--
ALTER TABLE `Opportunity_staticstage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `Order_addendumrequest`
--
ALTER TABLE `Order_addendumrequest`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Order_addressextension`
--
ALTER TABLE `Order_addressextension`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `Order_custcode`
--
ALTER TABLE `Order_custcode`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `Order_documentlines`
--
ALTER TABLE `Order_documentlines`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `Order_order`
--
ALTER TABLE `Order_order`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `PaymentTermsTypes_paymenttermstypes`
--
ALTER TABLE `PaymentTermsTypes_paymenttermstypes`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Project_project`
--
ALTER TABLE `Project_project`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `Quotation_addressextension`
--
ALTER TABLE `Quotation_addressextension`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `Quotation_appslave`
--
ALTER TABLE `Quotation_appslave`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Quotation_documentlines`
--
ALTER TABLE `Quotation_documentlines`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99;

--
-- AUTO_INCREMENT for table `Quotation_quotation`
--
ALTER TABLE `Quotation_quotation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `Tender_corrigendumlist`
--
ALTER TABLE `Tender_corrigendumlist`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_coverdetail`
--
ALTER TABLE `Tender_coverdetail`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_critcaldates`
--
ALTER TABLE `Tender_critcaldates`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_documents`
--
ALTER TABLE `Tender_documents`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_lowestone`
--
ALTER TABLE `Tender_lowestone`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_paymentinstrument`
--
ALTER TABLE `Tender_paymentinstrument`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_technicalopening`
--
ALTER TABLE `Tender_technicalopening`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_tender`
--
ALTER TABLE `Tender_tender`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_tenderopening`
--
ALTER TABLE `Tender_tenderopening`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_tendersubmission`
--
ALTER TABLE `Tender_tendersubmission`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_tenitem`
--
ALTER TABLE `Tender_tenitem`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Tender_workoritemdetails`
--
ALTER TABLE `Tender_workoritemdetails`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `BusinessPartner_businesspartner_BPLID`
--
ALTER TABLE `BusinessPartner_businesspartner_BPLID`
  ADD CONSTRAINT `BusinessPartner_busi_branch_id_08b51085_fk_Company_b` FOREIGN KEY (`branch_id`) REFERENCES `Company_branch` (`id`),
  ADD CONSTRAINT `BusinessPartner_busi_businesspartner_id_360bff0a_fk_BusinessP` FOREIGN KEY (`businesspartner_id`) REFERENCES `BusinessPartner_businesspartner` (`id`);

--
-- Constraints for table `Campaign_campaign`
--
ALTER TABLE `Campaign_campaign`
  ADD CONSTRAINT `Campaign_campaign_CampaignOwner_id_bd3c5d7e_fk_Employee_` FOREIGN KEY (`CampaignOwner_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Campaign_campaign_CampaignSetId_id_a4247c7b_fk_Campaign_` FOREIGN KEY (`CampaignSetId_id`) REFERENCES `Campaign_campaignset` (`id`);

--
-- Constraints for table `Campaign_campaignset`
--
ALTER TABLE `Campaign_campaignset`
  ADD CONSTRAINT `Campaign_campaignset_CampaignSetOwner_id_d7400ddd_fk_Employee_` FOREIGN KEY (`CampaignSetOwner_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Campaign_campaignset_CreateBy_id_b1ea51b5_fk_Employee_` FOREIGN KEY (`CreateBy_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`);

--
-- Constraints for table `Campaign_campaignsetmembers`
--
ALTER TABLE `Campaign_campaignsetmembers`
  ADD CONSTRAINT `Campaign_campaignset_CampSetId_id_0a3a55b7_fk_Campaign_` FOREIGN KEY (`CampSetId_id`) REFERENCES `Campaign_campaignset` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `Employee_target`
--
ALTER TABLE `Employee_target`
  ADD CONSTRAINT `Employee_target_SalesPersonCode_id_551e269b_fk_Employee_` FOREIGN KEY (`SalesPersonCode_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Employee_target_YearTarget_id_a65a6415_fk_Employee_targetyr_id` FOREIGN KEY (`YearTarget_id`) REFERENCES `Employee_targetyr` (`id`);

--
-- Constraints for table `Employee_targetqty`
--
ALTER TABLE `Employee_targetqty`
  ADD CONSTRAINT `Employee_targetqty_reportingTo_id_580c81c2_fk_Employee_` FOREIGN KEY (`reportingTo_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Employee_targetqty_SalesPersonCode_id_ea703785_fk_Employee_` FOREIGN KEY (`SalesPersonCode_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Employee_targetqty_YearTarget_id_93ad28c8_fk_Employee_` FOREIGN KEY (`YearTarget_id`) REFERENCES `Employee_targetyr` (`id`);

--
-- Constraints for table `Employee_targetyr`
--
ALTER TABLE `Employee_targetyr`
  ADD CONSTRAINT `Employee_targetyr_reportingTo_id_3573c9bf_fk_Employee_` FOREIGN KEY (`reportingTo_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Employee_targetyr_SalesPersonCode_id_9df9640d_fk_Employee_` FOREIGN KEY (`SalesPersonCode_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`);

--
-- Constraints for table `Item_item`
--
ALTER TABLE `Item_item`
  ADD CONSTRAINT `Item_item_ItemsGroupCode_id_d16d1b0b_fk_Category_category_Number` FOREIGN KEY (`ItemsGroupCode_id`) REFERENCES `Category_category` (`Number`);

--
-- Constraints for table `Lead_lead`
--
ALTER TABLE `Lead_lead`
  ADD CONSTRAINT `Lead_lead_assignedTo_id_f68215e3_fk_Employee_employee_id` FOREIGN KEY (`assignedTo_id`) REFERENCES `Employee_employee` (`id`),
  ADD CONSTRAINT `Lead_lead_employeeId_id_2da1ad6f_fk_Employee_employee_id` FOREIGN KEY (`employeeId_id`) REFERENCES `Employee_employee` (`id`);

--
-- Constraints for table `Quotation_quotation`
--
ALTER TABLE `Quotation_quotation`
  ADD CONSTRAINT `Quotation_quotation_APPROVEID_id_9834a047_fk_Employee_` FOREIGN KEY (`APPROVEID_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Quotation_quotation_Level1_id_ef56b38c_fk_Employee_` FOREIGN KEY (`Level1_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Quotation_quotation_Level2_id_1efba32f_fk_Employee_` FOREIGN KEY (`Level2_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`),
  ADD CONSTRAINT `Quotation_quotation_Level3_id_6bd281ad_fk_Employee_` FOREIGN KEY (`Level3_id`) REFERENCES `Employee_employee` (`SalesEmployeeCode`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
