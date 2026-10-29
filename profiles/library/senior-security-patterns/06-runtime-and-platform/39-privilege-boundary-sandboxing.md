# SEC-39 — Sandbox the Dangerous Boundary, Not Everything

## Core principle

Uniform sandboxing wastes cost; no sandboxing gives high-risk interpreters and plugins the same kernel/network privileges as ordinary services. Senior design isolates the components that execute attacker- or model-influenced code.

## Security invariant

Any component that executes dynamic code, untrusted parsers, third-party plugins, documents, model tools or conversion pipelines SHOULD run with stronger isolation and narrower network/filesystem authority than the control plane.

## Senior architecture

Use dedicated runtime classes, microVMs/gVisor/Kata-like isolation, seccomp/AppArmor/SELinux, ephemeral filesystems and egress deny. Separate parsing/rendering/AI tool execution from credential-bearing services via message/artifact boundaries.

## Application to the supplied ecosystem

Apply this particularly to future SenTient/agent tooling, document/media processors, source acquisition pipelines and any MCP/tool executor. Keep Konfid, policy and signing services outside the sandboxed untrusted execution environment and communicate through typed requests.

## Failure modes / anti-patterns

- Running user/plugin code inside the API process.
- Sandbox still has production credentials.
- Network unrestricted because filesystem is read-only.
- Parsing service shares host PID/socket.
- “Container” treated as sufficient isolation for hostile code.

## Evidence that proves the control

Compromise simulation in sandbox cannot reach control-plane network, host filesystem or cloud metadata. Credentials are absent. Escape-sensitive workloads have distinct runtime policy and nodes where justified.


## Reference anchors

- Kubernetes Security and Application Security Checklist: https://kubernetes.io/docs/concepts/security/application-security-checklist/
- NIST SP 800-207A Cloud-Native Zero Trust: https://csrc.nist.gov/pubs/sp/800/207/a/final
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
