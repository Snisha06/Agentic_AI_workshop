# role_recommender_cross_training_planner

# AI Career Profile Analyzer - Frontend

This is the frontend of the AI Career Profile Analyzer application, built with Flutter. It provides an intuitive user interface that allows users to upload their resume, submit GitHub and LinkedIn URLs, and view AI-driven analysis on skills, aptitudes, and career recommendations.

---

## Features

- Upload `.pdf`, `.doc`, or `.docx` resumes
- Input GitHub and LinkedIn profile URLs
- (Optional) Provide aptitude quiz results
- Send data to backend via HTTP Multipart Request
- Display AI-processed insights including:
  - Skills Extracted
  - Aptitudes Mapped
  - Recommended Roles
  - Transition Roadmap
  - Mentor Connections

---

## Technologies Used

- **Flutter**: UI development framework
- **Dart**: Programming language
- **http**: For making multipart API requests
- **file_selector**: For cross-platform file picking
- **ExpansionTile, Cards, Material UI**: UI rendering
- **SelectableText & JSON encoder**: Result presentation

---

## Folder Structure

lib/
├── main.dart
├── screens/
home_screen.dart
│ └── upload_screen.dart
├── widgets/
│ └── result_scaffold.dart
│ └── skills_extracted_screen.dart
│ └── aptitudes_mapped_screen.dart
│ └── roadmap_screen.dart
│ └── mentors_screen.dart

---

## How to Run

1. Ensure Flutter SDK is installed: [Flutter installation guide](https://flutter.dev/docs/get-started/install)
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/frontend-ai-analyzer.git
   cd frontend-ai-analyzer
   ```

   Got Dependencies:
   flutter pub get
   Run:
   flutter run

   Configuration:
   static const String baseUrl = 'http://<my-backend-ip>:8000';
