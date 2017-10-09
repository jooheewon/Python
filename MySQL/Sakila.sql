SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city FROM customer JOIN city JOIN address WHERE city.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id WHERE category.name = 'comedy';

SELECT actor.first_name, actor.last_name, film.title, film.description, film.release_year FROM actor JOIN film WHERE actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city, city.city_id, customer.store_id FROM customer JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id WHERE customer.store_id = 1 AND city.city_id IN (1, 42, 312, 459);

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, film.rating, actor.actor_id FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id WHERE rating = 'G' AND special_features LIKE 'Behind the Scenes%' AND actor.actor_id = 15;

SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, payment.amount FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN payment WHERE category.name = 'drama' AND payment.amount = 2.99;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'Kilmer' AND category.name = 'action';
