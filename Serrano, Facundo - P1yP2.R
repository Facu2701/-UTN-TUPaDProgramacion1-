# ------------------------------------------------
#             Tabla de Frecuencias
# ------------------------------------------------

#Cargamos la libreria de excel
if(!require(readxl)) install.packages("readxl")
library(readxl)

#Luego localizamos el archivo excel desde el equipo
archivo <- file.choose()
datos <- read_excel(archivo)

#
#------ VARIABLE CONTINUA: "Tiempo en horas semanales dedicadas al estudio"
#

#Variable a analizar
variable_continua = "TIEMPO_SEMANAL_ESTUDIO_HS"


#Numeros de intervalos por regla de Sturges con intervalos enteros
k <- ceiling(1 + 3.322 * log10(nrow(datos))) 
min_val <- floor(min(datos[[variable_continua]], na.rm = TRUE))   #valor minimo. Con floor truncamos el numero
max_val <- ceiling(max(datos[[variable_continua]], na.rm = TRUE)) #Valor maximo. Con ceiling redondeamos hacia arriba
amplitud <- ceiling((max_val - min_val)/k)                        #Amplitud para cada clase
max_tope <- min_val + amplitud *k                                 #Limite superior ajustado
cortes <- seq(min_val, max_tope, by = amplitud)                   #Secuencia de corte

#Crear columnas con intervalos
datos$clases <- cut(datos[[variable_continua]], breaks = cortes,
                    right = FALSE, include.lowest = TRUE)

#Marca de clase
marca_clase <- (head(cortes, -1) + tail(cortes, -1)) /2 #marca de clase de cada intervalo
#head y tail se usan para tomar los extremos de cada par consecutivo


#Tabla de frecuencias
tabla_clases <- table(datos$clases)
f_acum <- cumsum(tabla_clases) #Frecuencia acumulada
f_rel <- prop.table(tabla_clases) #Frecuencia relativa
f_rel_acum <- cumsum(f_rel) #Frecuencia relativa acumulada

#Mostrar tabla de frecuencias
tabla_frecuencias <- data.frame(
  Intervalo = names(tabla_clases),
  Marca = as.vector(marca_clase),
  Frec_abs = as.vector(tabla_clases),
  Frec_Acum = as.vector(f_acum),
  Frec_Rel = round(as.vector(f_rel),4),
  Frec_Rel_Acum = round(as.vector(f_rel_acum),4)
)

message("\n Tabla de Frecuencias - VARIABLE CONTINUA (", variable_continua,")")
print(tabla_frecuencias, row.names = FALSE)


#-------- VARIABLE CUALITATIVA: "Nivel de Satisfaccion" ----------

#Cuento cuantos niveles de satisfaccion hay
tabla_satisfaccion <- table(datos$SATISF_CON_CARRERA)

#Calculo cada frecuencia de la tabla
f_acum2 <- cumsum(tabla_satisfaccion) 
f_rel2 <- prop.table(tabla_satisfaccion)
f_rel_acum2 <- cumsum(f_rel2)

tabla_frecuencias2 <- data.frame(
  Nivel_de_satisfaccion = names(tabla_satisfaccion),
  Frec_abs = as.vector(tabla_satisfaccion),
  Frec_Acum = as.vector(f_acum2),
  Frec_Rel = round(as.vector(f_rel2),4),
  Frec_Rel_Acum = round(as.vector(f_rel_acum2),4)
)
message("\n Tabla de Frecuencias - VARIABLE CUALITATIVA (NIVEL DE SATISFACCION)")
print(tabla_frecuencias2, row.names = FALSE)
"1" = "Muy satisfecho"
"2" = "Satisfecho"
"3" = "Insatisfecho"
"4" = "Muy insatisfecho"