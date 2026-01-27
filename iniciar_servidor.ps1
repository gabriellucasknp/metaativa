# Script para iniciar o servidor Django METAATIVA
# Execute este arquivo no PowerShell para rodar a aplicação

Write-Host ""
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "   METAATIVA - Servidor Django" -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan
Write-Host ""

# Navegar até o diretório
Set-Location C:\Users\lixei\Downloads\metaativa-main

# Ativar ambiente virtual
& .\.venv\Scripts\Activate.ps1

# Rodar servidor
Write-Host ""
Write-Host "Iniciando servidor Django..." -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Acesse: http://127.0.0.1:8000/" -ForegroundColor Yellow
Write-Host "🔐 Admin:  http://127.0.0.1:8000/admin/" -ForegroundColor Yellow
Write-Host "   Usuario: admin" -ForegroundColor Yellow
Write-Host "   Senha: admin123" -ForegroundColor Yellow
Write-Host ""
Write-Host "Pressione CTRL+C para parar o servidor" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver
