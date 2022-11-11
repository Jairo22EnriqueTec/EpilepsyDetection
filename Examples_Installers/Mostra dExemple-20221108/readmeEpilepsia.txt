DATOS epilepsia MIT

Introduccion:

Los datos RAW de epilepsia del MIT originalmente tienen:
* 24 pacientes
* Por cada paciente un directorio con una serie de ficheros con grabaciones consecutivas, de 23 canales y el tiempo inicial y final, pero por razones 
de proteccion de datos no se sabe la fecha
* Los canales no son del sensor propiamente dicho sino de la diferencia entre dos sensores consecutivos conectados segun se especifica en la figura 3 
de DataDescription.pdf

Estos datos se han procesado para poner:
1. Todos los datos de un paciente en un solo fichero en directorio raw
2. Se ha generado un fichero excel con la informacion de estos datos que esta en directorio annot: df_annotation_full.xlsx

Este fichero tiene las siguientes columnas para cada  .edf file:
1. type: indica si el fichero .edf contiene un ataque: normal, si no hay ningún ataque, seizure, si hay alguno 
2. PatID: patient identifier
3. filename: .edf filename que identifica la grabación 
4.seizure_id: number that identifies the attack in the edf file, 0 if there is no attack, and the attack order in case there is more than one (e.g. if there are several consecutive attacks in the file it would be a 1 for the first a 2 for the second and so on).
5. seizure_start: time ( seconds) the attack begins in the .edf recording
6. seizure_end: : time ( seconds) the attack ends in the .edf recording
7. rec_duration: duration of the .edf recording (seconds)
8. seizure_duration: duration (seconds) of each attack

