# Sprint 4 - Nivel 1











## Exercici 2
/* Mostra la mitjana de la suma de transaccions per IBAN de les targetes de crèdit en la companyia Donec Ltd. utilitzant almenys 2 taules.*/
SELECT c.company_name, ROUND(AVG(t.amount), 2) AS media_amount FROM transactions t
JOIN  credit_cards cc 	ON t.card_id = cc.id
JOIN companies c 		ON t.business_id = c.company_id
WHERE c.company_name = "Donec Ltd"
GROUP BY c.company_name;










# Sprint 4 - Nivel 2
## Exercici 1

CREATE TABLE card_status AS
SELECT 	card_id, 	CASE WHEN SUM(declined) = 3 THEN "Inactiva"
					ELSE "Activa" END AS estado
FROM (	SELECT 	card_id, declined,
				ROW_NUMBER() OVER (PARTITION BY card_id	ORDER BY timestamp DESC) AS row_num
		FROM transactions) AS ranked_transactions
WHERE row_num <= 3 GROUP BY card_id;

/* Quantes targetes estan actives?*/
SELECT * FROM card_status;
SELECT count(card_id) FROM card_status WHERE estado = "Activa";



# Sprint 4 - Nivel 2
## Exercici 1
/* Necessitem conèixer el nombre de vegades que s'ha venut cada producte.*/
SELECT products.id,
	products.product_name,
	tabla.product,
	tabla.count_product
FROM products
	JOIN (
		SELECT CAST(
				SUBSTRING_INDEX(
					SUBSTRING_INDEX(transactions.product_ids, ',', product_id),
					',',
					-1
				) AS UNSIGNED
			) AS product,
			COUNT(*) AS count_product
		FROM transactions
			CROSS JOIN (
				SELECT id AS product_id
				FROM products
			) AS numbers # obtengo la lista de productos desde tabla "products"
		WHERE product_id <= (
				LENGTH(transactions.product_ids) - LENGTH(REPLACE(transactions.product_ids, ',', '')) + 1
			)
		GROUP BY product
		ORDER BY product
	) AS tabla ON tabla.product = products.id;