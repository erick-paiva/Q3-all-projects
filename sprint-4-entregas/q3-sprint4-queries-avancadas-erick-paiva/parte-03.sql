--1
SELECT * FROM enderecos;

--2
SELECT * from enderecos e
JOIN usuarios u
	ON (e.id = u.endereco_id);

--3
SELECT rs, u
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id);

--4
SELECT rs, u, e.rua rua, e.cidade cidade , e.pais pais
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id);

--5
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id);

--6
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id)
WHERE
	(rs.nome = 'Youtube');

--7
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id)
WHERE
	(rs.nome = 'Instagram');

--8
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id)
WHERE
	(rs.nome = 'Facebook');

--9
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id)
WHERE
	(rs.nome = 'TikTok');

--10
SELECT rs.nome rede_social, u.nome usuario, u.email email, e.cidade cidade  
FROM usuario_rede_sociais urs
JOIN usuarios u
	ON (urs.usuario_id = u.id)
JOIN redes_sociais rs
	ON (urs.rede_social_id = rs.id)
JOIN enderecos e
	ON (u.endereco_id = e.id)
WHERE
	(rs.nome = 'Twitter');