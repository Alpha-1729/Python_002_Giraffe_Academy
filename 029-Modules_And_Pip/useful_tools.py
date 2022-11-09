import random
feet_in_mile = 5280
meters_in_kilometer = 1000
car = ["Toyoto", "Maruti", "BMW", "Jaguar"]

def get_file_ext(file_name):
    return file_name[file_name.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
