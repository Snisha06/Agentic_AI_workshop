import 'package:flutter/material.dart';

class ResultScaffold extends StatelessWidget {
  final String title;
  final Widget body;

  const ResultScaffold({super.key, required this.title, required this.body});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
        centerTitle: true,
        backgroundColor: Colors.indigo,
      ),
      body: Padding(padding: const EdgeInsets.all(16.0), child: body),
    );
  }
}
