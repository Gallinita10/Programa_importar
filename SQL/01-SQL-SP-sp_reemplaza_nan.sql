CREATE PROCEDURE dbo.sp_reemplaza_nan AS
BEGIN
UPDATE fichas SET
		DNI = CASE WHEN DNI = 'nan' THEN '' ELSE DNI END,
		Nombre_Alumno = CASE WHEN Nombre_Alumno = 'nan' THEN '' ELSE Nombre_Alumno END,
		Domicilio = CASE WHEN Domicilio = 'nan' THEN '' ELSE Domicilio END,
		Celular = CASE WHEN Celular = 'nan' THEN '' ELSE Celular END,
		Mail = CASE WHEN Mail = 'nan' THEN '' ELSE Mail END,
		Fecha_de_Nacimiento = CASE WHEN Fecha_de_Nacimiento = 'nan' THEN '' ELSE Fecha_de_Nacimiento END,
		Ciudad_de_Residencia = CASE WHEN Ciudad_de_Residencia = 'nan' THEN '' ELSE Ciudad_de_Residencia END,
		Provincia_de_Residencia = CASE WHEN Provincia_de_Residencia = 'nan' THEN '' ELSE Provincia_de_Residencia END,
		Pais_de_Residencia = CASE WHEN Pais_de_Residencia = 'nan' THEN '' ELSE Pais_de_Residencia END,
		Ciudad_de_Nacimiento = CASE WHEN Ciudad_de_Nacimiento = 'nan' THEN '' ELSE Ciudad_de_Nacimiento END,
		Provincia_de_Nacimiento = CASE WHEN Provincia_de_Nacimiento = 'nan' THEN '' ELSE Provincia_de_Nacimiento END,
		Pais_de_Nacimiento = CASE WHEN Pais_de_Nacimiento = 'nan' THEN '' ELSE Pais_de_Nacimiento END,
		Estado_Civil = CASE WHEN Estado_Civil = 'nan' THEN '' ELSE Estado_Civil END,
		Trabaja = CASE WHEN Trabaja = 'nan' THEN '' ELSE Trabaja END,
		Obra_Social = CASE WHEN Obra_Social = 'nan' THEN '' ELSE Obra_Social END,
		Nombre_Obra_Social = CASE WHEN Nombre_Obra_Social = 'nan' THEN '' ELSE Nombre_Alumno END

END
GO