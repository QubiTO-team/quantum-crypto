## Access Lagrange quantum computer
To test your access to the quantum computer follow the subsequent points (note that the quantum computer can be only accessed by QubiTO members):
- install [uv package](https://docs.astral.sh/uv/getting-started/installation/);
- inside the repository's main folder run `uv sync`;
- in the same path run the command `lagrangeclient`;
- you should now have a file on the directory called `token.json`;
- run `uv run test_scripts/test_access_Lagrange.py`;
- You should see the results from the quantum computer printed out.
