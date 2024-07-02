document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        fetch('/sumar', {
            method: 'POST',
            body: new FormData(document.querySelector('form'))
        })
        .then(response => response.text())
        .then(data => {
            document.querySelector('body').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
        return false;
    };
});
