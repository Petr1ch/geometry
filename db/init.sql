SELECT 'CREATE DATABASE geometry'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'geometry');
\c geometry;

CREATE EXTENSION IF NOT EXISTS postgis;
SELECT PostGIS_Full_Version();
