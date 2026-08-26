from functools import reduce

# FUNCIONES DE VALIDACIÓN
# Usamos try-except para atajar el error si el usuario ingresa un string en vez de un número.
def es_entero(var_str):
    try:
        int(var_str)
        return True     
    except:
        return False

def es_float(var_str):
    try:
        float(var_str)
        return True 
    except:
        return False
    
# Usada para validar las opciones de menú, asegurando que el usuario ingrese un número dentro del rango permitido.
def solicitar_opcion_menu(mensaje, min_opcion, max_opcion):
    dato = input(mensaje)
    while not es_entero(dato) or int(dato) < min_opcion or int(dato) > max_opcion:
        print(f"Error: Ingrese una opción válida ({min_opcion} a {max_opcion}).")
        dato = input(mensaje)
    return int(dato)

# Validamos que el input no quede vacío y que no contenga solo números usando las validaciones.
def pedir_entero(mensaje):
    # Valida que el ingreso sea un número entero y mayor a cero (para códigos y cantidades).
    dato = input(mensaje)
    while not es_entero(dato) or int(dato) <= 0:
        print("Error: Debe ingresar un número entero positivo mayor a 0.")
        dato = input(mensaje)
    return int(dato)

def pedir_float(mensaje):
    # Valida que el ingreso sea un número decimal y mayor a cero (para precios y recargos).
    dato = input(mensaje)
    while not es_float(dato) or float(dato) <= 0:
        print("Error: Debe ingresar un número válido mayor a 0.")
        dato = input(mensaje)
    return float(dato)

def pedir_texto(mensaje):
    # Valida que el texto no esté vacío y no sea un número (puede contener números pero DEBE tener texto).
    dato = input(mensaje)
    # Falla si está vacío o si el usuario ingresó solo números
    while dato.strip() == "" or es_entero(dato) or es_float(dato):
        print("Error: Debe ingresar un texto válido (no numérico y no vacío).")
        dato = input(mensaje)
    return dato.strip()

# ORDENAMIENTOS

# Ordenamiento por burbuja para los productos (criterio elegido: precio)
# Empuja el valor más alto al final de la lista intercambiando elementos vecinos.
def ordenar_productos_burbuja(codigos, nombres, precios):
    n = len(precios)
    # El bucle externo controla cuántas pasadas hacemos sobre la lista
    for i in range(n - 1):
        # El bucle interno compara los elementos vecinos y los intercambia si están en el orden incorrecto
        for j in range(0, n - i - 1):
            # Condición: si el precio actual es MAYOR al que le sigue, los intercambiamos
            if precios[j] > precios[j + 1]:
                # 1. Intercambio en la lista de PRECIOS
                aux_precio = precios[j]
                precios[j] = precios[j + 1]
                precios[j + 1] = aux_precio
                # 2. Intercambio en la lista de NOMBRES
                aux_nombre = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux_nombre
                # 3. Intercambio en la lista de CÓDIGOS
                aux_codigo = codigos[j]
                codigos[j] = codigos[j + 1]
                codigos[j + 1] = aux_codigo

# Ordenamiento por selección para las categorías (criterio: código)
# Busca el código mínimo en el resto de la lista y lo ubica al principio.
def ordenar_categorias_seleccion(codigos, nombres, recargos, estados):
    n = len(codigos)
    # El bucle externo recorre cada posición donde se debe colocar el mínimo
    for i in range(n - 1):
        # Se asume que el elemento actual es el mínimo
        indice_minimo = i
        # El bucle interno busca el código mínimo en el resto de la lista
        for j in range(i + 1, n):
            # Condición: si encontramos un código menor al mínimo actual, actualizamos su índice
            if codigos[j] < codigos[indice_minimo]:
                indice_minimo = j 
        
        # Si el mínimo encontrado es diferente al de la posición actual, realizamos los intercambios
        if indice_minimo != i:
            # 1. Intercambio en la lista de CÓDIGOS
            aux_codigo = codigos[i]
            codigos[i] = codigos[indice_minimo]
            codigos[indice_minimo] = aux_codigo
            
            # 2. Intercambio en la lista de NOMBRES
            aux_nombre = nombres[i]
            nombres[i] = nombres[indice_minimo]
            nombres[indice_minimo] = aux_nombre
            
            # 3. Intercambio en la lista de RECARGOS
            aux_recargo = recargos[i]
            recargos[i] = recargos[indice_minimo]
            recargos[indice_minimo] = aux_recargo
            
            # 4. Intercambio en la lista de ESTADOS
            aux_estado = estados[i]
            estados[i] = estados[indice_minimo]
            estados[indice_minimo] = aux_estado

