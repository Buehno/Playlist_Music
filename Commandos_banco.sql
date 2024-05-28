create database playMusica;

use playMusica;

create table Musica(
	id_musica int primary key auto_increment not null,
    nome_musica varchar(50) not null,
    cantor_banda varchar(50) not null,
    genero_musica varchar(20) not null);

select * from Musica;

insert into Musica(nome_musica,  cantor_banda, genero_musica)
values('O sol' , 'Vitor Clay' , 'Pop');
insert into Musica(nome_musica,  cantor_banda, genero_musica)
values('todavia me alegrarei' , 'samuel messias' , 'gospel'),
('Isis' , 'MC Kako', 'funk'),
('lobo-guara', 'Hungria', 'Rep'),
('meu abrigo', 'mellin', 'popp');

select * from Musica where cantor_banda like '%e%';


select * from Musica where genero_musica <> 'popp';

select * from Musica;

update	Musica set genero_musica = 'Rap' where  id_musica = 4 ;

delete from Musica where id_musica = 2 ;

/* tabela dos Usuarios */

create table usuario(
	id_usuario int primary key auto_increment not null,
    nome_usuario varchar(50) not null,
    login_usuario varchar(20) not null,
    senha_usuario varchar (15) not null);
    
select * from usuario;
    
insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Ronaldo Bueno', 'Buenozim_', 'admin');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('vilma nunes', 'vilmanunes104', 'nunes');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Bueno Junior', 'Buenozim_', 'junior'), ('vilma nunes', 'vilmanunes104', 'nunes');

insert into usuario(nome_usuario, login_usuario, senha_usuario)
values('Ronaldo Bueno', 'Buenozim', 'admin');

truncate table usuario;

alter table usuario add unique(login_usuario);

select * from usuario;

delete from usuario where id_usuario = 4;