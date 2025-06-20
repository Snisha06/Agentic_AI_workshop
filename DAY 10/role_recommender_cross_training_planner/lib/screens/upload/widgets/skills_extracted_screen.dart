import 'package:flutter/material.dart';
import 'result_scaffold.dart';

class SkillsExtractedScreen extends StatelessWidget {
  final dynamic skills;

  const SkillsExtractedScreen({super.key, required this.skills});

  @override
  Widget build(BuildContext context) {
    final String text =
        (skills is List)
            ? skills.map((e) => e.toString()).join(', ')
            : 'No skills data available.';

    return ResultScaffold(
      title: 'Skills Extracted',
      body: Card(
        color: Colors.blue.shade50,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(text, style: const TextStyle(fontSize: 16)),
        ),
      ),
    );
  }
}
