curl -LsSf https://astral.sh/uv/install.sh | sh

export DATABASE_URL=postgresql://analyzer_user:analyzer_pass@localhost:5432/page_analyzer

make install && psql -a -d $DATABASE_URL -f database.sql