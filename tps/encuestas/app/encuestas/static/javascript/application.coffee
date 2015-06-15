is_data_new = (data) =>
    data.id == "None" || data.id == "new" || data.id == undefined

get_url = (base_url, data) =>
    if !is_data_new(data)
        return "#{base_url}#{data.id}"
    base_url

guardar = (url, data, callback) =>
    method = "PUT"
    if is_data_new(data)
        method = "POST"
        delete data.id

    $.ajax
        url: get_url(url, data)
        data: JSON.stringify data
        type: method
        accepts: "json"
        contentType: "application/json"
        success: callback

crear_usuario = (jsEvent) =>
    mail = $('#userMail').val()
    guardar "/api/v1/user/", {mail: mail}, (data) ->
        $select = $('select.usuarios')
        $new_user = $("<option/>", {value: data.id, text: mail})
        $select.append($new_user)
        $select.val($select.val().concat([data.id])).trigger("change")
        $('#userMail').val('')
        $('#crearUsuario').modal('hide')

crear_grupo = (jsEvent) =>
    nombre = $('#nombreGrupo').val()
    tab_id = $('ul.grupos li').size() + 1

    $("<li role='presentation'>" +
        "<a href='#grupo_#{tab_id}' role='tab' data-toggle='tab' aria-controls='grupo_#{tab_id}'>#{nombre}" +
        "</a></li>"
    ).appendTo('ul.grupos')
    $("<div class='tab-pane' id='grupo_#{tab_id}'>" +
        "<br>" +
        "<button class='btn btn-primary btn-sm pull-right agregar-pregunta' type='button' data-toggle='modal' data-target='#crearPregunta' data-grupo-id='#{tab_id}'>Agregar Pregunta</button>" +
        "<input class='grupo-id' type='hidden' value='new'>" +
        "<input class='grupo-nombre' type='hidden' value='#{nombre}'>" +
        "<table class='table table-striped table-bordered'>" +
          "<thead>" +
            "<tr>" +
              "<th width='80%'>Pregunta</th>" +
              "<th>Opciones</th>" +
              "<th>Acciones</th>" +
            "</tr></thead><tbody></tbody>"
    ).appendTo('div.grupos')
    $('ul.grupos a:last').tab('show')
    $('#nombreGrupo').val('')
    $('#crearGrupo').modal('hide')

crear_pregunta = (jsEvent) =>
    pregunta = $('#preguntaText').val()
    grupo_id = $('.grupos .tab-pane.active').attr('id')
    opciones = []
    $.each $('input.opcion'), (i, opcion) ->
        if opcion != ""
            opciones.push($(opcion).val())

    $('preguntaText').val('')
    while $('.form-group.opcion').size() > 1
        $('.form-group.opcion:last').remove()

    $('.form-group.opcion input.opcion').val('')

    $('#crearPregunta').modal('hide')

    $("<tr>" +
        "<td class='hidden pregunta-id'>new</td>" +
        "<td class='pregunta'>#{pregunta}</td>" +
        "<td>#{opciones.length}</td>" +
        "<td><a href='#'>Editar</a></td>" +
        "<td><a href='#'>Eliminar</a></td>" +
        "<td class='hidden opciones'>" +
          $.map(opciones, (opcion) ->
              "<span class='opcion'>" +
                  "<span class='opcion-text'>#{opcion}</span>" +
                  "<span class='opcion-id'>new</span>" +
              "</span>"
          ) +
        "</td></tr>").appendTo("##{grupo_id} table tbody")

agregar_opcion = (jsEvent) =>
    $('.form-group.opcion:first').clone().appendTo('#crearPregunta form')

guardar_opciones = (encuesta_id, $pregunta, id_pregunta, callback) =>
    $opciones = $pregunta.find('td.opciones span.opcion')
    $.each $opciones, (i, opcion) ->
        $opcion = $(opcion)
        opcion = {
            pregunta: "/api/v1/pregunta/#{id_pregunta}/"
            id: $opcion.find('.opcion-id').text()
            opcion: $opcion.find('.opcion-text').text()
        }
        guardar "/api/v1/opcion/", opcion, (data) ->
            callback(encuesta_id)

guardar_preguntas = (encuesta_id, $grupo, id_grupo, callback) =>
    $preguntas = $grupo.find('table tbody tr')
    $.each $preguntas, (i, pregunta) ->
        $pregunta = $(pregunta)
        pregunta = {
            grupo: "/api/v1/grupo/#{id_grupo}/"
            id: $pregunta.find('td.pregunta-id').text()
            pregunta: $pregunta.find('td.pregunta').text()
        }

        guardar "/api/v1/pregunta/", pregunta, (data) ->
            guardar_opciones(encuesta_id ,$pregunta, data.id, callback)

guardar_grupos = (encuesta_id, callback) =>
    $grupos = $('.tab-content.grupos .tab-pane')
    $.each $grupos, (i, grupo) ->
        $grupo = $(grupo)
        grupo = {
            encuesta: "/api/v1/encuesta/#{encuesta_id}/"
            id: $grupo.find('.grupo-id').val()
            nombre: $grupo.find('.grupo-nombre').val()
        }

        guardar "/api/v1/grupo/", grupo, (data) ->
            guardar_preguntas(encuesta_id, $grupo, data.id, callback)

guardar_encuesta = (callback) =>
    $usuarios = $('select.usuarios').find(':selected')
    encuesta = {
        id: $('input.id-encuesta').val()
        nombre: $('#nombre').val()
        fecha_expiracion: $('#fecha_expiracion').val()
        descripcion: $('#descripcion').val()
        usuarios: $.map $usuarios, (user) ->
            "/api/v1/user/#{$(user).val()}/"
    }

    guardar "/api/v1/encuesta/", encuesta, (data) ->
        guardar_grupos(data.id, callback)

guardar_y_volver = () =>
    guardar_encuesta (encuesta_id) ->
        window.location = "/encuestas/"

vista_previa = () =>
    guardar_encuesta (encuesta_id) ->
        window.location = "/vista_previa/#{encuesta_id}/"

enviar = () =>
    guardar_encuesta (encuesta_id) ->
        window.location = "/enviar/#{encuesta_id}/"

$ ->
    $('select.usuarios').select2()

    $('button.crear-usuario').on('click', crear_usuario)
    $('button.crear-grupo').on('click', crear_grupo)
    $('button.crear-pregunta').on('click', crear_pregunta)
    $('button.agregar-opcion').on('click', agregar_opcion)
    $('button.enviar').on('click', enviar)
    $('button.vista-previa').on('click', vista_previa)
    $('button.guardar').on('click', guardar_y_volver)
