<#
.SYNOPSIS
    문제 폴더의 Solution.java 를 컴파일하고 모든 테스트케이스를 검증합니다.

.EXAMPLE
    .\test.ps1 ds-tutorial-02-echo

.EXAMPLE
    # 내가 짠 다른 코드로 테스트하고 싶을 때
    .\test.ps1 ds-tutorial-02-echo -File .\work\MyTry.java
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Id,

    [string]$File
)

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
[Console]::InputEncoding = $utf8NoBom
[Console]::OutputEncoding = $utf8NoBom
$OutputEncoding = $utf8NoBom

$root = $PSScriptRoot
$prob = Join-Path $root "bank\$Id"

if (-not (Test-Path $prob)) {
    Write-Host "Problem folder not found: $prob" -ForegroundColor Red
    exit 1
}

$src = if ($File) { (Resolve-Path $File).Path } else { Join-Path $prob "Solution.java" }

if (-not (Test-Path $src)) {
    Write-Host "Source file not found: $src" -ForegroundColor Red
    Write-Host "Did you rename solution.java to Solution.java? (Java requires public class name = file name)" -ForegroundColor Yellow
    exit 1
}

$work = Join-Path $root ".work\$Id"
if (Test-Path $work) { Remove-Item -Recurse -Force $work }
New-Item -ItemType Directory -Force -Path $work | Out-Null

Copy-Item $src (Join-Path $work "Solution.java") -Force

Write-Host "[Compile] $src" -ForegroundColor Cyan
& javac -encoding UTF-8 -d $work (Join-Path $work "Solution.java")
if ($LASTEXITCODE -ne 0) {
    Write-Host "Compile failed" -ForegroundColor Red
    exit 1
}

function Normalize([string[]]$lines) {
    if ($null -eq $lines) { return "" }
    $t = @($lines | ForEach-Object { $_.TrimEnd() })
    while ($t.Count -gt 0 -and $t[-1] -eq "") { $t = $t[0..($t.Count - 2)] }
    return ($t -join "`n")
}

$inDir = Join-Path $prob "testcases\input"
$outDir = Join-Path $prob "testcases\output"
$inputs = @(Get-ChildItem (Join-Path $inDir "input*.txt") -ErrorAction SilentlyContinue | Sort-Object Name)

if ($inputs.Count -eq 0) {
    Write-Host "No testcases found: $inDir" -ForegroundColor Red
    exit 1
}

$pass = 0
$fail = 0
$firstFail = $null

foreach ($in in $inputs) {
    $n = $in.BaseName -replace '^input', ''
    $expFile = Join-Path $outDir "output$n.txt"

    if (-not (Test-Path $expFile)) {
        Write-Host ("  case {0}  SKIP  (missing output{0}.txt)" -f $n) -ForegroundColor Yellow
        continue
    }

    $actualRaw = Get-Content $in.FullName -Raw | & java -cp $work Solution 2>&1
    $actual = Normalize $actualRaw
    $expect = Normalize (Get-Content $expFile)

    if ($actual -ceq $expect) {
        Write-Host ("  case {0}  PASS" -f $n) -ForegroundColor Green
        $pass++
    }
    else {
        Write-Host ("  case {0}  FAIL" -f $n) -ForegroundColor Red
        $fail++
        if ($null -eq $firstFail) {
            $firstFail = [pscustomobject]@{
                Case   = $n
                Input  = (Get-Content $in.FullName -Raw)
                Expect = $expect
                Actual = $actual
            }
        }
    }
}

Write-Host ""
if ($fail -eq 0) {
    Write-Host "All passed  ($pass / $($pass + $fail))" -ForegroundColor Green
}
else {
    Write-Host "Passed $pass / Failed $fail" -ForegroundColor Red
    Write-Host ""
    Write-Host "-- First failed case $($firstFail.Case) --" -ForegroundColor Yellow
    Write-Host "[Input]"
    Write-Host $firstFail.Input
    Write-Host "[Expected]"
    Write-Host $firstFail.Expect
    Write-Host "[Actual]"
    Write-Host $firstFail.Actual
    exit 1
}
