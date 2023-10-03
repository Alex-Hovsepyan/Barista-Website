function burger(e){
    const elem = e.currentTarget;
    const header = document.querySelector('.header_container')
    
    switch(elem.className){
        case 'burger':
            elem.classList.add('burger_active')
            header.classList.add('active_header_container')
            setTimeout(() => {
                elem.classList.add('burger_active_rotate')
            }, 300);
            break

        default : {
            header.classList.remove('active_header_container')
            elem.classList.remove('burger_active_rotate')
            setTimeout(() => {
                elem.classList.remove('burger_active')
            }, 300);
        }
    }
}

window.onscroll = () => {
    console.log(window.scrollY);
    const header = document.querySelector('.header_container')
    const list = document.querySelectorAll('nav ul li')
    const active = document.querySelector('.active')
    if(window.scrollY >= 80){
        header.style.backgroundColor = '#000000A6'
    }
    else {
        header.style.backgroundColor = '#00000059'
    }
}