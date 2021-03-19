-- Create a table

-- Create a table of your choice inside the sample SQLite database, rename it, and add a new column.
-- Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.
-- As a solution to this task, create a file named: task1.sql, with all the SQL statements you have
-- used to accomplish this task

CREATE TABLE IF NOT EXISTS Recipes (
    recipes_id          bigserial PRIMARY KEY,
    recipes_name        varchar(128) NOT NULL,
    preparation_time    varchar(32),
    description         text
);

CREATE TABLE IF NOT EXISTS Ingredients (
    id                  bigserial PRIMARY KEY,
    name                varchar(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS IngredientsRecipes (
    ingredient_id       bigint REFERENCES Ingredients(id) ON DELETE CASCADE,
    recipe_id           bigint REFERENCES Recipes(id) ON DELETE CASCADE,
    quantity            varchar(32),
    unit                varchar(128),
    comment             varchar(128),
    PRIMARY KEY (ingredient_id, recipe_id)
);

INSERT INTO 
    Recipes (recipes_id, recipes_name, preparation_time)
VALUES 
    (1, 'Guacamole', '1h20m'),
    (2, 'Cheeseburger', '20m'),
    (3, 'Burger', '20m'),
    (4, 'Veggie Burger', '20m'),
    (5, 'Microwave Egg', '5m'),
    (6, 'Microwave Tomato', '12m'),
    (7, 'Microwave Onion', '12m'),
    (8, 'Sashimi', '10m'),
    (9, 'Brigadeiro', '30m'),
    (10, 'Fake Strawberry Mousse', '5m');

INSERT INTO 
    Ingredients (id, name)
VALUES
    (1, 'Haas avocato'),
    (2, 'lime'),
    (3, 'salt'),
    (4, 'onion'),
    (5, 'Roma tomato'),
    (6, 'ground beef'),
    (7, 'american cheese'),
    (8, 'burger bun'),
    (9, 'soy protein'),
    (10, 'egg'),
    (11, 'salmon'),
    (12, 'condensed milk'),
    (13, 'cocoa powder'),
    (14, 'cream'),
    (15, 'strawberry quik');

INSERT INTO 
    IngredientsRecipes (recipe_id, ingredient_id, quantity, unit, comment)
VALUES
    (1,1,'3',NULL,'halved, seeded and peeled'),
    (1,2,'1',NULL,'juiced'),
    (1,3,'1/2','teaspoon',NULL),
    (1,4,'1','medium',NULL),
    (1,5,'2',NULL,'seeded and diced'),
    (2,6,'6','ounces','chuck'),
    (2,3,'1','pinch',NULL),
    (2,7,'2','slices',NULL),
    (2,8,'1',NULL,NULL),
    (3,6,'6','ounces','chuck'),
    (3,3,'1','pinch',NULL),
    (3,8,'1',NULL,NULL),
    (4,9,'6','ounces',NULL),
    (4,3,'1','pinch',NULL),
    (4,8,'1',NULL,NULL),
    (5,10,'1',NULL,NULL),
    (5,3,'1','pinch',NULL),
    (6,5,'1',NULL,NULL),
    (6,3,'1','pinch',NULL),
    (7,4,'1',NULL,NULL),
    (7,3,'1','pinch',NULL),
    (8,11,'12','ounces','raw, unfilleted and skinned'),
    (9,12,'1','can',NULL),
    (9,13,'3','full spoons',NULL),
    (10,14,'1','pound',NULL),
    (10,15,'6','full spoons',NULL);

UPDATE Ingredients
SET name ='strawberry'
WHERE id = 15;

DELETE FROM Recipes
WHERE recipes_name='Microwave Tomato';