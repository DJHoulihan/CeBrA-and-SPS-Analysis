
void runInfo(TString path){
  
  char* dir  = gSystem->ExpandPathName(path.Data());
  void* dirp = gSystem->OpenDirectory(dir);
  
  const char* entry;
  const char* fileName;
  TString str;
  Int_t n = 0;
  
  while((entry = (char*)gSystem->GetDirEntry(dirp))) {
    str = entry;
    if(str.EndsWith(".root")){

      Int_t runNumber;
      std::sscanf(entry, "run_%d.root", &runNumber);
      
      fileName = gSystem->ConcatFileName(dir, entry);
      TFile *pF = new TFile(fileName);
      
      TParameter<double>* Theta;
      TParameter<double>* Bfield;
      TParameter<Long64_t>* beamint;

      pF->GetObject("Theta", Theta);
      pF->GetObject("Bfield", Bfield);
      pF->GetObject("beamint", beamint);

      if(n == 0)
	cout << Form("%5s%12s%12s%12s",
		     " ", "ThetaCM", "B Field", "Integrator")
	     << endl
	     << Form("%5s%12s%12s%12s",
		     "Run", "(deg)", "(Gauss)", "Counts")
	     << endl;
      
      cout << Form("%5d%12.1f%12.1f%12d",
		   runNumber, Theta->GetVal(),
		   Bfield->GetVal(), beamint->GetVal())
	   << endl;

      n++;

    }
  }
}

void runInfo(){
  runInfo("/home/dhoulihan/Projects/SPS_CEBRA_Oct2022ad/Workingdir/analyzed");
}

