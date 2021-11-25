import sys
import argparse

from PIL import Image
import numpy as np

def main (input_file, output_file):
    img_2d = np.array(Image.open(input_file))
    num_pix = img_2d.shape[0]*img_2d.shape[1]
    img_1d = img_2d.reshape(num_pix, -1)
    index_ordered = np.arange(img_1d.shape[0])
    index_random = np.copy(index_ordered)


    np.random.shuffle(index_random)
    img_out = np.copy(img_1d)
    img_out[index_random] = img_1d[index_ordered]
    result = Image.fromarray(img_out.reshape(img_2d.shape))
    result.save(output_file)
    return 0


if __name__ == '__main__':
    # Initialize the parse
    parser = argparse.ArgumentParser(
        description="null model generation"
    )

    # Add the parameter positional/optional
    parser.add_argument('input_file', help="Image that will be analyzed")
    parser.add_argument('output_file', help="Null Model generated")
    # Parse the arguments
    args = parser.parse_args()
    sys.exit(main(args.input_file, args.output_file))

