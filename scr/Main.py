#KEVIN JIMÉNEZ TORRES
#14/11/2019

#LISTAS PARA DATOS RANDOM
Fechas=["13/11/2019","14/11/2019","12/11/2019","10/11/2019","15/11/2019"]
Precios=[2000,2200,1500,1800,1250,2375]

#SE IMPORTAN LIBRERIAS NECESARIAS
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import uic

#LISTAS PARA ALMACENAR OBJETOS
Clients=[]
Restaurants=[]
Orders=[]
Details=[]

#SE DECLARAN CLASES PARA LOS OBJETOS
'''Clase para generar objetos de tipo usuario'''
class Clientes:
    def __init__(self):
        self.Nombre = ""
        self.Telefono = 0
        self.Provincia = ""
    def setInfo(self,n,t,p):
        self.Nombre= n
        self.Telefono= t
        self.Provincia= p
    def getTelefono(self):
        return self.Telefono
    def getNombre(self):
        return self.Nombre
    def getProvincia(self):
        return self.Provincia
'''Clase para generar objetos de tipo restaurante'''
class Restaurantes:
    def __init__(self):
        self.Nombre=""
        self.Provincia=""
        self.Tipo=""
        self.Especialidad=""
        self.ListaOpciones=[]
    def setInfo(self,n,p,t,e):
        self.Nombre = n
        self.Provincia = p
        self.Tipo = t
        self.Especialidad = e
    def getNombre(self):
        return self.Nombre
    def getProvincia(self):
        return self.Provincia
    def getEspecialidad(self):
        return self.Especialidad
    def getListaOpciones(self):
        return self.ListaOpciones
    def getTipo(self):
        return self.Tipo
'''Clase para generar objetos de tipo opcion(Comidas)'''
class Opciones:
    def __init__(self):
        self.Nombre = ""
        self.Codigo = 0
        self.Precio = 0
        self.Tipo = ""
        self.Veces= 0
    def setInfo(self,n,cod,p,t):
        self.Nombre = n
        self.Codigo = cod
        self.Precio = p
        self.Tipo = t
    def getCod(self):
        return self.Codigo
    def getPrecio(self):
        return self.Precio
    def getNombre(self):
        return self.Nombre
    def getTipo(self):
        return self.Tipo
    def modVeces(self,x):
        self.Veces += x
    def getVeces(self):
        return self.Veces
'''Clase para generar objetos de tipo pedido'''
class Pedidos:
    def __init__(self):
        self.TelefonoC=0
        self.Restaurante=""
        self.Estado=""
        self.Fecha=""
        self.NumPed=0
    def setInfo(self,t,r,e,num):
        self.TelefonoC = t
        self.Restaurante = r
        self.Estado = e
        self.NumPed= num
        self.Fecha= random.choice(Fechas)
    def getEstado(self):
        return self.Estado
    def getTelefonoC(self):
        return self.TelefonoC
    def getNumPed(self):
        return self.NumPed
    def getRestaurante(self):
        return self.Restaurante
    def Facturar(self):
        self.Estado = "FACTURADO"
'''Clase para generar objetos de tipo pedido'''
class Pedidos:
    def __init__(self):
        self.TelefonoC=0
        self.Restaurante=""
        self.Estado=""
        self.Fecha=""
        self.NumPed=0
    def setInfo(self,t,r,e,num):
        self.TelefonoC = t
        self.Restaurante = r
        self.Estado = e
        self.NumPed= num
        self.Fecha= random.choice(Fechas)
    def getEstado(self):
        return self.Estado
    def getTelefonoC(self):
        return self.TelefonoC
    def getNumPed(self):
        return self.NumPed
    def getRestaurante(self):
        return self.Restaurante
    def Facturar(self):
        self.Estado = "FACTURADO"
'''Clase para generar objetos de tipo detalle de pedido'''
class DetallePedido:
    def __init__(self):
        self.NumeroPedido=0
        self.CodOpcion=0
        self.Cantidad=0
        self.Monto=0
    def setInfo(self,n,cod,cant):
        self.NumeroPedido = n
        self.CodOpcion = cod
        self.Cantidad = cant
    def getNum(self):
        return self.NumeroPedido
    def getCod(self):
        return self.CodOpcion
    def getCant(self):
        return self.Cantidad
    def modMonto(self, x):
        self.Monto += x
    def getMonto(self):
        return self.Monto

