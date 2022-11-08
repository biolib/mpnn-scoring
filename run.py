from Bio import SeqIO
from pathlib import Path
import argparse
from collections import defaultdict
import json
from colabdesign.mpnn import mk_mpnn_model


# Args
parser = argparse.ArgumentParser()
parser.add_argument("--fasta", help="Path to input FASTA file", type=Path, required=True)
parser.add_argument("--pdb", help="Path to output PDB directory", type=Path, required=True)
args = parser.parse_args()

# Load the model
mpnn_model = mk_mpnn_model()
mpnn_model.prep_inputs(pdb_filename=args.pdb)
samples = mpnn_model.sample_parallel()

# Maybe print which structure it is


# Create a JSON file
os.makedirs("/home/biolib/output", exist_ok=True)
outfile = open("/home/biolib/output/output.json", "w")

# Read FASTA file
with open(args.fasta) as handle:
    # DICT FOR JSON OUTPUT
    score_dict =  defaultdict(dict)

    for record in SeqIO.parse(handle, "fasta"):
        # Print process
        dict_mpnn = mpnn_model.score(seq=record.seq)
        score = dict_mpnn["score"]
        print(f"ID: {record.id}\nSequence: {record.seq}\nScore: {score}")
        
        #Save process into JSON file
        score_dict[record.id]["sequence"] = str(record.seq)
        score_dict[record.id]["length"]= len(str(record.seq))
        score_dict[record.id]["score"]= f"{score:0.5f}"

# WRITING TO JSON FILE
json_object = json.dumps(score_dict, indent=4)

# Writing to sample.json
outfile.write(json_object)
outfile.close()        

