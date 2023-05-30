import os
# Directory constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.environ.get("INPUT_DIR", os.path.join(BASE_DIR, "input"))  
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", os.path.join(BASE_DIR, "output"))

if __name__ == "__main__":
    print("Hello World!")

    # read text file in input directory
    lines = []
    with open(f"{INPUT_DIR}/test.txt", "r") as f:
        # for each line, append to lines
        for line in f: 
            lines.append(line)
        print("Read lines from input directory")
    
    # write lines to output directory
    with open(f"{OUTPUT_DIR}/test.txt", "w") as f:
        for line in lines:
            f.write(line)
        print("Wrote lines to output directory")
