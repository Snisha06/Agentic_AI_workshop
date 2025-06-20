import 'package:flutter/material.dart';
import 'result_scaffold.dart';

class TransitionRoadmapScreen extends StatelessWidget {
  final dynamic roadmap;

  const TransitionRoadmapScreen({super.key, required this.roadmap});

  @override
  Widget build(BuildContext context) {
    final String text =
        (roadmap is List)
            ? roadmap.map((e) => e.toString()).join(', ')
            : 'No roadmap data available.';

    return ResultScaffold(
      title: 'Transition Roadmap',
      body: Card(
        color: Colors.orange.shade50,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(text, style: const TextStyle(fontSize: 16)),
        ),
      ),
    );
  }
}
