CREATE DATABASE IF NOT EXISTS ejercicios_python;

USE ejercicios_python;


CREATE TABLE IF NOT EXISTS resultados (

    id INT AUTO_INCREMENT PRIMARY KEY,

    ejercicio VARCHAR(100) NOT NULL,

    entrada VARCHAR(255) NOT NULL,

    resultado TEXT NOT NULL,

    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);