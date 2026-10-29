#Requires -Version 7.0
<#
.SYNOPSIS
    Publish the bundled English wiki pages to the separate GitHub Wiki Git repository.
.DESCRIPTION
    Uses Git's existing authentication, never force-pushes, never modifies audited
    source repositories, and requests explicit approval before committing/pushing.
    GitHub Wiki must already have at least its initial Home page created online.
.EXAMPLE
    pwsh -NoProfile -File .\PUBLISH_WIKI.ps1
.EXAMPLE
    pwsh -NoProfile -File .\PUBLISH_WIKI.ps1 -PreviewOnly
#>
[CmdletBinding()]
param([switch]$PreviewOnly)

$ErrorActionPreference = 'Stop'
$project = Split-Path -Parent $PSCommandPath
$source = Join-Path $project 'wiki'
$wikiUrl = 'https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit.wiki.git'
$wikiPage = 'https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem-GitHub-Audit/wiki'

if (-not (Test-Path -LiteralPath (Join-Path $source 'Home.md') -PathType Leaf)) {
    throw 'Wiki source pages not found. Run the script from the extracted complete application.'
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git for Windows is required. No files were uploaded.'
}

$tempBase = Join-Path ([IO.Path]::GetTempPath()) ('koa-wiki-' + [guid]::NewGuid().ToString('N'))
$cloneDir = Join-Path $tempBase 'wiki'
New-Item -Path $tempBase -ItemType Directory -Force | Out-Null
try {
    Write-Host "`n=== kOA — GitHub Wiki publisher ===" -ForegroundColor Cyan
    Write-Host "Wiki URL: $wikiPage"
    Write-Host 'Cloning the separate Wiki repository (not a source project)...'
    & git clone --quiet $wikiUrl $cloneDir
    if ($LASTEXITCODE -ne 0) {
        throw 'Wiki clone failed. On GitHub, enable Wiki and create its first Home page before running this helper. No publication occurred.'
    }

    $branch = (& git -C $cloneDir branch --show-current)
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($branch)) {
        throw 'Could not identify the wiki default branch. No publication occurred.'
    }
    $branch = $branch.Trim()

    # Only copy the Markdown pages intentionally shipped in the wiki folder.
    # Existing, unrelated Wiki pages are not removed.
    $pages = @(Get-ChildItem -LiteralPath $source -Filter '*.md' -File)
    if ($pages.Count -lt 2) {
        throw 'Wiki source is incomplete. No publication occurred.'
    }
    $pageNames = @($pages | ForEach-Object { $_.Name })
    foreach ($page in $pages) {
        $dest = Join-Path $cloneDir $page.Name
        Copy-Item -LiteralPath $page.FullName -Destination $dest -Force
    }

    & git -C $cloneDir add -- $pageNames
    if ($LASTEXITCODE -ne 0) { throw 'Could not stage Wiki Markdown pages.' }

    $changed = @(& git -C $cloneDir diff --cached --name-only)
    if ($LASTEXITCODE -ne 0) { throw 'Could not inspect staged changes.' }
    if ($changed.Count -eq 0) {
        Write-Host 'Wiki is already up to date. Nothing to publish.' -ForegroundColor Green
        exit 0
    }

    Write-Host "`n=== Changes to publish ===" -ForegroundColor Cyan
    & git -C $cloneDir --no-pager diff --cached --stat
    if ($LASTEXITCODE -ne 0) { throw 'Could not display Wiki diff summary.' }

    if ($PreviewOnly) {
        Write-Host 'Preview only: no commit, no push.' -ForegroundColor Yellow
        exit 0
    }

    $confirmation = Read-Host "Type PUBLISH to update $wikiPage (anything else cancels)"
    if ($confirmation -cne 'PUBLISH') {
        Write-Host 'Canceled. No commit or push was made.' -ForegroundColor Yellow
        exit 0
    }

    & git -C $cloneDir commit -m 'docs(wiki): publish English kOA audit guides'
    if ($LASTEXITCODE -ne 0) { throw 'Wiki commit failed; no push attempted.' }

    # No --force. A concurrent remote update causes rejection instead of overwrite.
    & git -C $cloneDir push origin "HEAD:refs/heads/$branch"
    if ($LASTEXITCODE -ne 0) {
        throw 'Wiki push was rejected. No force-push attempted; rerun to rebase on the latest Wiki.'
    }
    Write-Host "`nPublished Wiki successfully: $wikiPage" -ForegroundColor Green
}
finally {
    if (Test-Path -LiteralPath $tempBase) {
        Remove-Item -LiteralPath $tempBase -Recurse -Force -ErrorAction SilentlyContinue
    }
}
