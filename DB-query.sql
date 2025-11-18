CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TYPE w_role AS ENUM (
    'operador de caixa',
    'perfumista',
    'farmacêutico'
);

CREATE TYPE w_gender AS ENUM ('masculino', 'feminino');

CREATE TYPE w_operation AS ENUM ('ativo', 'inativo');

CREATE TYPE b_category AS ENUM ('trabalhador', 'diretoria');

CREATE TABLE worker (
    worker_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    picture TEXT,
    hiring_date DATE NOT NULL,
    operation w_operation NOT NULL,
    contact TEXT,
    worker_role w_role NOT NULL,
    gender w_gender
);

CREATE TABLE bagde (
    bagde_id UUID PRIMARY KEY REFERENCES worker(worker_id) ON DELETE CASCADE,
    bagde_check BOOLEAN DEFAULT FALSE,
    bagde_category b_category NOT NULL,
    bagde_receipt DATE
);

CREATE TABLE department (
    department_name TEXT,
    department_id CHAR(4) PRIMARY KEY,
    regional TEXT NOT NULL,
    city TEXT NOT NULL,
    department_state TEXT NOT NULL,
    manager UUID UNIQUE REFERENCES worker(worker_id) ON DELETE
    SET
        NULL
);

CREATE TABLE department_worker (
    worker_id UUID REFERENCES worker(worker_id) ON DELETE CASCADE,
    department_id CHAR(4) REFERENCES department(department_id) ON DELETE CASCADE,
    is_submanager BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (worker_id, department_id)
);

CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role_name TEXT NOT NULL UNIQUE,
    role_description TEXT,
);

CREATE TABLE operation (
    operation_id SERIAL PRIMARY KEY,
    operation_name TEXT,
    duration DATE
);