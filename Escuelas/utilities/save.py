from ..models import *

class Save:
	def guardarLocacion(self, data):
		try:
			entidad = Entidad.objects.get(nombre=data['ENTIDAD'])
		except Entidad.DoesNotExist:
			entidad = Entidad(
			clave = data['CLAVE ENTIDAD'],
			nombre = data['ENTIDAD'],
			)
			entidad.save()

		try:
			municipio = Municipio.objects.get(nombre=data['MUNICIPIO'], entidad=entidad)
		except Municipio.DoesNotExist:
			municipio = Municipio(
			entidad = entidad,
			clave = data['CLAVE MUNICIPIO'],
			nombre = data['MUNICIPIO'],
			)
			municipio.save()
		
		try:
			localidad = Localidad.objects.get(nombre=data['LOCALIDAD'], municipio=municipio)
		except Localidad.DoesNotExist:
			localidad = Localidad(
			municipio = municipio,
			clave = data['CLAVE LOCALIDAD'],
			nombre = data['LOCALIDAD'],
			)
			localidad.save()

		return localidad

	def guardarEducativo(self, data):
		try:
			tipo = Tipo_Educativo.objects.get(nombre = data['TIPO'])
		except Tipo_Educativo.DoesNotExist:
			tipo = Tipo_Educativo(
				nombre = data['TIPO']
			)
			tipo.save()

		try:
			nivel = Nivel_Educativo.objects.get(nombre = data['NIVEL'])
		except Nivel_Educativo.DoesNotExist:
			nivel = Nivel_Educativo(
				nombre = data['NIVEL']
			)
			nivel.save()

		try:
			servicio = Servicio_Educativo.objects.get(nombre = data['SERVICIO'])
		except Servicio_Educativo.DoesNotExist:
			servicio = Servicio_Educativo(
				nombre = data['SERVICIO']
			)
			servicio.save()

		try:
			educativo = Educativo.objects.get(tipo_educativo = tipo, nivel_educativo = nivel, servicio_educativo = servicio)
		except Educativo.DoesNotExist:
			educativo = Educativo(
				tipo_educativo = tipo,
				nivel_educativo = nivel,
				servicio_educativo = servicio
			)
			educativo.save()

		return educativo

	def guardarGeneral(self, data):
		try:
			turno = Turno.objects.get(nombre = data['TURNO'])
		except Turno.DoesNotExist:
			turno = Turno(
				nombre = data['TURNO']
			)
			turno.save()

		try:
			ambito = Ambito.objects.get(nombre = data['AMBITO'])
		except Ambito.DoesNotExist:
			ambito = Ambito(
				nombre = data['AMBITO']
			)
			ambito.save()

		try:
			control = Control.objects.get(nombre = data['CONTROL'])
		except Control.DoesNotExist:
			control = Control(
				nombre = data['CONTROL']
			)
			control.save()
		
		try:
			general = General.objects.get(turno = turno, ambito = ambito, control = control)
		except General.DoesNotExist:
			general = General(
				turno = turno,
				ambito = ambito,
				control = control
			)
			general.save()

		return general

	def guardarEscuela(self, data, localidad, educativo, general):
		escuela = Escuela(
			clave = data['CLAVE'],
			nombre = data['NOMBRE'],
			localidad = localidad,
			educativo = educativo,
			general = general
		)
		escuela.save()

		return escuela

	def guardarDireccion(self, data, escuela):
		direccion = Direccion(escuela = escuela)

		if data['NUMERO'] != "":
			direccion.numero = data['NUMERO']

		if data['CODIGO POSTAL'] != "":
			direccion.codigo_postal = data['CODIGO POSTAL']

		if data['DOMICILIO'] != "":
			try:
				calle_domicilio = Calle.objects.get(nombre = data['DOMICILIO'])
			except Calle.DoesNotExist:
				calle_domicilio = Calle(nombre = data['DOMICILIO'])
				calle_domicilio.save()
			direccion.domicilio = calle_domicilio

		if data['CALLE FIRST'] != "":
			try:
				calle_first = Calle.objects.get(nombre = data['CALLE FIRST'])
			except Calle.DoesNotExist:
				calle_first = Calle(nombre = data['CALLE FIRST'])
				calle_first.save()
			direccion.primera_calle = calle_first

		if data['CALLE SECOND'] != "":
			try:
				calle_second = Calle.objects.get(nombre = data['CALLE SECOND'])
			except Calle.DoesNotExist:
				calle_second = Calle(nombre = data['CALLE SECOND'])
				calle_second.save()
			direccion.primera_calle = calle_second

		if data['CALLE POSTERIOR'] != "":
			try:
				calle_posterior = Calle.objects.get(nombre = data['CALLE POSTERIOR'])
			except Calle.DoesNotExist:
				calle_posterior = Calle(nombre = data['CALLE POSTERIOR'])
				calle_posterior.save()
			direccion.posterior_calle = calle_posterior

		direccion.save()

	def guardarUbicacion(self, data, escuela):
		ubicacion = Ubicacion(
			escuela = escuela,
			altitud_msnm = data['ALTITUD_MSNM'],
			longitud = data['LONGITUD'],
			latitud = data['LATITUD'],
			longitud_gms = data['LONGITUD_GMS'],
			latitud_gms = data['LATITUD_GMS']
		)
		ubicacion.save()

	def guardarContacto(self, data, escuela):
		contacto = Contacto(escuela = escuela)

		if data['LADA'] != "":
			contacto.lada = data['LADA']

		if data['TELEFONO'] != "":
			contacto.telefono = data['TELEFONO']

		if data['EMAIL'] != "":
			contacto.email = data['EMAIL']

		contacto.save()

	def guardarPeriodo(self, periodo):
		years = periodo.split('-')
		try:
			periodo = Periodo.objects.get(inicio = int(years[0]), fin = int(years[1]))
		except Periodo.DoesNotExist:
			periodo = Periodo(
				inicio = int(years[0]),
				fin = int(years[1])
			)

			periodo.save()

		return periodo

	def guardarReg(self, escuela, periodo):
		try:
			registro = Registro.objects.get(escuela = escuela, periodo = periodo)
		except Registro.DoesNotExist:
			registro = Registro(escuela = escuela, periodo = periodo)
			registro.save()

		return registro

	def guardarPersonal(self, registro, data):
		personal = Personal(
			registro = registro,
			total = int(data['PERSONAL']),
			hombres = int(data['PERSONAL HOMBRES']),
			mujeres = int(data['PERSONAL MUJERES'])
		)

		personal.save()

	def guardarDocentes(self, registro, data):
		docentes = Docentes(
			registro = registro,
			total = int(data['DOCENTES']),
			hombres = int(data['DOCENTES HOMBRES']),
			mujeres = int(data['DOCENTES MUJERES'])
		)

		docentes.save()

	def guardarAlumnos(self, registro, data):
		alumnos = Alumnos(
			registro = registro,
			total = int(data['ALUMNOS']),
			hombres = int(data['ALUMNOS HOMBRES']),
			mujeres = int(data['ALUMNOS MUJERES'])
		)

		alumnos.save()

	def guardarGrupos(self, registro, data):
		grupos = Grupos(
			registro = registro,
			total = int(data['GRUPOS']),
			aulas_existentes = int(data['AULAS EXISTENTES']),
			aulas_uso = int(data['AULAS EN USO']),
			laboratorios = int(data['LABORATORIOS']),
			talleres = int(data['TALLERES'])
		)

		grupos.save()

	def guardarComputadoras(self, registro, data):
		computadoras = Computadoras(
			registro = registro,
			total = int(data['COMPUTADORAS']),
			internet = int(data['COMPUTADORAS INTERNET']),
			uso_educativo = int(data['COMPUTADORAS USO EDUCATIVO'])
		)

		computadoras.save()

	def guardarRegistro(self, data, escuela):
		periodo = self.guardarPeriodo(data['PERIODO'])
		
		registro = self.guardarReg(escuela = escuela, periodo = periodo)


		self.guardarPersonal(
			registro = registro,
			data = {
				'PERSONAL': data['PERSONAL'],
				'PERSONAL MUJERES': data['PERSONAL MUJERES'],
				'PERSONAL HOMBRES': data['PERSONAL HOMBRES'],
			}
		)

		self.guardarDocentes(
			registro = registro,
			data = {
				'DOCENTES': data['DOCENTES'],
				'DOCENTES MUJERES': data['DOCENTES MUJERES'],
				'DOCENTES HOMBRES': data['DOCENTES HOMBRES'],
			}
		)
		

		self.guardarAlumnos(
			registro = registro,
			data = {
				'ALUMNOS': data['ALUMNOS'],
				'ALUMNOS MUJERES': data['ALUMNOS MUJERES'],
				'ALUMNOS HOMBRES': data['ALUMNOS HOMBRES'],
			}
		)

		self.guardarGrupos(
			registro = registro,
			data = {
				'GRUPOS': data['GRUPOS'],
				'AULAS EXISTENTES': data['AULAS EXISTENTES'],
				'AULAS EN USO': data['AULAS EN USO'],
				'LABORATORIOS': data['LABORATORIOS'],
				'TALLERES': data['TALLERES']
			}
		)

		self.guardarComputadoras(
			registro = registro,
			data = {
				'COMPUTADORAS': data['COMPUTADORAS'],
				'COMPUTADORAS INTERNET': data['COMPUTADORAS INTERNET'],
				'COMPUTADORAS USO EDUCATIVO': data['COMPUTADORAS USO EDUCATIVO'],
			}
		)
