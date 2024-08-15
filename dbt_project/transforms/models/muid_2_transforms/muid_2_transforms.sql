-- This will create the `extracted_data` table
{{ config(materialized='table') }}

WITH extracted_elements AS (
    SELECT
        jsonb_array_elements(data) AS element
    FROM
        {{ source('public', 'muid_2') }}
)
SELECT
    element->>'tags' AS tags,
    element->>'measurement' AS measurement,
	element->>'timestamp' AS timestamp_,
	element->>'0100021D00FF' AS consumption
FROM
    extracted_elements

