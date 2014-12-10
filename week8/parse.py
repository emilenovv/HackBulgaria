def is_empty_line(line):
    return len(line.strip()) != 0


def lines(text_contents):
    return text_contents.split("\n")


def unlines(line_data):
    return "\n".join(line_data)


def get_file(file):
    return open(file).read()


def compose(f, g):
    return lambda x: f(g(x))


def capitalize(string):
    return string[0].upper() + string[1:]


def not_contains_dash(string):
    return '_' not in string


def remove_dash(dashed_list):
    return list(filter(not_contains_dash, dashed_list))


def get_test_class_name(file_name):
    file_name = file_name.split('.')
    return make_camel_case(file_name[0])


def make_camel_case(string):
    string = string.split("_")
    string = list(filter(remove_dash, string))
    for i in range(len(string)):
        string[i] = capitalize(string[i])
    return "".join(string)


def contains_import(string):
    return "import" in string and "->" not in string


def extract_imports(text_contents):
    return list(filter(contains_import, text_contents))


def remove_imports(text_contents):
    text_contents = list(filter(lambda x: "import" not in x, text_contents))
    return text_contents


def extract_main_description(text_contents):
    return text_contents[0]


def split_test(test):
    test = test.split("->")
    test[1] = test[1].split("==")
    test.append(test[1][0])
    test.append(test[1][1])
    test.remove(test[1])
    return test


def remove_main_description(text_contents):
    text_contents.remove(text_contents[0])
    return text_contents


def get_desctiption_for_a_test(test):
    test_list = split_test(test)
    return test_list[0].strip()


def get_test_rhs(test):
    test_list = split_test(test)
    return test_list[2].strip()


def get_test_lhs(test):
    test_list = split_test(test)
    return test_list[1].strip()


def parsed_test_assertTrue_assertFalse(test_name, test_lhs, test_rhs, test_comment):
    return """
    def {test_name}(self):
        self.assert{test_rhs}({test_lhs}, {test_comment})\n""".format(
        test_name=test_name, test_rhs=test_rhs, test_lhs=test_lhs,
        test_comment=test_comment)


def parsed_test_assertEqual(test_name, test_lhs, test_rhs, test_comment):
    return """
    def {test_name}(self):
        self.assertEqual({test_lhs}, {test_rhs}, {test_comment})\n""".format(
        test_name=test_name, test_rhs=test_rhs, test_lhs=test_lhs,
        test_comment=test_comment)


def parse_imports(list_of_imports):
    return "\n".join(list_of_imports)


def parse_file(imports, class_name, test_file_comment, tests):
    return """import unittest

{imports}


class {class_name}(unittest.TestCase):
    \"\"{test_file_comment}\"\"
{tests}

if __name__ == '__main__':
    unittest.main()""".format(
        imports=imports, class_name=class_name,
        test_file_comment=test_file_comment, tests=tests)


def main():
    contents = lines(get_file("is_prime_test.dsl"))
    no_empty_lines = list(filter(is_empty_line, contents))
    imports = parse_imports(extract_imports(no_empty_lines))
    no_empty_lines = remove_imports(no_empty_lines)
    test_file_comment = extract_main_description(no_empty_lines)
    class_name = get_test_class_name("is_prime_test.dsl")
    no_empty_lines = remove_main_description(no_empty_lines)
    tests = []
    num_of_test = 1
    for test in no_empty_lines:
        test_comment = get_desctiption_for_a_test(test)
        rhs = get_test_rhs(test)
        lhs = get_test_lhs(test)
        if rhs == "True" or rhs == "False":
            tests.append(
                parsed_test_assertTrue_assertFalse(
                    "test_case" + str(num_of_test), lhs, rhs, test_comment))
        else:
            tests.append(
                parsed_test_assertEqual(
                    "test_case" + str(num_of_test), lhs, rhs, test_comment))
        num_of_test += 1
    tests = "".join(tests)
    parsed_file = parse_file(imports, class_name, test_file_comment, tests)
    output_file = open("is_prime_test.py", "w")
    output_file.write(parsed_file)


if __name__ == '__main__':
    main()
