CREATE TABLE `datascience`.`badges` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `UserId` VARCHAR(45) NULL,
  `Name` VARCHAR(45) NULL,
  `Date` DATETIME NULL,
  `Class` INT NULL,
  `TagBased` BIT NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`comments` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `PostId` INT NULL,
  `score` DECIMAL NULL,
  `text` VARCHAR(255) NULL,
  `UserId` VARCHAR(45) NULL,
 PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`users` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `reputation` VARCHAR(45) NULL,
  `CreationDate` DATETIME NULL,
  `DisplayName` VARCHAR(45) NULL,
  `LastAccessDate` DATETIME NULL,
  `WebsiteUrl` VARCHAR(255) NULL,
  `Location` VARCHAR(255) NULL,
  `AboutMe` VARCHAR(255) NULL,
  `Views` INT NULL,
  `UpVotes` INT NULL,
  `DownVotes` INT NULL,
  `AccountId` INT NULL,
 PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`posthistory` (
   `Id` INT NOT NULL AUTO_INCREMENT,
   `PostHistoryTypeiD` INT NULL,
   `PostId` INT NULL,
   `RevisionGUID` VARCHAR(255) NULL,
   `CreationDate` DATETIME NULL,
   `UserId` INT NULL,
   `Text` VARCHAR(255) NULL,
   PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`postlink` (
  `Id` INT NOT NULL,
  `CreationDate` DATETIME NULL,
  `PostId` INT NULL,
  `RelatedPostid` INT NULL,
  `LinkTypeId` INT NULL,
 PRIMARY KEY (`Id`));

 CREATE TABLE `datascience`.`posts` (
  `Id` INT NOT NULL,
  `PostTypeId` INT NULL,
  `CreationDate` DATETIME NULL,
  `Score` DECIMAL NULL,
  `ViewCount` INT NULL,
  `Body` VARCHAR(255) NULL,
  `OwnerUserId` INT NULL,
  `LastActivityDate` DATETIME NULL,
  `Title` VARCHAR(255) NULL,
  `Tags` VARCHAR(45) NULL,
  `AnswerCount` INT NULL,
  `CommentCount` INT NULL,
  `FavoriteCount` INT NULL,
  `ClosedDate` DATETIME NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`tags` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `TagName` VARCHAR(45) NULL,
  `Count` INT NULL,
  `ExcerptPostId` INT NULL,
  `WikiPostId` INT NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `datascience`.`votes` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `PostId` INT NULL,
  `VoteTypeId` INT NULL,
  `CreationDate` DATETIME NULL,
  PRIMARY KEY (`Id`));
