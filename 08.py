import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    def build_tree(self, frequencies: dict[str, int]) -> Node:
        heap = []

        for char, freq in frequencies.items():
            heapq.heappush(heap, Node(char, freq))

        if not heap:
            self.root = None
            return None

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right

            heapq.heappush(heap, parent)

        self.root = heap[0]
        return self.root

    def generate_codes(self) -> dict[str, str]:
        self.codes = {}

        def traverse(node, code):
            if node is None:
                return

            if node.char is not None:
                self.codes[node.char] = code or "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        return self.codes


frequencies = {'a': 5,'b': 9,'c': 12,'d': 13,'e': 16,'f': 45}

coder = HuffmanCoder()
coder.build_tree(frequencies)

print("Huffman Codes:")
print(coder.generate_codes())
