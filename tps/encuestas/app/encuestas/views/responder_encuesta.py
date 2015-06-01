import uuid
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from encuestas.models.link import Link


def responder_encuesta(request):
    link_hash = request.GET.get('ref', None)

    if link_hash is None:
        return HttpResponseNotFound()

    link = None
    try:
        link = Link.objects.get(id=uuid.UUID(int=link_hash))
    except:
        return HttpResponseNotFound()

    if link.visitado:
        return HttpResponseNotFound()

    link.visitado = True
    link.save()

    request.session['link_hash'] = link_hash
    redirect("/static/responder_encuesta.html#/api/v1/encuesta/%d" % (link.encuesta.id,))
