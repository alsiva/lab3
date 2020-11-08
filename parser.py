
with open("lab3.json") as file:
    def skip_whitespaces(expect_comma = False):
        c = file.read(1)
        while c == " " or c == "\n" or c == "\t":
            c = file.read(1)

        if c == "," and expect_comma:
            return skip_whitespaces()

        return c


    def read_value(expect_comma = False):
        c = skip_whitespaces(expect_comma)
        
        if c == "\"":
            return read_string(), True
        elif c == "[":
            return read_array(), True
        elif c == "{":
            return read_object(), True
        else:
            return c, False
                

    def read_object():
        obj = {}
        expect_comma = False

        while True:
            c = skip_whitespaces(expect_comma)

            if c == "}":
                return obj
            elif c != "\"":
                raise Exception("expected \" or }, found " + c)

            key = read_string()
            read_colon()
            value, is_success = read_value()
            if not is_success:
                raise Exception("error reading value")

            obj[key] = value
            expect_comma = True
            


    def read_colon():
        c = skip_whitespaces()
        
        if c != ":":
            raise "expected :, found " + c


    def read_array():
        array = []
        expect_comma = False

        while True:
            value, is_success = read_value(expect_comma)    
            if not is_success:
                if value == "]":
                    return array
                else:
                    raise "error reading value"

            array.append(value)
            expect_comma = True       


    def read_string():
        result = ""

        c = file.read(1)
        while c != "\"":
            result += c
            c = file.read(1)

        return result


    json, is_success = read_value()
    if not is_success:
        raise Exception("error reading json")

###############################################################################################################

with open("lab3.yml", 'w') as output:
    def write_indent(indent):
        while indent > 0:
            output.write("  ")
            indent -= 1

    def write_dict(dictionary, indent, skip_indent = False):
        for key, value in dictionary.items():
            if not skip_indent:
                write_indent(indent)
            skip_indent = False
            output.write(key + ":")
            if type(value) is str:
                output.write(" ")
            else:
                output.write("\n")

            write_value(value, indent + 1)
           
    def write_value(value, indent = 0, skip_indent = False):
        if type(value) is str:
            write_string(value)
        elif type(value) is dict:
            write_dict(value, indent, skip_indent)
        elif type(value) is list:
            write_list(value, indent)
        
    def write_string(value):
        output.write(value + "\n")

    def write_list(list, indent):  
        for element in list:
            write_indent(indent - 1)
            output.write("- ")
            write_value(element, indent, True)

    write_value(json)