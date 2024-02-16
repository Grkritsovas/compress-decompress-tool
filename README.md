Huffman File Compression and Decompression
This project implements file compression and decompression using the Huffman coding algorithm. The Huffman algorithm is a widely used method for lossless data compression.

Overview
The project consists of two Python scripts:

1.compress.py: Responsible for compressing files using Huffman coding.
2.decompress.py: Responsible for decompressing files compressed using Huffman coding.
This README provides an overview of both scripts.

Installation
1.Clone this repository to your local machine.
2.Ensure you have Python installed (version 3.6 or higher).
3.No additional dependencies are required.
Compression (compress.py)
Usage
To compress a file:
'''
python compress.py <input_file>
'''
Example:
'''
python compress.py input.txt
'''
This will generate a compressed output file named compressed_output.bin.

How it Works
1.The script reads the input file and counts the occurrences of each byte.
2.It constructs a Huffman tree based on the frequencies of the bytes.
3.The Huffman tree is serialized using pickle and written to the output file.
4.The input file is then read again, and its content is compressed using the Huffman codes generated from the tree.
5.The compressed data is written to the output file along with a marker indicating the end of the header and the start of compressed data.
Decompression (decompress.py)
Usage:
To decompress a file:
'''
python decompress.py <input_file>
'''
Example:
'''
python decompress.py compressed_output.bin
'''
This will generate a decompressed output file named decompressed_output.txt.

How it Works
1.The script reads the compressed input file.
2.It reads the marker and Huffman tree information from the file.
3.The Huffman tree is reconstructed using pickle.
4.The compressed binary data is read.
5.The binary data is decoded using the Huffman tree, resulting in the original uncompressed text.
6.The uncompressed text is written to the output file.
