DELIMITER $$
 
CREATE PROCEDURE find_by_id(IN a_id INT(11),OUT a_name VARCHAR(20))
BEGIN
 	SELECT name INTO a_name FROM animals
 	WHERE id = a_id;
END$$
 
DELIMITER ;