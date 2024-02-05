import pickle
import sys
import io
from compress import main
from compress import NodeTree

def decode_huffman_tree(data, bit_string=''):
    if data.char is not None:
        return {bit_string: data.char}
    else:
        code = {}
        code.update(decode_huffman_tree(data.left, bit_string + '0'))
        code.update(decode_huffman_tree(data.right, bit_string + '1'))
        return code

def huffman_code_tree(node, binString='', code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = binString
        huffman_code_tree(node.left, binString + '0', code)
        huffman_code_tree(node.right, binString + '1', code)
    return code

def decompress(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            # Reading the marker and Huffman tree information
            marker = f.read(4)
            if marker != b'\x00\x01\x02\x03':
                raise ValueError("Invalid compressed file format")

            huffman_tree = pickle.load(f)

            # Reading the compressed binary data
            compressed_data = f.read()

        # Decode Huffman tree
        huffman_code = decode_huffman_tree(huffman_tree)

        # Decode binary data using Huffman tree
        bit_string = ''.join(f'{byte:08b}' for byte in compressed_data)
        decoded_text = ''
        current_code = ''
        for bit in bit_string:
            current_code += bit
            if current_code in huffman_code:
                decoded_text += huffman_code[current_code]
                current_code = ''

        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(decoded_text)

        print(f"File {output_file} decompressed successfully.")

    except Exception as e:
        print(f'An error occurred in decompress: {e}')

def main():
    try:
        input_data = sys.argv[-1]

        try:
            compressed_file = "compressed_output.bin"
            decompressed_file = "decompressed_output.txt"
            decompress(compressed_file, decompressed_file)


        except Exception as e:
            print(f'An error occurred while writing the output file from the input: {e}')

        print(f"File {decompressed_file} created successfully.")

    except Exception as e:
        print(f'An error occurred in main: {e}')

if __name__ == "__main__":
    main()