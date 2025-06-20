import 'package:flutter/material.dart';
import 'upload/upload_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Dynamic Role Recommender')),
      body: Center(
        child: ElevatedButton(
          child: Text("Start Role Discovery"),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => UploadScreen()),
            );
          },
        ),
      ),
    );
  }
}
