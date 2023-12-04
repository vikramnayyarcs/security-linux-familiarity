import requests 

r = requests.get("http://10.0.0.5/PKHGDNHMXH.php?solution='PKHGDNHMXH.php?solution='DoB,ZIP code,Gender,Disease\n02/08/1960,12153,F,Stroke\n23/08/1970,12153,M,High Cholesterol \n04/09/1970,12152,M,Hepatitis \n05/09/1970,12155,M,Pneumonia \n05/09/1960,12145,M,Flu\n12/09/1970,12148,F,Eczema \n10/08/1960,12140,F,Stroke\n05/08/1970,12142,F,Erythema \n10/09/1960,12158,F,Angina Pectoris \n20/09/1970,12143,F,Cardiomyopathy \n12/09/1960,12159,F,Cardiomyopathy\n17/08/1960,12154,F,Stroke\n30/08/1970,12156,M,Angina Pectoris \n02/09/1960,12147,F,Hepatitis\n07/08/1970,12141,F,High Cholesterol \n20/08/1960,12141,F,Stroke'")

print(r.text)