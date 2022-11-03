from django.db import models

# Create your models here.

# Locacion
class Entidad(models.Model):
	clave = models.BigAutoField(primary_key=True)
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="entidad"
		verbose_name_plural="entidades"
		db_table="Entidad"
		ordering=["nombre"]

class Municipio(models.Model):
	clave = models.IntegerField()
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
	entidad = models.ForeignKey(to=Entidad, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="municipio"
		verbose_name_plural="municipios"
		db_table="Municipio"
		ordering=["nombre"]

class Localidad(models.Model):
	clave = models.IntegerField()
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
	municipio = models.ForeignKey(to=Municipio, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="localidad"
		verbose_name_plural="localidades"
		db_table="Localidad"
		ordering=["nombre"]

# Educativo
class Tipo_Educativo(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="tipo educativo"
		verbose_name_plural="tipos educativos"
		db_table="Tipo_Educativo"
		ordering=["nombre"]

class Nivel_Educativo(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="nivel educativo"
		verbose_name_plural="niveles educativos"
		db_table="Nivel_Educativo"
		ordering=["nombre"]

class Servicio_Educativo(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="servicio educativo"
		verbose_name_plural="servicios educativos"
		db_table="Servicio_Educativo"
		ordering=["nombre"]

class Educativo(models.Model):
	tipo_educativo = models.ForeignKey(to=Tipo_Educativo, on_delete=models.CASCADE)
	nivel_educativo = models.ForeignKey(to=Nivel_Educativo, on_delete=models.CASCADE)
	servicio_educativo = models.ForeignKey(to=Servicio_Educativo, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.tipo_educativo} - {self.nivel_educativo} - {self.servicio_educativo}"

	class Meta:
		verbose_name="educativo"
		verbose_name_plural="educativos"
		db_table="Educativo"
		ordering=["tipo_educativo"]

#General

class Ambito(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="ambito"
		verbose_name_plural="ambitos"
		db_table="Ambito"
		ordering=["nombre"]

class Turno(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="turno"
		verbose_name_plural="turnos"
		db_table="Turno"
		ordering=["nombre"]

class Control(models.Model):
	nombre = models.CharField(max_length = 50, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="control"
		verbose_name_plural="cotroles"
		db_table="Control"
		ordering=["nombre"]

class General(models.Model):
	ambito = models.ForeignKey(to=Ambito, on_delete=models.CASCADE)
	turno = models.ForeignKey(to=Turno, on_delete=models.CASCADE)
	control = models.ForeignKey(to=Control, on_delete=models.CASCADE)

#!!!!Nota
	def __str__(self):
		return f"{self.ambito} - {self.turno} - { self.control }"

	class Meta:
		verbose_name="general"
		verbose_name_plural="generales"
		db_table="General"
		ordering=["ambito"]

# Escuela
class Escuela(models.Model):
	clave = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length = 100, verbose_name = "Nombre")
	localidad = models.ForeignKey(to=Localidad, on_delete=models.CASCADE)
	educativo = models.ForeignKey(to=Educativo, on_delete=models.CASCADE)
	general = models.ForeignKey(to=General, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name="escuela"
		verbose_name_plural="escuelas"
		db_table="Escuela"
		ordering=["nombre"]

class Ubicacion(models.Model):
	escuela = models.OneToOneField(to = Escuela , on_delete = models.CASCADE, primary_key = True)
	altitud_msnm = models.IntegerField()
	longitud = models.FloatField()
	latitud = models.FloatField()
	longitud_gms = models.CharField(max_length = 20)
	latitud_gms = models.CharField(max_length = 20)

	def __str__(self):
		return f"{self.altitud_msnm} - {self.longitud} - {self.latitud}"

	class Meta:
		verbose_name="grupos"
		verbose_name_plural="grupos"
		db_table="Ubicacion"


# Direccion
class Calle(models.Model):
	nombre = models.CharField(max_length = 100, verbose_name = "Nombre")

	def __str__(self):
		return self.nombre()

	class Meta:
		verbose_name="calle"
		verbose_name_plural="calles"
		db_table="Calle"
		ordering=["nombre"]

#!!!Nota
class Direccion(models.Model):
	escuela = models.OneToOneField(to = Escuela, on_delete = models.CASCADE, primary_key = True)
	domicilio = models.ForeignKey(to = Calle, on_delete = models.CASCADE, related_name = "direccion", null=True)
	primera_calle = models.ForeignKey(to = Calle, on_delete = models.CASCADE, null=True, related_name = "entre_calle")
	segunda_calle = models.ForeignKey(to = Calle, on_delete = models.CASCADE, null=True, related_name = "y_calle")
	posterior_calle = models.ForeignKey(to = Calle, on_delete = models.CASCADE, null=True, related_name = "calle_posterior")
	numero = models.CharField(max_length = 30, verbose_name="Numero", null=True)
	codigo_postal = models.IntegerField(verbose_name="Codigo Postal", null=True)

	def __str__(self):
		return f"{self.domicilio()}"

	class Meta:
		verbose_name="direccion"
		verbose_name_plural="direcciones"
		db_table="Direccion"

# Contacto
class Contacto(models.Model):
	escuela = models.OneToOneField(to = Escuela, on_delete = models.CASCADE, primary_key = True)
	lada = models.CharField(max_length = 7, null = True)
	telefono = models.CharField(max_length = 10, null = True)
	email = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.lada()

	class Meta:
		verbose_name="contacto"
		verbose_name_plural="contactos"
		db_table="Contacto"
		ordering=["escuela"]


# Registro
class Periodo(models.Model):
	inicio = models.IntegerField()
	fin = models.IntegerField()

	def __str__(self):
		return f"{self.inicio} - {self.fin}"

	class Meta:
		verbose_name="periodo"
		verbose_name_plural="periodos"
		db_table="Periodo"
		ordering=["inicio"]

class Registro(models.Model):
	escuela = models.ForeignKey(to = Escuela, on_delete = models.CASCADE)
	periodo = models.ForeignKey(to = Periodo, on_delete = models.CASCADE)

	def __str__(self):
		return f"{self.escuela} {self.periodo}"

	class Meta:
		verbose_name="registro"
		verbose_name_plural="registros"
		db_table="Registro"
		ordering=["escuela"]

class Personal(models.Model):
	registro = models.OneToOneField(to = Registro , on_delete = models.CASCADE, primary_key = True)
	total = models.IntegerField()
	hombres = models.IntegerField()
	mujeres = models.IntegerField()

	def __str__(self):
		return f"{self.registro}"

	class Meta:
		verbose_name="personal"
		verbose_name_plural="personal"
		db_table="Personal"

class Docentes(models.Model):
	registro = models.OneToOneField(to = Registro , on_delete = models.CASCADE, primary_key = True)
	total = models.IntegerField()
	hombres = models.IntegerField()
	mujeres = models.IntegerField()

	def __str__(self):
		return f"{self.registro}"

	class Meta:
		verbose_name="docentes"
		verbose_name_plural="docentes"
		db_table="Docentes"

class Alumnos(models.Model):
	registro = models.OneToOneField(to = Registro , on_delete = models.CASCADE, primary_key = True)
	total = models.IntegerField()
	hombres = models.IntegerField()
	mujeres = models.IntegerField()

	def __str__(self):
		return f"{self.registro}"

	class Meta:
		verbose_name="alumnos"
		verbose_name_plural="alumnos"
		db_table="Alumnos"

class Grupos(models.Model):
	registro = models.OneToOneField(to = Registro , on_delete = models.CASCADE, primary_key = True)
	total = models.IntegerField()
	aulas_existentes = models.IntegerField()
	aulas_uso = models.IntegerField()
	laboratorios = models.IntegerField()
	talleres = models.IntegerField()

	def __str__(self):
		return f"{self.registro}"

	class Meta:
		verbose_name="grupos"
		verbose_name_plural="grupos"
		db_table="Grupos"

class Computadoras(models.Model):
	registro = models.OneToOneField(to = Registro , on_delete = models.CASCADE, primary_key = True)
	total = models.IntegerField()
	internet = models.IntegerField()
	uso_educativo = models.IntegerField()

	def __str__(self):
		return f"{self.registro}"

	class Meta:
		verbose_name="computadoras"
		verbose_name_plural="computadoras"
		db_table="Computadoras"
