-- Data Base Holberton
delimiter //
CREATE TRIGGER RESET_VALID_AU
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;
//
