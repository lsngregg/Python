from os import path, remove


def load_file(filename: str) -> list[str]:
    my_file = open(filename, "r")
    content = my_file.read()
    data = content.split("\n")
    my_file.close()

    return data


if __name__ == "__main__":
    output_file = "video_export/output.txt"

    if path.exists(output_file):
        remove(output_file)

    simp_path = "video_export/videoExportExample.txt"
    full_path = abs_path = path.abspath(simp_path)

    data = load_file(full_path)

    write_lines = True
    wait = False
    block_removal = False
    count = 0

    for idx, line in enumerate(data):
        if "28.6fps" in line:
            write_lines = False
            block_removal = True
        elif "End Export" in line and block_removal:
            wait = True
            count = 1
        elif wait and count > 0:
            write_lines = False
            count += -1
        elif wait and count <= 0:
            wait = False
            block_removal = False
            write_lines = True

        print(write_lines)

        if write_lines:
            f = open(output_file, "a")
            f.write(f"{line}\n")
            f.close()
