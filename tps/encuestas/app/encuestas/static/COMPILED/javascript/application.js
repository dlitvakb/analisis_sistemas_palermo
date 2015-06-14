(function() {
  var crear_grupo, crear_usuario,
    _this = this;

  crear_usuario = function(jsEvent) {
    var mail;
    mail = $('#userMail').val();
    return $.ajax({
      url: "/api/v1/user/",
      data: JSON.stringify({
        mail: mail
      }),
      type: "POST",
      accepts: "json",
      contentType: "application/json",
      success: function(data) {
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
      }
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

  $(function() {
    $('select.usuarios').select2();
    $('button.crear-usuario').on('click', crear_usuario);
    return $('button.crear-grupo').on('click', crear_grupo);
  });

}).call(this);
