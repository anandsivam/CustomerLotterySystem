class Customer():
    #Non Primitive data types are Array, List, Tuples, Dictionary, Sets and Files.
    def __init__(self, customer_id, name, age, num1, num2, num3, num4, num5, num6):
        self.customer_info = {
            'customerId': customer_id,
            'name': name,
            'age': age,
            'lotteryNumber': [num1, num2, num3, num4, num5, num6]
        }

