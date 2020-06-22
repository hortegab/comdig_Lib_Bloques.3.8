# INTRODUCCION

comdig_Lib_Bloques.3.8 es una libreria de bloques jerarquicos para GNU Radio. Ha sido adaptada  y probada en la versión 3.8.1 de GNU Radio y con Python 3.8

# PRERREQUISITOS
- debe estar instalado GNURadio 3.8.1 o superior
- debe estar instalada el OOT E3TRadio3.8 ya que muchos de los bloques de este paquete reusan bloques de ese OOT

Si esos requisitos no se cumplen, sigue las instrucciones que señala el Readme del OOT E3TRadio3.8 en este enlace: https://github.com/hortegab/comdig_Lib_OOT_E3TRadio.3.8.git

# LA INSTALACION
- No hay que hacer una instalación por terminal de comandos
- Simplemente, abra GRC de GNURadio e instale bloque por bloque siguiendo este proceso:
  -- busca y abre el flujograma del bloque, lo corres. Eso es todo

# LA COMPROBACION
- Actualiza librerias del GRC: oprime el ícono de la fecha circular de actualización "Reload Blocks"
- En el panel derecho del GRC revisa que existe la categoría "comdiguis".  Si esta categoría no aparece a primera vista, revise dentro de la categoría “(no module specified)”

## Algunos consejos o notas:
- Es posible que un bloque no se pueda instalar debido a que consume un bloque que ya ha sido instalado pero que aún GNU Radio no lo reconoce porque la instalación fue muy reciente. En ese caso debes oprimir el ícono de la fecha circular de actualización "Reload Blocks"
- Es posible que un bloque no se pueda instalar debido a que consume un bloque que ya aún no ha sido instalado. En ese caso debes dejarlo para cuando ya tengas instalado esos los bloques.
- Note que los bloques de esta librería tienen un nombre que comienza por “_b”, pero si el bloque es tipo QT GUI, este comienza con “QT GUI_b”. Esto puede ser clave para reconocer qué tipo de bloque está usando un flujograma determina.

