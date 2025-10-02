from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from google import genai
import json
import re

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

class RecipeGenerator:
    def __init__(self):
        pass
    
    def generate_recipes(self, dish_name, dietary_preference, healthy_option):
        """Generate recipes using Gemini AI"""
        
        # Build prompt
        health_text = " The recipes should be healthier alternatives with lower calories, balanced nutrition, and light cooking methods." if healthy_option else ""
        
        prompt = f"""
        You are ChefAI, an Indian professional chef and nutritionist. 
        Generate exactly 3 delicious INDIAN ALTERNATIVE recipes for the dish: {dish_name}.
        
        Dietary preference: {dietary_preference.upper()}
        {health_text}
        
        IMPORTANT DIETARY RULES:
        - JAIN: Strictly NO onion, NO garlic, NO root vegetables, NO meat, NO fish, NO eggs
        - VEG: No meat, fish, egg but can include dairy, vegetables
        - NON-VEG: Can include all ingredients including meat, fish, eggs, dairy
        
        ALL RECIPES AND DISHES MUST BE ONES THAT CAN BE MADE WITH EASE IN AN AVERAGE INDIAN HOUSEHOLD.
        
        FORMAT REQUIREMENTS:
        Return ONLY valid JSON array with exactly 3 recipe objects. Each recipe must have:
        - "name": string (creative recipe name)
        - "ingredients": array of strings (include provided dish elements + common pantry items)
        - "instructions": array of strings (clear step-by-step cooking instructions)
        - "cook_time": number (total cooking time in minutes)
        - "difficulty": string ("Easy", "Medium", or "Hard")
        - "nutrition_info": object with "calories", "protein_g", "carbs_g", "fat_g"
        
        Make recipes practical, delicious, and suitable for home cooking.
        Ensure ingredients are commonly available.
        
        JSON FORMAT:
        [
        {{
            "name": "Recipe Name 1",
            "ingredients": ["ing1", "ing2", ...],
            "instructions": ["Step 1", "Step 2", ...],
            "cook_time": 30,
            "difficulty": "Easy",
            "nutrition_info": {{"calories": 350, "protein_g": 15, "carbs_g": 45, "fat_g": 10}}
        }},
        ...2 more recipes
        ]
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp",  # Using a more available model
                contents=prompt
            )
            
            # Extract JSON from response
            result_text = response.text
            
            # Clean the response to extract JSON
            json_match = re.search(r'\[.*\]', result_text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                recipes = json.loads(json_str)
                return recipes
            else:
                # Fallback: return sample data if JSON parsing fails
                return self._get_sample_recipes(dish_name, dietary_preference)
                
        except Exception as e:
            print(f"Error generating recipes: {e}")
            return self._get_sample_recipes(dish_name, dietary_preference)
    
    def _get_sample_recipes(self, dish_name, dietary_preference):
        """Fallback sample recipes in case API fails"""
        return [
            {
                "name": f"Healthy {dish_name} Alternative",
                "ingredients": ["Whole wheat flour", "Fresh vegetables", "Herbs and spices", "Low-fat dairy"],
                "instructions": [
                    "Prepare all ingredients as per requirement",
                    "Mix dry ingredients first",
                    "Add wet ingredients gradually",
                    "Cook on medium heat until done"
                ],
                "cook_time": 30,
                "difficulty": "Easy",
                "nutrition_info": {"calories": 280, "protein_g": 12, "carbs_g": 35, "fat_g": 8}
            },
            {
                "name": f"Light {dietary_preference} {dish_name}",
                "ingredients": ["Fresh produce", "Lean protein", "Healthy oils", "Natural seasonings"],
                "instructions": [
                    "Chop all vegetables finely",
                    "Marinate protein if needed",
                    "Cook with minimal oil",
                    "Garnish and serve hot"
                ],
                "cook_time": 25,
                "difficulty": "Medium",
                "nutrition_info": {"calories": 320, "protein_g": 18, "carbs_g": 28, "fat_g": 6}
            },
            {
                "name": f"Quick {dish_name} Makeover",
                "ingredients": ["Alternative grains", "Fresh herbs", "Spices", "Healthy substitutes"],
                "instructions": [
                    "Prepare the base ingredients",
                    "Layer flavors properly",
                    "Cook until perfectly done",
                    "Serve with healthy sides"
                ],
                "cook_time": 35,
                "difficulty": "Easy",
                "nutrition_info": {"calories": 260, "protein_g": 15, "carbs_g": 30, "fat_g": 7}
            }
        ]

# Initialize recipe generator
recipe_generator = RecipeGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-recipes', methods=['POST'])
def get_recipes():
    try:
        data = request.get_json()
        dish_name = data.get('dish_name', '').strip()
        dietary_preference = data.get('dietary_preference', 'Non-Veg')
        healthy_option = data.get('healthy_option', True)
        
        if not dish_name:
            return jsonify({'success': False, 'error': 'Please enter a dish name'})
        
        # Generate recipes using AI
        recipes = recipe_generator.generate_recipes(dish_name, dietary_preference, healthy_option)
        
        return jsonify({
            'success': True,
            'recipes': recipes,
            'dish_name': dish_name
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)