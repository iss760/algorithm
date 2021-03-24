from time import sleep


class MAP:
    def __init__(self):
        self.WINDOW_WIDTH = 8
        self.WINDOW_HEIGHT = 8

        self.map_structure = []
        self.set_map()

    def set_map(self):
        # first line
        self.map_structure.append([1 for _ in range(self.WINDOW_WIDTH+2)])
        # middle line
        for _ in range(self.WINDOW_HEIGHT):
            temp = []
            for wgt in range(self.WINDOW_WIDTH+2):
                if wgt == 0 or wgt == self.WINDOW_WIDTH+1:
                    temp.append(1)
                else:
                    temp.append(0)
            self.map_structure.append(temp)
        # last line
        self.map_structure.append([1 for _ in range(self.WINDOW_WIDTH+2)])

    def draw_map(self):
        for hgt in range(self.WINDOW_HEIGHT+2):
            for wgt in range(self.WINDOW_WIDTH+2):
                if self.map_structure[hgt][wgt] == 1:
                    print("1", end="")
                else:
                    print("0", end="")
            print()

    @staticmethod
    def remove_map():
        print('\r')
        print("aaa")


class Block:
    def __init__(self):
        self.BLOCK_WINDOW_WIDTH = 3
        self.BLOCK_WINDOW_HEIGHT = 3

        self.BLOCK_CANDIDATES = []
        self.set_blocks()

    def set_blocks(self):
        block1 = [[0, 0, 0],
                  [0, 1, 0],
                  [1, 1, 1]]

        self.BLOCK_CANDIDATES.append(block1)

    def down_block(self):
        passs
        


if __name__ == '__main__':
    tt_map = MAP()
    while True:
        tt_map.draw_map()
        sleep(1)

