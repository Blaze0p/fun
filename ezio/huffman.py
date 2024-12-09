import heapq

class Node:
    def __init__(self,symbol,freq):
        self.symbol = symbol
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):

    heap = [Node(symbol,freq) for symbol,freq in freq_table.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None,left.freq+right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap,merged)

    return heap[0]

def huffman_code(tree,prefix='',codes=None):

    if codes is None:
        codes = {}

    if tree.symbol is not None:
        codes[tree.symbol] =  prefix
    else:
        huffman_code(tree.right,prefix+"0",codes)
        huffman_code(tree.left,prefix+"1",codes)
    
    return codes


def huffman_data(encoded_data, huff_codes):
    reverse_codes = {v: k for k, v in huff_codes.items()}

    decoded_data = []
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_data)