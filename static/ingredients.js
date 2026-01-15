const ingredientCards = document.querySelectorAll('.ingredient-card');
const findBtn = document.getElementById('findBtn');
const loader = document.getElementById('loader');
const dishList = document.getElementById('dishList');

let selectedIngredients = [];

// Выбор ингредиентов (checkbox)
ingredientCards.forEach(card => {
  card.addEventListener('click', () => {
    const ingredient = card.dataset.ingredient;

    card.classList.toggle('active');

    if (selectedIngredients.includes(ingredient)) {
      selectedIngredients = selectedIngredients.filter(i => i !== ingredient);
    } else {
      selectedIngredients.push(ingredient);
    }
  });
});

// Поиск блюд
findBtn.addEventListener('click', () => {
  if (selectedIngredients.length === 0) {
    alert('Выберите хотя бы один ингредиент');
    return;
  }

  dishList.innerHTML = '';
  loader.style.display = 'flex';

  // имитация backend-запроса
  setTimeout(() => {
    loader.style.display = 'none';
    renderDishes();
  }, 1500);
});

// Мок данные блюд
function renderDishes() {
  const dishes = [
    {
      name: 'Жареная картошка',
      desc: 'Картошка, лук, масло',
      image: 'https://images.unsplash.com/photo-1585238342028-4bbc5b5f9c8a'
    },
    {
      name: 'Курица с овощами',
      desc: 'Курица, морковь, лук',
      image: 'https://images.unsplash.com/photo-1604909052573-8f7ecfc69b4e'
    },
    {
      name: 'Овощной салат',
      desc: 'Картошка, морковь, лук',
      image: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1'
    }
  ];

  dishes.forEach(dish => {
    const card = document.createElement('div');
    card.className = 'dish-card';
    card.innerHTML = `
      <img src="${dish.image}" alt="${dish.name}">
      <div class="dish-info">
        <h3>${dish.name}</h3>
        <p>${dish.desc}</p>
      </div>
    `;
    dishList.appendChild(card);
  });
}
