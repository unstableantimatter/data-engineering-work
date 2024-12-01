-- Building an Inventory Database with PostgreSQL

SELECT 
  constraint_name, table_name, column_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'parts';

ALTER TABLE parts
ALTER COLUMN description SET NOT NULL;

ALTER TABLE parts
ADD UNIQUE(code);

UPDATE parts
SET description = 'None Available'
WHERE description = '';

ALTER TABLE reorder_options
ALTER COLUMN price_usd SET NOT NULL;

ALTER TABLE reorder_options
ALTER COLUMN quantity SET NOT NULL;

INSERT INTO parts VALUES (54, 'None Available', 'V1-009', 9);

ALTER TABLE reorder_options
ADD CHECK (price_usd > 0 AND quantity > 0);

ALTER TABLE reorder_options
ADD CHECK (0.02 < price_usd / quantity AND price_usd / quantity < 25.00);

ALTER TABLE parts
ADD PRIMARY KEY (id);

ALTER TABLE reorder_options
ADD FOREIGN KEY (part_id) REFERENCES parts (id);

ALTER TABLE locations
ADD CHECK(qty > 0);

ALTER TABLE locations
ADD UNIQUE (part_id, location);

ALTER TABLE locations
ADD FOREIGN KEY (part_id) REFERENCES parts (id);

ALTER TABLE parts
ADD FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (id);

INSERT INTO manufacturers VALUES (
  11,
  'Pip-NNC'
);

SELECT * 
FROM manufacturers;

UPDATE parts
SET manufacturer_id = 11
WHERE id = 1 OR id = 2;