from app import app
import psycopg2


conn = psycopg2.connect(database="test_db",
                        user="admin",
                        password="1234",
                        host="postgres",
                        port=5432)
@app.route('/')
def index():
    with conn:
        with conn.cursor() as cur:
            # cur.execute("""
            #                CREATE TABLE test_table (test_col1 varchar(30),
	    #					    test_col2 varchar(30));
	    #             """)
            cur.execute("""
		           INSERT INTO test_table VALUES (%s, %s)
	                """, ('test message 1', 'test message 2'))
    return 'Home page'
