# Federated Learning Sdk

Federated learning SDK for privacy-preserving distributed training.

## Features
- FedAvg, FedProx, SCAFFOLD algorithms
- Differential privacy (DP-SGD)
- Secure aggregation with Shamir secret sharing
- Simulated and real distributed modes

## Architecture
```
Client 1 ─┐
Client 2 ─┤── Aggregator ── Global Model
Client N ─┘
```

## License
MIT
