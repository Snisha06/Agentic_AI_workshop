import 'package:flutter/material.dart';
import 'result_scaffold.dart';

class RecommendedRolesScreen extends StatelessWidget {
  final dynamic roles;

  const RecommendedRolesScreen({super.key, required this.roles});

  @override
  Widget build(BuildContext context) {
    final String text =
        (roles is List)
            ? roles.map((e) => e.toString()).join(', ')
            : 'No roles data available.';

    return ResultScaffold(
      title: 'Recommended Roles',
      body: Card(
        color: Colors.green.shade50,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(text, style: const TextStyle(fontSize: 16)),
        ),
      ),
    );
  }
}
