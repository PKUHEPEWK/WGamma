#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from wgModule import *
from countHistogramsLHEAndGenSelectionsModule import *

#from  wgGenModule import *

#from countHistogramsModule import *
#from countHistogramsPDFModule import *
#from countHistogramsQCDScaleModule import *


from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#p=PostProcessor(".",inputFiles(),None,"wg_keep_and_drop.txt",[countHistogramsModule(),countHistogramsLHEAndGenSelectionsModule(),puWeight_2016(),PrefCorr(),wgModule()],provenance=True,justcount=False,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel = "wg_output_branch_selection.txt")

p=PostProcessor(".",inputFiles(),None,"wg_keep_and_drop.txt",[countHistogramsModule(),puWeight_2016(),PrefCorr(),wgModule()],provenance=True,justcount=False,fwkJobReport=True,jsonInput=runsAndLumis(),noOut=False,outputbranchsel = "wg_output_branch_selection.txt")

p.run()

#print "DONE"
#os.system("ls -lR")



