import ROOT
import os

# Use this code as the first step in the cebra gain-matching analysis.
# It goes through each analyzed root file in your working directory and gives out just the cebraE{i} columns.
# Each new root file will have a folder for each detector. You can then hadd them in terminal into one root file.
# Use this root file in hdtv to fit and save peaks for gain matching. 



def histo1d(Frame, Name, X, X_List):
   #X_List should be something like X_List = [bins,initial,final]
   histo1d = Frame.Histo1D((f"{Name}",f"{Name}",X_List[0], X_List[1], X_List[2]),X)
   return histo1d


path = '/home/dhoulihan/Projects/SPS_CEBRA_Oct2022ad/Workingdir/analyzed/'

#Creates a list of run numbers give it the path.  Directory should only have the trees that you want to use
run_list = []
for filename in os.listdir(path):
   if filename.endswith(".root"):
       run_number = int(filename.split("_")[1].split(".")[0])
       run_list.append(run_number)

run_list.sort()


for i in range(len(run_list)):
   
   print(f"Run {run_list[i]}")
   
   df = ROOT.RDataFrame("SPSTree",f"{path}run_{run_list[i]}.root")
   cebraE_raw_to_ECal = []
   for j in range(5):     
       df_i = df.Filter(f"cebraE{j} != -1")
       cebraE_raw_to_ECal.append(histo1d(df_i,f"cebraE{j}_run_{run_list[i]}",f"cebraE{j}",[512,0,4096]))

   output = ROOT.TFile.Open(f"run_{run_list[i]}_cebraEnergy.root", "RECREATE")
   output.cd()
   for k in range(5):
       output.mkdir(f"det{k}")
       output.cd(f"det{k}")
       cebraE_raw_to_ECal[k].Write()
   
   output.Close()


