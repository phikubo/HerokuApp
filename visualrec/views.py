from django.shortcuts import render, redirect
from .models import venta_articulo
from .forms import articuloForm
from .forms import login_form
from .forms import registrar_usuario_form
from django.contrib.auth import login,logout, authenticate #para efectos de logeo.
from django.contrib.auth.models import User #para registrar usuarios.
#crear servicios web.
from django.http import HttpResponse
from django.core import serializers


# Create your views here.

#libreria de watson Fase3
import json
from watson_developer_cloud import VisualRecognitionV3 as VR
ApiVr = VR(version='2018-03-19',iam_api_key='0hKBk-h8hhOi9631MeFlabx28WF8N3XWMYq0DeKUNM_U')
#

def index(request):
    #espacio para el if post
    if request.method == 'POST':
        print(request.POST)
        form=articuloForm(request.POST, request.FILES)
        
        formTemporal=form.save(commit=False) #Con esto obtengo el objeto, luego puedo acceder
                                        #a los atributos de la forma tipica.
        #formTemporal.analisis="Holi" #Redefinicion de los atributos.
        formTemporal.analiticas="Holix2" #Redefinicion de los atributos.
        

        #clasificar imagen
        clase,valor = clasificarImagen(request.FILES['foto'])
        #print(clase,valor)

        formTemporal.analisis=str(clase) + " : " + str(valor) #Redefinicion de los atributos.


        #clasificar  descripcion.

        formTemporal.save()

        '''
        Antes de guardar el archivo, podría ubicar un nuevo atributo en la clase de tal forma
        que la validacion se haga al publicarse y no al listarse cada vez en la pagina.

        Si la validacion se hace al publicarse entonces debe haber un nuevo atributo llamado validacion.
        Este atributo contiene el analisis de la imagen.
        '''
      
    #cuando ocurre un get, osea cuando ingresamos a la pagina

    #Espacio para la instacia de articuloform
    inhtmlform = articuloForm()
    articulos = venta_articulo.objects.all()


    
    #el objeto que esta en la bd
    context={'objeto':inhtmlform, 'articulo':articulos }

    return render(request, 'visualrec/index.html', context)

def clasificarImagen(imagenTarget):
    resultadoClasif = ApiVr.classify(imagenTarget, threshold='0.6',classifier_ids='DefaultCustomModel_152343211')
    jsonresult = json.dumps(resultadoClasif,indent=2)
    #print(type(jsonresult))
    with open("data_file.json", "w") as write_file:
        json.dump(resultadoClasif, write_file)

    #print(jsonresult)
    #print(resultadoClasif)
    try:
        #print("Clase: ",resultadoClasif['images'][0]['classifiers'][0]['classes'][0]['class'])
        #print("Porcentaje: ",resultadoClasif['images'][0]['classifiers'][0]['classes'][0]['score'])
        clase = resultadoClasif['images'][0]['classifiers'][0]['classes'][0]['class']
        valor= resultadoClasif['images'][0]['classifiers'][0]['classes'][0]['score']
    except Exception as e:
        print(e)
    #print("Porcentaje: ",jsonresult['images'][0]['classifiers'][0]['classes'][0]['score']) No funciona
    return clase,valor

def clasificarDescripcion():
    pass

def ver_item_view(request, id_producto):
    #obj=articuloForm.objetcs.get(id=id_producto)
    
    try:
        #id_producto=1
        obj = venta_articulo.objects.get(id=id_producto)   
        #articulos = venta_articulo.objects.all()
        #print(articulos)
        #obj=articulos[id_producto]
        #print(obj)

    except Exception as e:
        print("La consulta no exite", e)
        msj="Error en la consulta, no existe el item."
    return render(request, 'visualrec/ver_item.html', locals())

def ingresar(request):
    
    if request.method=='POST':
        formulario=login_form(request.POST)
        if formulario.is_valid():
            user=formulario.cleaned_data['usuario']
            passw=formulario.cleaned_data['clave']
            usuario=authenticate(username=user,password=passw)
            if usuario is not None and usuario.is_active:
                login(request,usuario)
                return redirect('/miwatson/publicar/')
            else:
                msj="No se pudo iniciar sesion."
    formulario=login_form()
    return render(request,'visualrec/login.html',locals())


def salido(request):
    logout(request)
    return redirect('/miwatson/login/')
    #return render(request,'visualrec/logout.hml',locals())

def listar(request):
    inhtmlform = articuloForm()
    articulos = venta_articulo.objects.all()
    #el objeto que esta en la bd
    context={'objeto':inhtmlform, 'articulo':articulos }
    return render(request, 'visualrec/listar.html', context)

def registrar_view(request):
    formulario=registrar_usuario_form()
    if request.method=='POST':
        formulario=registrar_usuario_form(request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data['usuario']
            correo=formulario.cleaned_data['correo']
            password_1=formulario.cleaned_data['password_1']
            password_2=formulario.cleaned_data['password_2']
            usr=User.objects.create_user(username=usuario, email=correo, password=password_1)
            usr.save()
            return render(request, 'visualrec/gracias_por_registrarse.html')
        else:
            return render(request,'visualrec/registrar.html',locals())
    return render(request, 'visualrec/registrar.html', locals())

def servicio_web(request):
    #data=serializers.serialize('json', venta_articulo.objects.filter(status=True))
    data=serializers.serialize('json', venta_articulo.objects.all())
    return HttpResponse(data,content_type='application/json')