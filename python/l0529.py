class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        queue = [click]
        p2n = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'M':
                    continue
                for a in (-1, 0, 1):
                    for b in (-1, 0, 1):
                        if a == 0 and b == 0:
                            continue
                        elif 0 <= i+a <= len(board)-1 and 0 <= j+b <= len(board[0])-1:
                            p2n[(i+a, j+b)] = p2n.get((i+a, j+b), 0) + 1
        visited = set()
        while len(queue) != 0:
            x, y = queue[0]
            del queue[0]
            num_m = p2n.get((x, y), 0)
            if num_m != 0:
                board[x][y] = str(num_m)
                continue
            board[x][y] = 'B'
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= x+i <= len(board)-1 and 0 <= y+j <= len(board[0])-1 and board[x+i][y+j] == 'E' and (x+i, y+j) not in visited:
                        print(x+i, y+j)
                        queue.append([x+i, y+j])
                        visited.add((x+i, y+j))
        return board
