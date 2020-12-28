SELECT * FROM happiness_schema.happiness WHERE health > 1 OR freedom > 1 OR family > 1 OR government_trust > 1 OR  generosity > 1 OR happiness_score > 10;

UPDATE happiness_schema.happiness SET health = 1, freedom = 1, economy = 1, happiness_score = 7.1 WHERE id = 386;
