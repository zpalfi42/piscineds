DO $$
DECLARE
    table_name TEXT;
    sql_query TEXT := 'CREATE TABLE customers AS ';
    first_table BOOLEAN := TRUE;
BEGIN
    FOR table_name IN
        SELECT t.table_name
        FROM information_schema.tables t
        WHERE t.table_name LIKE 'data_202%_%%%' ESCAPE '\'
          AND t.table_schema = 'public'
    LOOP
        RAISE NOTICE 'Processing table: %', table_name;
        IF first_table THEN
            sql_query := sql_query || 'SELECT * FROM ' || table_name;
            first_table := FALSE;
        ELSE
            sql_query := sql_query || ' UNION ALL SELECT * FROM ' || table_name;
        END IF;
    END LOOP;
    EXECUTE sql_query;
END $$;