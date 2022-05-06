create table if not exists kopas(
	id BIGSERIAL primary key,
	selecao VARCHAR(128) unique,
	qnt_copas integer
)

insert into kopas
	(selecao, qnt_copas)
values
	('Brasil',5),
	('Alemanha',5),
	('Itália',4),
	('Argentina',2),
	('França',2),
	('Uruguai',2),
	('Inglaterra',1),
	('Espanha',1),
	('Japão',1);

update kopas set qnt_copas = 4 where id = 2;

delete from kopas where id = 9 returning *;

select * from kopas;