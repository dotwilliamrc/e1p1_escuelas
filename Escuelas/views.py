from django.shortcuts import redirect, render
from django.views.generic import View
import csv

from Escuelas.utilities.save import Save

from .models import *

# Create your views here.
class Home(View):
	def guardarExcel(self, row):
		saveFuncitons = Save()
		
		localidad = saveFuncitons.guardarLocacion({
			'CLAVE ENTIDAD': int(row['CLAVE ENTIDAD']),
			'CLAVE MUNICIPIO': int(row['CLAVE MUN./DEL.']),
			'CLAVE LOCALIDAD': int(row['CLAVE LOCALIDAD']),
			'ENTIDAD': row['ENTIDAD'],
			'MUNICIPIO': row['MUNICIPIO'],
			'LOCALIDAD': row['LOCALIDAD'],
		})

		educativo = saveFuncitons.guardarEducativo({
			'TIPO': row['TIPO EDUCATIVO'],
			'NIVEL': row['NIVEL EDUCATIVO'],
			'SERVICIO': row['SERVICIO EDUCATIVO'],
		})

		general = saveFuncitons.guardarGeneral({
			'TURNO': row['TURNO'],
			'AMBITO': row['AMBITO'],
			'CONTROL': row['CONTROL'],
		})

		escuela = saveFuncitons.guardarEscuela(
			localidad=localidad,
			educativo=educativo,
			general=general,
			data={
				'NOMBRE': row['CENTRO EDUCATIVO'],
				'CLAVE': row['CLAVE']
			}
		)

		saveFuncitons.guardarDireccion(
			escuela=escuela,
			data={
				'DOMICILIO': row['DOMICILIO'],
				'NUMERO': row['NUM. EXTERIOR'],
				'CALLE FIRST': row['ENTRE CALLE'],
				'CALLE SECOND': row['Y CALLE'],
				'CALLE POSTERIOR': row['CALLE POSTERIOR'],
				'CODIGO POSTAL': row['CÓDIGO POSTAL']
			}
		)

		saveFuncitons.guardarUbicacion(
		escuela=escuela,
			data={
				'ALTITUD_MSNM': int(row['ALTITUD (msnm)']),
				'LONGITUD': float(row['LONGITUD'].replace(',', '.')),
				'LATITUD': float(row['LATITUD'].replace(',', '.')),
				'LONGITUD_GMS': row['LONGITUD (gms)'],
				'LATITUD_GMS': row['LATITUD (gms)'],
			}
		)
		
		saveFuncitons.guardarContacto(
			escuela = escuela,
			data = {
				'LADA': row['LADA'],
				'TELEFONO': row['TELÉFONO'],
				'EMAIL': row['LADA']
			}
		)

		saveFuncitons.guardarRegistro(
			escuela=escuela,
			data={
				'PERIODO': row['PERIODO'],
				'PERSONAL': row['TOTAL DE PERSONAL'],
				'PERSONAL MUJERES': row['PERSONAL MUJERES'],
				'PERSONAL HOMBRES': row['PERSONAL HOMBRES'],
				'DOCENTES': row['TOTAL DE DOCENTES'],
				'DOCENTES MUJERES': row['DOCENTES MUJERES'],
				'DOCENTES HOMBRES': row['DOCENTES HOMBRES'],
				'ALUMNOS': row['TOTAL DE ALUMNOS'],
				'ALUMNOS MUJERES': row['ALUMNOS MUJERES'],
				'ALUMNOS HOMBRES': row['ALUMNOS HOMBRES'],
				'GRUPOS': row['TOTAL DE GRUPOS'],
				'AULAS EXISTENTES': row['AULAS EXISTENTES'],
				'AULAS EN USO': row['AULAS EN USO'],
				'LABORATORIOS': row['LABORATORIOS'],
				'TALLERES': row['TALLERES'],
				'COMPUTADORAS': row['COMPUTADORAS EN OPERACIÓN'],
				'COMPUTADORAS INTERNET': row['COMPUTADORAS EN OPERACIÓN + INTERNET'],
				'COMPUTADORAS USO EDUCATIVO': row['COMPUTADORAS EN OPERACIÓN USO EDUCATIVO']
			}
		)

	def post(self,request):
		file = request.FILES['datos']
		decoded_file = file.read().decode('utf-8').splitlines()
		reader = csv.DictReader(decoded_file)
		i = 1
		for row in reader:
			self.guardarExcel(row)
			print(i)
			i = i + 1

		return redirect(to=('Home'))
		
	def get(self, request):
		if 'option' in request.GET:
			if request.GET['option'] == "todo":
				return redirect(to=('Home'))
			elif request.GET['option'] == "escuela":
				alumnos = Alumnos.objects.select_related('registro').filter(registro__escuela__nombre__contains = request.GET['buscar'])
			elif request.GET['option'] == "alumnos":
				alumnos = Alumnos.objects.filter(total = int(request.GET['buscar']))
		
		else:
			alumnos = Alumnos.objects.all()

		return render(
			request = request,
			template_name = "Escuelas/home.html",
			context = {
				'alumnos': alumnos
			}
		)

def Detalles(request, id):
	registro = Registro.objects.get(id = id)
	escuela = registro.escuela

	personal = Personal.objects.get(registro = registro)
	docentes = Docentes.objects.get(registro = registro)
	alumnos = Alumnos.objects.get(registro = registro)
	grupos = Grupos.objects.get(registro = registro)
	computadoras = Computadoras.objects.get(registro = registro)
	
	localidad = escuela.localidad
	educativo = escuela.educativo
	general = escuela.general
	
	contacto = Contacto.objects.get(escuela = escuela)
	direccion = Direccion.objects.get(escuela = escuela)
	ubicacion = Ubicacion.objects.get(escuela = escuela)

	return render(
		request = request,
		template_name = "Escuelas/detalles.html",
		context={
			'registro': registro,
			'escuela': escuela,
			'personal': personal,
			'docentes': docentes,
			'alumnos': alumnos,
			'grupos': grupos,
			'computadoras': computadoras,
			'localidad': localidad,
			'educativo': educativo,
			'general': general,
			'contacto': contacto,
			'direccion': direccion,
			'ubicacion': ubicacion,
		}
	)
