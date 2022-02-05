import json
from random import randint
from . enums import CountryCode, Gender

_data_folder = __file__ + "/../data/"

_mail_domains = json.load(open(_data_folder + "mail_domains.json"))
_passchars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*_.,!?&%$=()[]}{\/")

class Person:
	def __init__(self, firstname, lastname, mailaddress, password, street, hsnr, plz, city):
		self.firstname = firstname
		self.lastname = lastname
		self.mailaddress = mailaddress
		self.password = password
		self.street = street
		self.hsnr = hsnr
		self.plz = plz
		self.city = city
	
	def __str__(self):
		return self.getFullName()

	def getFullName(self):
		return self.firstname + " " + self.lastname

	def getFullAddress(self):
		return self.street + " " + self.hsnr + ", " + self.plz + " " + self.city


def randomPerson(countrycode: CountryCode = CountryCode.US, gender: Gender = Gender.RANDOM):
	if gender == Gender.RANDOM:
		_first_names_m = json.load(open(_data_folder + "first_names_" + countrycode.value + "_m.json", encoding="UTF-8"))
		_first_names_f = json.load(open(_data_folder + "first_names_" + countrycode.value + "_f.json", encoding="UTF-8"))
		_first_names = _first_names_f + _first_names_m
	elif gender == Gender.MALE:
		_first_names = json.load(open(_data_folder + "first_names_" + countrycode.value + "_m.json", encoding="UTF-8"))
	elif gender == Gender.FEMALE:
		_first_names = json.load(open(_data_folder + "first_names_" + countrycode.value + "_f.json", encoding="UTF-8"))
	
	_last_names = json.load(open(_data_folder + "last_names_" + countrycode.value + ".json", encoding="UTF-8"))
	_street_names = json.load(open(_data_folder + "street_names_" + countrycode.value + ".json", encoding="UTF-8"))
	_city_names = json.load(open(_data_folder + "city_names_" + countrycode.value + ".json", encoding="UTF-8"))

	firstname = _first_names[randint(0, len(_first_names) - 1)]
	lastname = _last_names[randint(0, len(_last_names) - 1)]
	maildomain = _mail_domains[randint(0, len(_mail_domains) - 1)]
	password = ""
	street = _street_names[randint(0, len(_street_names) - 1)]
	hsnr = str(randint(1,512))
	plz = str(randint(10000, 99999))
	city = _city_names[randint(0, len(_city_names) - 1)]

	for p in range(randint(5,12)):
		password += _passchars[randint(0,len(_passchars) - 1)]
	
	return Person(firstname, lastname, firstname+"."+lastname+"@"+maildomain, password, street, hsnr, plz, city)