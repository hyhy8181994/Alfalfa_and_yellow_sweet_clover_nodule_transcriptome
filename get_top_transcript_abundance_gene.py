import pandas as pd
import pickle as pk

def get_top_gene(infile,annotation):
    ann = pk.load(open(annotation,"rb"))
    df = pd.read_table(infile)
    sorted_df = df.sort_values(["Average_tpm"],ascending=False)
    tpm_only_df = sorted_df[["Geneid","Average_tpm"]]
    id_list = list(tpm_only_df["Geneid"])


if __name__ == '__main__':
    
    alfalfa_gene = "./alfalfa_triplicate_salmon_tpm.txt"
    clover_gene = "./clover_triplicate_salmon_tpm.txt"
    alfalfa_ann = "./blast/alfalfa_functional_annotations.dat"
    clover_ann = "./blast/clover_functional_annotations.dat"
    get_top_gene(alfalfa_gene,alfalfa_ann)
    get_top_gene(clover_gene,clover_ann)
    