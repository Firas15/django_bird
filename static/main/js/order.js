document.addEventListener('DOMContentLoaded', function() {
        const form = document.getElementById('orderForm');
        const successMessage = document.getElementById('successMessage');
        const orderNumber = document.getElementById('orderNumber');
        const submitBtn = document.getElementById('submitBtn');

        // Регулярные выражения для валидации
        const patterns = {
            phone: /^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$/,
            email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            telegram: /^[a-zA-Z0-9_]{5,32}$/,
            name: /^[a-zA-Zа-яА-ЯёЁ\s\-]{2,50}$/
        };

        // Функция показа ошибки
        function showError(fieldId, messageId, show = true) {
            const field = document.getElementById(fieldId);
            const error = document.getElementById(messageId);

            if (show) {
                field.classList.add('error');
                field.classList.remove('success');
                error.classList.add('show');
            } else {
                field.classList.remove('error');
                error.classList.remove('show');

                // Если поле заполнено правильно, показываем успех
                if (field.value.trim()) {
                    field.classList.add('success');
                }
            }
        }

        // Валидация отдельных полей
        function validateField(fieldId, pattern = null, minLength = null) {
            const field = document.getElementById(fieldId);
            const value = field.value.trim();
            const isRequired = field.hasAttribute('required');

            // Если поле необязательное и пустое - пропускаем
            if (!isRequired && !value) {
                showError(fieldId, `${fieldId}-error`, false);
                return true;
            }

            // Проверка минимальной длины
            if (minLength && value.length < minLength) {
                showError(fieldId, `${fieldId}-error`, true);
                return false;
            }

            // Проверка по регулярному выражению
            if (pattern && !pattern.test(value)) {
                showError(fieldId, `${fieldId}-error`, true);
                return false;
            }

            // Проверка email
            if (fieldId === 'email' && !patterns.email.test(value)) {
                showError(fieldId, `${fieldId}-error`, true);
                return false;
            }

            // Проверка выпадающего списка
            if (field.tagName === 'SELECT' && !value) {
                showError(fieldId, `${fieldId}-error`, true);
                return false;
            }

            // Все проверки пройдены
            showError(fieldId, `${fieldId}-error`, false);
            return true;
        }

        // Валидация всей формы
        function validateForm() {
            let isValid = true;

            // Проверяем каждое поле
            if (!validateField('topic')) isValid = false;
            if (!validateField('name', patterns.name, 2)) isValid = false;
            if (!validateField('email', patterns.email)) isValid = false;
            if (!validateField('phone', patterns.phone)) isValid = false;
            if (!validateField('telegram', patterns.telegram)) isValid = false;
            if (!validateField('message', null, 20)) isValid = false;

            return isValid;
        }

        // События ввода для live-валидации
        const fields = ['topic', 'name', 'email', 'phone', 'telegram', 'message'];
        fields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (field) {
                field.addEventListener('blur', function() {
                    if (fieldId === 'phone') {
                        validateField(fieldId, patterns.phone);
                    } else if (fieldId === 'email') {
                        validateField(fieldId, patterns.email);
                    } else if (fieldId === 'telegram') {
                        validateField(fieldId, patterns.telegram);
                    } else if (fieldId === 'name') {
                        validateField(fieldId, patterns.name, 2);
                    } else if (fieldId === 'message') {
                        validateField(fieldId, null, 20);
                    } else {
                        validateField(fieldId);
                    }
                });

                field.addEventListener('input', function() {
                    // Убираем ошибку при вводе
                    showError(fieldId, `${fieldId}-error`, false);
                });
            }
        });

        // Обработчик отправки формы
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Валидируем форму
            if (!validateForm()) {
                // Прокрутка к первой ошибке
                const firstError = document.querySelector('.error');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstError.focus();
                }
                return;
            }

            // Блокируем кнопку отправки
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Отправка...';

            // Собираем данные формы
            const formData = {
                topic: document.getElementById('topic').value,
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value || 'Не указан',
                telegram: document.getElementById('telegram').value ?
                         '@' + document.getElementById('telegram').value : 'Не указан',
                message: document.getElementById('message').value,
                timestamp: new Date().toISOString()
            };

            // Генерируем номер заказа
            const randomNum = 'EMP-' + Date.now().toString().slice(-8);
            orderNumber.textContent = randomNum;

            // Имитация отправки на сервер (3 секунды)
            setTimeout(function() {
        // Меняем заголовок на "Готово!"
        const orderHeader = document.getElementById('orderHeader');
        const headerTitle = document.getElementById('headerTitle');
        const headerSubtitle = document.getElementById('headerSubtitle');

        // Добавляем класс для анимации
        orderHeader.classList.add('header-success');

        // Меняем содержимое заголовка
        orderHeader.innerHTML = `
            <div class="success-icon">✓</div>
            <h1>Готово!</h1>
            <p>Ваш заказ успешно оформлен. Мы свяжемся с вами в течение 24 часов.</p>
        `;

        // Показываем сообщение об успехе
        form.style.display = 'none';
        successMessage.style.display = 'block';

        // Прокрутка к сообщению
        successMessage.scrollIntoView({ behavior: 'smooth' });

        // Логируем данные
        console.log('Форма отправлена:', formData);
        console.log('Номер заказа:', randomNum);
    }, 2000);
        });

        // Автоматическое форматирование телефона
        const phoneInput = document.getElementById('phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function(e) {
                let value = e.target.value.replace(/\D/g, '');

                if (value.startsWith('8')) {
                    value = '+7' + value.slice(1);
                }

                if (value.length > 1) {
                    let formatted = '+7';

                    if (value.length > 1) {
                        formatted += ' (' + value.slice(1, 4);
                    }
                    if (value.length >= 5) {
                        formatted += ') ' + value.slice(4, 7);
                    }
                    if (value.length >= 8) {
                        formatted += '-' + value.slice(7, 9);
                    }
                    if (value.length >= 10) {
                        formatted += '-' + value.slice(9, 11);
                    }

                    e.target.value = formatted;
                }
            });
        }
    });