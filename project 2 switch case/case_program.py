def extract_switch_cases(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    cases = {}
    case_number = None
    case_code = []
    inside_switch = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if 'switch' in stripped_line:
            inside_switch = True
        
        if inside_switch:
            if stripped_line.startswith("case "):
                if case_number is not None:
                    cases[case_number] = case_code
                
                case_number = stripped_line.split()[1].strip(':')
                case_code = [stripped_line]
            elif stripped_line.startswith("default:"):
                if case_number is not None:
                    cases[case_number] = case_code
                case_number = 'default'
                case_code = [stripped_line]
            elif case_number is not None:
                case_code.append(stripped_line)
            
            if stripped_line == '}':
                if case_number is not None:
                    cases[case_number] = case_code
                inside_switch = False
                case_number = None
                case_code = []
    
    return cases

def compare_cases(cases1, cases2):
    all_cases = set(cases1.keys()).union(set(cases2.keys()))
    differences = []
    
    for case in all_cases:
        code1 = cases1.get(case, [])
        code2 = cases2.get(case, [])
        
        if code1 != code2:
            differences.append(case)
    
    return differences

def main(file1, file2):
    cases1 = extract_switch_cases(file1)
    cases2 = extract_switch_cases(file2)
    
    differences = compare_cases(cases1, cases2)
    
    if differences:
        for case in differences:
            print("error code is not same in case" ,case)
    else:
        print("No differences found in switch cases")

if __name__ == "__main__":
    file1 = "case_1.cpp"
    file2 = "case_2.cpp"
    main(file1, file2)

