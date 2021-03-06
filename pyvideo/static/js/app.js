function start_sync() {

    $.ajax({
        url: "/sync",
        beforeSend: function() {
            $(".sync_button")
                .notify("Syncing started", "success");
        },
        success: function (data) {
            if (data["reload"]) {
                $.notify("Syncing finished.\nReloading in 2 seconds", "success");
                setTimeout(function() { location.reload() }, 2000);
            } else {
                $.notify("Nothing new is there. Finished", "success");
            }
        }
    })
}


$(document).ready(function() {
    table = $('#videos').DataTable({
        "data": dataMovies,
        "columns": [
            {"title": "Added", "searchable": false},
            {"title": "Title"},
            {"title": "Converence"},
            {"title": "Video URL", "searchable": false, "orderable": false},
        ],
        "deferRender": true,
    });

    $('.simple-ajax-popup').magnificPopup({
        type: 'ajax',
    });

} );


function change_state(field, video_id) {
    $.ajax({
        url: "/change_state?field="+field+"&id="+video_id,
        beforeSend: function () {
            $.magnificPopup.close();
        },
        success: function(data) {
            $.notify(field+" changed to: " + data["new"], "success")
            post_change();
        },
        error: function(data){
            $.notify(data["msg"])
        }
    })
}