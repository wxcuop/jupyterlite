# JupyterLite 

JupyterLite deployed as a static site to GitHub Pages

➡️ **https://wxcuop.github.io/jupyterlite**

➡️**https://jupyterlite1.pages.dev/**

➡️**https://wxcuop.netlify.app/**
## Requirements

JupyterLite is being tested against modern web browsers:

- Firefox 90+
- Chromium 89+

## Further Information and Updates

For more info, keep an eye on the JupyterLite documentation:

- How-to Guides: https://jupyterlite.readthedocs.io/en/latest/howto/index.html
- Reference: https://jupyterlite.readthedocs.io/en/latest/reference/index.html

- https://pyodide.org/en/stable/usage/packages-in-pyodide.html

- https://www.bloomberg.com/company/stories/ipydatagrid-adds-interactive-data-grids-to-the-jupyter-ecosystem/
- https://github.com/innovationOUtside/ouseful_jupyterlite_utils/tree/main

- https://panel.holoviz.org/how_to/wasm/jupyterlite.html
- please note that the browser’s local storage has a limited capacity, and you might not be able to upload large files. But smaller files up to ~50MB should be fine.

- https://github.com/jupyterlite/jupyterlite/issues/403
- https://github.com/koenvo/pyodide-http
- https://pyodide.org/en/stable/usage/loading-custom-python-code.html


## WebR limitations
Due to limitations in the way the webR worker thread is implemented, the persistent JupyterLite file storage and the Emscripten VFS used by webR are not accessible to one another. The simplest way to import data into a webR notebook at the time of writing is by using R functions such as read.csv() with a publicly accessible URL.

While webR supports interrupting long running computations, interrupting cell execution has not yet been implemented in JupyterLite. An infinite looping cell can only be recovered by restarting the kernel.

## DuckDB limitations
https://duckdb.org/2024/10/02/pyodide.html
https://github.com/iqmo-org/magic_duckdb
Running in the browser is a more restrictive environment (for security purposes), so there are some limitations when using DuckDB in Pyodide. There is no free lunch!

Single-threaded
Pyodide currently limits execution to a single thread
A few extra steps to query remote files
Remote files can't be accessed by DuckDB directly
Instead, pull the files locally with Pyodide first
DuckDB-Wasm has custom enhancements to make this possible, but these are not present in DuckDB's Python client


## DuckDB limitations
No runtime-loaded extensions
Several extensions are automatically included: parquet, json, icu, tpcds, and tpch.
Release cadence aligned with Pyodide
At the time of writing, duckdb-pyodide is at 1.0.0 rather than 1.1.1


## Working around CORS
https://jarnaldich.me/blog/2023/01/29/jupyterlite-jsonp.html

## CORS Proxy
https://egghead.io/lessons/cloudflare-add-cors-headers-to-a-third-party-api-response-in-a-workers-api

https://github.com/Zibri/cloudflare-cors-anywhere
