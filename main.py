from services.auth import register_user
from db.database import create_tables_from_schema


create_tables_from_schema()


register_user("Ludde", "lufsen@hotmail.com", "ludvig123")

