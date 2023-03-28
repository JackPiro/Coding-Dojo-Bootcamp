-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ohana_rideshare_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ohana_rideshare_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ohana_rideshare_schema` DEFAULT CHARACTER SET utf8 ;
USE `ohana_rideshare_schema` ;

-- -----------------------------------------------------
-- Table `ohana_rideshare_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ohana_rideshare_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ohana_rideshare_schema`.`ride_requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ohana_rideshare_schema`.`ride_requests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NULL,
  `destination` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ohana_rideshare_schema`.`rides`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ohana_rideshare_schema`.`rides` (
  `user_id` INT NOT NULL,
  `ride_request_id` INT NOT NULL,
  INDEX `fk_rides_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_rides_ride_requests1_idx` (`ride_request_id` ASC) VISIBLE,
  CONSTRAINT `fk_rides_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `ohana_rideshare_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rides_ride_requests1`
    FOREIGN KEY (`ride_request_id`)
    REFERENCES `ohana_rideshare_schema`.`ride_requests` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
