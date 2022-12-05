from utils.input_parser import txt_to_list

INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"


def get_input_stacks(input):
    stacks_input = []
    line_cnt = 0
    for line in input:
        line_cnt += 1
        if line in ['\n', '\r\n']:
            break
        else:
            stacks_input.append(line.strip('\n'))

    print(stacks_input)

    stack_cnt = int(stacks_input.pop().strip().split(" ").pop())
    return stacks_input, stack_cnt, line_cnt


def get_input_moves(input, start_line):
    return input[start_line:]


class CrateStacks:
    def __init__(self, stack_cnt):
        self.stacks = []
        for i in range(stack_cnt):
            self.stacks.append([])

    def create_stacks(self, stack_input):
        for i in range(len(stack_input)-1, -1, -1):
            row_crates = stack_input[i]
            stack_no = 0
            for j in range(0, len(row_crates), 4):
                if row_crates[j] == '[':
                    self.stacks[stack_no].append(row_crates[j+1])
                stack_no += 1

    def get_stacks(self):
        return self.stacks

    def move_crate(self, stackA, stackB):
        """ Move crate from stackA to stackB """
        crate = self.stacks[stackA].pop()
        self.stacks[stackB].append(crate)

    def execute_moves(self, input_moves):
        for move in input_moves:
            move_cnt, stackA, stackB = self.parse_move(move)
            for i in range(move_cnt):
                self.move_crate(stackA, stackB)

    def execute_moves_new(self, input_moves):
        for move in input_moves:
            move_cnt, stackA, stackB = self.parse_move(move)
            temp_stack = []
            for i in range(move_cnt):
                temp_stack.append(self.stacks[stackA].pop())
            for i in range(move_cnt):
                self.stacks[stackB].append(temp_stack.pop())

    def get_top_crates(self):
        top_crates = []
        for stack in self.stacks:
            top_crates.append(stack[-1])

        return "".join(top_crates)


    @staticmethod
    def parse_move(move):
        move_split = move.strip().split(" ")
        return int(move_split[1]), int(move_split[3])-1, int(move_split[5])-1


if __name__ == '__main__':
    input_lst = txt_to_list(INPUT_PATH)

    input_stacks, stack_cnt, line_cnt = get_input_stacks(input_lst)
    input_moves = get_input_moves(input_lst, line_cnt)
    print(input_stacks, stack_cnt, line_cnt)
    print(input_moves)

    all_stacks = CrateStacks(stack_cnt)
    all_stacks.create_stacks(input_stacks)
    print(all_stacks.get_stacks())

    all_stacks.execute_moves_new(input_moves)
    print(all_stacks.get_stacks())
    print(all_stacks.get_top_crates())