# Ordenamiento por inserción para el inventario (criterio: cantidad)
# Toma la cantidad de unidades y la inserta en la posición correcta desplazando los elementos mayores hacia la derecha.
def ordenar_inventario_insercion(codigos, cod_prod, cod_cat, cantidades, depositos):
    n = len(cantidades)
    # El bucle externo itera desde el segundo elemento hasta el final
    for i in range(1, n):
        # Se guardan los valores del elemento a insertar de todas las listas paralelas
        llave_cantidad = cantidades[i]
        llave_codigo = codigos[i]
        llave_prod = cod_prod[i]
        llave_cat = cod_cat[i]
        llave_deposito = depositos[i]
        
        # Comenzamos a comparar desde el elemento anterior
        j = i - 1
        
        # Mientras haya elementos a la izquierda con cantidad mayor, desplazamos hacia la derecha
        while j >= 0 and cantidades[j] > llave_cantidad:
            # 1. Desplazamiento en la lista de CANTIDADES
            cantidades[j + 1] = cantidades[j]
            # 2. Desplazamiento en la lista de CÓDIGOS
            codigos[j + 1] = codigos[j]
            # 3. Desplazamiento en la lista de CÓDIGOS DE PRODUCTO
            cod_prod[j + 1] = cod_prod[j]
            # 4. Desplazamiento en la lista de CÓDIGOS DE CATEGORÍA
            cod_cat[j + 1] = cod_cat[j]
            # 5. Desplazamiento en la lista de DEPÓSITOS
            depositos[j + 1] = depositos[j]
            j -= 1
        
        # Una vez encontrada la posición correcta, insertamos el elemento
        cantidades[j + 1] = llave_cantidad
        codigos[j + 1] = llave_codigo
        cod_prod[j + 1] = llave_prod
        cod_cat[j + 1] = llave_cat
        depositos[j + 1] = llave_deposito

# Búsqueda binaria: Divide el espacio de búsqueda por la mitad en cada iteración, requiere que la lista esté ordenada previamente.
def busqueda_binaria(lista_codigos, codigo_buscado):
    # Inicializamos los límites de búsqueda (izquierdo y derecho)
    izquierda = 0
    derecha = len(lista_codigos) - 1

    # Mientras el rango de búsqueda sea válido (izquierda no supera derecha)
    while izquierda <= derecha:
        # Calculamos el punto medio del rango actual
        centro = (izquierda + derecha) // 2

        # Si encontramos el elemento en el centro, lo retornamos
        if lista_codigos[centro] == codigo_buscado:
            return centro
        # Si el elemento del centro es menor al buscado, buscamos en la mitad derecha
        elif lista_codigos[centro] < codigo_buscado:
            izquierda = centro + 1
        # Si el elemento del centro es mayor al buscado, buscamos en la mitad izquierda
        else:
            derecha = centro - 1
    
    # Si no encontramos el elemento, retornamos -1
    return -1

# Búsqueda secuencial: recorre la lista elemento por elemento hasta encontrar el código buscado.
def buscar_indice(lista_codigos, codigo_buscado):
    # Iteramos sobre cada posición de la lista
    for i in range(len(lista_codigos)):
        # Si encontramos el código buscado, retornamos su índice
        if lista_codigos[i] == codigo_buscado:
            return i 
    # Si no encontramos el código, retornamos -1
    return -1 

