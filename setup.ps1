# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

$VenvPath = ".\venv"

if (-not (Test-Path -Path $VenvPath -PathType Container)) {
    python -m venv $VenvPath
}

. (Join-Path $VenvPath "Scripts\Activate.ps1")
