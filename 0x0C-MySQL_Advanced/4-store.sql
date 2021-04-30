-- Data Base metal_bands
-- insert table orders and trigger items

CREATE TRIGGER UPDATE_ITEMS_BU 
BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name 