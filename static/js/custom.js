document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('[data-title-template]').forEach(function(element) {
        var titleTemplate = element.getAttribute('data-title-template');
        var title = titleTemplate.replace(/<br>/g, '\n');
        element.setAttribute('data-title', title);
    });
});