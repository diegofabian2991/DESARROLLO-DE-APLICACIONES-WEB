-- ============================================
-- ESQUEMA DE BASE DE DATOS - SMARTPREDICT AI
-- PostgreSQL 17
-- Proyecto Integrador - Semana 15
-- ============================================

-- ============================================
-- TABLA: USUARIOS
-- ============================================

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- ============================================
-- TABLA: PROVEEDORES
-- ============================================

CREATE TABLE IF NOT EXISTS proveedores (
    id_proveedor INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL
);

-- ============================================
-- TABLA: PRODUCTOS
-- ============================================

CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    id_proveedor INTEGER,

    CONSTRAINT fk_productos_proveedor
        FOREIGN KEY (id_proveedor)
        REFERENCES proveedores(id_proveedor)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- ============================================
-- TABLA: CLIENTES
-- ============================================

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sector VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL
);

-- ============================================
-- TABLA: FACTURAS
-- ============================================

CREATE TABLE IF NOT EXISTS facturas (
    id_factura INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    numero VARCHAR(30) UNIQUE NOT NULL,
    id_cliente INTEGER NOT NULL,
    total NUMERIC(10,2) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_facturas_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);