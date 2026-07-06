$path = 'c:\Users\USER\Downloads\Craftivo\Craftivo\index.html'
$text = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

# Fix garbled em dashes and smart quotes
$text = $text -replace 'Ã¢â‚¬â€œ', '"'
$text = $text -replace 'Ã¢â‚¬â€™', '"'
$text = $text -replace 'Ã¢â‚¬â€', '--'
$text = $text -replace 'Ã¢â‚¬â„¢', "'"
$text = $text -replace 'Ã¢â‚¬Â', ' - '
$text = $text -replace "Hi, I'm Jithya .* I'm a Digital Marketer", "Hi, I'm Jithya — I'm a Digital Marketer"

[System.IO.File]::WriteAllText($path, $text, [System.Text.Encoding]::UTF8)
Write-Host "Done fixing encoding"