def buscar_producto_secuencial(codigos, nombres, precios):
    # Solicitamos el código del producto a buscar (validado como entero positivo)
    codigo = pedir_entero("\nIngrese el código del producto: ")
    # Realizamos la búsqueda secuencial en la lista de códigos
    indice = buscar_indice(codigos, codigo)

    # Si no se encuentra (índice = -1), mostramos mensaje de error
    if indice == -1:
        print("Producto no encontrado.")
    # Si se encuentra, mostramos todos los datos del producto
    else:
        print("Código:", codigos[indice])
        print("Nombre:", nombres[indice])
        print("Precio:", precios[indice])

def buscar_producto_binaria(codigos, nombres, precios):
    # Solicitamos el código del producto a buscar (validado como entero positivo)
    codigo = pedir_entero("\nIngrese el código del producto: ")
    # Realizamos la búsqueda binaria en la lista de códigos (requiere que esté ordenada)
    indice = busqueda_binaria(codigos, codigo)

    # Si no se encuentra (índice = -1), mostramos mensaje de error
    if indice == -1:
        print("Producto no encontrado.")
    # Si se encuentra, mostramos todos los datos del producto
    else:
        print("Código:", codigos[indice])
        print("Nombre:", nombres[indice])
        print("Precio:", precios[indice])


# FUNCIONES BASE Y LOGIN
def iniciar_sesion():
    user = "admin"
    password = "inventario2026"
 
    logged_in = False
    intentos = 0
 
    # El usuario tiene 3 intentos para ingresar las credenciales correctas. Si falla los 3 intentos, se bloquea el acceso.
    while logged_in == False and intentos < 3:
        input_user = input("Ingrese su usuario: ")
        input_password = input("Ingrese su contraseña: ")
 
        if input_user == user and input_password == password:
            print("Inicio de sesión exitoso. Bienvenido al sistema de inventario!")
            logged_in = True
        else:
            intentos += 1
            if intentos < 3:
                print("Usuario o contraseña incorrectos. Intente nuevamente.\n")
            else:
                print("Fallaste 3 intentos. Volvé a intentarlo más tarde.")
 
    return logged_in

# 	DATOS HARDCODEADOS (LISTAS PARALELAS)
prod_codigos = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
prod_nombres = ["Cuaderno", "Lapicera", "Goma", "Carpeta", "Marcador", "Tijera", "Regla", "Corrector", "Mochila", "Cartuchera"]
prod_precios = [1500.0, 200.0, 150.0, 2500.0, 800.0, 1200.0, 300.0, 600.0, 15000.0, 3500.0]

cat_codigos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cat_nombres = ["Papelería", "Escritura", "Escolares", "Oficina", "Arte", "Mochilas", "Tecnología", "Libros", "Regalos", "Varios"]
cat_recargos = [15.0, 10.0, 20.0, 25.0, 30.0, 35.0, 40.0, 5.0, 50.0, 10.0]
cat_estados = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]

inv_codigos = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
inv_codigos_prod = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
inv_codigos_cat = [1, 2, 3, 1, 5, 3, 3, 3, 6, 3]
inv_cantidades = [50, 200, 100, 30, 150, 80, 45, 120, 90, 15]
inv_depositos = [1, 1, 2, 1, 3, 2, 1, 2, 1, 3]

# MATRICES (cada elemento es una columna = una lista paralela ya cargada)
columnas_prod = [prod_codigos, prod_nombres, prod_precios]
columnas_cat = [cat_codigos, cat_nombres, cat_recargos, cat_estados]
columnas_inv = [inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos]

# FUNCIONES CRUD 
# PRODUCTOS
def alta_producto(codigos, nombres, precios):
    codigo = pedir_entero("\nIngrese el código del nuevo producto: ")
    if buscar_indice(codigos, codigo) != -1:
        print("Error: Ya existe un producto con ese código.")
    else:
        nombre = pedir_texto("Ingrese el nombre del producto: ")
        precio = pedir_float("Ingrese el precio: $")
        codigos.append(codigo)
        nombres.append(nombre)
        precios.append(precio)
        print("¡Producto agregado con éxito!")

