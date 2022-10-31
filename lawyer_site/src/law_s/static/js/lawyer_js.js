document.addEventListener("scroll", function(){
                let y = document.getElementById('menu').getBoundingClientRect().top;
                let move = document.getElementById('movable');
                 if (y == 0) {
                    move.classList.remove('transparent')}
                 else if (y !== 0 ) {move.classList.add('transparent')}
                              });
