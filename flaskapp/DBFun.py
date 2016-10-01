import numpy
from scipy import stats
from sklearn import linear_model
from Canse1funfun import listChange
from Canse1funfun import listClean
import psycopg2

def survRegress(columnNames):
	conn = psycopg2.connect("host=localhost dbname=postgres user=postgres port=5432 password=stinkypoo")
	cur = conn.cursor()
	cur.execute('SELECT death FROM cancer_data;')
	DeathArray = map(lambda x: int(x[0]), cur.fetchall())
	CleanArrayOfArrays = []
	for Name in columnNames:
		cur.execute('SELECT ' + Name + ' FROM cancer_data;')
		DataArray = map(lambda x: int(x[0]), cur.fetchall())
		Arrays = listClean(DataArray,999,DeathArray,0)
		CleanArray = Arrays[0]
		CleanDeathArray = Arrays[1]
		CleanArrayOfArrays.append(CleanArray)

	FinalArray = numpy.array([CleanArrayOfArrays])
	FinalArray = numpy.squeeze(FinalArray.transpose((2,1,0)))

	Indices = [index for index,value in enumerate(CleanDeathArray) if value > 1000]
	FinalArray = numpy.delete(FinalArray,Indices,axis=0)
	for i in reversed(range(len(Indices))):
		CleanDeathArray.pop(Indices[i])


	clf = linear_model.LinearRegression()
	print 'FinalArray',FinalArray
	clf.fit(FinalArray,numpy.array(CleanDeathArray))

	Coeffs = clf.coef_
	print Coeffs.shape
	print Coeffs
	ypred = clf.predict(FinalArray)
	return [CleanDeathArray,ypred]


#Arrays = survRegress(['year','age','ablympho','blast','mono'])
#print 'Deaths',Arrays[0]
#print 'Predictions',Arrays[1]
