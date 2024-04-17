/**
 * Email Form Validation
 */
document.addEventListener('DOMContentLoaded', function () {
  var forms = document.querySelectorAll('.email-form');

  forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var formData = new FormData(form);

      var loadingMessage = form.querySelector('.loading');
      loadingMessage.classList.add('d-block');

      fetch(form.getAttribute('action'), {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          form.querySelector('.loading').classList.remove('d-block');
          form.querySelector('.error-message').classList.remove('d-block');

          form.querySelector('.sent-message').classList.add('d-block');
          form.reset();
        } else {
          throw new Error('Server response was not ok.');
        }
      })
      .catch(error => {
        form.querySelector('.loading').classList.remove('d-block');

        form.querySelector('.error-message').classList.add('d-block');
        form.querySelector('.error-message').textContent = error.message;

        console.error('Form submission error:', error);
      });
    });
  });
});
