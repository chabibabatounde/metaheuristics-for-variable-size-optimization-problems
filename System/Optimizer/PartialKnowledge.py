import random


class PartialKnowledge():
    name = None
    type = None  # int, float or tuple (as string not as type)
    range_start_point = None
    range_end_point = None
    probability = None
    value = None

    def __init__(self, name=None, attribute_type=None, range_start_point=None,
                 range_end_point=None, probability=None, value=None):
        self.name = name
        self.type = attribute_type
        self.range_start_point = range_start_point
        self.range_end_point = range_end_point
        self.probability = probability
        self.value = value

    def get_some(self):
        if self.value is not None:
            return self.value
        else:
            if self.probability is None:
                start = self.range_start_point
                stop = self.range_end_point
                if self.type == "int" or self.type == "float" or self.type is None:
                    if start is None:
                        start = -100
                    if stop is None:
                        stop = 100
                    value = random.uniform(start, stop)
                    if self.type == "int":
                        value = random.randint(start, stop)
                elif self.type == "tuple":
                    if start is None:
                        start = (-100, -100)
                    if stop is None:
                        stop = (100, 100)
                    value = (random.randint(start[0], stop[0]), random.randint(start[1], stop[1]))
                return value
            else:
                exit("Generate probability")

    def is_valid(self, value):
        result = True
        if self.type is None or self.type.lower() in ['int', 'float']:
            if not isinstance(value, (int, float)):
                result *= False
            else:
                if self.range_start_point is not None:
                    if value >= self.range_start_point:
                        result *= True
                    else:
                        result *= False
                if self.range_end_point is not None:
                    if value <= self.range_end_point:
                        result *= True
                    else:
                        result *= False
                if self.type is None:
                    result *= True
                elif self.type.lower() == "int" and isinstance(value, float):
                    result *= False

        elif self.type.lower() == 'tuple':
            if not isinstance(value, tuple):
                result *= False
            else:
                if self.range_start_point is not None:
                    if value[0] >= self.range_start_point[0]:
                        result *= True
                    else:
                        result *= False
                    if value[1] >= self.range_start_point[1]:
                        result *= True
                    else:
                        result *= False
                if self.range_end_point is not None:
                    if value[0] <= self.range_end_point[0]:
                        result *= True
                    else:
                        result *= False
                    if value[1] <= self.range_end_point[1]:
                        result *= True
                    else:
                        result *= False
        return result
