class FwfMapper:

    def __init__(self, width_mapping, trailing, field_mapping, data):
        self.width_mapping = width_mapping
        self.trailing = trailing
        self.field_mapping = field_mapping
        self.data = data

    def get_width(self, tuple):
        return tuple[1] - tuple[0]
    
    def get_output_field(self, input_field):
        for key, value in self.field_mapping.items():
            if input_field == value:
                return key

    def get_fw_value(self, width, value):
        if not isinstance(value, str):
            value = str(value)
        value = value.rjust(width, self.trailing)
        if len(value) > width:
            value = value[0:width]
        return value
    
    def calculate_gaps(self):
        gap_count = 0
        base = 0
        for key, item in self.width_mapping.items():
            gap_count += item[0] - base
            base = item[1]
        return gap_count + self.get_unmapped_gap_count()

    def insert_string(self, original, new, pos):
        return original[:pos] + new + original[pos:]
    
    def get_unmapped_gap_count(self):
        if(self.is_all_mapped()):
            return 0
        
        unmaped_counter = 0
        for width_key in self.width_mapping.keys():
            if width_key not in self.field_mapping.keys():
                unmaped_counter += self.width_mapping[width_key][1] - self.width_mapping[width_key][0]

        return unmaped_counter

            
    def get_result(self):
        result = ""
        gaps = self.calculate_gaps()

        for item in self.data:
            line = ""
            line += "".rjust(gaps, self.trailing)
            for key,value in item.items():
                output_field = self.get_output_field(key)
                width_tuple = self.width_mapping[output_field]
                width = self.get_width(width_tuple)
               
                
                line = self.insert_string(line, self.get_fw_value(width, value), width_tuple[0])
            result += "\n" + line
        return result
    
    def is_all_mapped(self):
        for width_key in self.width_mapping.keys():
            if width_key not in self.field_mapping.keys():
                return False
            
        for field_key in self.field_mapping.keys():
            if field_key not in self.width_mapping.keys():
                return False
        return True

