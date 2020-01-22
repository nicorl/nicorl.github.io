# Usage
# python number_of_days_to_date.py -d number_of_days
import argparse
from datetime import datetime, date, time, timedelta


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dias",
	help="numero de dias para convertir")
args = vars(ap.parse_args())
dias = int(args["dias"])

años = dias // 365
meses = int( (dias / 365 - dias // 365)*12 // 1 )
diasenmes = int( ((dias / 365 - dias // 365)*12 / 1 - (dias / 365 - dias // 365)*12 // 1)*30 // 1 )

print('{} días son: {} años, {} meses, {} días'.format(dias, años, meses, diasenmes, ))

fecha_origen = date.today() - timedelta(days=dias)
print('Todo esto empezó el {}'.format(fecha_origen))