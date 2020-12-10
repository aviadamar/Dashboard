
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#username').onclick =
        function () {
            var menu = document.querySelector(".user_options");
            if (menu.style.display === 'block') {
                menu.style.display = 'none';
            }
            else {
                menu.style.display = 'block';
            }
        };

    document.querySelector('#delete_link').onclick =
        function () {
            var menu = document.querySelectorAll(".link_cancel");
            if (menu[0].style.display === 'block') {
                for (var i = 0; i < menu.length; i++) {
                    menu[i].style.display = 'none';
                }
            }
            else {
                for (var i = 0; i < menu.length; i++) {
                    menu[i].style.display = 'block';
                }
            }
        };
});
