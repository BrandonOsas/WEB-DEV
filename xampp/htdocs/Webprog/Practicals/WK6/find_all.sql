DELIMITER $$
 
CREATE PROCEDURE find_all()
BEGIN
 SELECT id, name 
 FROM animals; 
END$$
 
DELIMITER ;