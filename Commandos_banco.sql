create database playMusica;

use playMusica;

create table Musica(
	id_musica int primary key auto_increment not null,
    nome_musica varchar(50) not null,
    cantor_banda varchar(50) not null,
    genero_musica varchar(20) not null);

select * from Musica;

insert into Musica(nome_musica,  cantor_banda, genero_musica)
values('todavia me alegrarei' , 'samuel messias' , 'gospel');

