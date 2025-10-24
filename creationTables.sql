create table Anime(
    id_anime int,
    titulo varchar(255),
    sinopsis varchar(512),
    intervalo_emision varchar(32) default null,
    episodios int,
    miembros int,
    popularidad double precision default 0,
    ranking int,
    puntuacion_anime double precision default 0,
    primary key (id_anime)
);

create table Genero(
    categoria varchar(64) primary key
);

create table Tipo(
    id_anime int,
    categoria varchar(64),
    primary key (id_anime, categoria),
    foreign key (id_anime) references Anime(id_anime),
    foreign key (categoria) references Genero(categoria)
);

create table Usuario(
    nombre_perfil varchar(255) primary key not null,
    genero_perfil varchar(16),
    cumpleanhos varchar(8)
);

CREATE TABLE favoritos (
    u_nombre_perfil VARCHAR(255),
    a_id_anime INT,
    FOREIGN KEY (u_nombre_perfil) REFERENCES Usuario(nombre_perfil),
    FOREIGN KEY (a_id_anime) REFERENCES Anime(id_anime)
);

create table Reviews(
    id_review int not null primary key,
    puntuacion double precision default 0,
)

create table Recibe(
    id_anime int,
    id_review int,
    foreign key id_anime references Anime(id_anime),
    foreign key id_review references Reviews(id_review)
)

create table Escribe(
    id_review int not null,
    nombre_perfil varchar(255),
    foreign key id_anime references Reviews(id_review),
    foreign key nombre_perfil references Reviews(nombre_perfil)
)

CREATE TABLE calificacion (
    nombre VARCHAR(64) PRIMARY KEY,
    valor DOUBLE PRECISION DEFAULT 0,
    id_review INT NOT NULL
);

