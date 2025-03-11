# Klass och funktioner för bankkonton
from db.database import connect_db

def create_new_bank_account(user_id, account_type="Savings", balance=0.0):

	try:
		conn = connect_db()
		cursor = conn.cursor()

		cursor.execute("""
		INSERT INTO accounts (user_id, account_type, balance)
		VALUES (?, ?, ?)
		""", (user_id, account_type, balance))

		conn.commit()
		return True
	except:
		return False
	finally:
		conn.close()