def baja_producto(codigos, nombres, precios, inv_prods):
    codigo = pedir_entero("\nIngrese el código del producto a eliminar: ")
    
    # Verificación de integridad de datos
    # Si el producto existe en el inventario, no se puede eliminar hasta que no esté eliminado el registro de inventario que contiene ese producto
    if buscar_indice(inv_prods, codigo) != -1:
        print("Error: No se puede eliminar. Hay stock de este producto en el inventario.")
        return 

    indice = buscar_indice(codigos, codigo)
    if indice == -1:
        print("Error: El producto no existe.")
    else:
        codigos.pop(indice)
        nombre_borrado = nombres.pop(indice)
        precios.pop(indice)
        print("Producto '" + nombre_borrado + "' eliminado correctamente.")

def modificar_producto(codigos, nombres, precios):
    codigo = pedir_entero("\nIngrese el código del producto a modificar: ")
    indice = buscar_indice(codigos, codigo)
    if indice == -1:
        print("Error: El producto no existe.")
    else:
        print("Producto actual: ", nombres[indice], "- Precio: $", precios[indice])
        nuevo_nombre = pedir_texto("Ingrese el nuevo nombre: ")
        nuevo_precio = pedir_float("Ingrese el nuevo precio: $")
        nombres[indice] = nuevo_nombre
        precios[indice] = nuevo_precio
        print("Producto actualizado.")

def listar_productos(codigos, nombres, precios):
    # Muestra el listado de productos. El armado del texto 
    # ahora lo hace generar_reporte_productos(), que usa reduce
    # para combinar todas las líneas en un único string antes de imprimirlas.
    print(generar_reporte_productos(codigos, nombres, precios))

# FUNCION DE AGREGACIÓN CON REDUCE (Lautaro Zanino)
def generar_reporte_productos(codigos, nombres, precios):
    if len(codigos) == 0:
        return "No hay productos cargados."

    lineas = []
    for i in range(len(codigos)):
        linea = "Cód: " + str(codigos[i]) + " | Nombre: " + nombres[i] + " | Precio: $" + str(precios[i])
        lineas.append(linea)

    # 'reduce' junta todas las líneas en un unico string.
    # Todo eso se guarda en la variable reporte la cual luego se usa para mostrar la informacion
    reporte = reduce(lambda acumulado, linea: acumulado + "\n" + linea, lineas)
    return "\n--- LISTA DE PRODUCTOS ---\n" + reporte
    


# CATEGORÍAS
def alta_categoria(codigos, nombres, recargos, estados):
    codigo = pedir_entero("\nIngrese el código de la nueva categoría: ")
    if buscar_indice(codigos, codigo) != -1:
        print("Error: Ya existe una categoría con ese código.")
    else:
        nombre = pedir_texto("Ingrese el nombre de la categoría: ")
        recargo = pedir_float("Ingrese el porcentaje de recargo (ej: 15.5): ")
        estado = solicitar_opcion_menu("Ingrese el estado (1 = activa / 0 = inactiva): ", 0, 1)
        codigos.append(codigo)
        nombres.append(nombre)
        recargos.append(recargo)
        estados.append(estado)
        print("¡Categoría agregada con éxito!")

def baja_categoria(codigos, nombres, recargos, estados, inv_cats):
    codigo = pedir_entero("\nIngrese el código de la categoría a eliminar: ")
    
    # Verificación de integridad de datos - Si la categoría existe en el inventario, no se puede eliminar hasta que no esté eliminado el registro de inventario que contiene esa categoría
    if buscar_indice(inv_cats, codigo) != -1:
        print("Error: No se puede eliminar. Hay productos en el inventario vinculados a esta categoría.")
        return 

    indice = buscar_indice(codigos, codigo)
    if indice == -1:
        print("Error: La categoría no existe.")
    else:
        codigos.pop(indice)
        nombre_borrado = nombres.pop(indice)
        recargos.pop(indice)
        estados.pop(indice)
        print("Categoría '" + nombre_borrado + "' eliminada correctamente.")

