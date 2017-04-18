// $(document).ready(function($){

//     $('#langModal').modal({'show': true,'keyboard': false,'backdrop':'static',});

//     $(function(){
//         var logo = $("#logoTop");var menu1 = $("#normalMenu");
//         var menu2 = $("#overlayMenu");var isologo = $("#isotipo");
//         $(window).scroll(function(){
//             var scroll = $(window).scrollTop();
//             var dots = $('#dot-nav');
//             if (scroll >= 500){
//                 if(!menu1.hasClass("hidden")){
//                     menu1.hide();
//                     menu2.removeClass('hidden').addClass("").fadeIn( "slow");
//                 }
//             } else {
//                 if(!menu1.hasClass("hidden")){
//                     menu2.hide();
//                     // logo.hide();
//                     menu1.removeClass("hidden").addClass('').fadeIn( "slow");
//                 }
//             }
//             if (scroll >= 1300){
//                 dots.removeClass('hidden');
//             } else {
//                 dots.addClass('hidden');
//             }
//         });
//     });

//     $('#grupophx-logo').click(function(){window.location.replace('/');});

//     $('#toggle').click(function(){
//         $(this).toggleClass('active');
//         $('#overlay').toggleClass('open');
//         $('#grupophx-logo').toggleClass('active');
//     });

//     $('.frame').click(function(){
//         $('.top').addClass('open');
//         $('.message').addClass('pull');
//     })

//     $(function(){
//         $('.material-card > .mc-btn-action').click(function(){
//             var card = $(this).parent('.material-card');
//             var icon = $(this).children('i');
//             icon.addClass('fa-spin-fast');
//             if (card.hasClass('mc-active')){
//                 card.removeClass('mc-active');
//                 window.setTimeout(function(){
//                     icon.removeClass('fa-arrow-left').removeClass('fa-spin-fast').addClass('fa-bars');
//                 }, 800);
//             } else {
//                 card.addClass('mc-active');

//                 window.setTimeout(function(){
//                     icon
//                         .removeClass('fa-bars')
//                         .removeClass('fa-spin-fast')
//                         .addClass('fa-arrow-left');

//                 }, 800);
//             }
//         });
//     });

//     function setModalMaxHeight(element){
//         this.$element = $(element);
//         this.$content = this.$element.find('.modal-content');
//         var borderWidth = this.$content.outerHeight() - this.$content.innerHeight();
//         var dialogMargin = $(window).width() < 768 ? 20 : 60;
//         var contentHeight = $(window).height() - (dialogMargin + borderWidth);
//         var headerHeight  = this.$element.find('.modal-header').outerHeight() || 0;
//         var footerHeight = this.$element.find('.modal-footer').outerHeight() || 0;
//         var maxHeight = contentHeight - (headerHeight + footerHeight);

//         this.$content.css({
//             'overflow': 'hidden'
//         });

//         this.$element.find('.modal-body').css({
//             'max-height': maxHeight,
//             'overflow-y': 'auto'
//         });
//     }

//     $('.modal').on('show.bs.modal', function(){
//         $(this).show();
//         setModalMaxHeight(this);
//     });

//     $(window).resize(function(){
//         if ($('.modal.in').length != 0){
//             setModalMaxHeight($('.modal.in'));
//         }
//     });

//     $('#scroll').click(function(){$(window).animate().scrollTop(700);});
//     $('.awesome-tooltip').tooltip({
//         placement: 'left'
//     });
    

// }); // End Documen.Ready

