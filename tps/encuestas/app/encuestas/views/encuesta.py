import uuid
import json
from django.http import HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from encuestas.models.link import Link
from encuestas.models.encuesta import Encuesta
from encuestas.models.user import User


@login_required
def listar_encuestas(request):
    return render(request, "encuestas", {
        'encuestas': Encuesta.objects.all()
    })


@login_required
def editar_encuesta(request, id_encuesta):
    return render(request, "editar_encuesta", {
        'encuesta': Encuesta.objects.get(id=id_encuesta),
        'users': User.objects.all()
    })


@login_required
def nueva_encuesta(request):
    return render(request, "editar_encuesta", {
        'encuesta': Encuesta(),
        'users': User.objects.all()
    })


@login_required
def eliminar_encuesta(request, id_encuesta):
    encuesta = None
    try:
        encuesta = Encuesta.objects.get(id=id_encuesta)
    except:
        return HttpResponseNotFound()

    try:
        encuesta.delete()
        return HttpResponse(status=204)
    except:
        return HttpResponse(status=422)


@login_required
def exportar_encuesta(request, id_encuesta):
    encuesta = None
    try:
        encuesta = Encuesta.objects.get(id=id_encuesta)
    except:
        return HttpResponseNotFound()

    try:
        export = json.dumps(encuesta.exportar(), sort_keys=True, indent=2, separators=(',', ': '))
    except:
        return HttpResponse("Encuesta no finalizada", status=403)

    response = HttpResponse(content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="%s.json"' % (encuesta.nombre,)
    response.write(export)

    return response


@login_required
def vista_previa_encuesta(request, id_encuesta):
    encuesta = None
    try:
        encuesta = Encuesta.objects.get(id=id_encuesta)
    except:
        return HttpResponseNotFound()

    return render(request, "vista_previa", {
        'encuesta': encuesta
    })


@login_required
def enviar_encuesta(request, id_encuesta):
    encuesta = None
    try:
        encuesta = Encuesta.objects.get(id=id_encuesta)
    except:
        return HttpResponseNotFound()

    encuesta.generar_links()

    return redirect("/encuestas/")


def gracias(request, link_hash):
    link = None
    try:
        link = Link.objects.get(id=uuid.UUID(int=int(link_hash)))
    except:
        return HttpResponseNotFound()

    link.finalizada = True
    link.save()

    return render(request, "encuesta_success")


def responder_encuesta(request):
    link_hash = request.GET.get('ref', None)

    if link_hash is None:
        return HttpResponseNotFound()

    link = None
    try:
        link = Link.objects.get(id=uuid.UUID(int=int(link_hash)))
    except:
        return HttpResponseNotFound()

    if link.visitado:
        return HttpResponseNotFound()

    link.visitado = True
    link.save()

    request.session['link_hash'] = link_hash
    request.session['usuario_id'] = link.user.id

    return render(request, "responder_encuesta", {
        'encuesta': link.encuesta,
        'user': link.user,
        'link': link
    })
