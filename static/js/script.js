    document.addEventListener('DOMContentLoaded', function() {
      const dietaryPreferences = document.querySelectorAll('.dietary-preference');
      const findRecipesBtn = document.getElementById('find-recipes');
      const recipeResults = document.getElementById('recipe-results');
      const dishName = document.getElementById('dish-name');
      const dishInput = document.getElementById('dish');
      const loadingIndicator = document.getElementById('loading');
      const recipesContainer = document.getElementById('recipes-container');
      const healthyCheckbox = document.getElementById('healthy');
      
      let currentDietaryPreference = 'Non-Veg';
      
      // Dietary preferences handling
      dietaryPreferences.forEach(pref => {
        pref.addEventListener('click', function() {
          dietaryPreferences.forEach(p => {
            p.classList.remove('active', 'bg-yellow-500', 'text-white');
            p.classList.add('bg-yellow-100', 'text-yellow-800');
          });
          
          this.classList.remove('bg-yellow-100', 'text-yellow-800');
          this.classList.add('active', 'bg-yellow-500', 'text-white');
          currentDietaryPreference = this.getAttribute('data-pref');
        });
      });
      
  
      findRecipesBtn.addEventListener('click', function() {
        const dish = dishInput.value.trim();
        
        if (!dish) {
          alert('Please enter a dish name');
          return;
        }
        

        loadingIndicator.style.display = 'block';
        recipeResults.classList.add('hidden');
        
        // API call to backend
        fetch('/get-recipes', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            dish_name: dish,
            dietary_preference: currentDietaryPreference,
            healthy_option: healthyCheckbox.checked
          })
        })
        .then(response => response.json())
        .then(data => {
          loadingIndicator.style.display = 'none';
          
          if (data.success) {
            dishName.textContent = dish;
            
            displayRecipes(data.recipes);
            
            recipeResults.classList.remove('hidden');
            
            recipeResults.scrollIntoView({ behavior: 'smooth' });
          } else {
            alert('Error: ' + data.error);
          }
        })
        .catch(error => {
          loadingIndicator.style.display = 'none';
          alert('Error fetching recipes: ' + error);
        });
      });
      
      function displayRecipes(recipes) {
        recipesContainer.innerHTML = '';
        
        recipes.forEach((recipe, index) => {
          const recipeCard = document.createElement('div');
          recipeCard.className = 'bg-white rounded-xl shadow-lg overflow-hidden';
          recipeCard.innerHTML = `
            <div class="p-6">
              <h4 class="text-xl font-bold mb-3 text-yellow-700">${recipe.name}</h4>
              
              <div class="flex justify-between items-center mb-4 text-sm">
                <span class="bg-yellow-100 text-yellow-800 px-2 py-1 rounded">${recipe.difficulty}</span>
                <span class="text-gray-600">⏱️ ${recipe.cook_time} mins</span>
              </div>
              
              <div class="mb-4">
                <h5 class="font-semibold mb-2">Ingredients:</h5>
                <ul class="text-sm text-gray-600 list-disc list-inside space-y-1">
                  ${recipe.ingredients.map(ing => `<li>${ing}</li>`).join('')}
                </ul>
              </div>
              
              <div class="mb-4">
                <h5 class="font-semibold mb-2">Instructions:</h5>
                <ol class="text-sm text-gray-600 list-decimal list-inside space-y-1">
                  ${recipe.instructions.map((step, i) => `<li>${step}</li>`).join('')}
                </ol>
              </div>
              
              <div class="border-t pt-3">
                <h5 class="font-semibold mb-2">Nutrition (per serving):</h5>
                <div class="grid grid-cols-2 gap-2 text-sm">
                  <div class="text-center bg-green-50 p-2 rounded">
                    <div class="font-bold text-green-700">${recipe.nutrition_info.calories}</div>
                    <div class="text-xs text-gray-600">Calories</div>
                  </div>
                  <div class="text-center bg-blue-50 p-2 rounded">
                    <div class="font-bold text-blue-700">${recipe.nutrition_info.protein_g}g</div>
                    <div class="text-xs text-gray-600">Protein</div>
                  </div>
                  <div class="text-center bg-purple-50 p-2 rounded">
                    <div class="font-bold text-purple-700">${recipe.nutrition_info.carbs_g}g</div>
                    <div class="text-xs text-gray-600">Carbs</div>
                  </div>
                  <div class="text-center bg-orange-50 p-2 rounded">
                    <div class="font-bold text-orange-700">${recipe.nutrition_info.fat_g}g</div>
                    <div class="text-xs text-gray-600">Fat</div>
                  </div>
                </div>
              </div>
            </div>
          `;
          recipesContainer.appendChild(recipeCard);
        });
      }
    });