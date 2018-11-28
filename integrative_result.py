import os
#from process_result import
import pandas
import csv
from os import listdir
from os.path import isfile, join


class ResultFile(object):
    """object used to encapsulate the file and his specific column to be processed and filtered"""
    def __init__(self, column,filepath):
        #super(AutomatizedTool, self).__init__()
        self.column = column
        self.filepath = filepath


def get_columns(filepath,column):
    df = pandas.read_csv(filepath, sep='\t')
    annotated_genes = df[column].tolist()

    #join list in a string separated by ';'
    annotated_genes = '; '.join(annotated_genes)
    print("\n\nannotated_genes:",annotated_genes,"\n\n")
    return annotated_genes


def filter_results(organism_name,filepath_v,filepath_r):
    vir=ResultFile(virulence_column,filepath_v)
    res=ResultFile(resistance_column,filepath_r)
    row_data=[organism_name,get_columns(vir.filepath,vir.column),get_columns(res.filepath,res.column)]
    return row_data





##################### PROCESS PIPELINE #############################
mypath="genomas"
virulence_column="Virulence factor"
resistance_column="Best_Hit_ARO"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#genomas = os.listdir(diretorio)
data = []
for genoma in onlyfiles:
    #print(genoma)
    filepath = os.path.abspath(mypath+"/"+genoma)
    #print(filepath)
    filename=genoma.split(".")[0]
    vir_result_file = filepath.rsplit("\\",1)[0]+"\\vir_"+filename+"\\results_tab.txt"
    res_result_file = filepath.rsplit("\\",1)[0]+"\\res_"+filename+"\\out_resistance.txt"
    #print("\n--------\n")
    #print(vir_result_file)
    #print(res_result_file)
    #print(filename)
    data.append(filter_results(filename,vir_result_file,res_result_file))

df = pandas.DataFrame(data,columns=["Organism","Virulence factors","Resistance Genes"])
print("writing and saving file...")
df.to_csv('integrative_analysis.csv')

print("\nall genomes processed...\n")
print("\npipeline finished!\n")
