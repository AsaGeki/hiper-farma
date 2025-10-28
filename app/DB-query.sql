CREATE TYPE op_worker AS ENUm ('ativo', 'inativo');

CREATE TABLE worker (

	worker_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	cpf CHAR(11) NOT NULL UNIQUE,
	picture TEXT,
	hiring_date DATE NOT NULL,
	operation OP_WORKER NOT NULL,
	bagde_check BOOLEAN DEFAULT FALSE,
	contact TEXT
	
)

CREATE TABLE pharm (

	pharm_name TEXT,
	pharm_id CHAR(4) PRIMARY KEY,
	region TEXT NOT NULL,
	city TEXT NOT NULL
);

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

ALTER TABLE pharm
ADD COLUMN manager UUID REFERENCES worker(worker_id) ON DELETE SET NULL;

SELECT * FROM pharm;

CREATE TABLE sub_manager (

	sub_manager_id UUID NOT NULL REFERENCES worker(worker_id) ON DELETE CASCADE,
	pharm_id CHAR(4) NOT NULL REFERENCES pharm(pharm_id) ON DELETE CASCADE,
	PRIMARY KEY(pharm_id, sub_manager_id)
);

CREATE TABLE worker_pharma (

	worker_id UUID NOT NULL REFERENCES worker(worker_id) ON DELETE CASCADE,
	pharm_id CHAR(4) NOT NULL REFERENCES pharm(pharm_id) ON DELETE CASCADE,
	PRIMARY KEY(pharm_id, worker_id)
)