#LECTURA Y ESCRITURA DE ARCHIVOS
'''Funcion que lee el archivo -clientes_proyecto_II.txt- y guarda los datos de los clientes suministrados en el mismo'''
def GenerarClientes():
    a=open("clientes_proyecto_II.txt","r")
    cont=0
    while cont != 10:
        line = a.readline()
        line = line[:-1]
        line = line.split(",")
        Tel = line[0]
        Nombre = line[1]
        Provincia = line[2]
        U = Clientes()
        U.setInfo(Nombre, Tel, Provincia)
        Clients.append(U)
        cont+=1
    a.close()
'''Funcion que lee el archivo -Restaurantes_proyecto_II.txt- y guarda los objetos de tipo restaurante con los datos suministrados en dichos archivos'''
def GenerarRestaurantes():
    a = open("Restaurantes_proyecto_II.txt", "r")
    cont=0
    while cont != 1:
        line = a.readline()
        line = line[:-1]
        line = line.split("/")
        Nombre = line[0]
        Tipo = line[1]
        Provincia = line[2]
        Especialidad= line[3]
        R = Restaurantes()
        R.setInfo(Nombre, Provincia, Tipo, Especialidad)
        Restaurants.append(R)
        cont+=1
    a.close()
'''Funcion que lee el archivo -opciones_-_platillos.txt- para generar las opciones de cada restaurante
 y guarda los objetos en las listas de opciones de los mismos'''
def GenerarOpciones():
    global DRINKS, STARTERS, MAINCOURSES, DESSERTS
    DRINKS=[]
    STARTERS=[]
    MAINCOURSES=[]
    DESSERTS=[]
    for i in Restaurants:
        a = open("opciones_-_platillos.txt", "r")
        Bebidas=0
        PlatoFuertes=0
        Postres=0
        Entradas=0
        cont=0
        while cont!=28:
            line = a.readline()
            line = line[:-1]
            line = line.split("/")
            Nombre = line[0]
            Tipo = line[1]
            Rest = i.getNombre()[0] + i.getNombre()[1] + i.getNombre()[2]
            if len(i.getListaOpciones())<10:
                Cod=Rest+("10"+str(len(i.getListaOpciones())))
            elif len(i.getListaOpciones()) < 100:
                Cod=Rest+("1"+str(len(i.getListaOpciones())))
            else:

                Cod=Rest+(str(100+len(i.getListaOpciones())))
            Precio=random.choice(Precios)
            if Tipo == "BEBIDA" and Bebidas!=6:
                Bebidas+=1
                O = Opciones()
                O.setInfo(Nombre, Cod, Precio, Tipo)
                i.getListaOpciones().append(O)
                DRINKS.append(O)
                cont += 1
            elif Tipo == "PLATO FUERTE" and PlatoFuertes!=10:
                PlatoFuertes+=1
                O = Opciones()
                O.setInfo(Nombre, Cod, Precio, Tipo)
                i.getListaOpciones().append(O)
                MAINCOURSES.append(O)
                cont += 1
            elif Tipo == "POSTRE" and Postres!=6:
                Postres+=1
                O = Opciones()
                O.setInfo(Nombre, Cod, Precio, Tipo)
                i.getListaOpciones().append(O)
                DESSERTS.append(O)
                cont += 1
            elif Tipo == "ENTRADA" and Entradas!=6:
                Entradas+=1
                O=Opciones()
                O.setInfo(Nombre,Cod,Precio,Tipo)
                i.getListaOpciones().append(O)
                STARTERS.append(O)
                cont+=1
            else:
                cont=cont
        a.close()
'''Funcion que lee el archivo -Pedidos_proyecto_II.txt- y genera 0 pedidos guardando los abjetos en una lista'''
def GenerarPedidos():
    a = open("Pedidos_proyecto_II.txt", "r")
    line = a.readline()
    while line != "":
        line = line[:-1]
        line = line.split("/")
        Num = line[0]
        TelCliente = line[1]
        NombreRest = line[2]
        Estado = line[3]
        P=Pedidos()
        P.setInfo(TelCliente,NombreRest,Estado,Num)
        Orders.append(P)
        line = a.readline()
    a.close()
