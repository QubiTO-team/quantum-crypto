# Quantum cryptography QubiTO project

Introduction

# Access Lagrange Quantum Computer
To test your access to the quantum computer follow the subsequent points (note that the quantum computer can be only accessed by QubiTO members):
- install [uv package](https://docs.astral.sh/uv/getting-started/installation/);
- inside the repository's main folder run `uv sync`;
- in the same path run the command `lagrangeclient`;
- you should now have a file on the directory called `token.json`;
- run `uv run test_scripts/test_access_Lagrange.py`;
- You should see the results from the quantum computer printed out.

# Useful References

## Classical Cryptography
- Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography (2nd ed.). Chapman and Hall/CRC.

## Quantum Random Number Generation
- Gnatowski, Andrzej, et al. "True Random Number Generators on IQM Spark." arXiv preprint arXiv:2512.09862 (2025).

# Contributing Guide

Firstly watch [this really good youtube video.](https://www.youtube.com/watch?v=nCKdihvneS0) Below you have a summary of the steps to be taken.

## Setting Up Your Local Environment

1. Fork the repository on GitHub using the apposite button
2. Clone your forked repository locally:

```bash
git clone https://github.com/your-username/quantum-crypto.git
cd quantum-crypto
```

3. Add the upstream repository as a remote:

```bash
git remote add upstream https://github.com/QubiTO-team/quantum-crypto.git
```

4. Create a new branch for your changes:

```bash
git checkout -b your-feature-name
```

## Making Changes

Do your changes, and then add and commit the files.

- Write clear, concise commit messages;
- Keep commits focused on a single issue or feature;
- Test your changes thoroughly before submitting;
- Comment the file thoroughly; anyone needs to understand reading the code.

## Submitting a Pull Request

### Before Submitting

1. Ensure your branch is up to date with the main branch:

```bash
git fetch upstream
git rebase upstream/main
```

2. Push your changes to your forked repository:

```bash
git push origin your-feature-name
```

### Creating the Pull Request

1. Go to the original repository on GitHub;
2. Click the "New Pull Request" button;
3. Select your fork and branch as the source;
4. Fill in the PR title and description with:
   - Clear explanation of the changes;
   - Reference to any related issues (use #issue-number);
   - Description of testing performed;
5. Click "Create Pull Request".

## PR Review Process

- Wait and be responsive to reviewer feedback.

## After Your PR is Merged

- Delete your feature branch locally and remotely;
- Be ready to eventually write a little article in the QubiTO website!

Thank you for contributing!
