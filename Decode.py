import sys
import bitIO
import Huffman

def scan_file(input_file, output_file):
    # Read the file
    with open(input_file, "rb") as file_in:
        bitstreamin = bitIO.BitReader(file_in)
        frequencies = []
        # Fill the list with frequencies, and get the sum of all the frequencies
        for _ in range(256):
            frequencies.append(bitstreamin.readint32bits())
        freq_sum = sum(frequencies)

        # Build huffman tree
        huffman_tree = Huffman.huffman_tree(frequencies)
        temp = huffman_tree

        # Write to the output file
        with open(output_file, "wb") as file_out:
            total_bytes = 0
            while bitstreamin.readsucces():
                # When total bytes is the same as the sum we stop writing
                if total_bytes == freq_sum:
                    break
                bit = bitstreamin.readbit()
                # Go down the tree until a leaf is hit
                if bit == 0:
                    temp = temp.left
                else:
                    temp = temp.right
                # Write the leafs value to the output file, set temp to the root again
                if temp.left is None and temp.right is None:
                    file_out.write(bytes([temp.data]))
                    temp = huffman_tree
                    total_bytes += 1

if __name__ == "__main__":
    scan_file(sys.argv[1], sys.argv[2])