(function() {
  var agregar_opcion, crear_grupo, crear_pregunta, crear_usuario, enviar, get_url, guardar, guardar_encuesta, guardar_grupos, guardar_opciones, guardar_preguntas, guardar_y_volver, is_data_new, vista_previa,
    _this = this;

  is_data_new = function(data) {
    return data.id === "None" || data.id === "new" || data.id === void 0;
  };

  get_url = function(base_url, data) {
    if (!is_data_new(data)) return "" + base_url + data.id;
    return base_url;
  };

  guardar = function(url, data, callback) {
    var method;
    method = "PUT";
    if (is_data_new(data)) {
      method = "POST";
      delete data.id;
    }
    return $.ajax({
      url: get_url(url, data),
      data: JSON.stringify(data),
      type: method,
      accepts: "json",
      contentType: "application/json",
      success: callback
    });
  };

  crear_usuario = function(jsEvent) {
    var mail;
    mail = $('#userMail').val();
    return guardar("/api/v1/user/", {
      mail: mail
    }, function(data) {
      var $new_user, $select;
      $select = $('select.usuarios');
      $new_user = $("<option/>", {
        value: data.id,
        text: mail
      });
      $select.append($new_user);
      $select.val($select.val().concat([data.id])).trigger("change");
      $('#userMail').val('');
      return $('#crearUsuario').modal('hide');
    });
  };

  crear_grupo = function(jsEvent) {
    var nombre, tab_id;
    nombre = $('#nombreGrupo').val();
    tab_id = $('ul.grupos li').size() + 1;
    $("<li role='presentation'>" + ("<a href='#grupo_" + tab_id + "' role='tab' data-toggle='tab' aria-controls='grupo_" + tab_id + "'>" + nombre) + "</a></li>").appendTo('ul.grupos');
    $(("<div class='tab-pane' id='grupo_" + tab_id + "'>") + "<br>" + ("<button class='btn btn-primary btn-sm pull-right agregar-pregunta' type='button' data-toggle='modal' data-target='#crearPregunta' data-grupo-id='" + tab_id + "'>Agregar Pregunta</button>") + "<input class='grupo-id' type='hidden' value='new'>" + ("<input class='grupo-nombre' type='hidden' value='" + nombre + "'>") + "<table class='table table-striped table-bordered'>" + "<thead>" + "<tr>" + "<th width='80%'>Pregunta</th>" + "<th>Opciones</th>" + "<th>Acciones</th>" + "</tr></thead><tbody></tbody>").appendTo('div.grupos');
    $('ul.grupos a:last').tab('show');
    $('#nombreGrupo').val('');
    return $('#crearGrupo').modal('hide');
  };

  crear_pregunta = function(jsEvent) {
    var grupo_id, opciones, pregunta;
    pregunta = $('#preguntaText').val();
    grupo_id = $('.grupos .tab-pane.active').attr('id');
    opciones = [];
    $.each($('input.opcion'), function(i, opcion) {
      if (opcion !== "") return opciones.push($(opcion).val());
    });
    $('preguntaText').val('');
    while ($('.form-group.opcion').size() > 1) {
      $('.form-group.opcion:last').remove();
    }
    $('.form-group.opcion input.opcion').val('');
    $('#crearPregunta').modal('hide');
    return $("<tr>" + "<td class='hidden pregunta-id'>new</td>" + ("<td class='pregunta'>" + pregunta + "</td>") + ("<td>" + opciones.length + "</td>") + "<td><a href='#'>Editar</a></td>" + "<td><a href='#'>Eliminar</a></td>" + "<td class='hidden opciones'>" + $.map(opciones, function(opcion) {
      return "<span class='opcion'>" + ("<span class='opcion-text'>" + opcion + "</span>") + "<span class='opcion-id'>new</span>" + "</span>";
    }) + "</td></tr>").appendTo("#" + grupo_id + " table tbody");
  };

  agregar_opcion = function(jsEvent) {
    return $('.form-group.opcion:first').clone().appendTo('#crearPregunta form');
  };

  guardar_opciones = function(encuesta_id, $pregunta, id_pregunta, callback) {
    var $opciones;
    $opciones = $pregunta.find('td.opciones span.opcion');
    return $.each($opciones, function(i, opcion) {
      var $opcion;
      $opcion = $(opcion);
      opcion = {
        pregunta: "/api/v1/pregunta/" + id_pregunta + "/",
        id: $opcion.find('.opcion-id').text(),
        opcion: $opcion.find('.opcion-text').text()
      };
      return guardar("/api/v1/opcion/", opcion, function(data) {
        return callback(encuesta_id);
      });
    });
  };

  guardar_preguntas = function(encuesta_id, $grupo, id_grupo, callback) {
    var $preguntas;
    $preguntas = $grupo.find('table tbody tr');
    return $.each($preguntas, function(i, pregunta) {
      var $pregunta;
      $pregunta = $(pregunta);
      pregunta = {
        grupo: "/api/v1/grupo/" + id_grupo + "/",
        id: $pregunta.find('td.pregunta-id').text(),
        pregunta: $pregunta.find('td.pregunta').text()
      };
      return guardar("/api/v1/pregunta/", pregunta, function(data) {
        return guardar_opciones(encuesta_id, $pregunta, data.id, callback);
      });
    });
  };

  guardar_grupos = function(encuesta_id, callback) {
    var $grupos;
    $grupos = $('.tab-content.grupos .tab-pane');
    return $.each($grupos, function(i, grupo) {
      var $grupo;
      $grupo = $(grupo);
      grupo = {
        encuesta: "/api/v1/encuesta/" + encuesta_id + "/",
        id: $grupo.find('.grupo-id').val(),
        nombre: $grupo.find('.grupo-nombre').val()
      };
      return guardar("/api/v1/grupo/", grupo, function(data) {
        return guardar_preguntas(encuesta_id, $grupo, data.id, callback);
      });
    });
  };

  guardar_encuesta = function(callback) {
    var $usuarios, encuesta;
    $usuarios = $('select.usuarios').find(':selected');
    encuesta = {
      id: $('input.id-encuesta').val(),
      nombre: $('#nombre').val(),
      fecha_expiracion: $('#fecha_expiracion').val(),
      descripcion: $('#descripcion').val(),
      usuarios: $.map($usuarios, function(user) {
        return "/api/v1/user/" + ($(user).val()) + "/";
      })
    };
    return guardar("/api/v1/encuesta/", encuesta, function(data) {
      return guardar_grupos(data.id, callback);
    });
  };

  guardar_y_volver = function() {
    return guardar_encuesta(function(encuesta_id) {
      return window.location = "/encuestas/";
    });
  };

  vista_previa = function() {
    return guardar_encuesta(function(encuesta_id) {
      return window.location = "/vista_previa/" + encuesta_id + "/";
    });
  };

  enviar = function() {
    return guardar_encuesta(function(encuesta_id) {
      return window.location = "/enviar/" + encuesta_id + "/";
    });
  };

  $(function() {
    $('select.usuarios').select2();
    $('button.crear-usuario').on('click', crear_usuario);
    $('button.crear-grupo').on('click', crear_grupo);
    $('button.crear-pregunta').on('click', crear_pregunta);
    $('button.agregar-opcion').on('click', agregar_opcion);
    $('button.enviar').on('click', enviar);
    $('button.vista-previa').on('click', vista_previa);
    return $('button.guardar').on('click', guardar_y_volver);
  });

}).call(this);
