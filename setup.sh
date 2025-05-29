#!/bin/bash

# BookHub Setup Script
echo "🚀 Setting up BookHub - Lightning Fast Search with Django & Algolia"
echo "=================================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Copy environment template if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating environment file..."
    cp env.template .env
    echo "📝 Please edit .env with your Algolia credentials"
fi

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "👤 Creating superuser (if needed)..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Load sample data
echo "📚 Loading sample books..."
python manage.py load_sample_books --count 30

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Edit .env with your Algolia credentials"
echo "2. Run: python manage.py runserver"
echo "3. Visit: http://localhost:8000"
echo ""
echo "📖 URLs:"
echo "   Homepage: http://localhost:8000/"
echo "   Search:   http://localhost:8000/search/"
echo "   Admin:    http://localhost:8000/admin/ (admin/admin123)"
echo ""
echo "🔍 To enable Algolia search:"
echo "1. Get free Algolia account at https://www.algolia.com"
echo "2. Add credentials to .env file"
echo "3. Run: python manage.py algolia_reindex"
echo "" 