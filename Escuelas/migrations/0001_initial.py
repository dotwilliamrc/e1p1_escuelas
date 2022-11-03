# Generated by Django 4.1.1 on 2022-11-03 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ambito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "ambito",
                "verbose_name_plural": "ambitos",
                "db_table": "Ambito",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Calle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "calle",
                "verbose_name_plural": "calles",
                "db_table": "Calle",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Control",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "control",
                "verbose_name_plural": "cotroles",
                "db_table": "Control",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Educativo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "educativo",
                "verbose_name_plural": "educativos",
                "db_table": "Educativo",
                "ordering": ["tipo_educativo"],
            },
        ),
        migrations.CreateModel(
            name="Entidad",
            fields=[
                ("clave", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "entidad",
                "verbose_name_plural": "entidades",
                "db_table": "Entidad",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Escuela",
            fields=[
                (
                    "clave",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                (
                    "educativo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.educativo",
                    ),
                ),
            ],
            options={
                "verbose_name": "escuela",
                "verbose_name_plural": "escuelas",
                "db_table": "Escuela",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Nivel_Educativo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "nivel educativo",
                "verbose_name_plural": "niveles educativos",
                "db_table": "Nivel_Educativo",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Periodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("inicio", models.IntegerField()),
                ("fin", models.IntegerField()),
            ],
            options={
                "verbose_name": "periodo",
                "verbose_name_plural": "periodos",
                "db_table": "Periodo",
                "ordering": ["inicio"],
            },
        ),
        migrations.CreateModel(
            name="Registro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "escuela",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.escuela",
                    ),
                ),
                (
                    "periodo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.periodo",
                    ),
                ),
            ],
            options={
                "verbose_name": "registro",
                "verbose_name_plural": "registros",
                "db_table": "Registro",
                "ordering": ["escuela"],
            },
        ),
        migrations.CreateModel(
            name="Servicio_Educativo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "servicio educativo",
                "verbose_name_plural": "servicios educativos",
                "db_table": "Servicio_Educativo",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Tipo_Educativo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "tipo educativo",
                "verbose_name_plural": "tipos educativos",
                "db_table": "Tipo_Educativo",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Turno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "turno",
                "verbose_name_plural": "turnos",
                "db_table": "Turno",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Alumnos",
            fields=[
                (
                    "registro",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.registro",
                    ),
                ),
                ("total", models.IntegerField()),
                ("hombres", models.IntegerField()),
                ("mujeres", models.IntegerField()),
            ],
            options={
                "verbose_name": "alumnos",
                "verbose_name_plural": "alumnos",
                "db_table": "Alumnos",
            },
        ),
        migrations.CreateModel(
            name="Computadoras",
            fields=[
                (
                    "registro",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.registro",
                    ),
                ),
                ("total", models.IntegerField()),
                ("internet", models.IntegerField()),
                ("uso_educativo", models.IntegerField()),
            ],
            options={
                "verbose_name": "computadoras",
                "verbose_name_plural": "computadoras",
                "db_table": "Computadoras",
            },
        ),
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "escuela",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.escuela",
                    ),
                ),
                ("lada", models.CharField(max_length=7, null=True)),
                ("telefono", models.CharField(max_length=10, null=True)),
                ("email", models.CharField(max_length=50, null=True)),
            ],
            options={
                "verbose_name": "contacto",
                "verbose_name_plural": "contactos",
                "db_table": "Contacto",
                "ordering": ["escuela"],
            },
        ),
        migrations.CreateModel(
            name="Docentes",
            fields=[
                (
                    "registro",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.registro",
                    ),
                ),
                ("total", models.IntegerField()),
                ("hombres", models.IntegerField()),
                ("mujeres", models.IntegerField()),
            ],
            options={
                "verbose_name": "docentes",
                "verbose_name_plural": "docentes",
                "db_table": "Docentes",
            },
        ),
        migrations.CreateModel(
            name="Grupos",
            fields=[
                (
                    "registro",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.registro",
                    ),
                ),
                ("total", models.IntegerField()),
                ("aulas_existentes", models.IntegerField()),
                ("aulas_uso", models.IntegerField()),
                ("laboratorios", models.IntegerField()),
                ("talleres", models.IntegerField()),
            ],
            options={
                "verbose_name": "grupos",
                "verbose_name_plural": "grupos",
                "db_table": "Grupos",
            },
        ),
        migrations.CreateModel(
            name="Personal",
            fields=[
                (
                    "registro",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.registro",
                    ),
                ),
                ("total", models.IntegerField()),
                ("hombres", models.IntegerField()),
                ("mujeres", models.IntegerField()),
            ],
            options={
                "verbose_name": "personal",
                "verbose_name_plural": "personal",
                "db_table": "Personal",
            },
        ),
        migrations.CreateModel(
            name="Ubicacion",
            fields=[
                (
                    "escuela",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.escuela",
                    ),
                ),
                ("altitud_msnm", models.IntegerField()),
                ("longitud", models.FloatField()),
                ("latitud", models.FloatField()),
                ("longitud_gms", models.CharField(max_length=20)),
                ("latitud_gms", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "grupos",
                "verbose_name_plural": "grupos",
                "db_table": "Ubicacion",
            },
        ),
        migrations.CreateModel(
            name="Municipio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clave", models.IntegerField()),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "entidad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.entidad",
                    ),
                ),
            ],
            options={
                "verbose_name": "municipio",
                "verbose_name_plural": "municipios",
                "db_table": "Municipio",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Localidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clave", models.IntegerField()),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "municipio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.municipio",
                    ),
                ),
            ],
            options={
                "verbose_name": "localidad",
                "verbose_name_plural": "localidades",
                "db_table": "Localidad",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ambito",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.ambito",
                    ),
                ),
                (
                    "control",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Escuelas.control",
                    ),
                ),
                (
                    "turno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Escuelas.turno"
                    ),
                ),
            ],
            options={
                "verbose_name": "general",
                "verbose_name_plural": "generales",
                "db_table": "General",
                "ordering": ["ambito"],
            },
        ),
        migrations.AddField(
            model_name="escuela",
            name="general",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Escuelas.general"
            ),
        ),
        migrations.AddField(
            model_name="escuela",
            name="localidad",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Escuelas.localidad"
            ),
        ),
        migrations.AddField(
            model_name="educativo",
            name="nivel_educativo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Escuelas.nivel_educativo",
            ),
        ),
        migrations.AddField(
            model_name="educativo",
            name="servicio_educativo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Escuelas.servicio_educativo",
            ),
        ),
        migrations.AddField(
            model_name="educativo",
            name="tipo_educativo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Escuelas.tipo_educativo",
            ),
        ),
        migrations.CreateModel(
            name="Direccion",
            fields=[
                (
                    "escuela",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="Escuelas.escuela",
                    ),
                ),
                (
                    "numero",
                    models.CharField(max_length=30, null=True, verbose_name="Numero"),
                ),
                (
                    "codigo_postal",
                    models.IntegerField(null=True, verbose_name="Codigo Postal"),
                ),
                (
                    "domicilio",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="direccion",
                        to="Escuelas.calle",
                    ),
                ),
                (
                    "posterior_calle",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calle_posterior",
                        to="Escuelas.calle",
                    ),
                ),
                (
                    "primera_calle",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entre_calle",
                        to="Escuelas.calle",
                    ),
                ),
                (
                    "segunda_calle",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="y_calle",
                        to="Escuelas.calle",
                    ),
                ),
            ],
            options={
                "verbose_name": "direccion",
                "verbose_name_plural": "direcciones",
                "db_table": "Direccion",
            },
        ),
    ]
