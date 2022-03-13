mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"victorblay3@yahoo.es\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml