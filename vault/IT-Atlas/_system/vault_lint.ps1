<#
  Vault lint for Windows (no Python needed): broken wikilinks, duplicate note names,
  notes nothing links to, and notes missing frontmatter.
  Usage (from the vault root):  powershell -ExecutionPolicy Bypass -File _system\vault_lint.ps1
  Exit code 1 if broken links or frontmatter problems are found.
#>
param([string]$Root = (Split-Path -Parent $PSScriptRoot))

$Root = (Resolve-Path -LiteralPath $Root).Path.TrimEnd('\', '/')
$skipDirs = '^(\.obsidian|\.claude|\.git|\.trash|_system|90 Templates)([\\/]|$)'
$noFront = @('Start here.md')
$enc = New-Object System.Text.UTF8Encoding($false)

$files = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter '*.md' | Where-Object {
    $rel = $_.FullName.Substring($Root.Length).TrimStart('\', '/')
    ($rel -notmatch $skipDirs) -and ($_.Name -ne 'CLAUDE.md')
}

$notes = @{}
$dupes = New-Object System.Collections.Generic.List[string]
foreach ($f in $files) {
    $n = [IO.Path]::GetFileNameWithoutExtension($f.Name)
    if ($notes.ContainsKey($n)) { $dupes.Add($n) } else { $notes[$n] = $f }
}

$linkRx = [regex]'\[\[([^\]\|#\^]+)(?:[#\^][^\]\|]*)?(?:\|[^\]]*)?\]\]'
$codeRx = [regex]'(?s)```.*?```'
$broken = New-Object System.Collections.Generic.List[string]
$missing = New-Object System.Collections.Generic.List[string]
$inbound = @{}
$types = @{}

foreach ($f in $files) {
    $rel = $f.FullName.Substring($Root.Length).TrimStart('\', '/')
    $text = [IO.File]::ReadAllText($f.FullName, $enc)
    foreach ($m in $linkRx.Matches($codeRx.Replace($text, ''))) {
        $target = $m.Groups[1].Value.Trim()
        if ($notes.ContainsKey($target)) { $inbound[$target] = $true }
        else { $broken.Add("$rel -> [[$target]]") }
    }
    if ($noFront -contains $f.Name) { continue }
    if (-not $text.StartsWith('---')) { $missing.Add("${rel}: no frontmatter"); continue }
    $end = $text.IndexOf("`n---", 3)
    if ($end -lt 0) { $missing.Add("${rel}: unterminated frontmatter"); continue }
    $front = $text.Substring(3, $end - 3)
    foreach ($k in @('type', 'tags')) {
        if ($front -notmatch "(?m)^$k\s*:") { $missing.Add("${rel}: missing '$k'") }
    }
    $t = 'none'
    $tm = [regex]::Match($front, '(?m)^type\s*:\s*"?([^"\r\n]+)"?')
    if ($tm.Success) { $t = $tm.Groups[1].Value.Trim() }
    if ($types.ContainsKey($t)) { $types[$t]++ } else { $types[$t] = 1 }
}

$unlinked = @($notes.Keys | Where-Object { -not $inbound.ContainsKey($_) -and $_ -ne 'Home' -and $_ -ne 'Start here' } | Sort-Object)

$summary = ($types.GetEnumerator() | Sort-Object Name | ForEach-Object { "$($_.Name): $($_.Value)" }) -join ', '
Write-Output "Notes scanned: $($notes.Count) | $summary"
Write-Output ""
Write-Output "Duplicate note names ($($dupes.Count)):";   $dupes   | ForEach-Object { "  $_" }
Write-Output "Broken links ($($broken.Count)):";          $broken  | Sort-Object | ForEach-Object { "  $_" }
Write-Output "Frontmatter problems ($($missing.Count)):"; $missing | Sort-Object | ForEach-Object { "  $_" }
Write-Output "Nothing links here ($($unlinked.Count)):";  $unlinked | ForEach-Object { "  $_" }

if ($broken.Count -gt 0 -or $missing.Count -gt 0 -or $dupes.Count -gt 0) { exit 1 }
exit 0
