import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject("John", 25, True)
    
    # Serialize the object to a file
    obj.serialize("custom_object.pkl")
    
    # Deserialize the object from the file
    loaded_obj = CustomObject.deserialize("custom_object.pkl")
    
    if loaded_obj:
        # Display the deserialized object's attributes
        loaded_obj.display()