'''Funcion que lee el archivos -DetallesPedidos_proyecto_II.txt- y genera detalles para cada pedido generado '''
def GenerarDetallesPed():
    a = open("DetallesPedidos_proyecto_II.txt", "r")
    line = a.readline()
    while line != "":
        line = line[:-1]
        line = line.split("/")
        Num = line[0]
        Cod = line[1]
        Cant = line[2]
        D = DetallePedido()
        D.setInfo(Num,Cod,Cant)
        Details.append(D)
        line = a.readline()
    a.close()
'''Funcion que crea los archivos de Pedidos y detalles de Pedidos y escribe en ellos los datos generados de forma aleatoria y extraidos desde los objetos'''
def EscribirPedidosYDetalles():
    a = open("Pedidos_proyecto_II.txt","a")
    ar = open("DetallesPedidos_proyecto_II.txt", "a")
    cont=0
    NUM=1
    while cont < 15:
        Cliente=random.choice(Clients)
        TelC=Cliente.getTelefono()
        Estado="PENDIENTE"
        Restaurante=random.choice(Restaurants)
        NRes=Restaurante.getNombre()
        a.write(str(NUM))
        a.write("/")
        a.write(str(TelC))
        a.write("/")
        a.write(str(NRes))
        a.write("/")
        a.write(str(Estado))
        a.write("\n")
        det=0
        while det < 2:
            Opcion=random.choice(Restaurante.getListaOpciones())
            Cod=Opcion.getCod()
            Cant=random.choice([1,2,3,4])
            ar.write(str(NUM))
            ar.write("/")
            ar.write(str(Cod))
            ar.write("/")
            ar.write(str(Cant))
            ar.write("\n")
            det += 1
        NUM+=1
        cont+=1
    ar.close()
    a.close()

#FUNCIONES QUE MODIFICAN DATOS PARA PODER REALIZAR LAS CONSULTAS
'''Funcion que modifica el atributo veces creado para determinar la cantidad de veces que se ha vendido una opcion'''
def ModVeces():
    for i in Details:
        for x in Restaurants:
            for z in x.getListaOpciones():
                if z.getCod()==i.getCod():
                    Cant=int(i.getCant())
                    z.modVeces(Cant)
'''Funcion que modifica el atributo de monto de cada detalle de pedido creado para determinar el costo de cada detalle'''
def ModMonto():
    for i in Details:
        for x in Orders:
            if i.getNum() == x.getNumPed():
                for z in Restaurants:
                    if x.getRestaurante() == z.getNombre():
                        for y in z.getListaOpciones():
                            if i.getCod()==y.getCod():
                                Mont=int(y.getPrecio())*int(i.getCant())
                                i.modMonto(Mont)

#CONSULTAS SOLICITADAS
'''Funcion que retorna en forma de lista los datos de las opciones más vendidas de cada tipo,
 estos datos corresponden a nombres y cantitad de veces vendidas'''
def OpcionesMasVendidas():
    bedC=0
    entC=0
    plfrC=0
    posC=0
    bedN="---"
    entN="---"
    plfrN="---"
    posN="---"
    for i in Restaurants[0].getListaOpciones():
        if i.getTipo()=="BEBIDA":
            if i.getVeces()>bedC:
                bedC= i.getVeces()
                bedN= i.getNombre()
        elif i.getTipo()=="ENTRADA":
            if i.getVeces()>entC:
                entC= i.getVeces()
                entN= i.getNombre()
        elif i.getTipo()=="PLATO FUERTE":
            if i.getVeces()>plfrC:
                plfrC= i.getVeces()
                plfrN= i.getNombre()
        elif i.getTipo()=="POSTRE":
            if i.getVeces()>posC:
                posC= i.getVeces()
                posN= i.getNombre()
    return [bedC,bedN,entC,entN,plfrC,plfrN,posC,posN]
