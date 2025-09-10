# Code Review Prompts for Claude

Use these prompts with Claude to get comprehensive code reviews and suggestions.

## 🔍 Security Review Prompt

```
Please review the following code for security vulnerabilities and provide specific recommendations:

[PASTE YOUR CODE HERE]

Focus on:
1. Input validation and sanitization
2. Authentication and authorization issues
3. Data exposure risks
4. Injection vulnerabilities (SQL, XSS, etc.)
5. Secure coding best practices
6. Dependency security considerations

For each issue found, please provide:
- Severity level (Critical/High/Medium/Low)
- Detailed explanation of the vulnerability
- Specific code fix recommendations
- Prevention strategies for similar issues
```

## ⚡ Performance Review Prompt

```
Analyze this code for performance optimization opportunities:

[PASTE YOUR CODE HERE]

Please evaluate:
1. Algorithm efficiency and time complexity
2. Memory usage patterns and potential leaks
3. Database query optimization opportunities
4. Caching strategies that could be implemented
5. Network request optimization
6. Resource management improvements

Provide:
- Specific bottlenecks identified
- Before/after performance impact estimates
- Alternative approaches with better performance
- Monitoring suggestions for these metrics
```

## 🧹 Code Quality Review Prompt

```
Review this code for overall quality and maintainability:

[PASTE YOUR CODE HERE]

Assess:
1. Code readability and clarity
2. Function/method organization and responsibilities
3. Naming conventions and consistency
4. Error handling and edge cases
5. Documentation and comments quality
6. Test coverage considerations
7. Design pattern usage and appropriateness

Please provide:
- Specific improvement suggestions
- Refactoring recommendations
- Best practice violations to address
- Maintainability concerns and solutions
```

## 🏗️ Architecture Review Prompt

```
Evaluate the architectural design and structure of this code:

[PASTE YOUR CODE HERE]

Please analyze:
1. Separation of concerns and modularity
2. Dependency management and coupling
3. Scalability considerations
4. Design pattern implementation
5. SOLID principles adherence
6. Extensibility and flexibility
7. Integration patterns and API design

Provide insights on:
- Architectural strengths and weaknesses
- Scalability bottlenecks
- Recommended structural improvements
- Future-proofing strategies
```

## 🧪 Testing Strategy Review Prompt

```
Review this code and suggest comprehensive testing strategies:

[PASTE YOUR CODE HERE]

Please provide:
1. Unit test recommendations with specific test cases
2. Integration testing scenarios
3. Edge cases and error conditions to test
4. Mock/stub strategies for dependencies
5. Test data setup and teardown considerations
6. Performance testing recommendations
7. Security testing approaches

Include:
- Sample test code snippets
- Testing framework recommendations
- Coverage goals and metrics
- Continuous integration considerations
```

## 🔄 Refactoring Suggestions Prompt

```
Suggest refactoring improvements for this code:

[PASTE YOUR CODE HERE]

Focus on:
1. Code duplication elimination
2. Function/method extraction opportunities
3. Variable and function naming improvements
4. Simplification of complex logic
5. Removal of code smells
6. Pattern implementation improvements

For each suggestion:
- Explain the benefit of the refactoring
- Provide before/after code examples
- Estimate the complexity of the change
- Highlight any risks or considerations
```

## 💡 Tips for Effective Code Reviews with Claude

### Preparation
- Provide **context** about the project and its goals
- Include **relevant background** about the codebase
- Specify your **target audience** (team size, experience level)
- Mention any **specific concerns** or areas of focus

### Follow-up Questions
```
- "Can you provide a specific example of how to implement this suggestion?"
- "What are the trade-offs of this approach vs. the current implementation?"
- "How would this change affect the existing test suite?"
- "Are there any backward compatibility concerns with this recommendation?"
- "Can you suggest a gradual migration path for this refactoring?"
```

### Context-Setting Prompts
```
"This code is part of a [web application/API/CLI tool/library] that [describe purpose].
The team consists of [experience level] developers, and we prioritize [performance/security/maintainability].
Our main concerns are [specific issues or goals]."
```

## 🔧 Customizing Prompts

### For Different Languages
- **Python**: Add focus on PEP 8, type hints, and Pythonic patterns
- **JavaScript/TypeScript**: Emphasize modern ES6+ features, async patterns
- **Java**: Include discussion of design patterns, memory management
- **Go**: Focus on idiomatic Go patterns, error handling, concurrency

### For Different Project Types
- **Web APIs**: Emphasize security, scalability, and API design
- **Frontend Applications**: Focus on performance, accessibility, user experience
- **Data Processing**: Highlight efficiency, error handling, data validation
- **Libraries/SDKs**: Emphasize API design, documentation, backward compatibility

## 📚 Related Resources

- [Claude Documentation](https://docs.anthropic.com/claude)
- [Secure Code Review Guide](https://owasp.org/www-project-code-review-guide/)
- [Clean Code Principles](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)