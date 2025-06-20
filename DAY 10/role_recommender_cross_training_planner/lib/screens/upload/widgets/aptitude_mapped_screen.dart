import 'package:flutter/material.dart';
import 'result_scaffold.dart';

class AptitudesMappedScreen extends StatelessWidget {
  final dynamic aptitudes;

  const AptitudesMappedScreen({super.key, required this.aptitudes});

  @override
  Widget build(BuildContext context) {
    final String text =
        (aptitudes is List)
            ? aptitudes.map((e) => e.toString()).join(', ')
            : 'No aptitude data available.';

    return ResultScaffold(
      title: 'Aptitudes Mapped',
      body: Card(
        color: Colors.teal.shade50,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(text, style: const TextStyle(fontSize: 16)),
        ),
      ),
    );
  }
}
