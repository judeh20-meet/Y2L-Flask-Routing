from model import Base, Product
from model import Base, Cart


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

def edit_product(id, name, price, picture_link, description):

	product_object = session.query(
		Product).filter_by(
		id=id).first()
	product_object.name = name
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

def query_by_id(their_id):
	product = session.query(Product).filter_by(id = their_id).first()
	return product

def Add_To_Cart(productID):
	add_to_cart = Cart(
		productID = productID)
	session.add(add_to_cart)
	session.commit()


add_product("green apple", 25, "two number nines", "i like to eat this apple becasue it is green")
add_product("red apple", 50, "a number 9 large", "i like to eat this apple becasue it is red")
add_product("yellow apple", 75, "a number 6 with extra dip", "i like to eat this apple becasue it is yellow")
print(query_by_id(1))