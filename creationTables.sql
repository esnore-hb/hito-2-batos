create table tindanime.Anime(
    id_anime int primary key,
    titulo varchar(255) ,
    sinopsis varchar(512),
    inicio_emision date default null,
    termino_emision date default null,
    episodios int,
    miembros int,
    popularidad double precision default 0,
    ranking int,
    puntuacion_anime double precision default 0
)

create table tindanime.Genero(
    categoria varchar(64) primary key
)

create table tindanime.Tipo(
    id_anime int,
    categoria varchar(64)
    foreign key id_anime references tindanime.Anime(id_anime),
    foreign key categoria references tindanime.Genero(categoria)
)

create table tindanime.Usuario(
    nombre_perfil varchar(255) primary key not null,
    genero_perfil varchar(1) check 'F' 'M',
    cumpleanhos varchar(8)
)

create table tindanime.Favoritos(
    nombre_perfil varchar(255),
    id_anime int,
    foreign key nombre_perfil references tindanime.Usuario(nombre_perfil),
    foreign key id_anime references tindanime.Anime(id_anime)
)

create table tindanime.Reviews(
    id_review int not null primary key,
    puntuacion double precision default 0,
)

create table tindanime.Recibe(
    id_anime int,
    id_review int,
    foreign key id_anime references tindanime.Anime(id_anime),
    foreign key id_review references tindanime.Reviews(id_review)
)

create table tindanime.Escribe(
    id_review int not null,
    nombre_perfil varchar(255),
    foreign key id_anime references tindanime.Reviews(id_review),
    foreign key nombre_perfil references tindanime.Reviews(nombre_perfil)
)

create table tindanime.Calificacion(
    nombre varchar(64) primary key,
    valor int default 0,
    id_review int not null,
)
