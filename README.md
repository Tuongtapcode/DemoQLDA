# English Vocabulary Learning App 📚

A mobile application for learning English vocabulary with intelligent spaced repetition system, built with React Native and Spring Boot.

## 🎯 Project Overview

This mobile application addresses the common challenge faced by English learners in Vietnam - systematic vocabulary memorization and retention. The app provides an interactive, personalized learning experience that helps users build and maintain their English vocabulary effectively.

### Key Features

- 📱 **Cross-platform mobile app** (Android & iOS) built with React Native
- 🧠 **Smart learning algorithm** using SM-2 spaced repetition system
- 📋 **Custom vocabulary lists** - create and manage personal word collections
- ❓ **Interactive quizzes** - multiple choice, fill-in-the-blank, and matching exercises
- 📊 **Progress tracking** - detailed statistics and learning analytics
- 🏆 **Achievement system** - gamified learning with streaks and milestones
- 🔐 **User authentication** - secure login and profile management

## 🏗️ Architecture

### Frontend (Mobile App)
- **Framework**: React Native
- **Platform**: Android & iOS
- **State Management**: React Hooks (useState, useReducer)
- **API Integration**: RESTful API communication

### Backend (Server)
- **Framework**: Spring Boot
- **Security**: Spring Security with JWT
- **Database**: MySQL with JPA/Hibernate
- **Architecture**: MVC pattern with layered design
- **API**: RESTful endpoints

### DevOps & Deployment
- **CI/CD**: Jenkins pipeline
- **Containerization**: Docker
- **Cloud Platform**: AWS (EC2, ECS)
- **Database Hosting**: Railway (MySQL)

## 🧮 SM-2 Algorithm Implementation

The app uses an enhanced version of the SM-2 (SuperMemo 2) algorithm that considers word difficulty levels:

```
Standard SM-2: I₁ = 1, I₂ = 6, Iₙ = Iₙ₋₁ × EF (n ≥ 3)

Enhanced with difficulty adjustment:
adjustedQuality = max(0, q - round(difficultyFactor - 1))
```

**Difficulty Levels**:
- A1 (Beginner): difficultyFactor = 1.0
- A2-B1 (Intermediate): difficultyFactor = 1.5-2.0  
- B2-C1 (Upper-Intermediate): difficultyFactor = 2.5-3.0
- C2 (Advanced): difficultyFactor = 3.5

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- Java 11 or higher
- MySQL 8.0
- Android Studio / Xcode (for mobile development)
- Docker (optional)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/english-vocab-app.git
   cd english-vocab-app/backend
   ```

2. **Configure database**
   ```properties
   # application.properties
   spring.datasource.url=jdbc:mysql://localhost:3306/vocab_db
   spring.datasource.username=your_username
   spring.datasource.password=your_password
   ```

3. **Run the application**
   ```bash
   ./mvnw spring-boot:run
   ```

   Or with Docker:
   ```bash
   docker build -t vocab-backend .
   docker run -p 8080:8080 vocab-backend
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure API endpoint**
   ```javascript
   // config/api.js
   export const API_BASE_URL = 'http://localhost:8080/api';
   ```

4. **Run the app**
   ```bash
   # For iOS
   npx react-native run-ios
   
   # For Android  
   npx react-native run-android
   ```

## 📊 Database Schema

### Core Tables
- **Users**: User accounts and profiles
- **Words**: Vocabulary database with CEFR levels
- **Categories**: Subject-based word groupings
- **Vocabulary_lists**: User-created word collections
- **Word_progress**: SM-2 algorithm tracking data
- **Study_sessions**: Learning session records
- **Exercises**: Quiz and practice activities

### Key Relationships
```
Users ↔ Vocabulary_lists (1:N)
Vocabulary_lists ↔ Words (N:N) 
Users ↔ Word_progress ↔ Words (1:N:1)
Users ↔ Study_sessions ↔ Exercises (1:N:N)
```

## 🛠️ API Endpoints

### Authentication
```
POST /api/auth/login
POST /api/auth/register
POST /api/auth/refresh
```

### Vocabulary Management
```
GET    /api/words?category={id}&level={level}
POST   /api/vocabulary-lists
GET    /api/vocabulary-lists/user/{userId}
POST   /api/vocabulary-lists/{listId}/words/{wordId}
```

### Learning & Progress
```
GET    /api/study/review-words/{userId}
POST   /api/study/sessions
PUT    /api/word-progress/{wordId}
GET    /api/users/{userId}/statistics
```

## 🎮 Usage Examples

### Creating a Vocabulary List
```javascript
// Create new vocabulary list
const response = await fetch('/api/vocabulary-lists', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({
    name: "TOEIC Preparation",
    description: "Words for TOEIC exam"
  })
});
```

### Starting a Study Session
```javascript
// Get words due for review
const reviewWords = await fetch(`/api/study/review-words/${userId}`);

// Submit study session results
await fetch('/api/study/sessions', {
  method: 'POST',
  body: JSON.stringify({
    userId,
    exerciseId,
    answers: userAnswers,
    score: calculatedScore
  })
});
```

## 📱 Screenshots

### Main Features
- Browse vocabulary by categories and CEFR levels
- Create custom vocabulary lists
- Interactive learning with flashcards and quizzes
- Smart review system based on SM-2 algorithm
- Progress tracking and statistics
- User profile and achievement system

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📈 Future Enhancements

- **AI-powered features**: Personalized learning paths
- **Audio integration**: Pronunciation practice and listening exercises  
- **Social features**: Study groups and leaderboards
- **Premium subscription**: Advanced analytics and exclusive content
- **Offline mode**: Learn without internet connection
- **Multiple languages**: Extend beyond English vocabulary

## 🏆 Technical Achievements

- **Scalable architecture** with microservices-ready design
- **Automated CI/CD** pipeline with Jenkins and Docker
- **Cloud deployment** on AWS with auto-scaling capabilities
- **Advanced algorithms** - Enhanced SM-2 with difficulty adjustment
- **Cross-platform compatibility** - Single codebase for iOS and Android

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Developer**: [Your Name]
- **Advisor**: [Advisor Name]
- **Institution**: [University Name]

## 📞 Support

For support or questions, please contact:
- Email: your.email@example.com
- Issues: [GitHub Issues](https://github.com/yourusername/english-vocab-app/issues)

---

⭐ **Star this repository if you find it helpful!**

Built with ❤️ for English learners worldwide
