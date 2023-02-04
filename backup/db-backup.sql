-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: testsarkari.mysql.pythonanywhere-services.com    Database: testsarkari$sarkarivigyaapan
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_honeypot_loginattempt`
--

DROP TABLE IF EXISTS `admin_honeypot_loginattempt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_honeypot_loginattempt` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `session_key` varchar(50) DEFAULT NULL,
  `user_agent` longtext,
  `timestamp` datetime(6) NOT NULL,
  `path` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_honeypot_loginattempt`
--

LOCK TABLES `admin_honeypot_loginattempt` WRITE;
/*!40000 ALTER TABLE `admin_honeypot_loginattempt` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_honeypot_loginattempt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add site',7,'add_site'),(26,'Can change site',7,'change_site'),(27,'Can delete site',7,'delete_site'),(28,'Can view site',7,'view_site'),(29,'Can add state',8,'add_state'),(30,'Can change state',8,'change_state'),(31,'Can delete state',8,'delete_state'),(32,'Can view state',8,'view_state'),(33,'Can add Job',9,'add_job'),(34,'Can change Job',9,'change_job'),(35,'Can delete Job',9,'delete_job'),(36,'Can view Job',9,'view_job'),(37,'Can add Ministry',10,'add_ministry'),(38,'Can change Ministry',10,'change_ministry'),(39,'Can delete Ministry',10,'delete_ministry'),(40,'Can view Ministry',10,'view_ministry'),(41,'Can add subscriber',11,'add_subscriber'),(42,'Can change subscriber',11,'change_subscriber'),(43,'Can delete subscriber',11,'delete_subscriber'),(44,'Can view subscriber',11,'view_subscriber'),(45,'Can add newsletter',12,'add_newsletter'),(46,'Can change newsletter',12,'change_newsletter'),(47,'Can delete newsletter',12,'delete_newsletter'),(48,'Can view newsletter',12,'view_newsletter'),(49,'Can add tag',13,'add_tag'),(50,'Can change tag',13,'change_tag'),(51,'Can delete tag',13,'delete_tag'),(52,'Can view tag',13,'view_tag'),(53,'Can add tagged item',14,'add_taggeditem'),(54,'Can change tagged item',14,'change_taggeditem'),(55,'Can delete tagged item',14,'delete_taggeditem'),(56,'Can view tagged item',14,'view_taggeditem'),(57,'Can add login attempt',15,'add_loginattempt'),(58,'Can change login attempt',15,'change_loginattempt'),(59,'Can delete login attempt',15,'delete_loginattempt'),(60,'Can view login attempt',15,'view_loginattempt');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$DurIKn8xD5JGbIvYUSWLK5$o02mLy6fi+gnKo10URln7+et/Dfxt562eT98YQLymrs=','2023-01-23 19:23:53.131928',1,'Tanweer','The Tanweer','','tanweeralam1312@gmail.com',1,1,'2023-01-23 08:13:51.000000'),(2,'pbkdf2_sha256$260000$EcO1rMUhjr57FliHomi8uN$YxYGGknBkfQiZWsppM++Rd/sTAvn/5npnB3KlwgjUDQ=',NULL,1,'Sohan','','','sohan8092@gmail.com',1,1,'2023-01-23 08:18:24.059630');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-01-23 08:21:55.295988','1','Tanweer',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',4,1),(2,'2023-01-23 19:24:20.624630','1','sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Domain name\"]}}]',7,1),(3,'2023-01-23 19:26:45.628195','1','www.sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',7,1),(4,'2023-01-23 19:26:53.796959','1','www.sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Display name\"]}}]',7,1),(5,'2023-01-23 19:27:14.909031','1','sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',7,1),(6,'2023-01-23 19:27:27.789375','1','sarkarivigyaapan.com',2,'[]',7,1),(7,'2023-01-23 19:28:08.993809','1','www.sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',7,1),(8,'2023-01-23 19:36:42.264809','1','sarkarivigyaapan.com',2,'[{\"changed\": {\"fields\": [\"Domain name\", \"Display name\"]}}]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(15,'admin_honeypot','loginattempt'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'jobs','job'),(10,'jobs','ministry'),(8,'jobs','state'),(12,'newsletters','newsletter'),(11,'newsletters','subscriber'),(6,'sessions','session'),(7,'sites','site'),(13,'taggit','tag'),(14,'taggit','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-01-23 08:02:11.358026'),(2,'auth','0001_initial','2023-01-23 08:03:11.329218'),(3,'admin','0001_initial','2023-01-23 08:03:23.820200'),(4,'admin','0002_logentry_remove_auto_add','2023-01-23 08:03:23.836093'),(5,'admin','0003_logentry_add_action_flag_choices','2023-01-23 08:03:23.849370'),(6,'admin_honeypot','0001_initial','2023-01-23 08:03:33.130258'),(7,'admin_honeypot','0002_auto_20160208_0854','2023-01-23 08:03:33.192995'),(8,'admin_honeypot','0003_alter_loginattempt_id','2023-01-23 08:03:33.255486'),(9,'contenttypes','0002_remove_content_type_name','2023-01-23 08:03:33.356877'),(10,'auth','0002_alter_permission_name_max_length','2023-01-23 08:03:33.417371'),(11,'auth','0003_alter_user_email_max_length','2023-01-23 08:03:33.474637'),(12,'auth','0004_alter_user_username_opts','2023-01-23 08:03:33.488299'),(13,'auth','0005_alter_user_last_login_null','2023-01-23 08:03:33.557097'),(14,'auth','0006_require_contenttypes_0002','2023-01-23 08:03:33.563176'),(15,'auth','0007_alter_validators_add_error_messages','2023-01-23 08:03:33.575756'),(16,'auth','0008_alter_user_username_max_length','2023-01-23 08:03:33.633034'),(17,'auth','0009_alter_user_last_name_max_length','2023-01-23 08:03:33.718376'),(18,'auth','0010_alter_group_name_max_length','2023-01-23 08:03:33.787604'),(19,'auth','0011_update_proxy_permissions','2023-01-23 08:03:33.802198'),(20,'auth','0012_alter_user_first_name_max_length','2023-01-23 08:03:33.878142'),(21,'taggit','0001_initial','2023-01-23 08:03:43.790244'),(22,'taggit','0002_auto_20150616_2121','2023-01-23 08:03:43.860008'),(23,'taggit','0003_taggeditem_add_unique_index','2023-01-23 08:03:43.908343'),(24,'taggit','0004_alter_taggeditem_content_type_alter_taggeditem_tag','2023-01-23 08:03:43.930531'),(25,'taggit','0005_auto_20220424_2025','2023-01-23 08:03:43.940041'),(26,'jobs','0001_initial','2023-01-23 08:04:27.249807'),(27,'jobs','0002_auto_20221210_1637','2023-01-23 08:04:28.989587'),(28,'jobs','0003_auto_20221214_1420','2023-01-23 08:04:29.044628'),(29,'jobs','0004_auto_20221226_1635','2023-01-23 08:04:36.191739'),(30,'jobs','0005_job_tags','2023-01-23 08:04:36.210270'),(31,'jobs','0006_auto_20230104_2030','2023-01-23 08:05:03.773044'),(32,'jobs','0007_auto_20230104_2051','2023-01-23 08:05:05.006025'),(33,'jobs','0008_alter_job_tags','2023-01-23 08:05:05.033014'),(34,'jobs','0009_job_keywords','2023-01-23 08:05:06.354189'),(35,'jobs','0010_auto_20230116_0700','2023-01-23 08:05:16.321326'),(36,'jobs','0011_remove_job_dept_of_ministry','2023-01-23 08:05:16.466668'),(37,'jobs','0012_job_image','2023-01-23 08:05:17.674815'),(38,'jobs','0013_auto_20230119_0819','2023-01-23 08:05:17.721438'),(39,'jobs','0014_state_state','2023-01-23 08:05:19.277026'),(40,'jobs','0015_remove_state_state','2023-01-23 08:05:19.348328'),(41,'jobs','0016_auto_20230121_0624','2023-01-23 08:05:20.939243'),(42,'jobs','0017_job_is_archived','2023-01-23 08:05:22.198878'),(43,'main','0001_initial','2023-01-23 08:05:27.694821'),(44,'main','0002_delete_main','2023-01-23 08:05:27.720964'),(45,'newsletters','0001_initial','2023-01-23 08:05:34.781059'),(46,'newsletters','0002_newsletter','2023-01-23 08:05:41.625457'),(47,'sessions','0001_initial','2023-01-23 08:05:46.706242'),(48,'sites','0001_initial','2023-01-23 08:05:51.162898'),(49,'sites','0002_alter_domain_unique','2023-01-23 08:05:51.246467');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('yijvyq74g7wh3jjzr96vgnyjfzfynhqz','.eJxVjDsOwjAQBe_iGllar-MPJT1nsNbeNQ6gRIqTCnF3iJQC2jcz76USbWtLW5cljazOCtTpd8tUHjLtgO803WZd5mldxqx3RR-06-vM8rwc7t9Bo96-NVpnS-UgUOOAzoIhRELnLWTD1YMECVCxRLFgib0JLuaCjnjgmqN6fwDSHzfg:1pK2Q5:8u8PfVSvq8HM9RpRk9h8or95bV5JBT4g8I5EEicqitI','2023-02-06 19:23:53.147189');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'sarkarivigyaapan.com','sarkarivigyaapan.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job`
--

DROP TABLE IF EXISTS `jobs_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_job` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `post_title` varchar(200) NOT NULL,
  `brief_intro` longtext NOT NULL,
  `notification_date` date DEFAULT NULL,
  `online_application_date` date DEFAULT NULL,
  `application_expiry_date` datetime(6) DEFAULT NULL,
  `application_mode` varchar(30) NOT NULL,
  `application_link` varchar(200) DEFAULT NULL,
  `minimum_qualification` varchar(50) NOT NULL,
  `total_posts` int(10) unsigned NOT NULL,
  `application_fee` longtext NOT NULL,
  `official_site` varchar(200) DEFAULT NULL,
  `admit_card_link` varchar(200) DEFAULT NULL,
  `notification_link` varchar(200) DEFAULT NULL,
  `is_published` tinyint(1) NOT NULL,
  `created_on` date NOT NULL,
  `updated_on` date NOT NULL,
  `slug` varchar(300) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `state_id` bigint(20) DEFAULT NULL,
  `content` longtext NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `result_link` varchar(200) DEFAULT NULL,
  `syllabus_link` varchar(200) DEFAULT NULL,
  `answerkey_link` varchar(200) DEFAULT NULL,
  `correction_date` date DEFAULT NULL,
  `exam_date` date DEFAULT NULL,
  `fee_last_date` date DEFAULT NULL,
  `is_admission` tinyint(1) NOT NULL,
  `keywords` varchar(200) NOT NULL,
  `ministry_id` bigint(20) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `age` longtext NOT NULL,
  `is_archived` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_job_author_id_0b2faee3_fk_auth_user_id` (`author_id`),
  KEY `jobs_job_state_id_0caa2221_fk_jobs_state_id` (`state_id`),
  KEY `jobs_job_slug_3118e1f8` (`slug`),
  KEY `jobs_job_ministry_id_b2f0f318_fk_jobs_ministry_id` (`ministry_id`),
  CONSTRAINT `jobs_job_author_id_0b2faee3_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `jobs_job_ministry_id_b2f0f318_fk_jobs_ministry_id` FOREIGN KEY (`ministry_id`) REFERENCES `jobs_ministry` (`id`),
  CONSTRAINT `jobs_job_state_id_0caa2221_fk_jobs_state_id` FOREIGN KEY (`state_id`) REFERENCES `jobs_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job`
--

LOCK TABLES `jobs_job` WRITE;
/*!40000 ALTER TABLE `jobs_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_ministry`
--

DROP TABLE IF EXISTS `jobs_ministry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_ministry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(180) DEFAULT NULL,
  `slug` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_ministry`
--

LOCK TABLES `jobs_ministry` WRITE;
/*!40000 ALTER TABLE `jobs_ministry` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_ministry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_state`
--

DROP TABLE IF EXISTS `jobs_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs_state` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `slug` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_state_slug_9a06a236` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_state`
--

LOCK TABLES `jobs_state` WRITE;
/*!40000 ALTER TABLE `jobs_state` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `newsletters_newsletter`
--

DROP TABLE IF EXISTS `newsletters_newsletter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newsletters_newsletter` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `subject` varchar(150) NOT NULL,
  `contents` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newsletters_newsletter`
--

LOCK TABLES `newsletters_newsletter` WRITE;
/*!40000 ALTER TABLE `newsletters_newsletter` DISABLE KEYS */;
/*!40000 ALTER TABLE `newsletters_newsletter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `newsletters_subscriber`
--

DROP TABLE IF EXISTS `newsletters_subscriber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `newsletters_subscriber` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `conf_num` varchar(15) NOT NULL,
  `confirmed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `newsletters_subscriber`
--

LOCK TABLES `newsletters_subscriber` WRITE;
/*!40000 ALTER TABLE `newsletters_subscriber` DISABLE KEYS */;
INSERT INTO `newsletters_subscriber` VALUES (1,'tanweeralam1312@gmail.com','913325344434',0);
/*!40000 ALTER TABLE `newsletters_subscriber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_tag`
--

DROP TABLE IF EXISTS `taggit_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_tag`
--

LOCK TABLES `taggit_tag` WRITE;
/*!40000 ALTER TABLE `taggit_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `taggit_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taggit_taggeditem`
--

DROP TABLE IF EXISTS `taggit_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taggit_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uniq` (`content_type_id`,`object_id`,`tag_id`),
  KEY `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` (`tag_id`),
  KEY `taggit_taggeditem_object_id_e2d7d1df` (`object_id`),
  KEY `taggit_taggeditem_content_type_id_object_id_196cc965_idx` (`content_type_id`,`object_id`),
  CONSTRAINT `taggit_taggeditem_content_type_id_9957a03c_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `taggit_taggeditem_tag_id_f4f5b767_fk_taggit_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `taggit_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taggit_taggeditem`
--

LOCK TABLES `taggit_taggeditem` WRITE;
/*!40000 ALTER TABLE `taggit_taggeditem` DISABLE KEYS */;
/*!40000 ALTER TABLE `taggit_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-24 11:25:48