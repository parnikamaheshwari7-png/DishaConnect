document.addEventListener("DOMContentLoaded", function () {

    const disclaimerModal = new bootstrap.Modal(
        document.getElementById("disclaimerModal")
    );

   // disclaimerModal.show();

    const agreeCheck = document.getElementById("agreeCheck");
    const continueBtn = document.getElementById("continueBtn");

    agreeCheck.addEventListener("change", function () {

        continueBtn.disabled = !this.checked;

    });

});