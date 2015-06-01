import json
from django.http import HttpResponseNotFound, HttpResponse
from encuestas.models.encuesta import Encuesta

def exportar_encuesta(request, id_encuesta):
    encuesta = None
    try:
        encuesta = Encuesta.objects.get(id_encuesta)
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
