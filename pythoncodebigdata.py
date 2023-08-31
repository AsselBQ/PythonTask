import csv
import argparse

def read_csv_file(file_name, num_columns):
    with open(file_name, "r") as f:
        cells = f.read().replace("\n", ",").split(",")[0:-1]
        col_ind = 1
        row_ind = 1
        for cell_value in cells:
            yield (cell_value, col_ind, row_ind)
            col_ind += 1
            if col_ind > num_columns:
                col_ind = 1
                row_ind += 1
        yield (None, col_ind, row_ind)

def create_occurrences_dictionary(file_name, error_color, num_columns):
    color_count = {}
    gen = read_csv_file(file_name, num_columns)
    while True:
        cell_value, col_ind, row_ind = next(gen)
        if cell_value is None:
            break
        if str(cell_value) == error_color:
            print(f"Found broken cell in row {row_ind}, column {col_ind}.")
            continue
        if cell_value in color_count:
            color_count[cell_value] += 1
        else:
            color_count[cell_value] = 1
    return color_count

def main():
    parser = argparse.ArgumentParser(description="Count color occurrences in a CSV file.")
    parser.add_argument("-error", dest="error_color", help="Color to trigger an error condition")

    error_color = parser.parse_args().error_color

    csv_file_path = "Colors.csv"
    num_columns = 3

    print("Reading CSV file")
    print(" ")
    try:
        color_count = create_occurrences_dictionary(csv_file_path, error_color, num_columns)
    except FileNotFoundError:
        print("Error : File Not Found.")
        exit(1)
    print(" ")
    print("Done Reading CSV file")
    print(" ")

    for item, count in color_count.items():
        print(f"{item}: Number of cells {count}")

if __name__ == "__main__":
    main()
