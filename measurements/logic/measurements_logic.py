import datetime
from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all() 
    return measurements

def get_measurement(mer_pk):
    measurement = Measurement.objects.get(pk=mer_pk)
    return measurement

def update_measurement(mer_pk, new_mer):
    measurement = Measurement.objects.get(pk=mer_pk)
    variable = Measurement.objects.get(pk=new_mer["variable"])
    measurement.variable = variable
    measurement.value = new_mer["value"]
    measurement.unit = new_mer["unit"]
    measurement.place = new_mer["place"]
    # date_time = datetime.strptime(new_mer["datTime"], '%Y-%m-%dT%H:%M:%S.%f%z')
    # measurement.dateTime = date_time
    measurement.save()
    return measurement

def create_measurement(mer):
    variable = Variable.objetcs.get(pk=mer["variable"])
    measurement = Measurement(variable=variable, 
                              value=mer["value"], 
                              unit=mer["unit"], 
                              place=mer["place"])
                            #   dateTime=mer["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(mer_pk):
    measurement = get_measurement(mer_pk)
    measurement.delete
    measurement.save()
    return measurement
    