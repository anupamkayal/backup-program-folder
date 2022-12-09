import pdb
pdb.set_trace()
class Book:
	def __init__(self,book_name,price,price_off):
		self.book_name=book_name
		self.price=price
		self.price_off=price_off
	def amount_discount(self,number_percentage):
		num=(number_percentage/100)*self.price
		return (self.price-num)
				
			
num=Book("bengali",200,20)
print(Book.amount_discount(num,20))