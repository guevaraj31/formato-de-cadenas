#!/usr/python
## Normaliza el nombre de 
## las imagenes

image_name = str(raw_input('Ingrese el nombre de su imagen: '))
image_name = image_name.lower()

# valida los caracteres invalidos para el nombre
image_name            = image_name.replace('\'','').replace(',','-').replace('_','-').replace('\"','')
image_name            = image_name.replace(' ','-').replace('&','').replace('%','').replace('#','-')
image_name            = image_name.replace('(','-').replace(')','-')   

print 'EL nuevo nombre es: {}'.format(image_name)

