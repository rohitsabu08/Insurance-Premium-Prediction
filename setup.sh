mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml

config.toml = 
[theme]
primaryColor="#c54d4d"
backgroundColor="#5a0216"
secondaryBackgroundColor="#5c2d41"
textColor="#f5f0f0"
font="serif"