def modificar_categoria(codigos, nombres, recargos, estados):
    codigo = pedir_entero("\nIngrese el código de la categoría a modificar: ")
    indice = buscar_indice(codigos, codigo)
    if indice == -1:
        print("Error: La categoría no existe.")
    else:
        print("Categoría actual:", nombres[indice], "| Recargo:", recargos[indice], "% | Estado:", estados[indice])
        nuevo_nombre = pedir_texto("Ingrese el nuevo nombre: ")
        nuevo_recargo = pedir_float("Ingrese el nuevo recargo: ")
        nuevo_estado = solicitar_opcion_menu("Ingrese el nuevo estado (1 = activa / 0 = inactiva): ", 0, 1)
        nombres[indice] = nuevo_nombre
        recargos[indice] = nuevo_recargo
        estados[indice] = nuevo_estado
        print("Categoría actualizada.")

def listar_categorias(codigos, nombres, recargos, estados):
    # Muestra el listado de categorías. El que se encarga de armar el texto es la nueva funcion 
    # generar_reporte_categoria(), la cual usa 'reduce' para
    # combinar todas las líneas en un único string antes de imprimirlas
    print(generar_reporte_categoria(codigos, nombres, recargos, estados))

# OPERACIÓN DE AGREGACIÓN CON REDUCE (Lautaro Zanino)
def generar_reporte_categoria(codigos, nombres, recargos, estados):
    if len(codigos) == 0:
        return "No hay categorias cargadas."

    lineas = []
    for i in range(len(codigos)):
        # traduce el estado numérico (1/0) a texto legible antes de armar la línea
        estado_texto = "Activa" if estados[i] == 1 else "Inactiva"
        linea = "Código: " + str(codigos[i]) + " | Nombre: " + nombres[i] + " | Recargo: " + str(recargos[i]) + "% | Estado: " + estado_texto
        lineas.append(linea)

    # 'reduce' combina todas las líneas en un unico string 
    # para luego mostrar el contenido a traves del return 
    reporte = reduce(lambda acumulado, linea: acumulado + "\n" + linea, lineas)
    return "\n--- LISTA DE CATEGORIAS ---\n" + reporte

# INVENTARIO
def alta_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps, prod_codigos, cat_codigos):
    codigo = pedir_entero("\nIngrese el código del nuevo registro de inventario: ")
    if buscar_indice(inv_cods, codigo) != -1:
        print("Error: Ya existe un registro de inventario con ese código.")
    else:
        cod_prod = pedir_entero("Ingrese el código del producto: ")
        if buscar_indice(prod_codigos, cod_prod) == -1:
            print("Error: El producto no existe en el sistema. Alta cancelada.")
            return
        cod_cat = pedir_entero("Ingrese el código de la categoría: ")
        if buscar_indice(cat_codigos, cod_cat) == -1:
            print("Error: La categoría no existe en el sistema. Alta cancelada.")
            return
        cantidad = pedir_entero("Ingrese la cantidad de unidades: ")
        deposito = solicitar_opcion_menu("Ingrese el número de depósito (1 o 2): ", 1, 2)
        
        inv_cods.append(codigo)
        inv_prods.append(cod_prod)
        inv_cats.append(cod_cat)
        inv_cants.append(cantidad)
        inv_deps.append(deposito)
        print("¡Registro de inventario agregado con éxito!")

def baja_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps):
    codigo = pedir_entero("\nIngrese el código de inventario a eliminar: ")
    indice = buscar_indice(inv_cods, codigo)
    if indice == -1:
        print("Error: El registro no existe.")
    else:
        inv_cods.pop(indice)
        inv_prods.pop(indice)
        inv_cats.pop(indice)
        inv_cants.pop(indice)
        inv_deps.pop(indice)
        print("Registro de inventario eliminado correctamente.")

