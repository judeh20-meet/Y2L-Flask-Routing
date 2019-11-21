from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name, price, picture_link, description):

	product_object = Product(
		name = name,
		price = price,
		picture_link = picture_link,
		description = description)
	session.add(product_object)
	session.commit()

def edit_product(name, price, picture_link, description):

	product_object = session.query(
		Product).filter_by(
		name=name).first()
		product_object.price = price
		product_object.picture_link = picture_link
		product_object.description = description
	session.add(product_object)
	session.commit()

def delete_product(name):
	session.query(Product).filter_by(
		name = name).delete()
	session.commit()

def return_all_products():
	products = session.query(Product).all()
	return products