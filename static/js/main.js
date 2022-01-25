document.addEventListener('DOMContentLoaded', () => {
    var alerts = document.querySelectorAll('.alert')

    alerts.forEach( alert => {
        if (alert) {
            setTimeout(() => {
                alert.classList.remove('show')
                alert.classList.add('hide')
                setTimeout(() => {
                    alert.remove();
                },300)
            }, 3000)
        }
    } )



});