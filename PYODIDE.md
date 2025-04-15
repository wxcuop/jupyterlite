Only the Python standard library is available after importing Pyodide. To use other packages, you’ll need to load them using either:

micropip.install() (Python) for pure Python packages with wheels as well as Pyodide packages (including Emscripten/wasm32 binary wheels). 

It can install packages from PyPI, the JsDelivr CDN or from other URLs.

pyodide.loadPackage() (Javascript) for packages built with Pyodide. 

This is a function with less overhead but also more limited functionality. 

micropip uses this function to load Pyodide packages. 

In most cases you should be using micropip.

In some cases, and in particular in the REPL, packages are installed implicitly from imports. 

The Pyodide REPL uses pyodide.loadPackagesFromImports() to automatically download all packages that the code snippet imports. 

This is useful since users might import unexpected packages in REPL.

At present, loadPackagesFromImports() will not download packages from PyPI, it will only download packages included in the Pyodide distribution.

## Packages built in Pyodide
This is the list of Python packages included with the current version of Pyodide. These packages can be loaded with pyodide.loadPackage() or micropip.install()


| Package Name       | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| affine             | Provides methods to handle affine transformations like scaling, translation, rotation, and shearing.         |
| aiohttp            | An asynchronous HTTP client/server framework for Python.                                                     |
| aiosignal          | Provides a high-performance asynchronous signal/slot pattern for Python.                                     |
| altair             | A declarative statistical visualization library for Python.                                                  |
| annotated-types    | Provides runtime-validated and annotated types for Python.                                                   |
| anyio              | A high-level asynchronous I/O library that works with asyncio and trio.                                      |
| apsw               | Python bindings for SQLite with advanced features like custom functions and virtual tables.                  |
| argon2-cffi        | A Python binding for Argon2, a secure password hashing algorithm.                                            |
| argon2-cffi-bindings | Low-level bindings for Argon2 password hashing.                                                             |
| arro3-compute      | Part of the arro3 ecosystem, focused on computational utilities.                                              |
| arro3-core         | Core library for the arro3 framework, providing foundational utilities.                                       |
| arro3-io           | Input/output utilities for the arro3 framework.                                                              |
| asciitree          | A library to render ASCII trees for visualizing hierarchical data.                                            |
| astropy            | A Python library for astronomy and astrophysics research.                                                    |
| astropy_iers_data  | Provides Earth rotation data for precise astronomical calculations.                                           |
| asttokens          | Helps in analyzing Python source code and producing abstract syntax trees.                                   |
| async-timeout      | A library to manage timeout control for asyncio tasks.                                                       |
| atomicwrites       | Provides atomic file writing in Python, ensuring data consistency.                                           |
| attrs              | A library for defining classes with minimal boilerplate code.                                                |
| autograd           | Enables automatic differentiation for Python and supports gradients and Hessians for mathematical functions.  |
| awkward-cpp        | Provides C++ bindings for the awkward array library.                                                         |
| b2d                | A 2D physics engine for Python.                                                                              |
| bcrypt             | A password hashing library using the bcrypt algorithm.                                                       |
| beautifulsoup4     | A library for parsing HTML and XML documents, commonly used for web scraping.                                |
| biopython          | Tools for biological computation, including DNA and protein sequence analysis.                               |
| bitarray           | Efficient implementation of bit arrays and operations in Python.                                             |
| bitstring          | A Python library to manipulate binary data structures.                                                       |
| bleach             | A library to sanitize and clean HTML and prevent XSS attacks.                                                |
| bokeh              | A library for interactive visualization and web-based charts.                                                |
| boost-histogram    | A high-performance histogramming library for Python.                                                         |
| brotli             | A compression library implementing the Brotli algorithm.                                                     |
| cachetools         | Provides utilities for caching in Python, including LRU and TTL caches.                                      |
| Cartopy            | A library for cartographic projections and geospatial data visualization.                                     |
| casadi             | A library for symbolic computation and numerical optimization.                                                |
| cbor-diag          | Provides diagnostic tools for CBOR (Concise Binary Object Representation).                                   |
| certifi            | Provides a curated list of root certificates for secure SSL/TLS connections.                                 |
| cffi               | A Foreign Function Interface for Python to call C code.                                                     |
| cffi_example       | An example package demonstrating how to use cffi for Python.                                                 |
| cftime             | A library for date/time handling, often used with netCDF files.                                              |
| charset-normalizer | A library to detect character encodings in text files.                                                       |
| Package Name       | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| clarabel           | A Python library for conic optimization.                                                                     |
| click              | A Python package for creating command-line interfaces (CLIs) with minimal code.                              |
| cligj              | Command-line utilities for GeoJSON operations.                                                               |
| clingo             | A grounder and solver for logic programs used in artificial intelligence and computational logic.             |
| cloudpickle        | Extended pickling support for Python objects, useful for distributed systems.                                |
| cmyt               | A Python library for color mapping in scientific visualizations.                                             |
| colorspacious      | A library for perceptual color space transformations.                                                        |
| contourpy          | A library for creating contour plots in Python.                                                              |
| coolprop           | A library for thermodynamic and transport property calculations.                                             |
| coverage           | A tool for measuring code coverage in Python programs.                                                       |
| cramjam            | A library providing high-performance compression algorithms.                                                 |
| crc32c             | A library for CRC32C (Cyclic Redundancy Check) checksum calculations.                                        |
| cryptography       | A library for cryptographic recipes and primitives in Python.                                                |
| css-inline         | A library for inlining CSS into HTML files.                                                                  |
| cssselect          | Provides the ability to use CSS-like selectors to query XML or HTML documents.                               |
| cvxpy-base         | A Python library for convex optimization.                                                                    |
| cycler             | A library for creating composable cycles, primarily for matplotlib property cycling.                         |
| cysignals          | Signal handling and exceptions for Cython.                                                                   |
| cytoolz            | Cython implementation of the `toolz` library for functional programming.                                     |
| decorator          | Simplifies the creation of decorators in Python.                                                             |
| demes              | A library for demographic modeling of populations.                                                           |
| deprecation        | A library for marking deprecated features and managing deprecation warnings.                                 |
| distlib            | A library for packaging and distribution utilities.                                                          |
| distro             | Provides information about the OS distribution on which Python runs.                                         |
| docutils           | A text processing system for converting reStructuredText into various output formats.                        |
| duckdb             | An in-process SQL OLAP database management system.                                                           |
| ewah_bool_utils    | Provides utility functions for efficient boolean operations.                                                 |
| exceptiongroup     | A library for handling multiple exceptions in Python.                                                        |
| executing          | Allows introspection of currently executing code, used in debugging tools.                                   |
| fastparquet        | A Python library for reading and writing Apache Parquet files.                                               |
| fiona              | A Python library for reading and writing geospatial data files.                                              |
| fonttools          | A library for manipulating fonts, including TrueType and OpenType fonts.                                     |
| freesasa           | A library for calculating solvent-accessible surface areas of proteins.                                      |
| frozenlist         | A list implementation that is immutable once frozen.                                                         |
| fsspec             | A library for handling filesystems and file-like objects in Python.                                          |
| future             | Provides compatibility between Python 2 and Python 3.                                                        |
| galpy              | A Python library for galactic dynamics simulations.                                                          |
| gensim             | A library for topic modeling and document similarity analysis.                                               |
| geopandas          | Extends pandas to handle geospatial data.                                                                    |
| gmpy2              | A library for arbitrary-precision arithmetic, useful for mathematical computations.                          |
| gsw                | Provides tools for oceanographic computations based on the TEOS-10 standard.                                 |
| h11                | A Python library for implementing HTTP/1.1 protocol in Python.                                               |
| h3                 | A Python wrapper for the H3 spatial indexing system.                                                        |
| h5py               | A Python interface to the HDF5 data model for storing large datasets.                                        |
| html5lib           | A library for parsing HTML, including malformed HTML documents.                                              |
| httpcore           | A low-level HTTP library designed for asyncio and HTTPX.                                                     |
| httpx              | A fully featured HTTP client for Python with async support.                                                  |
| idna               | Implements the Internationalized Domain Names (IDNA) standard in Python.                                     |
| igraph             | A Python library for creating and manipulating graphs and networks.                                          |
| imageio            | A library for reading and writing images in Python.                                                          |
| iminuit            | A library for function minimization and error propagation.                                                   |
| iniconfig          | A library for handling .ini configuration files in Python.                                                   |
| ipython            | An interactive Python shell with advanced features like syntax highlighting and debugging.                   |
| jedi               | A library for autocompletion and static analysis of Python code.                                             |
| Jinja2             | A templating engine for Python that allows dynamic generation of text files.                                 |
| Package Name       | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| jiter              | A library for creating and iterating over random distributions.                                              |
| joblib             | A library for lightweight pipelining and parallel execution in Python.                                       |
| jsonschema         | A library for validating JSON schemas.                                                                       |
| jsonschema_specifications | Provides standard JSON Schema specifications for validation.                                            |
| kiwisolver         | A fast implementation of the Cassowary constraint-solving algorithm.                                         |
| lakers-python      | A library for working with LAKERS data (likely domain-specific).                                             |
| lazy-object-proxy  | A library for creating lazy object proxies, useful for deferred initialization.                              |
| lazy_loader        | A utility for lazy loading of Python modules.                                                                |
| libcst             | A concrete syntax tree parser and transformer library for Python.                                            |
| lightgbm           | A gradient boosting framework that uses tree-based learning algorithms.                                      |
| logbook            | A logging system for Python, designed to be an alternative to the `logging` module.                         |
| lxml               | A library for processing XML and HTML documents with the libxml2 and libxslt C libraries.                   |
| MarkupSafe         | A library for escaping text for safe use in HTML and XML.                                                    |
| matplotlib         | A comprehensive library for creating static, animated, and interactive visualizations in Python.             |
| matplotlib-inline  | Provides inline plotting for IPython and Jupyter notebooks.                                                  |
| matplotlib-pyodide | A version of matplotlib optimized for use in Pyodide (Python in the browser).                                |
| memory-allocator   | A library for managing memory allocation in Python.                                                          |
| micropip           | A package installer for Python running in WebAssembly environments like Pyodide.                            |
| mmh3               | A Python wrapper for the MurmurHash3 hashing algorithm.                                                     |
| mne                | A library for processing and analyzing electrophysiological data (e.g., EEG, MEG).                          |
| more-itertools     | A collection of additional tools for working with Python iterators.                                          |
| mpmath             | A library for arbitrary-precision floating-point arithmetic.                                                |
| msgpack            | A library for serializing and deserializing data in the MessagePack format.                                  |
| msgspec            | A library for fast serialization and validation of structured data.                                          |
| msprime            | A library for simulating ancestry and genetic variation.                                                    |
| multidict          | A multidict implementation, a dictionary supporting multiple values per key.                                |
| munch              | A dictionary that supports attribute-style access.                                                          |
| mypy               | A static type checker for Python.                                                                           |
| narwhals           | A library for working with marine biology or related datasets (specific domain).                            |
| netcdf4            | A library for working with NetCDF data format, commonly used in scientific data.                            |
| networkx           | A library for creating, analyzing, and visualizing complex networks and graphs.                             |
| newick             | A library for parsing and working with Newick tree format, used in phylogenetics.                           |
| nh3                | A Python wrapper for the NH3 algorithm, used for text summarization.                                        |
| nlopt              | A library for nonlinear optimization, supporting various algorithms.                                         |
| nltk               | The Natural Language Toolkit, a library for working with human language data.                               |
| numcodecs          | A library for encoding and decoding numerical data, often used in compression.                              |
| numpy              | A fundamental package for scientific computing with powerful multidimensional array support.                |
| openai             | A library for interfacing with OpenAI's APIs, including GPT models.                                         |
| opencv-python      | A library for computer vision and image processing tasks.                                                   |
| optlang            | A Python library for mathematical optimization modeling.                                                    |
| orjson             | A fast JSON library for Python, with support for serialization.                                             |
| osqp               | A library for solving quadratic programming problems.                                                       |
| packaging          | A library for handling Python package metadata and versioning.                                              |
| pandas             | A library for data analysis and manipulation using dataframes.                                              |
| parso              | A Python library for parsing and analyzing Python code.                                                     |
| patsy              | A library for describing statistical models and building design matrices.                                   |
| pcodec             | A library for parallel data encoding and decoding.                                                          |
| peewee             | A lightweight and expressive ORM for SQL databases in Python.                                               |
| pi-heif            | A library for reading and writing HEIF/HEIC image formats.                                                 |
| Pillow             | A Python Imaging Library (PIL) fork for image processing.                                                   |
| pillow-heif        | A plugin for Pillow to support HEIF images.                                                                 |
| pkgconfig          | A library for querying the pkg-config package manager from Python.                                          |
| pluggy             | A library for creating and managing plugins in Python.                                                     |
| polars             | A DataFrame library in Python for fast data manipulation.                                                   |
| pplpy              | A Python wrapper for the Parma Polyhedra Library, used in mathematical computations.                        |
| primecountpy       | A Python library for counting prime numbers efficiently.                                                    |
| prompt_toolkit     | A library for building interactive command-line applications in Python.                                     |
| protobuf           | A library for serializing structured data using Google's Protocol Buffers.                                  |
| pure-eval          | A library for evaluating Python expressions safely.                                                         |
| py                 | A library with utilities for Python development, often used with pytest.                                    |
| pyarrow            | A library for working with Apache Arrow data formats.                                                      |
| pyclipper          | A Python wrapper for the Clipper library, used for polygon clipping and offsetting.                         |
| pycparser          | A library for parsing and analyzing C language code.                                                       |
| pycryptodome       | A library for cryptographic functions and algorithms.                                                       |
| pydantic           | A Python library for data validation and settings management using type annotations.                        |
| pydantic_core      | The core library for Pydantic, focused on data validation performance.                                      |
| pyerfa             | A Python wrapper for the ERFA library, used in astronomy for transformations between coordinate systems.     |
| pygame-ce          | A community edition of Pygame for building games and multimedia applications.                               |
| Pygments           | A library for syntax highlighting in Python.                                                               |
| pyheif             | A library for handling HEIF/HEIC image formats.                                                             |
| pyiceberg          | A library for working with Apache Iceberg, a tabular data format for big data.                              |
| pyinstrument       | A Python performance profiler for analyzing bottlenecks.                                                   |
| pynacl             | A Python binding for the Networking and Cryptography (NaCl) library.                                       |
| Package Name       | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| pyodide-http       | A library for making HTTP requests in the Pyodide environment (Python running in the browser).               |
| pyodide-unix-timezones | Provides timezone data for Pyodide's unix-like environment.                                               |
| pyparsing          | A library for defining and executing grammars for parsing text.                                              |
| pyproj             | A Python interface to the PROJ library for cartographic projections and coordinate transformations.           |
| pyrsistent         | A library for immutable data structures in Python.                                                           |
| pysam              | A library for reading and writing SAM and BAM files, commonly used in bioinformatics.                        |
| pyshp              | A library for reading and writing shapefile data.                                                            |
| pytest             | A framework for writing and running tests in Python.                                                        |
| pytest-asyncio     | A pytest plugin for testing asyncio-based code.                                                              |
| pytest-benchmark   | A pytest plugin for benchmarking code performance.                                                           |
| pytest_httpx       | A pytest plugin for testing HTTPX-based code.                                                                |
| python-dateutil    | A library for parsing, formatting, and manipulating dates and times.                                         |
| python-flint       | A Python wrapper for the FLINT library for fast number theory computations.                                  |
| python-magic       | A library for identifying file types.                                                                        |
| python-sat         | A library for solving boolean satisfiability (SAT) problems.                                                 |
| python-solvespace  | A Python binding for the SolveSpace 3D CAD application.                                                      |
| pytz               | A library for working with time zones in Python.                                                             |
| pywavelets         | A library for wavelet transforms in signal processing and image analysis.                                    |
| pyxel              | A retro game development toolkit for Python.                                                                 |
| pyxirr             | A library for calculating internal rates of return (IRR) and related financial metrics.                      |
| pyyaml             | A library for parsing and writing YAML data.                                                                 |
| rasterio           | A library for reading and writing geospatial raster data.                                                    |
| rateslib           | A library for building interest rate and derivatives pricing models.                                         |
| rebound            | A library for simulating gravitational dynamics in astrophysics.                                             |
| reboundx           | An extension library for REBOUND, adding additional physics to simulations.                                  |
| referencing        | A library for resolving and referencing schemas or documents.                                                |
| regex              | A library for advanced regular expression matching in Python.                                                |
| requests           | A simple and widely used HTTP library for Python.                                                            |
| retrying           | A library for retrying function calls upon failure.                                                          |
| rich               | A library for producing beautiful and formatted terminal output, including tables, progress bars, and syntax highlighting. |
| river              | A library for online machine learning, handling data streams.                                                |
| RobotRaconteur     | A library for distributed robotics and automation systems.                                                   |
| rpds-py            | A library for high-performance immutable data structures.                                                    |
| ruamel.yaml        | A YAML parser and emitter supporting YAML 1.2.                                                               |
| rust-abi-test      | A library for testing Rust's ABI (Application Binary Interface).                                             |
| rust-panic-test    | A library for testing Rust panic scenarios.                                                                  |
| scikit-image       | A library for image processing in Python.                                                                    |
| scikit-learn       | A machine learning library for Python, offering tools for classification, regression, clustering, and more.  |
| scipy              | A library for scientific computing, offering modules for optimization, integration, interpolation, and more. |
| screed             | A library for reading and writing FASTA and FASTQ files in bioinformatics.                                   |
| setuptools         | A library for building, packaging, and distributing Python projects.                                         |
| shapely            | A library for working with geometric objects and performing operations like intersection, union, and difference. |
| simplejson         | A JSON library for Python, focusing on performance and compliance.                                           |
| sisl               | A library for simulation and analysis of tight-binding models in physics.                                    |
| six                | A Python 2 and 3 compatibility library.                                                                      |
| smart-open         | A library for efficient streaming of large files from various sources like S3, GCS, and HDFS.               |
| sniffio            | A library for detecting which asynchronous library is running in the current environment.                    |
| sortedcontainers   | A library for sorted collections like lists, dicts, and sets.                                                |
| soupsieve          | A library for CSS-like selectors to filter elements in HTML or XML documents.                                |
| sourmash           | A library for scalable bioinformatics, particularly for comparing DNA and protein sequences.                 |
| soxr               | A library for high-quality audio sample rate conversion.                                                     |
| sparseqr           | A library for solving sparse linear least squares problems.                                                  |
| sqlalchemy         | A SQL toolkit and ORM for Python, enabling database interaction.                                              |
| stack-data         | A library for introspecting Python stack frames.                                                             |
| statsmodels        | A library for statistical modeling and hypothesis testing.                                                   |
| strictyaml         | A library for parsing and validating YAML with a focus on security.                                          |
| svgwrite           | A Python library for creating SVG drawings.                                                                  |
| swiglpk            | A Python wrapper for the GLPK (GNU Linear Programming Kit) library.                                          |
| sympy              | A library for symbolic mathematics and algebra in Python.                                                   |
| tblib              | A library for pickling tracebacks and exceptions in Python.                                                  |
| termcolor          | A library for adding color to terminal text output.                                                          |
| texttable          | A library for creating simple ASCII tables.                                                                  |
| threadpoolctl      | A library for controlling thread pools in Python.                                                            |
| Package Name       | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| tiktoken           | A library for tokenizing text used in OpenAI's language models.                                               |
| tomli              | A library for parsing TOML files in Python.                                                                  |
| tomli-w            | A library for writing TOML files in Python.                                                                  |
| toolz              | A functional programming library for Python, offering utilities for iterators, functions, and collections.    |
| tqdm               | A library for creating progress bars in Python applications.                                                 |
| traitlets          | A Python library for managing attributes and events in classes.                                              |
| traits             | A library for defining object attributes with type checking and validation.                                  |
| tree-sitter        | A parser generator for building incremental parsers for various programming languages.                       |
| tree-sitter-go     | A tree-sitter grammar for the Go programming language.                                                       |
| tree-sitter-java   | A tree-sitter grammar for the Java programming language.                                                     |
| tree-sitter-python | A tree-sitter grammar for the Python programming language.                                                   |
| tskit              | A library for working with tree sequence data in population genetics.                                        |
| typing-extensions  | Extensions to the Python `typing` module, providing additional type hints.                                   |
| tzdata             | Provides timezone data for Python applications.                                                              |
| uncertainties      | A library for performing calculations with uncertainty propagation.                                          |
| unyt               | A library for handling physical quantities with units in numerical computations.                             |
| urllib3            | A powerful HTTP library for Python, used for making HTTP requests.                                           |
| vega-datasets      | Provides example datasets for visualization libraries like Altair and Vega.                                  |
| wcwidth            | A library for measuring the display width of Unicode characters.                                             |
| webencodings       | A library for handling text encoding in web development.                                                     |
| wordcloud          | A library for generating word clouds from text data.                                                         |
| wrapt              | A library for decorators and function wrappers.                                                              |
| xarray             | A library for working with labeled multi-dimensional arrays and datasets.                                    |
| xgboost            | A machine learning library for gradient boosting frameworks.                                                 |
| xlrd               | A library for reading data from Excel files (legacy `.xls` format).                                          |
| xxhash             | A library for fast, non-cryptographic hashing algorithms.                                                    |
| xyzservices        | Provides APIs for accessing XYZ tile services for maps.                                                     |
| yarl               | A library for constructing and manipulating URLs.                                                            |
| yt                 | A library for analyzing and visualizing volumetric data in scientific simulations.                           |
| zarr               | A library for working with chunked, compressed, N-dimensional arrays.                                        |
| zengl              | A library for modern rendering and graphics programming in Python.                                           |
| zfpy               | A library for lossy compression of floating-point arrays.                                                    |
| zstandard          | A library for fast data compression and decompression using the Zstandard algorithm.                         |
