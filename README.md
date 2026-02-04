# sv-doc

A documentation generator that processes SystemVerilog source comments and produces HTML documentation.

## Architectural skeleton

```
sv-doc/
├── src/
│   └── sv_doc/
│       ├── __init__.py          # Package metadata
│       ├── main.py              # Composition root / application service
│       ├── config.py            # Configuration models
│       ├── interfaces.py        # Protocols for pluggable components
│       ├── registry.py          # Registry for discoverable plugins
│       ├── pipeline/
│       │   └── orchestrator.py  # Pipeline orchestration
│       ├── parsers/
│       │   ├── comment_extractor.py  # Raw comment extraction strategies
│       │   └── comment_parser.py     # Comment parsing strategies
│       ├── renderers/
│       │   └── html_renderer.py # HTML rendering strategy placeholder
│       ├── io/
│       │   └── filesystem.py    # Output writing abstraction
│       └── models/
│           ├── comment.py        # Comment block models
│           └── document.py       # Documentation tree models
└── tests/
    └── test_architecture.py      # Placeholder tests for structure/contract checks
```

### Responsibilities

- **`main.py`**: Coordinates configuration and pipeline execution (composition root).
- **`config.py`**: Holds configuration dataclasses to keep input/output settings together.
- **`interfaces.py`**: Defines Protocol-based abstractions for extractors, parsers, renderers, and writers to satisfy SOLID/DI requirements.
- **`registry.py`**: Provides a registry for plugin discovery and easy extension of formats.
- **`pipeline/orchestrator.py`**: Encapsulates the end-to-end flow without owning concrete implementations.
- **`parsers/`**: Houses comment extraction and parsing strategies, making it easy to add new comment styles.
- **`renderers/`**: Contains output format renderers (HTML now, other formats later).
- **`io/`**: Isolates filesystem or other output targets to keep IO concerns separate.
- **`models/`**: Contains shared domain models for comment blocks and documentation nodes.
- **`tests/`**: Placeholder tests for verifying wiring, contracts, and extension points.
