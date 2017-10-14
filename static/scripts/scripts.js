$(document).ready(function(){
    var form = $("#form_name")
    console.log(form)
    form.on('submit', function(event) {
        event.preventDefault()
        console.log("ok")
        var id = $('#vk_id').val()
        console.log('id: ', id)
    })

    var campagians_form = $("#campagians_form")
    console.log(campagians_form)
    campagians_form.on('submit', function(event) {
        event.preventDefault()
        console.log("ok")
        var cabinet_id = $('#cabinet_id').val()
        var camp_type = $('#camp_type').val()
        var camp_name = $('#camp_name').val()
        var day_limit = $('#day_limit').val()
        var limit = $('#limit').val()
        var start_time = $('#start_time').val()
        var stop_time = $('#stop_time').val()
        var camp_status = $('#camp_status').val()
        console.log("name:", camp_name)
        console.log("day_limit:", day_limit)
        console.log("start_time:", start_time)
    })
})

// $(function() {
//   $('.btn').click(function() {
//     $.getJSON('script.html', function(data) {
//       $('#output-box').val(data)
//     })
//     return false;
//   })
// })
