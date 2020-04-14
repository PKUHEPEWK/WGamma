import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import math

mg5amc_nlo_xs = 178.6

mg5amc_wgjets_filename = "/afs/cern.ch/work/a/amlevin/data/wg/2016/1June2019/wgjets.root"

mg5amc_wgjets_file = ROOT.TFile(mg5amc_wgjets_filename)

n_weighted_mg5amc_pass_fid_selection = mg5amc_wgjets_file.Get("nEventsGenWeighted_PassFidSelection").GetBinContent(1)

n_weighted_mg5amc = mg5amc_wgjets_file.Get("nEventsGenWeighted").GetBinContent(1)

mg5amc_nlo_fiducial_xs = mg5amc_nlo_xs*n_weighted_mg5amc_pass_fid_selection/n_weighted_mg5amc

#text2hdf5.py ~/wg/wg_dcard_theory_exp.txt 
#combinetf.py ~/wg/wg_dcard_theory_exp.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory.txt
#combinetf.py ~/wg/wg_dcard_theory.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 
#text2hdf5.py ~/wg/wg_dcard_exp.txt
#combinetf.py ~/wg/wg_dcard_exp.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory_exp.txt -S 0 
#combinetf.py ~/wg/wg_dcard_theory_exp.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 
rexp = 1  
rexpunc = 0.039546
rexptheoryunc = 0.006748
rexpexpunc = 0.038928
rexpnosystunc = 0.002961

#text2hdf5.py ~/wg/wg_dcard_theory_exp_el_chan.txt
#combinetf.py ~/wg/wg_dcard_theory_exp_el_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory_el_chan.txt
#combinetf.py ~/wg/wg_dcard_theory_el_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1
#text2hdf5.py ~/wg/wg_dcard_exp_el_chan.txt 
#combinetf.py ~/wg/wg_dcard_exp_el_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory_exp_el_chan.txt -S 0 
#combinetf.py ~/wg/wg_dcard_theory_exp_el_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1
rexpelectron = 1  
rexpelectronunc = 0.062047
rexpelectrontheoryunc = 0.011856
rexpelectronexpunc = 0.059980
rexpelectronnosystunc = 0.005243

#text2hdf5.py ~/wg/wg_dcard_theory_exp_mu_chan.txt 
#combinetf.py ~/wg/wg_dcard_theory_exp_mu_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory_mu_chan.txt
#combinetf.py ~/wg/wg_dcard_theory_mu_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1
#text2hdf5.py ~/wg/wg_dcard_exp_mu_chan.txt 
#combinetf.py ~/wg/wg_dcard_exp_mu_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1 --binByBinStat
#text2hdf5.py ~/wg/wg_dcard_theory_exp_mu_chan.txt -S 0 
#combinetf.py ~/wg/wg_dcard_theory_exp_mu_chan.hdf5 --useSciPyMinimizer -t -1 --expectSignal=1
rexpmuon = 1  
rexpmuonunc = 0.047604
rexpmuontheoryunc = 0.008272 
rexpmuonexpunc = 0.046550
rexpmuonnosystunc = 0.003587

print "xs = %0.2f +/- %0.2f"%(mg5amc_nlo_fiducial_xs * rexp,mg5amc_nlo_fiducial_xs * rexpunc)

print "xs = %0.2f +/- %0.2f (stat) +/- %0.2f (exp) +/- %0.2f (theory)"%(mg5amc_nlo_fiducial_xs * rexp,mg5amc_nlo_fiducial_xs * rexpnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpexpunc,2)-pow(rexpnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpunc,2)-pow(rexpexpunc,2)))

print "xs = \sigma = %0.2f \\pm %0.2f \\text{ pb} = %0.2f \\pm %0.2f \\text{ (stat)} \\pm %0.2f \\text{ (exp)} \\pm %0.2f \\text{ (theory) pb}"%(mg5amc_nlo_fiducial_xs * rexp,mg5amc_nlo_fiducial_xs * rexpunc,mg5amc_nlo_fiducial_xs * rexp,mg5amc_nlo_fiducial_xs * rexpnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpexpunc,2)-pow(rexpnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpunc,2)-pow(rexpexpunc,2)))

print "xs based on electron channel = %0.2f +/- %0.2f"%(mg5amc_nlo_fiducial_xs * rexpelectron,mg5amc_nlo_fiducial_xs * rexpelectronunc)

print "xs based on electron channel = %0.2f +/- %0.2f (stat) +/- %0.2f (exp) +/- %0.2f (theory)"%(mg5amc_nlo_fiducial_xs * rexpelectron,mg5amc_nlo_fiducial_xs * rexpelectronnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpelectronexpunc,2)-pow(rexpelectronnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpelectronunc,2)-pow(rexpelectronexpunc,2)))

print "xs based on electron channel = \sigma = %0.2f \\pm %0.2f \\text{ pb} = %0.2f \\pm %0.2f \\text{ (stat)} \\pm %0.2f \\text{ (exp)} \\pm %0.2f \\text{ (theory) pb}"%(mg5amc_nlo_fiducial_xs * rexpelectron,mg5amc_nlo_fiducial_xs * rexpelectronunc,mg5amc_nlo_fiducial_xs * rexpelectron,mg5amc_nlo_fiducial_xs * rexpelectronnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpelectronexpunc,2)-pow(rexpelectronnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpelectronunc,2)-pow(rexpelectronexpunc,2)))

print "xs based on muon channel = %0.2f +/- %0.2f"%(mg5amc_nlo_fiducial_xs * rexpmuon,mg5amc_nlo_fiducial_xs * rexpmuonunc)

print "xs based on muon channel = %0.2f +/- %0.2f (stat) +/- %0.2f (exp) +/- %0.2f (theory)"%(mg5amc_nlo_fiducial_xs * rexpmuon,mg5amc_nlo_fiducial_xs * rexpmuonnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpmuonexpunc,2)-pow(rexpmuonnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpmuonunc,2)-pow(rexpmuonexpunc,2)))

print "xs based on muon channel = \sigma = %0.2f \\pm %0.2f \\text{ pb} = %0.2f \\pm %0.2f \\text{ (stat)} \\pm %0.2f \\text{ (exp)} \\pm %0.2f \\text{ (theory) pb}"%(mg5amc_nlo_fiducial_xs * rexpmuon,mg5amc_nlo_fiducial_xs * rexpmuonunc,mg5amc_nlo_fiducial_xs * rexpmuon,mg5amc_nlo_fiducial_xs * rexpmuonnosystunc,mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpmuonexpunc,2)-pow(rexpmuonnosystunc,2)),mg5amc_nlo_fiducial_xs * math.sqrt(pow(rexpmuonunc,2)-pow(rexpmuonexpunc,2)))

