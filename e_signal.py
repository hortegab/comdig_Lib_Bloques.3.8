################################################################################
##           Funciones sigulares en Tratamiento de senales y sistemas         ##
################################################################################
# Lo siguiente aplica para todas las funciones aqui incluidas:
# cada funcion busca generar un tipo de forma de pulso rodeada de ceros
# los resultados se entregan en forma de un vector x
# Estos son los parametros usados:
# ntaps: es el tamano del vector y coincide con la duracion de la senal generada
# nzero: es el numero de ceros que rodean el pulso generado. Si nzero=0 no 
# habran ceros.
import numpy as np

def pulse_rect(ntaps,nzeros):
# Descripcion: esta funcion permite generar un pulso rectangular discreto
	n_val=ntaps-nzeros             # el numero de valores no iguales a cero
	x=np.zeros(ntaps)       # crea un vector de tamano ntaps lleno de ceros
	ntaps_m= int(ntaps/2)                # el punto medio del vector
	ntaps_i= ntaps_m-int(n_val/2)        # el punto de inicio para los unos
	x[ntaps_i:ntaps_i+n_val:1]=np.ones(n_val) # llenado de los unos
	return x

def pulse_ramp(ntaps,nzeros):
# Descripcion: esta funcion permite generar un pulso en forma de rampa discreto
	n_val=ntaps-nzeros            
	x=np.zeros(ntaps)             
	ntaps_m= int(ntaps/2)         
	ntaps_i= ntaps_m-int(n_val/2) 
	x[ntaps_i:ntaps_i+n_ones:1]=np.linspace(0,n_val-1,n_val) 
	return x

def pulse_delta(ntaps):
# Descripcion: esta funcion permite generar la funcion impulso o funcion
# delta de Dirac discreta
	x=np.zeros(ntaps)                      
	ntaps_m= int(ntaps/2)                  
	x[ntaps_m]=1                           
	return x

def pulse_doublet(ntaps):
# Descripcion: esta funcion permite generar una funcion doblete unitario discreta
	x=np.zeros(ntaps)                      
	ntaps_m= int(ntaps/2)                  
	x[ntaps_m]=1                           
	x[ntaps_m+1]=-1                        
	return x

def pulse_step(ntaps, nzeros):
# Descripcion: esta funcion permite generar una funcion escalon de Heaviside
	n_val=ntaps-nzeros                     
	x=np.zeros(ntaps)                      
	x[nzeros:ntaps:1]=np.ones(n_val) 
	return x

def pulse_exp(ntaps,nzeros, C, a):
# Descripcion: Para generar una funcion exponencial de la forma Ca^n, 
# donde n es tiempo discreto
	n_val=ntaps-nzeros                        
	x=np.zeros(ntaps)                         
	ntaps_i = nzeros                    
	n=np.linspace(0,n_val-1,n_val)      
	x[ntaps_i:ntaps:1]=C*np.power(a,n) 
	return x

