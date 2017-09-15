
$(document).ready(function(){
    $('.btn-get').click(function() {
        $('.output').text(function() {
            vkApiTest.vkApiTest()
        })
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
