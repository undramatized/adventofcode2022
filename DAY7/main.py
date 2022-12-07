from utils.input_parser import txt_to_list

INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.directories = []
        self.files = []
        self.parent = parent

    def add_file(self, name, size):
        self.files.append({'name': name, 'size': int(size)})

    def add_directory(self, directory):
        self.directories.append(directory)

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_directory(self, name):
        for directory in self.directories:
            if name == directory.get_name():
                return directory
        return False

    def get_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file['size']
        for directory in self.directories:
            total_size += directory.get_total_size()

        # print(self, total_size)

        return total_size

    def get_total_sizes(self):
        total_sizes = []
        curr_dir_total = 0
        for file in self.files:
            curr_dir_total += file['size']

        for directory in self.directories:
            total_sizes.extend(directory.get_total_sizes())
            curr_dir_total += total_sizes[-1]

        total_sizes.append(curr_dir_total)

        return total_sizes


    def __str__(self):
        return f"directory_{self.name}"

    def __repr__(self):
        return f"directory_{self.name}"


class FileSystem:
    def __init__(self, commands: list):
        self.root = Directory('root')
        self.curr_dir = self.root
        self.commands = commands

    def get_dir(self, dir_name):
        if self.curr_dir.get_directory(dir_name):
            return self.curr_dir.get_directory(dir_name)
        else:
            new_dir = Directory(dir_name, self.curr_dir)
            self.curr_dir.add_directory(new_dir)
            return new_dir

    def traverse(self, dir_name):
        if dir_name == '/':
            self.curr_dir = self.root
        elif dir_name == '..':
            self.curr_dir = self.curr_dir.get_parent()
        else:
            self.curr_dir = self.get_dir(dir_name)
        # print(dir_name, self.curr_dir)

    def populate(self):
        curr_item = self.get_next_command()
        while curr_item[0] != '$':
            input_split = curr_item.split(" ")
            if input_split[0] == 'dir':
                self.get_dir(input_split[1].strip())
            else:
                filename = input_split[1].strip()
                filesize = input_split[0].strip()
                self.curr_dir.add_file(filename, filesize)

            if self.has_next_command():
                curr_item = self.get_next_command()
            else:
                break
        self.commands.insert(0, curr_item)

    def get_next_command(self):
        if len(self.commands) > 0:
            return self.commands.pop(0)
        else:
            return False

    def has_next_command(self):
        return len(self.commands) > 0

    def parse_command(self, command):
        # print(command, self.root.directories)
        command_split = command.strip().split(" ")
        if command_split[1] == 'cd':
            # print("traversing", command_split)
            self.traverse(command_split[2])
        elif command_split[1] == 'ls':
            # print("populating", command_split)
            self.populate()

    def execute_commands(self):
        while self.has_next_command():
            self.parse_command(self.get_next_command())

    def get_root(self):
        return self.root

    def delete_largest_directory(self):
        curr_size = self.root.get_total_size()
        all_dir_sizes = sorted(self.root.get_total_sizes())

        min_dir_size = 30000000 - (70000000 - curr_size)

        print(curr_size, min_dir_size)

        for dir in all_dir_sizes:
            if dir > min_dir_size:
                return dir



def get_max_vals(totals_list, max):
    total = 0
    for val in totals_list:
        if val < max:
            total += val

    return total

if __name__ == '__main__':
    filesystem = FileSystem(txt_to_list(INPUT_PATH))
    filesystem.execute_commands()
    total_sizes = filesystem.get_root().get_total_sizes()
    print(total_sizes)
    print(get_max_vals(total_sizes, 100000))
    print(filesystem.delete_largest_directory())

