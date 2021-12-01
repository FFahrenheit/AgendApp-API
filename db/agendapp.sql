--Modelo

CREATE DATABASE agendapp;
USE agendapp;

CREATE TABLE usuario(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(128) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    nombre VARCHAR(60) NOT NULL
);

CREATE TABLE contacto(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(120),
    facebook VARCHAR(64),
    linkedin VARCHAR(128),
    twitter VARCHAR(64),
    foto VARCHAR(1024),
    usuarioId INT UNSIGNED NOT NULL,
    FOREIGN KEY(usuarioId)
    REFERENCES usuario(id)
);