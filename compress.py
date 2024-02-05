import pickle
import sys
import io

class NodeTree(object):
    def __init__(self, left=None, right=None, char=None, freq=0):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq

    def children(self):
        return self.left, self.right

def huffman_code_tree(node, binString='', code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = binString
        huffman_code_tree(node.left, binString + '0', code)
        huffman_code_tree(node.right, binString + '1', code)
    return code

def count_occurances(input_data):
    try:
        freq = {}
        with open(input_data, 'rt', encoding='utf-8') as f:
            while byte := f.read(1):
                if byte in freq:
                    freq[byte].freq += 1
                else:
                    freq[byte] = NodeTree(char=byte, freq=1)
        return freq
    except Exception as e:
        print(f'An error occurred in count_occurances: {e}')
        return None

def main():
    try:
        input_data = sys.argv[-1]
        output_file = "compressed_output.bin"  # Specify your output file name

        freq = count_occurances(input_data)
        nodes = list(freq.values())

        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq, reverse=True)
            left = nodes.pop()
            right = nodes.pop()
            node = NodeTree(left, right, freq=left.freq + right.freq)
            nodes.append(node)

        huffmanCode = huffman_code_tree(nodes[0])

        try:
            with open(input_data, 'r', encoding='utf-8') as f:
                # Remove BOM if present
                data = f.read()
                if data and ord(data[0]) == 65279:
                    data = data[1:]
                f = io.StringIO(data)

                with open(output_file, 'wb') as output:
                    # Writing a marker to indicate the end of the header and start of compressed data
                    output.write(b'\x00\x01\x02\x03')  # You can use any unique pattern or marker

                    # Writing Huffman tree information
                    pickle.dump(nodes[0], output)  # Using pickle to serialize the tree

                    # Convert Huffman codes to binary and write to the output file
                    bit_string = ''.join([huffmanCode[byte] for byte in data])
                    while len(bit_string) % 8 != 0:
                        bit_string += '0'  # Padding with zeros to make the length a multiple of 8
                    bytes_array = bytearray([int(bit_string[i:i+8], 2) for i in range(0, len(bit_string), 8)])
                    output.write(bytes_array)

        except Exception as e:
            print(f'An error occurred while writing the output file from the input: {e}')

        print(f"File {output_file} created successfully.")

        return freq

    except Exception as e:
        print(f'An error occurred in main: {e}')


if __name__ == "__main__":
    main()