def modificar_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps, prod_codigos, cat_codigos):
    codigo = pedir_entero("\nIngrese el código de inventario a modificar: ")
    indice = buscar_indice(inv_cods, codigo)
    if indice == -1:
        print("Error: El registro no existe.")
    else:
        print("Registro actual -> Prod:", inv_prods[indice], "| Cat:", inv_cats[indice], "| Cant:", inv_cants[indice], "| Depósito:", inv_deps[indice])
        nuevo_cod_prod = pedir_entero("Ingrese el nuevo código de producto: ")
        if buscar_indice(prod_codigos, nuevo_cod_prod) == -1:
            print("Error: El producto no existe. Modificación cancelada.")
            return
        nuevo_cod_cat = pedir_entero("Ingrese el nuevo código de categoría: ")
        if buscar_indice(cat_codigos, nuevo_cod_cat) == -1:
            print("Error: La categoría no existe. Modificación cancelada.")
            return
        nueva_cant = pedir_entero("Ingrese la nueva cantidad: ")
        nuevo_dep = solicitar_opcion_menu("Ingrese el nuevo depósito (1 o 2): ", 1, 2)
        
        inv_prods[indice] = nuevo_cod_prod
        inv_cats[indice] = nuevo_cod_cat
        inv_cants[indice] = nueva_cant
        inv_deps[indice] = nuevo_dep
        print("Registro de inventario actualizado.")

def listar_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps):
    # Muestra el listado de inventario. El armado del texto (incluido el caso de
    # lista vacía) lo hace generar_reporte_inventario(), que usa reduce el cual
    # combina todas las líneas en un único string antes de imprimirlas.
    print(generar_reporte_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps))

# OPERACIÓN DE AGREGACIÓN CON REDUCE (Lautaro Zanino)
def generar_reporte_inventario(inv_cods, inv_prods, inv_cats, inv_cants, inv_deps):
    if len(inv_cods) == 0:
        return "No hay registros en el inventario."

    lineas = []
    for i in range(len(inv_cods)):
        linea = "Codigo: " + str(inv_cods[i]) + " | Producto: " + str(inv_prods[i]) + " | Categoria: " + str(inv_cats[i]) + " | Cantidad: " + str(inv_cants[i]) + " | Deposito: " + str(inv_deps[i])
        lineas.append(linea)

    # 'reduce' junta todas las líneas en un unico string, separadas por salto de línea
    reporte = reduce(lambda acumulado, linea: acumulado + "\n" + linea, lineas)
    return "\n--- LISTA DE INVENTARIO ---\n" + reporte


# CONSULTAS
def consulta_productos_en_stock(columnas_prod, columnas_inv):
    # Extraemos las columnas relevantes de la matriz de productos
    prod_codigos = columnas_prod[0]   
    prod_nombres = columnas_prod[1]   

    # Extraemos las columnas relevantes de la matriz de inventario
    inv_prods = columnas_inv[1]   
    inv_cants = columnas_inv[3]   

    print("\n--- PRODUCTOS EN STOCK ---")
    # Recorremos cada producto
    for p in range(len(prod_codigos)):
        # Inicializamos el acumulador de unidades para este producto
        total = 0
        # Buscamos todas las apariciones de este producto en el inventario y sumamos sus cantidades
        for i in range(len(inv_prods)):
            if inv_prods[i] == prod_codigos[p]:
                total += inv_cants[i]
        # Mostramos el producto con su total de unidades en stock
        print("Producto:", prod_nombres[p], "- Unidades en stock:", total)

def consulta_por_categoria(inv_cods, inv_cats, inv_prods, inv_cants, inv_deps):
    # Solicitamos el código de categoría a consultar
    cat_buscada = pedir_entero("\nIngrese el código de categoría a consultar: ")
    # Flag para detectar si se encontraron registros
    encontrado = False
    print("\n--- STOCK DE LA CATEGORÍA", cat_buscada, "---")
    # Recorremos todos los registros de inventario
    for i in range(len(inv_cods)):
        # Si la categoría coincide con la buscada, mostramos el registro
        if inv_cats[i] == cat_buscada:
            print("Cód Inv:", inv_cods[i], "| Producto:", inv_prods[i], "| Cantidad:", inv_cants[i], "| Depósito:", inv_deps[i])
            encontrado = True
    # Si no se encontraron registros, mostramos un mensaje informativo
    if not encontrado:
        print("No hay stock registrado para esta categoría.")

