# Custom Pyodide Distribution Setup Guide

This guide provides step-by-step instructions for setting up a custom Pyodide distribution to bypass CDN access issues (such as Zscaler proxy blocking) in JupyterLite.

## Overview

By default, JupyterLite uses the official Pyodide CDN which may be blocked by corporate firewalls or proxy services like Zscaler. This solution hosts Pyodide assets on GitHub Pages or alternative hosting services to ensure reliable access.

## Quick Start

The JupyterLite configuration in this repository is already set up to use a custom Pyodide distribution hosted at:
- **Custom URL**: `https://wxcuop.github.io/pyodide-assets/pyodide.js`
- **Configuration File**: `repl/jupyter-lite.json`

## Setting Up Your Own Pyodide Assets Repository

### Step 1: Create the Assets Repository

1. **Create a new GitHub repository** (e.g., `wxcuop/pyodide-assets`)
   ```bash
   # Clone or create your new repository
   git clone https://github.com/wxcuop/pyodide-assets.git
   cd pyodide-assets
   ```

2. **Create the basic repository structure**:
   ```
   pyodide-assets/
   ├── README.md
   ├── .gitignore
   └── (Pyodide distribution files will go here)
   ```

### Step 2: Download and Extract Pyodide Distribution

1. **Download the specific Pyodide version** you want to use:
   ```bash
   # Example for Pyodide 0.27.6 (adjust version as needed)
   PYODIDE_VERSION="0.27.6"
   wget https://github.com/pyodide/pyodide/releases/download/${PYODIDE_VERSION}/pyodide-${PYODIDE_VERSION}.tar.bz2
   ```

2. **Extract the distribution**:
   ```bash
   tar -xjf pyodide-${PYODIDE_VERSION}.tar.bz2
   ```

3. **Copy files to your repository**:
   ```bash
   # Copy all Pyodide files to the root of your repository
   cp -r pyodide/* .
   
   # Clean up
   rm -rf pyodide pyodide-${PYODIDE_VERSION}.tar.bz2
   ```

4. **Verify essential files are present**:
   ```
   ├── pyodide.js              # Main Pyodide JavaScript file
   ├── pyodide.asm.js          # WebAssembly fallback
   ├── pyodide.asm.wasm        # WebAssembly binary
   ├── pyodide_py.tar          # Python standard library
   ├── packages.json           # Package metadata
   └── *.whl                   # Python packages
   ```

### Step 3: Configure GitHub Pages

1. **Enable GitHub Pages** for your repository:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Source: Deploy from a branch
   - Branch: `main` (or your preferred branch)
   - Folder: `/ (root)`

2. **Create a .gitignore file** (optional):
   ```gitignore
   # Temporary files
   *.tmp
   *.log
   
   # Archive files (keep only extracted content)
   *.tar.bz2
   *.tar.gz
   *.zip
   ```

3. **Commit and push your changes**:
   ```bash
   git add .
   git commit -m "Add Pyodide ${PYODIDE_VERSION} distribution"
   git push origin main
   ```

4. **Wait for deployment** (usually 5-10 minutes)
   - Your Pyodide distribution will be available at: `https://yourusername.github.io/pyodide-assets/`

### Step 4: Update JupyterLite Configuration

Update your `jupyter-lite.json` configuration to point to your custom Pyodide distribution:

```json
{
  "jupyter-lite-schema-version": 0,
  "jupyter-config-data": {
    "disabledExtensions": [
      "@jupyterlab/drawio-extension",
      "jupyterlab-kernel-spy",
      "jupyterlab-tour",
      "@jupyterlab/apputils-extension:announcements"
    ]
  },
  "litePluginSettings": {
    "@jupyterlite/pyodide-kernel-extension:kernel": {
      "pyodideUrl": "https://yourusername.github.io/pyodide-assets/pyodide.js"
    }
  }
}
```

### Step 5: Build and Test

1. **Build your JupyterLite site**:
   ```bash
   jupyter lite build --contents content --output-dir dist
   ```

2. **Serve locally for testing**:
   ```bash
   cd dist
   python -m http.server 8000
   ```

3. **Open in browser** and verify Pyodide loads correctly:
   - Navigate to `http://localhost:8000`
   - Open a Python notebook
   - Verify the kernel starts without errors

## Alternative Hosting Methods

### GitHub Releases

Instead of GitHub Pages, you can host Pyodide files as release assets:

1. **Create a release** in your GitHub repository
2. **Upload the Pyodide tar.bz2 file** as a release asset
3. **Use the release URL** in your JupyterLite configuration:
   ```bash
   # Build command with release URL
   jupyter lite build --contents content --output-dir dist --pyodide https://github.com/yourusername/pyodide-assets/releases/download/v0.27.6/pyodide-0.27.6.tar.bz2
   ```

