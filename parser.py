
with open("lab3.json") as file:
    c = file.read(1)

    object = read_value(file)

    def skip_whitespaces():
        while c == " ":
            c = file.read(1)


    def read_value():
        skip_whitespaces()
        
        if c == "\"":
            read_string(file)
        elif c == "[":
            read_array(file)
        elif c == "{":
            read_object(file)
                

    def read_object():
        while (c := file.read(1)) != "}":
            if c == " ":
                continue
            elif c == "\"":
                key = read_string(file)
                read_colon(file)
                value = read_value(file)

    def read_colon():
        while (c := file.read(1)) != ":":
            if c == " ":
                continue
            else
                raise "expected :, found " + c

    def read_array():
        array = []

        while True:    
            skip_whitespaces()
            array += read_value(file)
            skip_whitespaces()


        if c == ",":

        elif c == "]":
            return array
        else
            raise "incorrect end of array; found " + c

    def read_string():
        result = ""
        while c != "\"":
            result += c
            c = file.read(1)


        return result

