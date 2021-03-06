import os
import re
import numpy
import time
from scipy import stats
import matplotlib.pyplot as plt
import sklearn
def getData():
	NameList = []
	RegExList = []
	ColumnNameList = []
	NameList.append('Patient Barcode')
	RegExList.append('bcr_patient_barcode.+>(.+)<')
	ColumnNameList.append('barcode')
	NameList.append('Gender')
	RegExList.append('gender preferred_name.+>(.+)<')
	ColumnNameList.append('gender')
	NameList.append('Year Diagnosed')
	RegExList.append('year_of_initial_pathologic_diagnosis.+>(.+)<')
	ColumnNameList.append('year')
	NameList.append('Age Diagnosed')
	RegExList.append('age_at_initial_pathologic_diagnosis.+>(.+)<')
	ColumnNameList.append('age')
	NameList.append('Blast Percent')
	RegExList.append('lab_procedure_blast_cell_outcome_percentage_value.+>(.+)<')
	ColumnNameList.append('blast')
	NameList.append('Bone Marrow Blast Percent')
	RegExList.append('lab_procedure_bone_marrow_blast_cell_outcome_percent_value.+>(.+)<')
	ColumnNameList.append('BMblast')
	NameList.append('Bone Marrow Promyelocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_promyelocyte_result_percent_value.+>(.+)<')
	ColumnNameList.append('promyelo')
	NameList.append('Bone Marrow Myelocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_myelocyte_result_percent_value.+>(.+)<')
	ColumnNameList.append('myelo')
	NameList.append('Bone Marrow Metamyelocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_metamyelocyte_result_value.+>(.+)<')
	ColumnNameList.append('metamyelo')
	NameList.append('Bone Marrow Band Percent')
	RegExList.append('lab_procedure_bone_marrow_band_cell_result_percent_value.+>(.+)<')
	ColumnNameList.append('band')
	NameList.append('Bone Marrow Neutrophil Percent')
	RegExList.append('lab_procedure_bone_marrow_neutrophil_result_percent_value.+>(.+)<')
	ColumnNameList.append('neutro')
	NameList.append('Bone Marrow Eosinophil Percent')
	RegExList.append('lab_procedure_bone_marrow_lab_eosinophil_result_percent_value .+>(.+)<')
	ColumnNameList.append('eosino')
	NameList.append('Bone Marrow Basophil Percent')
	RegExList.append('lab_procedure_bone_marrow_basophil_result_percent_value.+>(.+)<')
	ColumnNameList.append('baso')
	NameList.append('Bone Marrow Lymphocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_lymphocyte_outcome_percent_value.+>(.+)<')
	ColumnNameList.append('lympho')
	NameList.append('Bone Marrow Monocyte Percent')
	RegExList.append('lab_procedure_monocyte_result_percent_value.+>(.+)<')
	ColumnNameList.append('mono')
	NameList.append('Bone Marrow Prolymphocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_prolymphocyte_result_percent_value.+>(.+)<')
	ColumnNameList.append('prolympho')
	NameList.append('Bone Marrow Promonocyte Percent')
	RegExList.append('lab_procedure_bone_marrow_promonocyte_count_result_percent_value.+>(.+)<')
	ColumnNameList.append('promono')
	NameList.append('Abnormal Lymphocyte Percent')
	RegExList.append('lab_procedure_abnormal_lymphocyte_result_percent_value.+>(.+)<')
	ColumnNameList.append('ablympho')
	NameList.append('PML-RAR')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(PML-RAR.+)<')
	ColumnNameList.append('PML_RAR')
	NameList.append('FLT3')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(FLT3.+)<')
	ColumnNameList.append('FLT3')
	NameList.append('IDH1 R132')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(IDH1 R132.+)<')
	ColumnNameList.append('IDH1_R132')
	NameList.append('IDH1 R140')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(IDH1 R140.+)<')
	ColumnNameList.append('IDH1_R140')
	NameList.append('IDH1 R172')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(IDH1 R172.+)<')
	ColumnNameList.append('IDH1_R172')
	NameList.append('Activating RAS')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(Activating RAS.+)<')
	ColumnNameList.append('RAS')
	NameList.append('NPMc')
	RegExList.append('molecular_analysis_abnormality_testing_result.+>(NPMc.+)<')
	ColumnNameList.append('NPMc')
	NameList.append('Risk Category')
	RegExList.append('acute_myeloid_leukemia_calgb_cytogenetics_risk_category.+>(.+)<')
	ColumnNameList.append('risk')
	NameList.append('Days To Death')
	RegExList.append('days_to_death.+>(.+)<')
	ColumnNameList.append('death')

	path = 'D:\Anaconda\Project Canse\Data\Clinical\XML'
	FileNames = os.listdir(path)
	DatArray = [[0]*(len(FileNames)-200) for xyz in range(len(NameList))]

	for i in range(200):#,len(FileNames)):
		b = open(path + '\\' + FileNames[i+200])
		c = b.readlines()
		for lines in c:
			for j in range(len(RegExList)):
				if re.search(RegExList[j],lines):
					g = re.findall(RegExList[j],lines)
					#print g[0],type(g[0])
					b = g[0]
					if re.search('egative',b):
						g[0]=0
					if re.search('ositive',b):
						g[0]=1
					if re.search('Intermediate/Normal',b):
						g[0]=1
					if re.search('Favorable',b):
						g[0]=0
					if re.search('Poor',b):
						g[0]=2
					DatArray[j][i] = g[0]
	return [DatArray, NameList, ColumnNameList]

def listChange(List,num,changeto):
	NewList = []
	for i in range(len(List)):
		if int(List[i])==num:
			NewList.append(changeto)
		elif int(List[i])>2000:
			NewList.append(int(List[i])-2000)
		else:
			NewList.append(int(List[i]))
	return NewList

def listClean(list1,remitem1,list2,remitem2):
	NewList1 = []
	NewList2 = []
	for i in range(len(list1)):
		if int(float(list1[i]))!=remitem1:
			if int(float(list2[i]))!=remitem2:
				NewList1.append(int(float(list1[i])))
				NewList2.append(int(float(list2[i])))
	return [NewList1,NewList2]


#print DatArray
NameList = []
RegExList = []


