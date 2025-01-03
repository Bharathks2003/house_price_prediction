document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        const inputs = form.querySelectorAll('input[type="text"]');
        let valid = true;

        inputs.forEach(input => {
            if (input.value.trim() === '') {
                valid = false;
                input.style.border = '1px solid red';
            } else {
                input.style.border = '1px solid #ddd';
            }
        });

        if (!valid) {
            event.preventDefault();
            alert('Please fill in all fields');
        }
    });
});
