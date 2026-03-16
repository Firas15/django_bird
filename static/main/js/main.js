// Открытие галереи при клике на карточку
function openGallery(serviceType) {
    const galleryModal = document.getElementById('galleryModal');
    const galleryContent = document.getElementById('galleryContent');



    galleryContent.innerHTML = '';

    images.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image;
        imgElement.alt = 'Gallery Image';
        imgElement.style.width = '100%';
        imgElement.style.marginBottom = '10px';
        galleryContent.appendChild(imgElement);
    });

    galleryModal.style.display = 'block';
}

// Закрытие галереи
function closeGallery() {
    const galleryModal = document.getElementById('galleryModal');
    galleryModal.style.display = 'none';  // Скрываем модальное окно
}



// Получаем кнопки и форму
const orderBtn = document.getElementById('order-btn');
const portfolioBtn = document.getElementById('portfolio-btn');
const orderForm = document.getElementById('order-form');

// Обработчик для кнопки "Заказать вышивку"
orderBtn.addEventListener('click', function (e) {
    e.preventDefault(); // Останавливаем стандартное поведение ссылки

    // Переключаем активность кнопки "Заказать вышивку"
    orderBtn.classList.add('active');
    portfolioBtn.classList.remove('active');

    // Показываем форму для заказа
    orderForm.style.display = 'block';
});

// Обработчик для кнопки "Портфолио"
portfolioBtn.addEventListener('click', function (e) {
    e.preventDefault(); // Останавливаем стандартное поведение ссылки

    // Переключаем активность кнопки "Портфолио"
    portfolioBtn.classList.add('active');
    orderBtn.classList.remove('active');

    // Прячем форму для заказа
    orderForm.style.display = 'none';
});


function openModal(categoryId){
    fetch(`/get-category-izdeliya/${categoryId}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById('categoryNameModal').textContent = data['category_name'];
    });
}