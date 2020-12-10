
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#username').onclick =
        function () {
            var menu = document.querySelector(".user_options");
            if (menu.style.display == 'block') {
                menu.style.display = 'none';
            }
            else {
                menu.style.display = 'block';
            }
        };

    document.querySelector('#delete_link').onclick =
        function () {
            var menu = document.querySelectorAll(".link_cancel");
            if (menu[0].style.opacity == 0) {
                for (var i = 0; i < menu.length; i++) {
                    menu[i].style.opacity = 1;
                    menu[i].style.pointerEvents = "none";
                }
            }
            else {
                for (var i = 0; i < menu.length; i++) {
                    menu[i].style.opacity = 0;
                    menu[i].style.pointerEvents = "auto";
                }
            }
        };
});
