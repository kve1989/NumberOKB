document.addEventListener('DOMContentLoaded', () => {
    let alerts = document.querySelectorAll('.alert')

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

    let form = document.querySelector('#SearchFormFromAdminPage')
    let select = form.querySelector('select')

    select.addEventListener('change', (e) => {
        form.submit();
    })


});