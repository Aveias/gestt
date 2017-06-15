-- --------------------------------------------------------
-- Hôte :                        127.0.0.1
-- Version du serveur:           10.2.6-MariaDB - mariadb.org binary distribution
-- SE du serveur:                Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Export de la structure de la base pour gestt
DROP DATABASE IF EXISTS `gestt`;
CREATE DATABASE IF NOT EXISTS `gestt` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `gestt`;

-- Export de la structure de la table gestt. client
DROP TABLE IF EXISTS `client`;
CREATE TABLE IF NOT EXISTS `client` (
  `IDClie` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `Raison sociale` char(100) NOT NULL,
  `Code client` char(20) DEFAULT NULL,
  PRIMARY KEY (`IDClie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Client de l''entreprise, commanditaire du projet';

-- Export de données de la table gestt.client : ~0 rows (environ)
DELETE FROM `client`;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
/*!40000 ALTER TABLE `client` ENABLE KEYS */;

-- Export de la structure de la table gestt. date
DROP TABLE IF EXISTS `date`;
CREATE TABLE IF NOT EXISTS `date` (
  `IDDate` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  PRIMARY KEY (`IDDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Liste des dates';

-- Export de données de la table gestt.date : ~0 rows (environ)
DELETE FROM `date`;
/*!40000 ALTER TABLE `date` DISABLE KEYS */;
/*!40000 ALTER TABLE `date` ENABLE KEYS */;

-- Export de la structure de la table gestt. description
DROP TABLE IF EXISTS `description`;
CREATE TABLE IF NOT EXISTS `description` (
  `IDDesc` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `IDType` tinyint(3) unsigned NOT NULL,
  `Libellé` char(200) NOT NULL,
  PRIMARY KEY (`IDDesc`),
  KEY `FK_description_type` (`IDType`),
  CONSTRAINT `FK_description_type` FOREIGN KEY (`IDType`) REFERENCES `type` (`IDType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Description de la tâche';

-- Export de données de la table gestt.description : ~0 rows (environ)
DELETE FROM `description`;
/*!40000 ALTER TABLE `description` DISABLE KEYS */;
/*!40000 ALTER TABLE `description` ENABLE KEYS */;

-- Export de la structure de la table gestt. fonction
DROP TABLE IF EXISTS `fonction`;
CREATE TABLE IF NOT EXISTS `fonction` (
  `IDFonc` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `IDPole` tinyint(3) unsigned NOT NULL,
  `Intitulé` char(100) NOT NULL,
  PRIMARY KEY (`IDFonc`),
  KEY `FK_fonction_pole` (`IDPole`),
  CONSTRAINT `FK_fonction_pole` FOREIGN KEY (`IDPole`) REFERENCES `pole` (`IDpole`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Libellé des fonctions des employés de l''entreprise';

-- Export de données de la table gestt.fonction : ~0 rows (environ)
DELETE FROM `fonction`;
/*!40000 ALTER TABLE `fonction` DISABLE KEYS */;
INSERT INTO `fonction` (`IDFonc`, `IDPole`, `Intitulé`) VALUES
	(1, 2, 'test');
/*!40000 ALTER TABLE `fonction` ENABLE KEYS */;

-- Export de la structure de la table gestt. frais
DROP TABLE IF EXISTS `frais`;
CREATE TABLE IF NOT EXISTS `frais` (
  `IDFrai` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `Description` char(250) NOT NULL,
  `Montant` float NOT NULL,
  `IDGenr` tinyint(3) unsigned NOT NULL,
  `IDProj` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`IDFrai`),
  KEY `FK_frais_projet` (`IDProj`),
  KEY `FK_frais_genre` (`IDGenr`),
  CONSTRAINT `FK_frais_genre` FOREIGN KEY (`IDGenr`) REFERENCES `genre` (`IDGenr`),
  CONSTRAINT `FK_frais_projet` FOREIGN KEY (`IDProj`) REFERENCES `projet` (`IDProj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Frias engagés pour un projet';

-- Export de données de la table gestt.frais : ~0 rows (environ)
DELETE FROM `frais`;
/*!40000 ALTER TABLE `frais` DISABLE KEYS */;
/*!40000 ALTER TABLE `frais` ENABLE KEYS */;

-- Export de la structure de la table gestt. genre
DROP TABLE IF EXISTS `genre`;
CREATE TABLE IF NOT EXISTS `genre` (
  `IDGenr` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `Type` char(10) NOT NULL,
  PRIMARY KEY (`IDGenr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Type de frais';

-- Export de données de la table gestt.genre : ~0 rows (environ)
DELETE FROM `genre`;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;

-- Export de la structure de la table gestt. pole
DROP TABLE IF EXISTS `pole`;
CREATE TABLE IF NOT EXISTS `pole` (
  `IDpole` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `Libelle` char(50) NOT NULL,
  PRIMARY KEY (`IDpole`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='Pôle principaux de l''entreprise';

-- Export de données de la table gestt.pole : ~1 rows (environ)
DELETE FROM `pole`;
/*!40000 ALTER TABLE `pole` DISABLE KEYS */;
INSERT INTO `pole` (`IDpole`, `Libelle`) VALUES
	(2, 'test');
/*!40000 ALTER TABLE `pole` ENABLE KEYS */;

-- Export de la structure de la table gestt. projet
DROP TABLE IF EXISTS `projet`;
CREATE TABLE IF NOT EXISTS `projet` (
  `IDProj` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `Intitulé` char(50) NOT NULL,
  `Description` text DEFAULT NULL,
  `NumDossier` char(20) DEFAULT NULL,
  `Budget` float unsigned DEFAULT NULL,
  `IDUtil` tinyint(3) unsigned NOT NULL,
  `IDStat` tinyint(3) unsigned NOT NULL,
  `IDClient` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`IDProj`),
  KEY `FK_projet_utilisateur` (`IDUtil`),
  KEY `FK_projet_client` (`IDClient`),
  KEY `FK_projet_statut` (`IDStat`),
  CONSTRAINT `FK_projet_client` FOREIGN KEY (`IDClient`) REFERENCES `client` (`IDClie`),
  CONSTRAINT `FK_projet_statut` FOREIGN KEY (`IDStat`) REFERENCES `statut` (`IDStat`),
  CONSTRAINT `FK_projet_utilisateur` FOREIGN KEY (`IDUtil`) REFERENCES `utilisateur` (`IDUtil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Entité projet';

-- Export de données de la table gestt.projet : ~0 rows (environ)
DELETE FROM `projet`;
/*!40000 ALTER TABLE `projet` DISABLE KEYS */;
/*!40000 ALTER TABLE `projet` ENABLE KEYS */;

-- Export de la structure de la table gestt. role
DROP TABLE IF EXISTS `role`;
CREATE TABLE IF NOT EXISTS `role` (
  `IDRole` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `Libellé` char(50) NOT NULL,
  PRIMARY KEY (`IDRole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Liste des rôles utilisateur';

-- Export de données de la table gestt.role : ~0 rows (environ)
DELETE FROM `role`;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;

-- Export de la structure de la table gestt. roleattribution
DROP TABLE IF EXISTS `roleattribution`;
CREATE TABLE IF NOT EXISTS `roleattribution` (
  `IDAttr` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `IDUtil` tinyint(3) unsigned NOT NULL,
  `IDRole` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`IDAttr`),
  KEY `FK_roleattribution_utilisateur` (`IDUtil`),
  KEY `FK_roleattribution_role` (`IDRole`),
  CONSTRAINT `FK_roleattribution_role` FOREIGN KEY (`IDRole`) REFERENCES `role` (`IDRole`),
  CONSTRAINT `FK_roleattribution_utilisateur` FOREIGN KEY (`IDUtil`) REFERENCES `utilisateur` (`IDUtil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Table de croisement d''attribution des rôles aux utilisateurs';

-- Export de données de la table gestt.roleattribution : ~0 rows (environ)
DELETE FROM `roleattribution`;
/*!40000 ALTER TABLE `roleattribution` DISABLE KEYS */;
/*!40000 ALTER TABLE `roleattribution` ENABLE KEYS */;

-- Export de la structure de la table gestt. statut
DROP TABLE IF EXISTS `statut`;
CREATE TABLE IF NOT EXISTS `statut` (
  `IDStat` tinyint(4) unsigned NOT NULL AUTO_INCREMENT,
  `Statut` char(20) NOT NULL,
  PRIMARY KEY (`IDStat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Statut des projets';

-- Export de données de la table gestt.statut : ~0 rows (environ)
DELETE FROM `statut`;
/*!40000 ALTER TABLE `statut` DISABLE KEYS */;
/*!40000 ALTER TABLE `statut` ENABLE KEYS */;

-- Export de la structure de la table gestt. tache
DROP TABLE IF EXISTS `tache`;
CREATE TABLE IF NOT EXISTS `tache` (
  `IDTach` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  `HeureDebut` time NOT NULL,
  `HeureFin` time NOT NULL,
  `Commentaire` text DEFAULT NULL,
  `IDUtil` tinyint(3) unsigned NOT NULL,
  `IDDate` smallint(5) unsigned NOT NULL,
  `IDProj` smallint(5) unsigned NOT NULL,
  `IDDesc` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`IDTach`),
  KEY `FK_tache_utilisateur` (`IDUtil`),
  KEY `FK_tache_date` (`IDDate`),
  KEY `FK_tache_projet` (`IDProj`),
  KEY `FK_tache_description` (`IDDesc`),
  CONSTRAINT `FK_tache_date` FOREIGN KEY (`IDDate`) REFERENCES `date` (`IDDate`),
  CONSTRAINT `FK_tache_description` FOREIGN KEY (`IDDesc`) REFERENCES `description` (`IDDesc`),
  CONSTRAINT `FK_tache_projet` FOREIGN KEY (`IDProj`) REFERENCES `projet` (`IDProj`),
  CONSTRAINT `FK_tache_utilisateur` FOREIGN KEY (`IDUtil`) REFERENCES `utilisateur` (`IDUtil`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Entité d''entrée de temps';

-- Export de données de la table gestt.tache : ~0 rows (environ)
DELETE FROM `tache`;
/*!40000 ALTER TABLE `tache` DISABLE KEYS */;
/*!40000 ALTER TABLE `tache` ENABLE KEYS */;

-- Export de la structure de la table gestt. type
DROP TABLE IF EXISTS `type`;
CREATE TABLE IF NOT EXISTS `type` (
  `IDType` tinyint(4) unsigned NOT NULL AUTO_INCREMENT,
  `Libellé` char(50) NOT NULL,
  PRIMARY KEY (`IDType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Type de tâche';

-- Export de données de la table gestt.type : ~0 rows (environ)
DELETE FROM `type`;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
/*!40000 ALTER TABLE `type` ENABLE KEYS */;

-- Export de la structure de la table gestt. utilisateur
DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `IDUtil` tinyint(3) unsigned NOT NULL AUTO_INCREMENT,
  `IDFonc` tinyint(3) unsigned NOT NULL,
  `Nom` char(50) NOT NULL,
  `Prénom` char(50) NOT NULL,
  `Identifiant` char(20) NOT NULL,
  `MdP` char(255) NOT NULL,
  `SalaireBrut` float DEFAULT NULL,
  PRIMARY KEY (`IDUtil`),
  UNIQUE KEY `Identifiant` (`Identifiant`),
  KEY `FK_utilisateur_fonction` (`IDFonc`),
  CONSTRAINT `FK_utilisateur_fonction` FOREIGN KEY (`IDFonc`) REFERENCES `fonction` (`IDFonc`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COMMENT='Employé de l''entreprise utilisateur du logiciel';

-- Export de données de la table gestt.utilisateur : ~2 rows (environ)
DELETE FROM `utilisateur`;
/*!40000 ALTER TABLE `utilisateur` DISABLE KEYS */;
INSERT INTO `utilisateur` (`IDUtil`, `IDFonc`, `Nom`, `Prénom`, `Identifiant`, `MdP`, `SalaireBrut`) VALUES
	(1, 1, 'Test', 'Test', 'test', '098f6bcd4621d373cade4e832627b4f6', 5000);
/*!40000 ALTER TABLE `utilisateur` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