def consulta_por_deposito(inv_cods, inv_deps, inv_prods, inv_cants):
    # Solicitamos el número de depósito a consultar (validado entre 1 y 2)
    dep_buscado = solicitar_opcion_menu("\nIngrese el número de depósito a consultar (1 o 2): ", 1, 2)
    # Flag para detectar si se encontraron registros
    encontrado = False
    print("\n--- STOCK DEL DEPÓSITO", dep_buscado, "---")
    # Recorremos todos los registros de inventario
    for i in range(len(inv_cods)):
        # Si el depósito coincide con el buscado, mostramos el registro
        if inv_deps[i] == dep_buscado:
            print("Cód Inv:", inv_cods[i], "| Producto:", inv_prods[i], "| Cantidad:", inv_cants[i])
            encontrado = True
    # Si no se encontraron registros, mostramos un mensaje informativo
    if not encontrado:
        print("No hay stock registrado en este depósito.")

def consulta_unidades_categoria_deposito(inv_cods, inv_cats, inv_prods, inv_cants, inv_deps):
    # Solicitamos el código de categoría a consultar
    cat_buscada = pedir_entero("\nIngrese el código de categoría a consultar: ")
    # Solicitamos el número de depósito a consultar (validado entre 1 y 2)
    dep_buscado = solicitar_opcion_menu("Ingrese el número de depósito a consultar (1 o 2): ", 1, 2)
    # Acumulador para sumar todas las unidades encontradas
    total = 0
    # Bandera para detectar si se encontraron registros
    encontrado = False
    print("\n--- UNIDADES DE LA CATEGORÍA", cat_buscada, "EN EL DEPÓSITO", dep_buscado, "---")
    # Recorremos todos los registros de inventario
    for i in range(len(inv_cods)):
        # Si coinciden tanto la categoría como el depósito, mostramos el registro y sumamos las unidades
        if inv_cats[i] == cat_buscada and inv_deps[i] == dep_buscado:
            print("Cód Inv:", inv_cods[i], "| Producto:", inv_prods[i], "| Cantidad:", inv_cants[i])
            total += inv_cants[i]
            encontrado = True
    # Si se encontraron registros, mostramos el total de unidades acumuladas
    if encontrado:
        print("Cantidad total de unidades:", total)
    # Si no se encontraron registros, mostramos un mensaje informativo
    else:
        print("No hay stock registrado para esta categoría en ese depósito.")

# PROGRAMA PRINCIPAL (MENÚ)
logged_in = iniciar_sesion()

opcion_menu = 1
opcion_submenu_categoria = 1
opcion_submenu_inventario = 1
opcion_submenu_consultas = 1

