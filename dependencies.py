from sqlalchemy.orm import sessionmaker
from Models.EcommerceModel import database

def SessionCommerce():
    sessaoecommerce = None
    try:
        SessionEcommerce = sessionmaker(bind=database)
        sessaoecommerce = SessionEcommerce()
        yield sessaoecommerce
    finally:
        sessaoecommerce.close()
        