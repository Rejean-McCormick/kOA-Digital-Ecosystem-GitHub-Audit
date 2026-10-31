<!-- Frozen source: https://github.com/Rejean-McCormick/Kontainer/wiki/Python-API | commit: c9674410bf4a3167240457a63ed37ddf51b76b25 | SHA-256: 8c09e61419ef49ff48eeaf9b7a11296fed5834de8f1dca70fea826426449f87d -->

# Python API

The distribution exposes the local `kristal_container` Python package. The code samples below reflect the **1.0.0rc1** surface; use the repository's `docs/API.md` for details and error contracts.

## Create and inspect an encrypted container

```python
from getpass import getpass
from pathlib import Path
from kristal_container import Container, Credentials, Protection, pack

phrase = getpass("New container passphrase: ")
pack(
    Path("my-folder"),
    Path("my-data.kristal"),
    protection=Protection(password=phrase),
)

with Container(
    Path("my-data.kristal"),
    credentials=Credentials(password=phrase),
    require_encrypted=True,
) as reader:
    print(reader.report)
    for member in reader.list():
        print(member["path"], member["size"])
```

Never log, serialize, or put user secrets in shell arguments. The library keeps readers and credentials separate and does not install any global daemon.

## Creation options

```python
pack(
    source,
    destination,
    protection=Protection(),
    selected=None,
    signing_key=None,
    allow_sensitive=False,
    overwrite=False,
    limits=Limits(),
    expected_members=None,
)
```

`selected` is a tuple of **exact relative files**. `None` inventories recursively; `()` creates a package with no user members. `signing_key` is a 32-byte Ed25519 seed supplied by the application. `expected_members` can bind the physical bytes to a separately obtained validated selection and is used by the Local Kit adapter.

`Protection(password=None, factor=None, factor_provider=None, recipients=(), recovery=None)` supports distinct optional access paths. Binary factor and recovery secrets are 32 bytes. A normal password-factor slot needs both secrets; separate recovery/recipient slots allow independent opening.

## Reading and exporting

```python
from kristal_container import Container, Credentials

with Container("my-data.kristal", credentials=Credentials(password=phrase)) as reader:
    entries = reader.list()
    # For small members only: reader.read("state/snapshot.json")
    with open("verified-snapshot.json", "xb") as output:
        reader.copy_to("state/snapshot.json", output)
```

The application **must** decide whether a plaintext export is authorized and whether its destination is safe. `read()` has a default 16 MiB limit; `copy_to()` streams larger files in chunks. `extract(new_directory)` exports all members into a destination that must not exist. No per-member ACL is enforced by the container library.

Constructor policies include `trusted_signers`, `require_signature`, `require_encrypted`, `expected_sha256`, and `limits`. A signature reported as `valid-untrusted` is not approved; an `expected_sha256` must come from a trusted source external to the container.

## Useful methods

| Method | Role |
| --- | --- |
| `reader.list()` | Verified file metadata |
| `reader.read(relative_path)` | Small member as bytes |
| `reader.copy_to(relative_path, binary_stream)` | Chunked member export |
| `reader.extract(new_directory)` | Explicit plaintext directory extraction |
| `reader.rewrap(destination, protection=..., overwrite=False, allow_plaintext=False)` | Fresh outer protection, identical inner ZIP |
| `reader.close()` | Close reader and encrypted temporary spool |
| `inspect_header(path)` | **Unverified** public header only |

Expected exceptions derive from `ContainerError` and have stable `code` fields such as `invalid-format`, `integrity-failed`, `access-denied`, `policy-denied`, `limit-exceeded`, and `unsupported-profile`.

## Integration adapter

```python
from pathlib import Path
from kristal_container import Protection
from kristal_container.integration import pack_read_surface

# projection is obtained from the authorized Local Kit caller.
pack_read_surface(
    Path("workspace"),
    Path("reading.kristal"),
    projection,
    protection=Protection(password=phrase),
)
```

The adapter requires a ready, error-free `read-surface/1.0` projection, copies **only** the enumerated bytes, and checks sizes and digests. It does **not** run a build, download external objects, or revalidate Kristal State semantics. See [Ecosystem Integration](Ecosystem-Integration).
