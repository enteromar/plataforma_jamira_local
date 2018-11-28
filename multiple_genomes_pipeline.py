import os
from run_tools import AutomatizedTool

diretorio="genomas"
genomas = os.listdir(diretorio)
for genoma in genomas:
    print(genoma)
    filepath = os.path.abspath(diretorio+"/"+genoma)
    print(filepath)
    filename=genoma.split(".")[0]
    #running tools for each genome
    print("\nrunning virulence analysis for " +filename+"...\n")
    job1 = AutomatizedTool('VirulenceFinder',filepath)
    job1.start("vir_"+filename)
    print("\nrunning virulence analysis for " +filename+"...\n")
    job2 = AutomatizedTool('RGI',filepath)
    job2.start("res_"+filename)
print("\nall genomes processed...\n")
print("\npipeline finished!\n")