'''Funcion que retorna una lista con la imformacion de los pedidos de los clientes,
estos datos son correspondientes a la cantidad de pedidos realizados en el Restaurante y el monto total pagado'''
def ClientesPorRestaurante():
        ACant = 0
        AMontoTotal = 0
        BCant = 0
        BMontoTotal = 0
        CCant = 0
        CMontoTotal = 0
        DCant = 0
        DMontoTotal = 0
        ECant = 0
        EMontoTotal = 0
        FCant = 0
        FMontoTotal = 0
        GCant = 0
        GMontoTotal = 0
        HCant = 0
        HMontoTotal = 0
        ICant = 0
        IMontoTotal = 0
        JCant = 0
        JMontoTotal = 0
        for z in Orders:
            if z.getTelefonoC() == Clients[0].getTelefono():
                ACant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        AMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[1].getTelefono():
                BCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        BMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[2].getTelefono():
                CCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        CMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[3].getTelefono():
                DCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        DMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[4].getTelefono():
                ECant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        EMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[5].getTelefono():
                FCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        FMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[6].getTelefono():
                GCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        GMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[7].getTelefono():
                HCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        HMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[8].getTelefono():
                ICant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        IMontoTotal += y.getMonto()
            elif z.getTelefonoC() == Clients[9].getTelefono():
                JCant += 1
                for y in Details:
                    if z.getNumPed() == y.getNum():
                        JMontoTotal += y.getMonto()
        return [ACant, AMontoTotal, BCant, BMontoTotal, CCant, CMontoTotal, DCant, DMontoTotal, ECant, EMontoTotal,
                FCant, FMontoTotal, GCant, GMontoTotal, HCant, HMontoTotal, ICant, IMontoTotal, JCant, JMontoTotal]

