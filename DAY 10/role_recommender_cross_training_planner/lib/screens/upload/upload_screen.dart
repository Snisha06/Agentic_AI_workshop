// Only the visual/text style elements have been modified.
import 'dart:convert';

import 'package:file_selector/file_selector.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class UploadScreen extends StatefulWidget {
  const UploadScreen({super.key});

  @override
  State<UploadScreen> createState() => _UploadScreenState();
}

class _UploadScreenState extends State<UploadScreen> {
  XFile? selectedFile;
  final githubController = TextEditingController();
  final linkedinController = TextEditingController();
  final quizController = TextEditingController();

  bool isLoading = false;
  Map<String, dynamic>? processedData;
  String? errorMessage;

  static const String baseUrl = 'http://192.168.168.16:8000';

  Future<void> pickFile() async {
    try {
      final file = await openFile(
        acceptedTypeGroups: [
          XTypeGroup(label: 'Documents', extensions: ['pdf', 'doc', 'docx']),
        ],
      );
      if (file != null) {
        setState(() {
          selectedFile = file;
          errorMessage = null;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = "Error picking file: $e";
      });
    }
  }

  Future<void> submitData() async {
    if (selectedFile == null) {
      setState(() {
        errorMessage = "Please select a resume file";
      });
      return;
    }

    if (githubController.text.isEmpty || linkedinController.text.isEmpty) {
      setState(() {
        errorMessage = "GitHub and LinkedIn URLs are required";
      });
      return;
    }

    setState(() {
      isLoading = true;
      errorMessage = null;
      processedData = null;
    });

    try {
      final uri = Uri.parse('$baseUrl/process-profile');
      var request = http.MultipartRequest('POST', uri);

      request.files.add(
        await http.MultipartFile.fromPath('resume', selectedFile!.path),
      );
      request.fields['github'] = githubController.text.trim();
      request.fields['linkedin'] = linkedinController.text.trim();
      request.fields['quiz'] = quizController.text.trim();

      final response = await request.send();
      final resBody = await response.stream.bytesToString();

      if (response.statusCode == 200) {
        final parsed = json.decode(resBody);
        setState(() {
          processedData = parsed;
          isLoading = false;
        });
      } else {
        setState(() {
          errorMessage = "Server Error (${response.statusCode}): $resBody";
          isLoading = false;
        });
      }
    } catch (e) {
      setState(() {
        errorMessage = "Network Error: $e";
        isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    githubController.dispose();
    linkedinController.dispose();
    quizController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("AI Career Profile Analyzer"),
        backgroundColor: Colors.blue.shade700,
        foregroundColor: Colors.white,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Expanded(
              child: ListView(
                children: [
                  _buildFileUploadSection(),
                  const SizedBox(height: 20),
                  _buildInputFields(),
                  const SizedBox(height: 30),
                  _buildSubmitButton(),
                  const SizedBox(height: 20),
                  if (errorMessage != null) _buildErrorSection(),
                  if (isLoading) _buildLoadingSection(),
                  if (processedData != null) _buildResultsSection(),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildFileUploadSection() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Upload Resume",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: Colors.deepPurple,
              ),
            ),
            const SizedBox(height: 10),
            ElevatedButton.icon(
              onPressed: pickFile,
              icon: const Icon(Icons.upload_file),
              label: Text(
                selectedFile == null
                    ? "Choose PDF/DOCX File"
                    : "Selected: ${selectedFile!.name}",
              ),
              style: ElevatedButton.styleFrom(
                minimumSize: const Size(double.infinity, 50),
                backgroundColor: Colors.deepPurple,
                foregroundColor: Colors.white,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInputFields() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Profile Information",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: Colors.teal,
              ),
            ),
            const SizedBox(height: 15),
            TextField(
              controller: githubController,
              decoration: const InputDecoration(
                labelText: 'GitHub Profile URL *',
                labelStyle: TextStyle(color: Colors.black87),
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.code, color: Colors.deepPurple),
              ),
            ),
            const SizedBox(height: 15),
            TextField(
              controller: linkedinController,
              decoration: const InputDecoration(
                labelText: 'LinkedIn Profile URL *',
                labelStyle: TextStyle(color: Colors.black87),
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.person, color: Colors.deepPurple),
              ),
            ),
            const SizedBox(height: 15),
            TextField(
              controller: quizController,
              maxLines: 3,
              decoration: const InputDecoration(
                labelText: 'Aptitude Quiz Results (Optional)',
                labelStyle: TextStyle(color: Colors.black87),
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.quiz, color: Colors.deepPurple),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSubmitButton() {
    return SizedBox(
      width: double.infinity,
      height: 50,
      child: ElevatedButton.icon(
        onPressed: isLoading ? null : submitData,
        icon:
            isLoading
                ? const SizedBox(
                  width: 20,
                  height: 20,
                  child: CircularProgressIndicator(
                    strokeWidth: 2,
                    color: Colors.white,
                  ),
                )
                : const Icon(Icons.psychology),
        label: Text(isLoading ? "Processing..." : "Analyze Profile"),
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.green.shade700,
          foregroundColor: Colors.white,
          textStyle: const TextStyle(fontSize: 16),
        ),
      ),
    );
  }

  Widget _buildErrorSection() {
    return Card(
      color: Colors.red.shade50,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          children: [
            Icon(Icons.error, color: Colors.red.shade700),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                errorMessage ?? '',
                style: const TextStyle(color: Colors.red),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLoadingSection() {
    return const Card(
      child: Padding(
        padding: EdgeInsets.all(20.0),
        child: Column(
          children: [
            CircularProgressIndicator(),
            SizedBox(height: 15),
            Text("AI agents are analyzing your profile..."),
            SizedBox(height: 10),
            Text(
              "This may take a few moments",
              style: TextStyle(color: Colors.grey),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildResultsSection() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.check_circle, color: Colors.green.shade600),
                const SizedBox(width: 10),
                const Text(
                  "Analysis Complete!",
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.green,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            _buildResultSection("Skills Extracted", processedData!['skills']),
            _buildResultSection(
              "Aptitudes Mapped",
              processedData!['aptitudes'],
            ),
            _buildResultSection("Recommended Roles", processedData!['roles']),
            _buildResultSection(
              "Transition Roadmap",
              processedData!['roadmap'],
            ),
            _buildResultSection(
              "Mentor Connections",
              processedData!['mentors'],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildResultSection(String title, dynamic data) {
    return ExpansionTile(
      title: Text(
        title,
        style: const TextStyle(
          fontWeight: FontWeight.w600,
          color: Colors.indigo,
        ),
      ),
      children: [
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(12),
          margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
          decoration: BoxDecoration(
            color: Colors.grey.shade100,
            borderRadius: BorderRadius.circular(8),
          ),
          child: SelectableText(
            JsonEncoder.withIndent('  ').convert(data),
            style: const TextStyle(
              fontFamily: 'monospace',
              fontSize: 12,
              color: Colors.black87,
            ),
          ),
        ),
      ],
    );
  }
}
