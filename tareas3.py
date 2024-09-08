def cantidad_actual_inventario(palabra):
    while True:
        try:
              cantidad_en_inventario = int(input(palabra))
              if cantidad_en_inventario < 0:
                print(" La cantidad Ingresada no puede ser negativa, vuelva a intentarlo")
              else:
                  return cantidad_en_inventario   
        except ValueError:
             
            print("La cantidad ingresada debe ser un numero entero.\n")        
            
def principal():
   
    print("Sistema Control Inventario Empresa  Chocolamú\n")    
    while True:
        inventario_actual = cantidad_actual_inventario ("Ingrese cantidad Inventario Actual\n")       
        cantidad_vendida = cantidad_actual_inventario("Ingrese cantidad Vendida en el día\n")
        if  cantidad_vendida > inventario_actual:
            print("La cantidad vendida no debe exceder la cantidad del inventario actual\n")
        else:
           inventario_actual -= cantidad_vendida
        print(f"La nueva cantidad en inventario es: {inventario_actual}\n")
        break
    print("Gracias por utilizar el sistema de control de inventario de Chocolamú.")

if __name__ == "__main__":
    principal()
        
     