#SE DECLARAN CLASES DE LA INTERFAZ GRAFICA
Ui_MainWindow, QtBaseClass = uic.loadUiType('Login.ui')
'''Clase de la ventana inical de la aplicacion'''
class VentPrin(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(VentPrin,self).__init__(parent)
        loadUi('Login.ui',self)
        self.BotonIngreso.clicked.connect(self.Options)

    def Options(self):
        global CLIENTE
        CLIENTE=self.getUser
        self.hide()
        nuevaventana= MenuInicio(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('MenuInicio.ui')
        nuevaventana.show()

    def getUser(self):
        LOGEADO = self.ListUsu.currentText()
        return LOGEADO
    def closeEvent(self, event):
        resultado=QMessageBox.question(self,"Saliendo...","¿Seguro que desea salir?",
        QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event.accept()
        else: event.ignore()
'''Clase de la ventana del menu de la aplicacion, donde se decide si realizar pedido o ver algunas de las consultas'''
class MenuInicio(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MenuInicio,self).__init__(parent)
        loadUi('MenuInicio.ui',self)
        self.Pedir.clicked.connect(self.Opciones)
        self.Consulta1.clicked.connect(self.Consultar1)
        self.Consulta2.clicked.connect(self.Consultar2)
        self.volver.clicked.connect(self.Volver)

    def Opciones(self):
        global PEDIDO
        PEDIDO = []
        self.hide()
        nuevaventana=VentMenu(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Menu.ui')
        nuevaventana.show()

    def Consultar1(self):
        self.hide()
        nuevaventana=Cons1(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Consulta1.ui')
        nuevaventana.show()

    def Consultar2(self):
        self.hide()
        nuevaventana=Cons2(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Consulta2.ui')
        nuevaventana.show()

    def Volver(self):
        self.hide()
        nuevaventana=VentPrin(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Login.ui')
        nuevaventana.show()
'''Clase de la ventana de la consulta1 de la aplicacion'''
class Cons1(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Cons1,self).__init__(parent)
        loadUi("Consulta1.ui",self)
        ModVeces()
        Datos= OpcionesMasVendidas()
        CantB=Datos[0]
        NomB=Datos[1]
        CantE=Datos[2]
        NomE=Datos[3]
        CantPF=Datos[4]
        NomPF=Datos[5]
        CantP=Datos[6]
        NomP=Datos[7]
        self.bebidaN.setText(str(NomB))
        self.bebidaC.setText(str(CantB))
        self.entradaN.setText(str(NomE))
        self.entradaC.setText(str(CantE))
        self.platoN.setText(str(NomPF))
        self.platoC.setText(str(CantPF))
        self.postreN.setText(str(NomP))
        self.postreC.setText(str(CantP))
        self.volver.clicked.connect(self.Volver)

    def Volver(self):
        self.hide()
        nuevaventana=MenuInicio(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('MenuInicio.ui')
        nuevaventana.show()
'''Clase de la ventana de la consulta2 de la aplicacion'''
class Cons2(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Cons2,self).__init__(parent)
        loadUi("Consulta2.ui",self)
        self.volver.clicked.connect(self.Volver)
        ModMonto()
        Datos=ClientesPorRestaurante()
        Cantidad1=Datos[0]
        Monto1=Datos[1]
        Cantidad2=Datos[2]
        Monto2=Datos[3]
        Cantidad3=Datos[4]
        Monto3=Datos[5]
        Cantidad4=Datos[6]
        Monto4=Datos[7]
        Cantidad5=Datos[8]
        Monto5=Datos[9]
        Cantidad6=Datos[10]
        Monto6=Datos[11]
        Cantidad7=Datos[12]
        Monto7=Datos[13]
        Cantidad8=Datos[14]
        Monto8=Datos[15]
        Cantidad9=Datos[16]
        Monto9=Datos[17]
        Cantidad10=Datos[18]
        Monto10=Datos[19]
        self.CANT1.setText(str(Cantidad1))
        self.CANT2.setText(str(Cantidad2))
        self.CANT3.setText(str(Cantidad3))
        self.CANT4.setText(str(Cantidad4))
        self.CANT5.setText(str(Cantidad5))
        self.CANT6.setText(str(Cantidad6))
        self.CANT7.setText(str(Cantidad7))
        self.CANT8.setText(str(Cantidad8))
        self.CANT9.setText(str(Cantidad9))
        self.CANT10.setText(str(Cantidad10))
        self.MONT1.setText(str(Monto1))
        self.MONT2.setText(str(Monto2))
        self.MONT3.setText(str(Monto3))
        self.MONT4.setText(str(Monto4))
        self.MONT5.setText(str(Monto5))
        self.MONT6.setText(str(Monto6))
        self.MONT7.setText(str(Monto7))
        self.MONT8.setText(str(Monto8))
        self.MONT9.setText(str(Monto9))
        self.MONT10.setText(str(Monto10))

    def Volver(self):
        self.hide()
        nuevaventana = MenuInicio(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('MenuInicio.ui')
        nuevaventana.show()
'''Clase de la ventana del menu del restaurante, donde se elige entre los tipos de opciones'''
class VentMenu(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(VentMenu,self).__init__(parent)
        loadUi("Menu.ui",self)
        self.volver.clicked.connect(self.Volver)
        self.BED.clicked.connect(self.BEBIDAS)
        self.facturar.clicked.connect(self.Facturacion)
        self.ENT.clicked.connect(self.ENTRADAS)
        self.PLFR.clicked.connect(self.PLATOSFUERTES)
        self.POS.clicked.connect(self.POSTRES)

    def ItemsFactura(self):
        TOTALTOTAL = 0
        for y in Clients:
            if str(CLIENTE) == y.getTelefono():
                Namee = y.getNombre()
        for i in PEDIDO:
            self.cantidades.addItem(str(i[0]))
            self.descripciones.addItem(str(i[1]))
            for x in Restaurants[0].getListaOpciones():
                if i[1] == x.getNombre():
                    self.precios.addItem(str(x.getPrecio()))
                    TotalItem = int(x.getPrecio()) * int(i[0])
                    TOTALTOTAL += TotalItem
        self.subtotal.setText(str(TOTALTOTAL))
        self.impuesto.setText(str(TOTALTOTAL * 0.13))
        self.total.setText(str((TOTALTOTAL * 0.13) + TOTALTOTAL))
        self.Tcliente.setText(str(CLIENTE))
        self.Ncliente.setText(str(Namee))

    def Volver(self):
        self.hide()
        nuevaventana = MenuInicio(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('MenuInicio.ui')
        nuevaventana.show()

    def Facturacion(self):
        self.hide()
        nuevaventana=factura(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Factura.ui')
        self.ItemsFactura
        nuevaventana.show()

    def BEBIDAS(self):
        self.hide()
        nuevaventana = bebidas(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Bebidas.ui')
        nuevaventana.show()
    def ENTRADAS(self):
        self.hide()
        nuevaventana = entradas(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Entradas.ui')
        nuevaventana.show()
    def PLATOSFUERTES(self):
        self.hide()
        nuevaventana = platosfuertes(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('PlatosFuertes.ui')
        nuevaventana.show()
    def POSTRES(self):
        self.hide()
        nuevaventana = postres(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Postres.ui')
        nuevaventana.show()
'''Clase de la ventana donde se muestran las bebidas'''
class bebidas(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(bebidas,self).__init__(parent)
        loadUi('Bebidas.ui',self)
        self.P1.setText(str(DRINKS[0].getPrecio()))
        self.P2.setText(str(DRINKS[1].getPrecio()))
        self.P3.setText(str(DRINKS[2].getPrecio()))
        self.P4.setText(str(DRINKS[3].getPrecio()))
        self.P5.setText(str(DRINKS[4].getPrecio()))
        self.P6.setText(str(DRINKS[5].getPrecio()))
        self.cancel.clicked.connect(self.Cancelar)
        self.B1A.clicked.connect(self.Ag1)
        self.B2A.clicked.connect(self.Ag2)
        self.B3A.clicked.connect(self.Ag3)
        self.B4A.clicked.connect(self.Ag4)
        self.B5A.clicked.connect(self.Ag5)
        self.B6A.clicked.connect(self.Ag6)

    def Cancelar(self):
        self.hide()
        nuevaventana = VentMenu(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Menu.ui')
        nuevaventana.show()

    def Ag1(self):
        Cant = self.B1C.value()
        Name = self.B1.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag2(self):
        Cant = self.B2C.value()
        Name = self.B2.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag3(self):
        Cant = self.B3C.value()
        Name = self.B3.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag4(self):
        Cant = self.B4C.value()
        Name = self.B4.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag5(self):
        Cant = self.B5C.value()
        Name = self.B5.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag6(self):
        Cant = self.B6C.value()
        Name = self.B6.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
'''Clase de la ventana donde se muestran las entradas'''
class entradas(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(entradas,self).__init__(parent)
        loadUi('Entradas.ui',self)
        self.P1.setText(str(STARTERS[0].getPrecio()))
        self.P2.setText(str(STARTERS[1].getPrecio()))
        self.P3.setText(str(STARTERS[2].getPrecio()))
        self.P4.setText(str(STARTERS[3].getPrecio()))
        self.P5.setText(str(STARTERS[4].getPrecio()))
        self.P6.setText(str(STARTERS[5].getPrecio()))
        self.cancel.clicked.connect(self.Cancelar)
        self.E1A.clicked.connect(self.Ag1)
        self.E2A.clicked.connect(self.Ag2)
        self.E3A.clicked.connect(self.Ag3)
        self.E4A.clicked.connect(self.Ag4)
        self.E5A.clicked.connect(self.Ag5)
        self.E6A.clicked.connect(self.Ag6)

    def Cancelar(self):
        self.hide()
        nuevaventana = VentMenu(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Menu.ui')
        nuevaventana.show()

    def Ag1(self):
        Cant = self.E1C.value()
        Name = self.E1.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag2(self):
        Cant = self.E2C.value()
        Name = self.E2.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag3(self):
        Cant = self.E3C.value()
        Name = self.E3.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag4(self):
        Cant = self.E4C.value()
        Name = self.E4.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag5(self):
        Cant = self.E5C.value()
        Name = self.E5.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag6(self):
        Cant = self.E6C.value()
        Name = self.E6.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
'''Clase de la ventana donde se muestran los platos fuertes'''
class platosfuertes(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(platosfuertes,self).__init__(parent)
        loadUi('PlatosFuertes.ui',self)
        self.P1.setText(str(MAINCOURSES[0].getPrecio()))
        self.P2.setText(str(MAINCOURSES[1].getPrecio()))
        self.P3.setText(str(MAINCOURSES[2].getPrecio()))
        self.P4.setText(str(MAINCOURSES[3].getPrecio()))
        self.P5.setText(str(MAINCOURSES[4].getPrecio()))
        self.P6.setText(str(MAINCOURSES[5].getPrecio()))
        self.P7.setText(str(MAINCOURSES[6].getPrecio()))
        self.P8.setText(str(MAINCOURSES[7].getPrecio()))
        self.P9.setText(str(MAINCOURSES[8].getPrecio()))
        self.P10.setText(str(MAINCOURSES[9].getPrecio()))
        self.cancel.clicked.connect(self.Cancelar)
        self.PF1A.clicked.connect(self.Ag1)
        self.PF2A.clicked.connect(self.Ag2)
        self.PF3A.clicked.connect(self.Ag3)
        self.PF4A.clicked.connect(self.Ag4)
        self.PF5A.clicked.connect(self.Ag5)
        self.PF6A.clicked.connect(self.Ag6)
        self.PF7A.clicked.connect(self.Ag7)
        self.PF8A.clicked.connect(self.Ag8)
        self.PF9A.clicked.connect(self.Ag9)
        self.PF10A.clicked.connect(self.Ag10)
    def Cancelar(self):
        self.hide()
        nuevaventana = VentMenu(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Menu.ui')
        nuevaventana.show()

    def Ag1(self):
        Cant = self.PF1C.value()
        Name = self.PF1.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag2(self):
        Cant = self.PF2C.value()
        Name = self.PF2.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag3(self):
        Cant = self.PF3C.value()
        Name = self.PF3.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag4(self):
        Cant = self.PF4C.value()
        Name = self.PF4.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag5(self):
        Cant = self.PF5C.value()
        Name = self.PF5.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag6(self):
        Cant = self.PF6C.value()
        Name = self.PF6.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag7(self):
        Cant = self.PF7C.value()
        Name = self.PF7.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag8(self):
        Cant = self.PF8C.value()
        Name = self.PF8.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag9(self):
        Cant = self.PF9C.value()
        Name = self.PF9.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
    def Ag10(self):
        Cant = self.PF10C.value()
        Name = self.PF10.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
'''Clase de la ventana donde se muestran los postres'''
class postres(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(postres,self).__init__(parent)
        loadUi('Postres.ui',self)
        self.P1.setText(str(DESSERTS[0].getPrecio()))
        self.P2.setText(str(DESSERTS[1].getPrecio()))
        self.P3.setText(str(DESSERTS[2].getPrecio()))
        self.P4.setText(str(DESSERTS[3].getPrecio()))
        self.P5.setText(str(DESSERTS[4].getPrecio()))
        self.P6.setText(str(DESSERTS[5].getPrecio()))
        self.cancel.clicked.connect(self.Cancelar)
        self.P1A.clicked.connect(self.Ag1)
        self.P2A.clicked.connect(self.Ag2)
        self.P3A.clicked.connect(self.Ag3)
        self.P4A.clicked.connect(self.Ag4)
        self.P5A.clicked.connect(self.Ag5)
        self.P6A.clicked.connect(self.Ag6)

    def Cancelar(self):
        self.hide()
        nuevaventana = VentMenu(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('Menu.ui')
        nuevaventana.show()

    def Ag1(self):
        Cant = self.P1C.value()
        Name = self.PS1.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag2(self):
        Cant = self.P2C.value()
        Name = self.PS2.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag3(self):
        Cant = self.P3C.value()
        Name = self.PS3.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag4(self):
        Cant = self.P4C.value()
        Name = self.PS4.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag5(self):
        Cant = self.P5C.value()
        Name = self.PS5.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()

    def Ag6(self):
        Cant = self.P6C.value()
        Name = self.PS6.text()
        PEDIDO.append([Cant, Name])
        self.Cancelar()
'''Clase de la ventana de facturacion'''
class factura(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(factura,self).__init__(parent)
        loadUi('Factura.ui',self)
        self.volvermenu.clicked.connect(self.VolverM)

    def VolverM(self):
        self.hide()
        nuevaventana=MenuInicio(self)
        Ui_MainWindow, QtBaseClass = uic.loadUiType('MenuInicio.ui')
        nuevaventana.show()

    def ItemsFactura(self):
        TOTALTOTAL = 0
        for y in Clients:
            if str(CLIENTE) == y.getTelefono():
                Namee = y.getNombre()
        for i in PEDIDO:
            self.cantidades.addItem(str(i[0]))
            self.descripciones.addItem(str(i[1]))
            for x in Restaurants[0].getListaOpciones():
                if i[1] == x.getNombre():
                    self.precios.addItem(str(x.getPrecio()))
                    TotalItem = int(x.getPrecio()) * int(i[0])
                    TOTALTOTAL += TotalItem
        self.subtotal.setText(str(TOTALTOTAL))
        self.impuesto.setText(str(TOTALTOTAL * 0.13))
        self.total.setText(str((TOTALTOTAL * 0.13) + TOTALTOTAL))
        self.Tcliente.setText(str(CLIENTE))
        self.Ncliente.setText(str(Namee))

#FUNCION PRINCIPAL, CON LLAMADOS NECESARIOS PARA INICIAR LA APLICACION
'''Funcion que reune el llamado de todas las otras funciones, y de este modo solo ella ejecuta el programa'''
def Main():
    GenerarClientes()
    GenerarRestaurantes()
    GenerarOpciones()
    EscribirPedidosYDetalles()
    GenerarPedidos()
    GenerarDetallesPed()
    app = QApplication(sys.argv)
    Login = VentPrin()
    Login.show()
    app.exec_()


#INICIO DE LA APLICACION
Main()