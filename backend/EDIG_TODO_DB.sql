CREATE SCHEMA `EDIT_TODO`;

CREATE TABLE `EDIG_TODO`.`todos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NOT NULL,
  `complete` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`ID`))