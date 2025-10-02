
# DietDash 🥗

[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)](https://tailwindcss.com)

AI-powered diet-friendly recipe alternatives generator. Transform your favorite dishes into nutritious versions using Google Gemini AI.

## 🌟 Features

- **🤖 AI-Powered Recipes**: Generate diet-friendly alternatives using Google Gemini AI
- **🍽️ Dietary Preferences**: Support for Non-Veg, Veg, and Jain dietary restrictions
- **📊 Nutrition Tracking**: Detailed calorie, protein, carbs, and fat information
- **⏱️ Cook Time & Difficulty**: Practical cooking instructions with time estimates
- **🎨 Beautiful UI**: Responsive design built with Tailwind CSS
- **🚀 Fast & Lightweight**: Built with Flask for optimal performance

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kish-0/dietdash
   cd dietdash
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 🛠️ Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **AI/ML**: Google Gemini API
- **Deployment**: Ready for Vercel/Railway

## 📁 Project Structure

```
dietdash/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (ignored in git)
├── templates/
│   └── index.html     # Main frontend template
└── static/
    └── js/            # JavaScript assets
```

## 🎯 How It Works

1. **Input Your Dish**: Enter any dish you want to make diet-friendly
2. **Choose Preferences**: Select dietary preference (Non-Veg/Veg/Jain)
3. **AI Processing**: Gemini AI generates 3 diet-friendly alternatives
4. **Get Results**: Receive recipes with ingredients, instructions, and nutrition facts

## 🍕 Example Usage

- Input: "Butter Chicken"
- Dietary Preference: "Non-Veg" 
- Output: 3 diet-friendly butter chicken recipes with reduced calories and balanced nutrition

## 🔧 API Endpoints

- `GET /` - Serve main application
- `POST /get-recipes` - Generate recipes (JSON API)

## 🌐 Live Demo

[Add your deployment link here]

## 📸 Screenshots

[Add screenshots of your application here]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kishan S**
- GitHub: [@kish-0](https://github.com/kish-0)
- Project Link: [https://github.com/kish-0/dietdash](https://github.com/kish-0/dietdash)

## 🙏 Acknowledgments

- Google Gemini AI for recipe generation
- Tailwind CSS for the beautiful UI components
- Flask community for the excellent web framework

---

⭐ Star this repo if you found it helpful!

