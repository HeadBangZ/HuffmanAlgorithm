import sys
import bitIO
import Huffman

# One could choose to use int.from_bytes(bytes, byteorder, *, signed=False) instead of ord
def frequency(input_file):
    frequencies = [0] * 256
    # Read input file and create frequency list
    with open(input_file, "rb") as file_in:
        b = file_in.read(1)
        while b != b"":
            frequencies[ord(b)] += 1
            b = file_in.read(1)
    return frequencies

def scan_file(input_file, output_file):
    # Scan file first time to build frequency list
    frequencies = frequency(input_file)
    # Build huffman tree
    huffman_tree = Huffman.huffman_tree(frequencies)
    # Write to the output file
    codes = Huffman.inorder(huffman_tree, "", {})
    # Write file
    with open(output_file, "wb") as file_out:
        # Write frequency to file
        bitstreamout = bitIO.BitWriter(file_out)
        for i in frequencies:
            bitstreamout.writeint32bits(i)
        # Read file again 1 bit at the time
        with open(input_file, "rb") as file_in:
            b = file_in.read(1)
            while b != b"":
                # Read file again and convert the byte to an int, use that int to know which code to get
                code = codes[ord(b)]
                for c in code:
                    bitstreamout.writebit(int(c))
                b = file_in.read(1)
        bitstreamout.close()

if __name__ == "__main__":
    scan_file(sys.argv[1], sys.argv[2])