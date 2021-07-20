import pandas as pd

def get_top_gene(infile,annotation):
    ann_df = pd.read_table(annotation)
    for index,row in ann_df.iterrows():
        id = row["contig_id"]

    df = pd.read_table(infile)
    sorted_df = df.sort_values(["Average_tpm"],ascending=False)
    tpm_only_df = sorted_df[["Geneid","Average_tpm"]]
    id_list = list(tpm_only_df["Geneid"])


if __name__ == '__main__':
    
    alfalfa_gene = "./alfalfa_triplicate_salmon_tpm.txt"
    clover_gene = "./clover_triplicate_salmon_tpm.txt"
    alfalfa_ann = "./blast/alfalfa_filtered_annotations_1.tsv"
    clover_ann = "./blast/clover_filtered_annotations_1.tsv"
    get_top_gene(alfalfa_gene,alfalfa_ann)
    get_top_gene(clover_gene,clover_ann)
    