require(['jquery', 'mockup-patterns-modal'], function($, Modal) {
  $(document).ready(function() {
    $('#formfield-form-widgets-image').each(function() {
      $(this)
        .children('.pat-relateditems')
        .on('select2-loaded', function() {
          $('.image-modal').each(function(i, el) {
            var modal = new Modal($(el), {
              backdropOptions: {
                closeOnEsc: true,
                closeOnClick: true,
                zIndex: '10000',
                opacity: '0.90',
              },
              templateOptions: {
                classBodyName: 'plone-modal-body image-modal',
              },
              content: '#content',
              loadLinksWithinModal: false,
            });
            modal.on('shown', function() {
              $('.plone-modal-body > div > div > figure > a').removeAttr(
                'href'
              );
            });
            modal.on('after-render', function() {
              $(
                '.plone-modal-header > a.plone-modal-close, .plone-modal-footer > a.plone-modal-close, .plone-modal-body > div > div > figure > a',
                self.$modal
              )
                .off('click')
                .on('click', function(e) {
                  e.stopPropagation();
                  e.preventDefault();
                  $(e.target).trigger('destroy.plone-modal.patterns');
                });
            });
          });
        });
    });
  });
});