### Raw GitHub Files

For smaller setups, you can use raw GitHub file URLs:

```json
{
  "litePluginSettings": {
    "@jupyterlite/pyodide-kernel-extension:kernel": {
      "pyodideUrl": "https://raw.githubusercontent.com/yourusername/pyodide-assets/main/pyodide.js"
    }
  }
}
```

**Note**: Raw GitHub URLs have rate limits and are not recommended for production use.

### Self-Hosted Solutions

For enterprise environments, consider:

- **Internal web server**: Host Pyodide files on your organization's web server
- **CDN alternatives**: Use enterprise-approved CDN services
- **Docker containers**: Package Pyodide with your JupyterLite deployment

## Performance Optimization

### File Compression

Enable gzip compression on your hosting service to reduce download times:

```nginx
# Nginx configuration example
location ~* \.(js|wasm|tar)$ {
    gzip on;
    gzip_types application/javascript application/wasm application/x-tar;
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### CDN Integration

For better global performance, consider using a CDN that integrates with GitHub Pages:

- **Cloudflare**: Automatic CDN for GitHub Pages
- **jsDelivr**: `https://cdn.jsdelivr.net/gh/yourusername/pyodide-assets@main/pyodide.js`
- **unpkg**: Alternative CDN for GitHub repositories

### Caching Strategy

Configure appropriate cache headers to improve loading times:

```yaml
# GitHub Pages _config.yml
plugins:
  - jekyll-default-layout

defaults:
  - scope:
      path: "*.js"
    values:
      layout: null
  - scope:
      path: "*.wasm"
    values:
      layout: null
```

## Troubleshooting

### Common Issues

1. **404 Error on Pyodide URL**
   - Verify GitHub Pages is enabled and deployed
   - Check the exact file path in your repository
   - Ensure files are in the repository root or adjust URL accordingly

2. **CORS Issues**
   - GitHub Pages should automatically set appropriate CORS headers
   - If using custom hosting, ensure CORS headers allow your JupyterLite domain

3. **Slow Loading**
   - Verify all required files are present in your repository
   - Check network tab in browser developer tools for failed requests
   - Consider using a CDN for better performance

4. **Version Mismatches**
   - Ensure your Pyodide version is compatible with your JupyterLite version
   - Check the `packages.json` file for package compatibility

### Verification Steps

1. **Test Pyodide URL directly**:
   ```bash
   curl -I https://yourusername.github.io/pyodide-assets/pyodide.js
   ```

2. **Check browser console** for error messages when loading JupyterLite

3. **Verify file integrity**:
   ```bash
   # Compare checksums with official distribution
   sha256sum pyodide.js
   ```

### Debug Configuration

Enable debug logging in JupyterLite to troubleshoot loading issues:

```json
{
  "jupyter-config-data": {
    "disabledExtensions": [...],
    "LabApp": {
      "level": "DEBUG"
    }
  }
}
```

## Maintenance

### Updating Pyodide Version

1. **Download new Pyodide version**
2. **Extract and replace files** in your repository
3. **Update version references** in documentation
4. **Test compatibility** with your JupyterLite setup
5. **Update your JupyterLite configuration** if needed

### Monitoring

- **Set up GitHub Actions** to automatically check for new Pyodide releases
- **Monitor repository size** to stay within GitHub limits
- **Track usage** through GitHub Pages analytics

## Security Considerations

- **Verify file integrity**: Always verify checksums when downloading Pyodide distributions
- **Use HTTPS**: Ensure all URLs use HTTPS protocol
- **Regular updates**: Keep Pyodide version updated for security patches
- **Access control**: Consider private repositories for sensitive environments

## Support

For issues related to:
- **JupyterLite configuration**: Check [JupyterLite documentation](https://jupyterlite.readthedocs.io/)
- **Pyodide**: Visit [Pyodide documentation](https://pyodide.org/)
- **GitHub Pages**: See [GitHub Pages documentation](https://docs.github.com/en/pages)

## Example Configuration

Here's a complete working example of a `jupyter-lite.json` file with custom Pyodide configuration:

```json
{
  "jupyter-lite-schema-version": 0,
  "jupyter-config-data": {
    "disabledExtensions": [
      "@jupyterlab/drawio-extension",
      "jupyterlab-kernel-spy",
      "jupyterlab-tour",
      "@jupyterlab/apputils-extension:announcements"
    ]
  },
  "litePluginSettings": {
    "@jupyterlite/pyodide-kernel-extension:kernel": {
      "pyodideUrl": "https://wxcuop.github.io/pyodide-assets/pyodide.js"
    }
  }
}
```

This configuration will ensure JupyterLite uses your custom Pyodide distribution instead of the default CDN, effectively bypassing any corporate firewall or proxy restrictions.