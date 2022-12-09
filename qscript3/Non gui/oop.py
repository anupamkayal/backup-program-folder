class Laptop:
	def ___init___(self,brand_name, model_no,price):
		self.laptop_brand_name=brand_name
		self.laptop_model_no=model_no
		self.laptop_price=price
	def apply_discount(self,num):		
		total=(num/100)*self.laptop_price
		return (self.laptop_price-total)
		
p1=Laptop("hp","f20176",36000)
p2=Laptop("dell","x4327",43000)
print(p1.laptop_brand_name)
print(p1.apply_discount(20,20))	       