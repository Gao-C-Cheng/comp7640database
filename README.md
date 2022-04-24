# comp7640database

- source retail.sql #create tables or you can create table using SQL command

CREATE SCHEMA IF NOT EXISTS `retail` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `retail` ;

-- -----------------------------------------------------
-- Table `retail`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`customer` (
  `idcustomer` INT NOT NULL,
  `address` VARCHAR(45) NULL DEFAULT NULL,
  `cname` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idcustomer`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`items` (
  `idItems` INT NOT NULL,
  `Itname` VARCHAR(45) NOT NULL,
  `prince` DECIMAL(6,2) NOT NULL,
  `keyword` VARCHAR(10) NOT NULL,
  `qty` INT NOT NULL,
  PRIMARY KEY (`idItems`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`orders` (
  `idorders` INT NOT NULL,
  `idcustomer` INT NOT NULL,
  `order_date` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`idorders`),
  INDEX `idcustomer_idx` (`idcustomer` ASC) VISIBLE,
  CONSTRAINT `idcustomer`
    FOREIGN KEY (`idcustomer`)
    REFERENCES `retail`.`customer` (`idcustomer`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`order_has_items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`order_has_items` (
  `idorders` INT NOT NULL,
  `idItems` INT NOT NULL,
  `order_date` DATE NULL DEFAULT NULL,
  `qty` INT NOT NULL,
  PRIMARY KEY (`idorders`, `idItems`),
  INDEX `fk_items_idx` (`idItems` ASC) VISIBLE,
  CONSTRAINT `fk_items`
    FOREIGN KEY (`idItems`)
    REFERENCES `retail`.`items` (`idItems`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_orders`
    FOREIGN KEY (`idorders`)
    REFERENCES `retail`.`orders` (`idorders`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`website`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`website` (
  `idWebsite` INT NOT NULL,
  `WebsitName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idWebsite`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`shop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`shop` (
  `idshop` INT NOT NULL,
  `sname` CHAR(20) NULL DEFAULT NULL,
  `rating` INT NULL DEFAULT NULL,
  `Location` CHAR(45) NULL DEFAULT NULL,
  `idWebsite` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idshop`),
  INDEX `fk_website` (`idWebsite` ASC) VISIBLE,
  CONSTRAINT `fk_website`
    FOREIGN KEY (`idWebsite`)
    REFERENCES `retail`.`website` (`idWebsite`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


-- -----------------------------------------------------
-- Table `retail`.`shop_has_items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retail`.`shop_has_items` (
  `idItems` INT NOT NULL,
  `idshop` INT NOT NULL,
  PRIMARY KEY (`idItems`, `idshop`),
  INDEX `fk_idshop_idx` (`idshop` ASC) VISIBLE,
  CONSTRAINT `fk_idItems`
    FOREIGN KEY (`idItems`)
    REFERENCES `retail`.`items` (`idItems`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_idshop`
    FOREIGN KEY (`idshop`)
    REFERENCES `retail`.`shop` (`idshop`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

insertion:
INSERT INTO `retail`.`website` (`idWebsite`, `WebsitName`) VALUES ('30', 'group 30 retail');

INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('1', 'pencil', '5.2', 'stationery', '20');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('2', 'notbook', '20.3', 'stationery', '20');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('3', 'eraser', '3.3', 'stationery', '30');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('4', 'orange', '4', 'fruit', '15');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('5', 'calculator', '200', 'stationery', '100');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('6', 'tomato', '4.23', 'vegetable', '100');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('7', 'potato', '3.99', 'vegetable', '160');
INSERT INTO `retail`.`items` (`idItems`, `Itname`, `prince`, `keyword`, `qty`) VALUES ('8', 'mango', '20.5', 'fruit', '13');

edit config.ini file

run: python main.py


