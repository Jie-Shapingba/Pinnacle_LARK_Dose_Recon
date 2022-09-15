#!/usr/bin/python

import sys
import os

fo=open('/usr/local/adacnew/PinnacleSiteData/Scripts/HotScripts/Physics/LARK_Dose_Recon_v1.4/create_poi.Script','w+')
fo.write('//create_poi\n')

xx=sys.argv[1]

file_name='/home/p3rtp/RadCalc/LARK/'+xx+'_with_LARK.txt'

fi=open(file_name,'r')
a=fi.readlines()[1:]
fi.close()

for i in a:
	j=list(i.split(' '))
	k=j[1].replace('.000000','.0')
	k=k.strip()
	gantry=k.rjust(6,' ')
	j[2]=j[2].strip()
	j[2]=float(j[2])/10
	j[3]=j[3].strip()
	j[3]=float(j[3])/10
	j[4]=j[4].strip()
	j[4]=float(j[4])/10
	fo.write('Store.FreeAt.poi_nm="";\n')
	fo.write('Store.StringAt.poi_nm="with_LARK_";\n')
	fo.write('Store.At.poi_nm.AppendString=Store.StringAt.prsc;\n')
	fo.write('Store.At.poi_nm.AppendString="_'+gantry+'";\n')
	fo.write('CreateNewPOI="";\n')
	fo.write('PoiList.Last.Name=Store.StringAt.poi_nm;\n')
	fo.write('Store.FloatAt.poix=Store.FloatAt.x;\n')
	fo.write('Store.At.poix.Subtract='+str(j[2])+';\n')
	fo.write('PoiList.Last.XCoord=Store.FloatAt.poix;\n')
	fo.write('Store.FloatAt.poiy=Store.FloatAt.y;\n')
	fo.write('Store.At.poiy.Subtract='+str(j[3])+';\n')
	fo.write('PoiList.Last.YCoord=Store.FloatAt.poiy;\n')
	fo.write('Store.FloatAt.poiz=Store.FloatAt.z;\n')
	fo.write('Store.At.poiz.Subtract='+str(j[4])+';\n')
	fo.write('PoiList.Last.ZCoord=Store.FloatAt.poiz;\n\n')

file_name1='/home/p3rtp/RadCalc/LARK/'+xx+'_without_LARK.txt'

fi1=open(file_name1,'r')
b=fi1.readlines()[1:]
fi1.close()

for h in b:
	j=list(h.split(' '))
	k=j[1].replace('.000000','.0')
	k=k.strip()
	gantry=k.rjust(6,' ')
	j[2]=j[2].strip()
	j[2]=float(j[2])/10
	j[3]=j[3].strip()
	j[3]=float(j[3])/10
	j[4]=j[4].strip()
	j[4]=float(j[4])/10
	fo.write('Store.FreeAt.poi_nm="";\n')
	fo.write('Store.StringAt.poi_nm="without_LARK_";\n')
	fo.write('Store.At.poi_nm.AppendString=Store.StringAt.prsc;\n')
	fo.write('Store.At.poi_nm.AppendString="_'+gantry+'";\n')
	fo.write('CreateNewPOI="";\n')
	fo.write('PoiList.Last.Name=Store.StringAt.poi_nm;\n')
	fo.write('Store.FloatAt.poix=Store.FloatAt.x;\n')
	fo.write('Store.At.poix.Subtract='+str(j[2])+';\n')
	fo.write('PoiList.Last.XCoord=Store.FloatAt.poix;\n')
	fo.write('Store.FloatAt.poiy=Store.FloatAt.y;\n')
	fo.write('Store.At.poiy.Subtract='+str(j[3])+';\n')
	fo.write('PoiList.Last.YCoord=Store.FloatAt.poiy;\n')
	fo.write('Store.FloatAt.poiz=Store.FloatAt.z;\n')
	fo.write('Store.At.poiz.Subtract='+str(j[4])+';\n')
	fo.write('PoiList.Last.ZCoord=Store.FloatAt.poiz;\n\n')


fo.close()
