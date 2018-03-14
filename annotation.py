class Annotation():
    def __init__(self, str_type, int_begin, int_end):
        self.type = str_type
        self.begin = int_begin
        self.end = int_end
        self.metadata = {}

