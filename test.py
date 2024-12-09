from ezio.huffman import build_huffman_tree, huffman_code, huffman_data

def test_huffman():
    # Example input data
    data = "this is an example for huffman encoding"
    
    # Step 1: Build frequency table
    freq_table = {}
    for char in data:
        freq_table[char] = freq_table.get(char, 0) + 1

    # Step 2: Build Huffman tree
    huffman_tree = build_huffman_tree(freq_table)

    # Step 3: Generate Huffman codes
    huffman_codes = huffman_code(huffman_tree)

    # Debugging: Check type of huffman_codes
    print("Huffman Codes:", huffman_codes)
    print("Type of huffman_codes:", type(huffman_codes))  # Ensure it's a dictionary

    # Step 4: Encode the data
    encoded_data = ''.join(huffman_codes[char] for char in data)
    print("Encoded Data:", encoded_data)

    # Step 5: Decode the data
    decoded_data = huffman_data(encoded_data, huffman_codes)
    print("Decoded Data:", decoded_data)

    # Validation
    assert data == decoded_data, "Decoded data does not match original!"
    print("Test passed!")

if __name__ == "__main__":
    test_huffman()
