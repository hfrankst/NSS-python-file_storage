class Car_Dictionary:
	"""write a method that reads the car-makes
	   write a method that reads the car-models 
	   write a method that invokes the above methods and generates a dict with the make as the key, and the model as the value of the k,v pair
	"""
	def __init__(self):
		self.car_makes = list()
		self.car_models = list()
		self.car_dictionary = dict()

	def read_makes(self):
		'''this method reads the makes of the cars from the car-makes file'''
		
		with open('car-makes', 'r') as car_makes:
			for car in car_makes:
				self.car_makes.append(car.replace('\n', ''))				

	def read_models(self):
		'''this method reads the models of the cars from the car-models file'''
		with open('car-models', 'r') as car_models:
			for car in car_models:
				self.car_models.append(car.replace('\n', ''))	


	def generate_car_dictionary(self):
		'''dictionary should use the car make as the key, and the model as the value'''
		self.read_makes()
		self.read_models()
		
		for car_make in self.car_makes:
			self.car_dictionary[car_make] = list()
			for  car_model in self.car_models:
				if car_model[0] == car_make[0]:
					self.car_dictionary[car_make].append(car_model[4:])
		print("--------------------------------")
		print("Here is the Car Dictionary: \n", self.car_dictionary)
		print("\n--------------------------------")



# YOU NEED TO MAKE AN INSTANCE OF A CLASS FOR IT TO DO ANYTHING. STOP FORGETTING THIS SHIT
c = Car_Dictionary()
# c.read_makes()
c.generate_car_dictionary()