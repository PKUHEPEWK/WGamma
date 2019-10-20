#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  wgRealPhotonTemplateModule import *

from PhysicsTools.NanoAODTools.postprocessing.modules.common.countHistogramsModule import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *

p=PostProcessor(".",['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/3E72F1BB-3625-8744-A7A6-6EF26EC42149.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/52B2EA94-D29B-D94D-82C2-B29616232363.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/7FD2046E-73DC-9748-80DA-EE6AC1EC5D9D.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/8588D51B-A113-5949-9471-37CBF95D0DCE.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/A7616F77-C392-8D44-9DAD-D00EF4D6AB47.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/AEC9046A-8BE9-D74D-9429-207C746AAE89.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/C6DC3A22-1A85-CC46-B187-64341AA768FD.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/909B9464-5C4D-584D-BB63-054ECF5A37FE.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/EFC1BDD3-7856-3B4B-9BBE-1A35E0041590.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/EE0D9AB9-EA5B-7247-9D53-B275C338D609.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/7F996938-4C00-4343-9A7B-2ABAFF6236C7.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/6FC5B0DC-1F6D-2F4D-AD54-A4D7B444252A.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/2AFC4DCC-3D93-8941-9FD4-A7D089B382A2.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/250000/05F970F6-4774-424D-99F4-EDB3D9609BF0.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/FEA4AD8B-8552-AF4F-8553-2D8E1D1ACF26.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/D996AA74-D703-3B4F-B203-9D82BE713163.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/20E140BE-CECF-3541-9F26-9B93C8D94144.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/120000/059AF23F-F834-2D42-BCE0-7FF1A8C61F32.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/D8CD07A1-4C52-124E-A00A-8E29DD67AF4A.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/CC1B9135-5928-6140-A03D-D20E38F83F6F.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/C31A582E-9B63-A14E-8966-72E96E2B7507.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/C15AC854-9AD1-F249-A2A1-A4FAA6FE59A0.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/AEE1E411-B260-624A-87F7-16737973829E.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/ABA91A5F-367C-EA42-A647-2B3BECEB12D8.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/7897258A-EA1C-D040-A3EB-AB5564E3F4F7.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/6DC8450E-4CDA-0945-BAAB-178FAD3292BC.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/0B66CFC1-9468-CB4D-8C47-62282EE3981B.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/A8FAC162-1469-CD47-909D-93CC8C5ED5EF.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/2254BFBB-E783-A048-828C-2DB1096CC775.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/100000/63232918-95EE-794F-8BEF-2F6EDF093CE8.root',
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAODv5/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/3127AE24-1D48-154F-AF3D-C51F87DFA73B.root'],None,"wg_real_photon_template_keep_and_drop.txt",[countHistogramsModule(),wgRealPhotonTemplateModule(),puWeight_2016(),PrefCorr()],provenance=True,justcount=False,noOut=False,fwkJobReport=True,outputbranchsel = "wg_real_photon_template_output_branch_selection.txt")

p.run()

print "DONE"

