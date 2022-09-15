#!/usr/bin/python

import sys
import os

x=sys.argv[1]

fo=open('/usr/local/adacnew/PinnacleSiteData/Scripts/HotScripts/Physics/LARK_Dose_Recon_v1.4/create_2dgr.Script','w+')

for i in range(0,int(x)):
	fo.write('Store.FloatAt.startG=TrialList.Current.BeamList.#"#'+str(i)+'".CPManager.ControlPointList.#"#0".Gantry;\n')
	fo.write('Store.FloatAt.stopG=TrialList.Current.BeamList.#"#'+str(i)+'".CPManager.ControlPointList.#"#1".Gantry;\n')
	fo.write('Store.At.startG.Subtract=Store.FloatAt.stopG;\n')
	fo.write('Store.At.startG.Absolute="";\n')
	fo.write('Store.FloatAt.Four=4;\n')
	fo.write('IF.Store.FloatAt.startG.EQUALTO.Store.FloatAt.Four.THEN.PluginManager.InversePlanningManager.InterpolateControlPointsForBeam = TrialList.Current.BeamList.#"#'+str(i)+'";\n')
	fo.write('Store.FreeAt.startG="";\n')
	fo.write('Store.FreeAt.stopG="";\n\n')
fo.write('TrialList.Current.ComputeUncomputedBeams=1;')
fo.close()
