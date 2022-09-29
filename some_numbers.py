class Obj_student:
    def __init__(self, data_string):
        self.name = data_string[0]
        self.properties = []
        self.properties.Append(Property("Округ", data_string[2], Compare_Regions))
        self.properties.Append(Property("Знак зодиака", data_string[3], Compare_Signs))
        #    todo;
        self.properties.Append(Property("Время сна", data_string[4], Compare_Sleep_Time))
        self.properties.Append(Property("Время подъема", data_string[5], Compare_Get_Up_Time))
        self.properties.Append(Property("Наличие работы", data_string[6], Compare_Job))
        self.drink = data_string['N4']

    def Propose_Drink_Type(self, students_list, k):
        comparsion_list = []
        number = 0
        for student in students_list:
            distances = []
            for property in student.properties:
                raw_distance = next(p for p in self.properties if p.name == property.name).Compare(property.value)
                distances.append([("property", property.name), ("raw_distance", raw_distance), ("normalized_distance", -1)])
            comparsion_list.append([("distances", distances), ("number", number), ("sum", -1)])
            number += 1
        
        for property in self.properties:
            property_distances = next([cur_dir["raw_distance"] for cur_dir in [next(d["distances"] for d in comparsion_list)]])
            property.min_value = min(property_distances)
            property.max_value = max(property_distances)
        
        for comparsion in comparsion_list:
            for distance in comparsion["distances"]:
                current_property = next(p for p in self.properties if p.name == distance["property"])
                distance["normalized_distance"] = sqrt((distance["raw_distance"] - current_property.min_value) / (current_property.max_value - current_property.min_value))
                sum += normalized_distance
            comparsion["sum"] = sum
        
        sorted_distances = comparsion_list.sort(key = lambda c: c["sum"])
        
        tea_count = 0
        coffee_count = 0
        for i in range(0, min(k, len(sorted_distances))):
            current_student = students_list[sorted_distances[i]["number"]]
            if current_student.drink == "Ч":
                tea_count += 1
            elif current_student.drink == "К":
                coffee_count += 1
        
        if tea_count == coffee_count:
            current_student = students_list[sorted_distances[k]["number"]]
            if current_student.drink == "Ч":
                tea_count += 1
            elif current_student.drink == "К":
                coffee_count += 1
        
        if tea_count > coffee_count:
            print("Tea")
        elif coffee_count > tea_count:
            print("coffee")
        else:
            print("Something wrong, i can feel it...")

class Property:
    def __init__(self, name, value, comparsion_method, weight = 1):
        self.name = name
        self.value = value
        self.comparsion_method = comparsion_method
        self.weight = weight
        
# todo
def Compare(self, compared_value):
    return self.weigth * self.comparsion_method(self.value, compared_value)

def Compare_Regions(region_1, region_2):
    pass # метод Феди

def CompareSigns(sign_1, sign_2):
    pass # метод Вани

def Compare_Sleep_Time(sleep_time_1, sleep_time_2):
    return abs(sleep_time_1 - sleep_time_2)

def Compare_Get_Up_Time(time_1, time_2):
    difference = min(abs(time_1 - time_2), abs(time_1 - time_2 + 24), abs(time_1 - time_2 - 24))
    return difference

def Compare_Job(job_1, job_2):
    return abs(job_1 - job_2)