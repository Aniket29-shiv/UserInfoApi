from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic.base import View
from .serializers import InputTableserializer
from .models import InputTable
from User.models import UserInformation
import re
import json

def finger_print(teststr):
	teststr = teststr.split(" ")
	res = ""
	for i in teststr:
		if re.search("utm", i):
			res = i
	res = res.split("&")
	newdict = {}
	for i in res:
		key, value = i.split("=")
		value = value.replace(',', '')
		newdict[key] = value
	return newdict




class stri:
	def __init__(self,requestId,visitorId,confidenceScore,errorMessage):
		self.requestId=requestId
		self.visitorId=visitorId
		self.confidenceScore=confidenceScore['score']
		self.errorMessage=errorMessage
	
	@classmethod
	def from_json(cls,json_string):
		json_dict=json.loads(json_string)
		return cls(**json_dict)

	def name(self):
		li=[]
		li.append(self.requestId)
		li.append(self.visitorId)
		return li




# Create your views here.
@api_view(['POST','GET'])
def User_info_create(request):
	if request.method=='POST':
		InputTableserializerobj=InputTableserializer(data=request.data)
		if InputTableserializerobj.is_valid():
			InputTableserializerobj.save()
			InputTableObj=InputTable.objects.get(id=InputTableserializerobj.data["id"])
			newdict=finger_print(InputTableObj.Input_str1)
			newlist=stri.from_json(InputTableObj.Input_str2)
			UserInformation_n = UserInformation(utm_source=newdict["utm_source"],utm_medium=newdict["utm_medium"],requestId=newlist.name()[0],visitorId=newlist.name()[1])
			UserInformation_n.save()
		return Response(InputTableserializerobj.data)
	else:
		InputTableObj=InputTable.objects.all()
		InputTableObjserializer=InputTableserializer(InputTableObj,many=True)
		return Response(InputTableObjserializer.data)
