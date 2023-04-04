class Student:
    def __init__(self, name, grade, class_list):
        self.name = name
        self.grade = grade
        self.class_list = class_list

    def add_class(self, class_name):
        self.class_list.append(class_name)
        return self.class_list
    
    def get_num_classes(self):
        return len(self.class_list)
    
    def display_classes(self):
        return(", ".join(self.class_list))
    
    def __str__(self):
        return(f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes" \
                f"{self.get_num_classes()} classes: {self.display_classes()}")

    def student_with_more_classes(self, student_1, student_2):
        if student_1.get_num_classes() > student_2.get_num_classes():
            return student_1
