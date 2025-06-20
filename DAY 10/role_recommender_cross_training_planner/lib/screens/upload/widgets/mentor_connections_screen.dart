import 'package:flutter/material.dart';
import 'result_scaffold.dart';

class MentorConnectionsScreen extends StatelessWidget {
  final dynamic mentors;

  const MentorConnectionsScreen({super.key, required this.mentors});

  @override
  Widget build(BuildContext context) {
    final String text =
        (mentors is List)
            ? mentors.map((e) => e.toString()).join(', ')
            : 'No mentor data available.';

    return ResultScaffold(
      title: 'Mentor Connections',
      body: Card(
        color: Colors.purple.shade50,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(text, style: const TextStyle(fontSize: 16)),
        ),
      ),
    );
  }
}
