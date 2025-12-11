import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Alinear cadenas

titulo = 'Sitio Web de GlobalMentoring.com.mx'

# center - Centrar un str
print(titulo.center(len(titulo)+10,'-'))

# ljust - Alinear a la izquierda
print(titulo.ljust(len(titulo)+10,'-'))

# rjust - Alinear a la derecha
print(titulo.rjust(len(titulo)+10,'-'))

# Remplazar contenido en un str
print(contenido.replace(' ','-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:', titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:', titulo, len(titulo))
titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print('Cadena modificada:', titulo, len(titulo))