if logged_in: 
    while opcion_menu != 999:
        print("\nElija una de las siguientes opciones:")
        print("(1) ABM de producto")
        print("(2) ABM de categoria")
        print("(3) ABM de inventario")
        print("(4) Realizar consultas sobre el stock")
        print("(0) Salir del sistema")
        
        opcion_menu = solicitar_opcion_menu("\nIngrese una opción válida: ", 0, 4)

        if opcion_menu == 0:
            print("Quiere salir de la app?")
            salir = int(input("1 para salir 2 para quedarse"))
            if salir == 1:
                opcion_menu = 999
            else:
                opcion_menu = solicitar_opcion_menu("\nIngrese una opción válida: ", 0, 4)
            
        
        if opcion_menu == 1:
            opcion_submenu_producto = -1 
            while opcion_submenu_producto != 0: 
                print("\n--- ABM PRODUCTOS ---")
                print("(1) Alta de producto")
                print("(2) Baja de producto")
                print("(3) Modificar un producto")
                print("(4) Lista de productos")
                print("(5) Buscar producto (Secuencial)")
                print("(6) Buscar producto (Binaria)")
                print("(0) Volver atrás")

                opcion_submenu_producto = solicitar_opcion_menu("\nIngrese una opción válida: ", 0, 6)
                
                if opcion_submenu_producto == 1:
                    alta_producto(prod_codigos, prod_nombres, prod_precios)
                elif opcion_submenu_producto == 2:
                    baja_producto(prod_codigos, prod_nombres, prod_precios, inv_codigos_prod)
                elif opcion_submenu_producto == 3:
                    modificar_producto(prod_codigos, prod_nombres, prod_precios)
                elif opcion_submenu_producto == 4:
                    ordenar_productos_burbuja(prod_codigos, prod_nombres, prod_precios)
                    listar_productos(prod_codigos, prod_nombres, prod_precios)
                elif opcion_submenu_producto == 5:
                    buscar_producto_secuencial(prod_codigos, prod_nombres, prod_precios)
                elif opcion_submenu_producto == 6:
                    buscar_producto_binaria(prod_codigos, prod_nombres, prod_precios)

        elif opcion_menu == 2:
            opcion_submenu_categoria = -1
            while opcion_submenu_categoria != 0: 
                print("\n--- ABM CATEGORÍAS ---")
                print("(1) Alta de categoria")
                print("(2) Baja de categoria")
                print("(3) Modificar una categoria")
                print("(4) Lista de categorias")
                print("(0) Volver atrás")
                
                opcion_submenu_categoria = solicitar_opcion_menu("\nIngrese una opción válida: ", 0, 4)
                
                if opcion_submenu_categoria == 1:
                    alta_categoria(cat_codigos, cat_nombres, cat_recargos, cat_estados)
                elif opcion_submenu_categoria == 2:
                    baja_categoria(cat_codigos, cat_nombres, cat_recargos, cat_estados, inv_codigos_cat)
                elif opcion_submenu_categoria == 3:
                    modificar_categoria(cat_codigos, cat_nombres, cat_recargos, cat_estados)
                elif opcion_submenu_categoria == 4:
                    ordenar_categorias_seleccion(cat_codigos, cat_nombres, cat_recargos, cat_estados)
                    listar_categorias(cat_codigos, cat_nombres, cat_recargos, cat_estados)

        elif opcion_menu == 3:
            opcion_submenu_inventario = -1
            while opcion_submenu_inventario != 0: 
                print("\n--- ABM INVENTARIO ---")
                print("(1) Alta de inventario")
                print("(2) Baja de inventario")
                print("(3) Modificar inventario")
                print("(4) Lista de inventario")
                print("(0) Volver atrás")

                opcion_submenu_inventario = solicitar_opcion_menu("\nIngrese una opción válida: ", 0, 4)

                if opcion_submenu_inventario == 1:
                    alta_inventario(inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos, prod_codigos, cat_codigos)
                elif opcion_submenu_inventario == 2:
                    baja_inventario(inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos)
                elif opcion_submenu_inventario == 3:
                    modificar_inventario(inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos, prod_codigos, cat_codigos)
                elif opcion_submenu_inventario == 4:
                    ordenar_inventario_insercion(inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos)
                    listar_inventario(inv_codigos, inv_codigos_prod, inv_codigos_cat, inv_cantidades, inv_depositos)

        elif opcion_menu == 4:
            opcion_submenu_consultas = -1
            while opcion_submenu_consultas != 0: 
                print("\n--- CONSULTAS ---")
                print("(1) Ver productos en stock")
                print("(2) Ver categorías con stock")
                print("(3) Ver depósitos con stock")
                print("(4) Cantidad total de unidades por categoría y depósito")
                print("(0) Volver atrás")
                
                opcion_submenu_consultas = solicitar_opcion_menu("\nIngrese una opcion válida: ", 0, 4)
                
                if opcion_submenu_consultas == 1:
                    consulta_productos_en_stock(columnas_prod, columnas_inv)
                elif opcion_submenu_consultas == 2:
                    consulta_por_categoria(inv_codigos, inv_codigos_cat, inv_codigos_prod, inv_cantidades, inv_depositos)
                elif opcion_submenu_consultas == 3:
                     consulta_por_deposito(inv_codigos, inv_depositos, inv_codigos_prod, inv_cantidades)
                elif opcion_submenu_consultas == 4:
                    consulta_unidades_categoria_deposito(inv_codigos, inv_codigos_cat, inv_codigos_prod, inv_cantidades, inv_depositos)
    
    print("\nSaliendo del sistema. ¡Gracias por usarlo!")		