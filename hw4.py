№1
# class Car:
#     def init(self, make, model):
#         self.make = make
#         self.model = model

#     def getattr(self, item):
#         return "This attribute is not available"
# c = Car("Toyota", "Corolla")
# print(c.make) 
# print(c.color)
# №2
# class Rectangle:
#     def init(self, width, height):

#         self.width = width
#         self.height = height

#     def setattr(self, name, value):
#         if name not in ('width', 'height'):
#             raise AttributeError("Local attributes are not allowed")
#         super().setattr(name, value)

# r = Rectangle(10, 20)
# r.width = 15
# r.height = 25
# r.color = 'red'
