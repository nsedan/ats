// Workout sorting
$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);

    let selectedVal = selector.val();
    if (selectedVal != "reset") {
        let sort = selectedVal.split("_")[0];
        let direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

// Remove from cart
$('.remove-item').click(function (e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).attr('id').split('remove_')[1];
    let url = `/cart/remove/${itemId}/`;
    let data = { 'csrfmiddlewaretoken': csrfToken };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})


// Review system
$('#div_id_rating').hide()
$('#1rat').on('click', function(){
    $('.fa-dumbbell').removeClass('checked')
    $(this).addClass('checked')
    $('#id_rating').val('1')
})
$('#2rat').on('click', function(){
    $('.fa-dumbbell').removeClass('checked')
    $(this).addClass('checked')
    $('#1rat').addClass('checked')
    $('#id_rating').val('2')
})
$('#3rat').on('click', function(){
    $('.fa-dumbbell').removeClass('checked')
    $(this).addClass('checked')
    $('#1rat').addClass('checked')
    $('#2rat').addClass('checked')
    $('#id_rating').val('3')
})
$('#4rat').on('click', function(){
    $('.fa-dumbbell').removeClass('checked')
    $(this).addClass('checked')
    $('#1rat').addClass('checked')
    $('#2rat').addClass('checked')
    $('#3rat').addClass('checked')
    $('#id_rating').val('4')
})
$('#5rat').on('click', function(){
    $('.fa-dumbbell').removeClass('checked')
    $(this).addClass('checked')
    $('#1rat').addClass('checked')
    $('#2rat').addClass('checked')
    $('#3rat').addClass('checked')
    $('#4rat').addClass('checked')
    $('#id_rating').val('5')
})