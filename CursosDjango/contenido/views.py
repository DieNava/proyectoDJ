from django.shortcuts import render, HttpResponse
menu= """
    <a href="/">Home</a>
    <a href="/cursos">Cursos</a>  
    <a href="/contacto">Contactanos</a>  
    """

def principal(request):
    contenido= "<h1>HOLA DJANGO</h1>"  
    return HttpResponse (menu +contenido)


def principal(request):
    contenido="""
        <h1>La Escuelita</h1>
        <h2>Aquí encontrarás los mejores cursos de todo México</h2>
        """
    return HttpResponse(menu +contenido)


def cursos(request):  
    contenido="""<h2> Cursos Disponibles </h2>  
    <p>Cursos:  
        <select name="cursos">  
            <option>Base de Datos</option>  
            <option>HTML</option>  
            <option>Redes</option>  
            <option>Ciberseguridad</option>  
        </select>  
    </p>
    """ 
    return HttpResponse(menu +contenido)  

def contacto(request):  
    contenido="""<h2>Contacto</h2>   
    <p>Nombre:<input type="text" name="nombre"></p>
    <p>Correo Electronico: <input type="text" name="correo"</p> 
    <p>Cursos:
        <select name="cursos">  
            <option>Base de Datos</option>  
            <option>HTML</option>  
            <option>Redes</option>  
            <option>Ciberseguridad</option>  
        </select>  
    </p>
    <p>Comentarios:</p><p><textarea cols="50" rows="10"></textarea></p>
    <p><input type="Button" name="enviar" value="Enviar"/></p>"""  
    return HttpResponse(menu +contenido)  

