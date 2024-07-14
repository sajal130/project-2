import re

def read_number(filename, has_extra_column=False):
    seq_data = {}
    with open(filename, 'r') as file:
        for line in file:
            match = re.match(r'^(\d+)\s+(-?\d+\.?\d*)', line)
            if match:
                seq = int(match.group(1))
                if seq not in seq_data:  # Only take the first occurrence
                    parts = line.strip().split()
                    data = float(parts[2] if has_extra_column else parts[1])
                    seq_data[seq] = data
    return seq_data

def compare(file1_data, file2_data):
    results = []
    all_seq = sorted(set(file1_data.keys()).union(file2_data.keys()))

    for seq in all_seq:
        file1_value = file1_data.get(seq)
        file2_value = file2_data.get(seq)
        lower_bound = upper_bound = None
        result = "missing"

        if file1_value is not None and file2_value is not None:
            lower_bound = round(file1_value * 0.9, 4)
            upper_bound = round(file1_value * 1.1, 4)
            if lower_bound <= file2_value <= upper_bound:
                result = "yes"
            else:
                result = "no"
        elif file1_value is not None:
            result = "file2 missing"
        elif file2_value is not None:
            result = "file1 missing"

        results.append((seq, file1_value, lower_bound, upper_bound, file2_value, result))
    return results

def print_result(results):
    print("seq file1_data lower_bound upper_bound file2_data result")
    for result in results:
        seq, file1_data, lower_bound, upper_bound, file2_data, outcome = result
        file1_str = '{:.4f}'.format(file1_data) if file1_data is not None else ""
        file2_str = '{:.4f}'.format(file2_data) if file2_data is not None else ""
        lower_str = '{:.4f}'.format(lower_bound) if lower_bound is not None else ""
        upper_str = '{:.4f}'.format(upper_bound) if upper_bound is not None else ""
        print(seq, file1_str, lower_str, upper_str, file2_str, outcome)

def main():
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    file1_data = read_number(file1_path)
    file2_data = read_number(file2_path, has_extra_column=True)
    results = compare(file1_data, file2_data)
    print_result(results)

if __name__ == "__main__":
    main()
