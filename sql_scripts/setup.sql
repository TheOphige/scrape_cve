-- Setup the ratings database an d create the basic table
CREATE DATABASE IF NOT EXISTS cve;
USE cve;
CREATE TABLE cve (
    exploit_id VARCHAR(120),
    cve_id VARCHAR(256)
);
-- DROP DATABASE cve;