filepath = "./data/12-01.txt"


def load_data(filepath: str, split_delimiter: str):
    with open(filepath) as file:
        data = file.read()

    return data.split(split_delimiter)


# Load data
data = load_data(filepath, "\n")

# Split values
data = [i.split() for i in data]

# Transpose and sort
a_list, b_list = [sorted(list(i)) for i in zip(*data)]

# Find differences
differences = [abs(int(i[0]) - int(i[1])) for i in zip(a_list, b_list)]

# Print sum
print(sum(differences))
