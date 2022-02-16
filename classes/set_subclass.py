class PositiveSet(set):
    """PositiveSet class documentation"""

    def __init__(self, input_set):
        """constructor"""
        super(PositiveSet, self).__init__({number for number in set(input_set)
                                           if isinstance(number, (int, float)) and number > 0})

    def add(self, element):
        if element > 0:
            super(PositiveSet, self).add(element)

    def update(self, elements):
        super(PositiveSet, self).update({number for number in set(elements) if number > 0})

    def __or__(self, elements):
        self.update(elements)
        return self


if __name__ == "__main__":
    original_collection = [2, -12, 'hello', 4, 0, "world", 5, 7, 2, -245, 2, 4, 0, 2]
    print(original_collection)
    positive_set_example = PositiveSet(original_collection)
    print(positive_set_example)
    positive_set_example.add(14)
    print(positive_set_example)
    print(type(positive_set_example))
    positive_set_example.update([45, 23, 67, 21, -23421, 21, 21, 0, -456, 21])
    print(positive_set_example)
    print(positive_set_example | {6, 46, -7, 34, 99, 0, -73})
